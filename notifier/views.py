from django.http import HttpResponse
from django.shortcuts import render
from bs4 import BeautifulSoup
import urllib2


def index(request):
    return render(request, 'index.html', {})


def read_so():
    ctr = 0
    page = urllib2.urlopen('https://stackoverflow.com/questions/tagged/python-2.7')
    soup = BeautifulSoup(page, 'html.parser')
    questions = soup.findAll("div", {"class": "question-summary"})
    for q in questions:
        title = q.find('a').text
        summary = q.find('div', {'class': 'excerpt'}).text
        url = q.find('a')['href']
        q_id = url.split('/')[2]
        href = 'http://stackoverflow.com%s' % url

        print title
        print summary
        print url
        print q_id
        print href
        ctr +=1

    print ctr



