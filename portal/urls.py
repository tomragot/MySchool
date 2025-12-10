"""
URL configuration for myschool project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.admin, name='admin'),
    # path('add_item/', views.add_item, name='add_item'),








    # path('admissions/request/', views.admissions_request, name='admissions_request'),
    # path('application/', views.submit_application, name='submit_application'),


    # path('admissions-request/', views.admissions_request, name='admissions_request'),

    path('index/', views.index, name='index'),
    path('admissions/', views.admissions, name='admissions'),
    path('about/', views.about, name='about'),
    path('404/', views.error, name='404'),
    path('about/',views.about, name='about'),
    path('academics/', views.academics, name='academics'),
    path('contact/',views.contact, name='contact'),
    path('alumni/',views.alumni, name='alumni'),
    path('assessment_list/',views.assessment_list, name='assessment_list'),
    path('campus-facilities/',views.campus_facilities, name='campus-facilities'),
    path('create_assessment/',views.create_assessment, name='create_assessment'),
    path('eventDetails/', views.eventDetails, name='eventDetails'),
    path('events/', views.events, name='events'),
    path('faculty-staff/',views.faculty_staff, name='faculty-staff'),
    path('news/', views.news, name='news'),
    path('news-details/', views.news_details, name='news-details'),
    path('students-life/', views.students_life, name='students-life'),
    path('termOfservice/',views.termOfservice, name='termOfservice'),
    path('update-assessment/', views.update_assessment, name='update-assessment'),
    path('privacy/', views.privacy, name='privacy'),
    path('starter_page/', views.starter_page, name='starter-page'),
    path('assessments/', views.assessments, name='assessments'),




]
