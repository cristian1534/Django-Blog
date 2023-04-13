from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    params= {}
    params['site_name'] = '@Django Blog-home'

    return render(request, 'blog/index.html', params)

def register(request):
    params= {}
    params['site_name'] = '@Django Blog-register'

    return render(request, 'blog/register.html', params)

def login(request):
    params= {}
    params['site_name'] = '@Django Blog-login'
    
    return render(request, "blog/login.html", params)

def contact(request):
    params= {}
    params['site_name'] = '@Django Blog-contact'

    return render(request, 'blog/contact.html', params)