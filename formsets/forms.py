from django.forms import TextInput, Textarea
from suit.widgets import AutosizedTextarea

from django.forms.formsets import BaseFormSet
from django import forms
from django.forms import formset_factory
from .models import *
from django.forms import ModelForm


TYPES = (
    ('S', 'Symptoms/Lab Tests'),
    ('D', 'Diagnosis'),
    ('T', 'Treatment'),
)

class TodoListForm(ModelForm):
  class Meta:
    model = TodoList
    fields = "__all__"



class TodoItemForm(ModelForm):
  #another = forms.MultipleChoiceField(choices = COLORS)
  Type = forms.ChoiceField(choices = TYPES)
  class Meta:
    model = TodoItem
    widgets = {
        'Descriptions': AutosizedTextarea,

        # You can also specify html attributes
        'Descriptions': AutosizedTextarea(attrs={'rows': 2, 'cols': 30, 'class': 'input-small'}),
    }

    exclude = ('list',)
