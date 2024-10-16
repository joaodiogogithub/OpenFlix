from django.shortcuts import render
from django.db import models
from .models import Movie
from django.views.generic import ListView, UpdateView
from django.urls import reverse_lazy

# Create your views here.
def home(request):
    return render(request, 'app/home.html')

class MovieListView(ListView):
    model = Movie
    template_name = 'app/home.html'
    context_object_name = 'movies'
    ordering = ['title']

class titlesUpdateView(UpdateView):
    model = Movie
    fields = ['title','genre','descripton','qnt_episodes','rating']
    success_url = reverse_lazy('home')
    template_name = 'app/title_page.html'