from django.conf.urls import url
from . import views

app_name = 'website'

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^about/', views.about, name="about"),
    url(r'^faculty/$', views.FacultyListView.as_view(), name="faculty-list-view"),
    url(r'^faculty/(?P<pk>[0-9]+)/', views.FacultyDetailView.as_view(), name="faculty-detail-view"),
    url(r'^students/(?P<pk>[0-9]+)/', views.StudentDetailView.as_view(), name="student-detail-view"),
    url(r'^students/$', views.StudentListView.as_view(), name="student-list-view"),
    url(r'^houses/(?P<pk>\d)/', views.HouseDetailView.as_view(), name="house-detail-view"),
]
