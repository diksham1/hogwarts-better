from django import forms
from .models import Student
from django.core.exceptions import ValidationError


class SearchForm(forms.Form):
    student_name = forms.CharField()

class RegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Student
        fields = '__all__'
