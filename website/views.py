# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import Faculty


def index(request):
    return render(request, 'website/index.html')

def about(request):
    return render(request, 'website/about.html')

class FacultyListView(ListView):
    model = Faculty
    template_name = 'website/faculty.html'

class FacultyDetailView(DetailView):
    model = Faculty
    fields = '__all__'
