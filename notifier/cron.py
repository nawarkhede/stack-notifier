import os
import sys
import django

BASE_DIRECTORY = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))  # noqa
sys.path.append(BASE_DIRECTORY)  # noqa
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")  # noqa
django.setup()

from bs4 import BeautifulSoup  # NOQA
import urllib2  # NOQA
from django.db import IntegrityError  # NOQA
from notifier import models  # NOQA


def read_so():
    ctr = 0
    tags = ['python', 'python-2.7', 'django']
    for tag in tags:
        page = urllib2.urlopen('https://stackoverflow.com/questions/tagged/%s' % tag)
        soup = BeautifulSoup(page, 'html.parser')
        questions = soup.findAll("div", {"class": "question-summary"})
        for q in questions:
            title = q.find('a').text
            summary = q.find('div', {'class': 'excerpt'}).text
            url = q.find('a')['href']
            q_id = url.split('/')[2]
            href = 'http://stackoverflow.com%s' % url

            try:
                stack = models.StackOverflow.objects.create(
                    question_id=int(q_id),
                    title=title,
                    summary=summary,
                    href=href
                )
            except IntegrityError:
                print('Question with id %s already exists, skip to next...' % q_id)
            else:
                print('object created..')

    print ctr


read_so()
