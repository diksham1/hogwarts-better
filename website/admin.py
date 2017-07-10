from __future__ import unicode_literals
from .models import Student, Faculty, House, Subject
from .models import Result, Photo, Infrastructure, Rule, Alumini
from .models import News, Acheivement
from django.contrib import admin


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'dob', 'semester', 'house']
    list_filter = ['house', 'semester']

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ['name', 'dob', 'subject', 'qualification', 'research_areas']
    list_filter = ['qualification', 'experience']

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ['name', 'head', 'colors']

admin.site.register(Subject)

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ['student_name', 'subject_name', 'grade']
    list_filter = ['grade', 'subject_name']

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']

@admin.register(Infrastructure)
class InfrastructureAdmin(admin.ModelAdmin):
    list_display = ['name','no']

@admin.register(Rule)
class RuleAdmin(admin.ModelAdmin):
    list_display = ['title', 'wef']
    list_filter = ['wef',]

@admin.register(Alumini)
class AluminiAdmin(admin.ModelAdmin):
    list_display = ['name', 'year', 'current_position', 'joining_date']
    list_filter = ['year', ]

@admin.register(Acheivement)
class AcheivementAdmin(admin.ModelAdmin):
    list_display = ['title', 'student_name', 'year']

admin.site.register(News)
