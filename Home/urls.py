from django.contrib import admin
from django.urls import path
from Home import views
urlpatterns = [
    path('',views.index,name='home'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('applicantportal',views.applicant,name='applicantPortal')
]
