from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    params= {}
    params['site_name'] = "@Django Blog"

    return render(request, 'blog/index.html', params)