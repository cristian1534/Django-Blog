from django.urls import path
from blog import views

urlpatterns = [
    path('', views.index, name="index"),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('contact', views.contact, name="contact"),
]
