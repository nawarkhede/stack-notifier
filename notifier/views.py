from django.http import HttpResponse
from django.shortcuts import render
from bs4 import BeautifulSoup
import urllib2


def index(request):
    return render(request, 'index.html', {})



