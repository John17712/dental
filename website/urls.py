from django.urls import path
from . import views

urlpatterns = [
    path('home.html', views.home, name='home'),
    path('contact.html', views.contact, name='contact'),
    path('about.html', views.about, name='about'),
    path('service.html', views.service, name='service'),
    path('price.html', views.price, name='price'),
    path('team.html', views.team, name='team'),
    path('testimonial.html', views.testimonial, name='testimonial'),
    path('appointment.html', views.appointment, name='appointment'),

]