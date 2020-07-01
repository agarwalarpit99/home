from . import views
from django.urls import path

urlpatterns=[
	path('',views.home,name="home"),
	path('about',views.about,name="about"),
	path('admissions',views.admissions,name='admissions'),
	path('contact',views.contact,name='contact'),
	path('calendar',views.calendar,name='calendar'),
	path('registration',views.registration,name='registration')

]
