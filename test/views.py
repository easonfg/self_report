from django.contrib.auth.models import User
from django import forms
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone
#from .forms import PostForm
from .forms import MyForm


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'test/post_list.html', {'posts': posts})



#class MyForm(forms.Form):
#    original_field = forms.CharField()
#    extra_field_count = forms.CharField(widget=forms.HiddenInput())
#
#    def __init__(self, *args, **kwargs):
#        extra_fields = kwargs.pop('extra', 0)
#
#        super(myform, self).__init__(*args, **kwargs)
#        self.fields['extra_field_count'].initial = extra_fields
#
#        for index in range(int(extra_fields)):
#            # generate extra fields in the number specified via extra_fields
#            self.fields['extra_field_{index}'.format(index=index)] = \
#                forms.charfield()

def post_new(request):
    if request.method == 'POST':
        form = MyForm(request.POST, extra=request.POST.get('extra_field_count'))
        if form.is_valid():
            print "valid!"
    else:
        form = MyForm()
    return render(request, 'test/post_edit.html', {'form': form})

#def post_new(request):
#    if request.method == "POST":
#        form = MyForm(request.POST)
#        if form.is_valid():
#            post = form.save(commit=False)
#            post.author = request.user
#            post.published_date = timezone.now()
#            post.save()
#            return redirect('post_detail', pk=post.pk)
#    else:
#        form = MyForm()
#    #return render(request, 'blog/post_edit.html', {'form': form})
#    return render(request, 'test/post_edit.html', {'form': form})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'test/post_detail.html', {'post': post})


