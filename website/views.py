# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render, get_object_or_404
from .models import Faculty, Student, House, Photo, Result, Infrastructure
from .forms import SearchForm
from .forms import RegistrationForm
from .models import Alumini, Acheivement
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import datetime


def index(request):
    return render(request, 'website/index.html')

def about(request):
    return render(request, 'website/about.html')

class FacultyListView(ListView):
    model = Faculty
    template_name = 'website/faculty.html'

class AcheivementsListView(ListView):
    model = Acheivement
    template_name = 'website/acheivement.html'

class AluminiCreateView(CreateView):
    model = Alumini
    fields = '__all__'
    template_name = 'website/registration.html'

    def get_success_url(self):
        return reverse('website:alumini-list-view')

class AluminiListView(ListView):
    model = Alumini
    template_name = 'website/alumini.html'

class FacultyDetailView(DetailView):
    model = Faculty
    fields = '__all__'

class StudentListView(ListView):
    model = Student
    template_name = 'website/students.html'

class StudentDetailView(DetailView):
    model = Student
    fields = '__all__'

class InfrastructureListView(ListView):
    model = Infrastructure
    template_name = 'website/infra.html'

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

def Register(request):
    if request.method == 'GET':
        form = RegistrationForm()
    else:
        if request.method == 'POST':
            form = RegistrationForm(request.POST, request.FILES)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                date_joined = datetime.datetime.now()
                new_user = User(username=username, password=password, date_joined=date_joined)
                new_user.save()
                name = form.cleaned_data['name']
                dob = form.cleaned_data['dob']
                year = form.cleaned_data['year']
                interests = form.cleaned_data['interests']
                description = form.cleaned_data['description']
                picture = request.FILES['picture']
                house = form.cleaned_data['house']
                subjects = form.cleaned_data['subjects']
                
                new_stu = Student(name=name, dob=dob, interests=interests,description=description, house=house, picture=picture)
                new_stu.save();
                for subject in subjects:
                    new_stu.subjects.add(subject)
                
                return HttpResponseRedirect(reverse('website:student-list-view'))
    return render(request, 'website/registration.html', {'form': form})
