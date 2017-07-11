# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import Faculty, Student, House


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

class StudentListView(ListView):
    model = Student
    template_name = 'website/students.html'

class StudentDetailView(DetailView):
    model = Student
    fields = '__all__'

class HouseDetailView(DetailView):
    model = House
    fields = '__all__'
