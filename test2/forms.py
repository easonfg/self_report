
from django import forms

from .models import Post

#class PostForm(forms.ModelForm):
#
#    class Meta:
#        model = Post
#        fields = ('title', 'text',)

#class MyForm(forms.Form):
#    original_field = forms.CharField()
#    extra_field_count = forms.CharField(widget=forms.HiddenInput())
#
#    def __init__(self, *args, **kwargs):
#        extra_fields = kwargs.pop('extra', 0)
#
#        super(MyForm, self).__init__(*args, **kwargs)
#        self.fields['extra_field_count'].initial = extra_fields
#
#        for index in range(int(extra_fields)):
#            # generate extra fields in the number specified via extra_fields
#            self.fields['extra_field_{index}'.format(index=index)] = \
#                forms.CharField()


#def myview(request):
#    if request.method == 'POST':
#        form = MyForm(request.POST, extra=request.POST.get('extra_field_count'))
#        if form.is_valid():
#            print "valid!"
#    else:
#        form = MyForm()
#    return render(request, "template", { 'form': form })


class TestCharField(forms.CharField):
    def __init__(self, *args, **kwargs):
        super(TestCharField, self).__init__(*args, **kwargs) # Needs * and **
    def clean(self, value):
        super(TestCharField, self).clean(value)
        # Do custom validation in here
        return value

class testform(forms.Form):
    def __init__(self, *args, **kwargs):
        super(testform, self).__init__(args, kwargs)

        # args should be a list with the single QueryDict (GET or POST dict)
        # that you passed it
        for k,v in args[0].items():
            if k.startswith('Q') and k not in self.fields.keys():
                self.fields[k] = TestCharField(initial=v, required=True)
