from django.core.mail import send_mail
from django.contrib.auth.models import User
from django import forms
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone
#from .forms import PostForm
#from .forms import MyForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import NameForm, ContactForm, PostForm, js_form

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            #subject = form.cleaned_data['subject']
            #message = form.cleaned_data['message']
            #sender = form.cleaned_data['sender']
            #cc_myself = form.cleaned_data['cc_myself']

            #recipients = ['info@example.com']
            #if cc_myself:
            #    recipients.append(sender)

            #send_mail(subject, message, sender, recipients)

            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()

            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        #form = NameForm()
        form = ContactForm()

    #return render(request, 'test/manage_articles.html', {'form': form})
    return render(request, 'test/index.html', {'form': form})


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

#def post_new(request):
#    if request.method == 'POST':
#        form = MyForm(request.POST, extra=request.POST.get('extra_field_count'))
#        if form.is_valid():
#            print "valid!"
#    else:
#        form = MyForm()
#    return render(request, 'test/post_edit.html', {'form': form})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            #return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    #return render(request, 'blog/post_edit.html', {'form': form})
    return render(request, 'test/single_edit.html', {'form': form})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'test/post_detail.html', {'post': post})


from django.forms import formset_factory
from django.shortcuts import render_to_response
from .forms import ArticleForm

def manage_articles(request):
    ArticleFormSet = formset_factory(ArticleForm, extra = 3)
    if request.method == 'POST':
        formset = ArticleFormSet(request.POST, request.FILES)
        if formset.is_valid():
            # do something with the formset.cleaned_data
            pass
    else:
        formset = ArticleFormSet()
    return render_to_response('test/manage_articles.html', {'formset': formset})


def dynamic_js(request):
    if request.method == 'POST':
        form = js_form(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()

            return HttpResponseRedirect('/thanks/')

    else:
        form = js_form()

    return render(request, 'test/dynamic_JS_form.html', {'form': form})
