
from django import forms
from django.forms import formset_factory
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('Symptoms', 'Treatments','Diagnosis',)


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)


class ArticleForm(forms.Form):
    title = forms.CharField()
    pub_date = forms.DateField()



class js_form(forms.Form):
    Symptoms = forms.CharField(widget=forms.Textarea)
    Diagnosis = forms.CharField(widget=forms.Textarea)
    Treatment =forms.CharField(widget=forms.Textarea)
