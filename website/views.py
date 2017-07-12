# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from .models import Faculty, Student, House, Photo, Result
from .forms import SearchForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


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

class PhotoListView(ListView):
    model = Photo
    template_name = 'website/photos.html'

def ResultView(request, pk):
    
    student = get_object_or_404(Student,pk = pk)

    query = Result.objects.filter(student_name = pk);

    subject_and_grades_list = []
    
    for item in query:
        subject_and_grades_list.append((item.subject_name, item.grade))

    return render(request, 'website/result.html', 
        {'student':student,
         'subject_and_grades_list': subject_and_grades_list,
    })

def DisplayResult(request):
    if request.method == 'GET':
        form = SearchForm()

    else: 
        if request.method == 'POST':
            form = SearchForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['student_name']
                name = name.title()
                stu  = get_object_or_404(Student, name = name)
            
                return HttpResponseRedirect(reverse('website:result', args=[str(stu.id)]))
    return render(request, 'website/displayresult.html', {'form': form})
