from __future__ import unicode_literals

from django.db import models


class TodoList(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name



class TodoItem(models.Model):
    Type = models.CharField(max_length=150,default='')
    Descriptions = models.TextField()
    list = models.ForeignKey(TodoList)
    #another = models.ChoiceField(choices=COLORS, label=u'Country')

               #help_text="e.g. Buy milk, wash dog etc",

    #Descriptions = models.CharField(max_length=150, default = ''

    def __unicode__(self):
        return self.name + " (" + str(self.list) + ")"
