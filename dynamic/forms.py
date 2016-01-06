
from django import forms
from django.forms import formset_factory
from .models import Post

class js_form(forms.Form):
    Symptoms = forms.CharField(widget=forms.Textarea)
    Diagnosis = forms.CharField(widget=forms.Textarea)
    Treatments =forms.CharField(widget=forms.Textarea)
