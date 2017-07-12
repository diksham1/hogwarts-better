from django import forms
from .models import Student
from django.core.exceptions import ValidationError


class SearchForm(forms.Form):
    student_name = forms.CharField()
