from django.shortcuts import render

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
#from .forms import NameForm, ContactForm, PostForm, js_form
from .forms import js_form



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

    return render(request, 'test/index.html', {'form': form})
