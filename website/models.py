from __future__ import unicode_literals
from django.db import models
import datetime
from django.urls import reverse

YEAR_CHOICES = []

for r in range(1980, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r,r))


class Student(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField('Date of Birth')
    semester = models.IntegerField()
    interests = models.CharField(max_length=300)
    description = models.TextField(help_text="A brief bio of the student")
    picture = models.FileField(blank = True, null=True)
    house = models.ForeignKey('House', on_delete=models.CASCADE)
    subjects = models.ManyToManyField('Subject')

    def __str__(self):
        return self.name + ", Semester " + str(self.semester)


class Faculty(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField('Date of Birth')
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)
    CHOICES = (
        ('owl', 'Owl'),
        ('newt', 'Newt'),
        ('above newt', 'Above Newt'),
    )
    qualification = models.CharField(max_length=30, choices = CHOICES)
    experience = models.IntegerField(default=0)
    research_areas = models.CharField(max_length=500)
    picture = models.FileField(blank=True, null = True)
    description = models.TextField()

    def __str__(self):
        return self.name +', ' + str(self.subject.name) + ' faculty'

    def get_absolute_url(self):
        return reverse('website:faculty-detail-view', args=[str(self.id)])



class House(models.Model):
    name = models.CharField(max_length=100)
    head = models.ForeignKey(Faculty, on_delete = models.CASCADE)
    notable_alumini = models.CharField(max_length=500)
    description = models.TextField()
    photo = models.FileField(blank=True, null=True)
    colors = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Photo(models.Model):
    image = models.FileField()
    date = models.DateField()
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title + ', ' + str(self.date)

class Result(models.Model):
    subject_name = models.ForeignKey(Subject, on_delete=models.CASCADE, help_text='Subject')
    student_name = models.ForeignKey(Student, on_delete=models.CASCADE, help_text='Student')
    CHOICES = (
        ('O', 'Outstanding'),
        ('E', 'Exceeds Expectations'),       
        ('A', 'Acceptable'),
        ('P', 'Poor'),
        ('D', 'Dreadful'),
        ('T', 'Troll'),   
    )
    grade = models.CharField(max_length=1, choices=CHOICES)

    def __str__(self):
        return self.stu_name.name + ',' + self.sub_name.name

class Alumini(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField(choices=YEAR_CHOICES)
    current_position = models.CharField(max_length=500, help_text="What the Alumini is currently doing e.g Student, Software Engineer etc")
    joining_date = models.DateField(help_text='Date of joining this position')

    def __str__(self):
        return self.name


class Rule(models.Model):
    title = models.CharField(max_length=500)
    wef = models.DateField('With Effect From')
    description = models.TextField()
    
    def __str__(self):
        return str(self.wef) + ': ' + self.title;


class Infrastructure(models.Model):
    name = models.CharField(max_length=100)
    no = models.IntegerField('Number')
    picture = models.FileField()
    description = models.TextField()
    
    def __str__(self):  
        return self.name


class Acheivement(models.Model):
    title = models.CharField(max_length=500)
    student_name = models.ForeignKey(Student, on_delete=models.CASCADE)
    year = models.IntegerField(choices=YEAR_CHOICES)
    description = models.TextField()

    def __str__(self):
        return self.title + ' by ' + self.stu_name.name


class News(models.Model):
    title = models.CharField(max_length=500)
    date = models.DateField()
    description = models.TextField()
    
    def __str__(self):
        return str(self.date) + ': ' + self.title




#####################   END   ######################
