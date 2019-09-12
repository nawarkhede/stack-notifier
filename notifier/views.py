from django.shortcuts import render

from .models import StackOverflow


def index(request):
    stacks = StackOverflow.objects.order_by("-question_id")
    return render(request, "index.html", {"stacks": stacks})
