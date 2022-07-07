from django.shortcuts import render
from django.http import request
from django.views import generic
from blog import models

class Index(generic.ListView):
    model = models.Post
    template_name = 'index.html'

class Posts(generic.ListView):
    model = models.Post
    template_name = 'posts.html'

class Post(generic.DetailView):
    model = models.Post
    template_name = 'post.html'

class Contact(generic.TemplateView):
    template_name = 'contact.html'

class Donate(generic.TemplateView):
    template_name = 'donate.html'