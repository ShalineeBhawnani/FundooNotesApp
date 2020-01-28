from django.shortcuts import render
from django.http import HttpResponse
from .models import Note


def index(request):
    return HttpResponse("Hello, world. You're at the smaple note index.")