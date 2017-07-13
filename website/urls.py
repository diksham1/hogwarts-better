from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'website'

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^about/', views.about, name="about"),
    url(r'^faculty/$', views.FacultyListView.as_view(), name="faculty-list-view"),
    url(r'^faculty/(?P<pk>[0-9]+)/', views.FacultyDetailView.as_view(), name="faculty-detail-view"),
    url(r'^students/(?P<pk>[0-9]+)/', views.StudentDetailView.as_view(), name="student-detail-view"),
    url(r'^students/$', views.StudentListView.as_view(), name="student-list-view"),
    url(r'^results/(?P<pk>\d+)', views.ResultView, name="result"),
    url(r'^displayresult', views.DisplayResult, name="display"),
    url(r'^register/', views.Register, name="register"),
    url(r'^houses/(?P<pk>\d)/', views.HouseDetailView.as_view(), name="house-detail-view"),
    url(r'^media/$', views.PhotoListView.as_view(), name="photo-list-view")]

urlpatterns += static(settings.STATIC_URL,
document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

