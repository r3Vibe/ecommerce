from django.shortcuts import render, HttpResponse

# Create your views here.


def store(req, category_slug=None):
    return HttpResponse(f"{category_slug}")
