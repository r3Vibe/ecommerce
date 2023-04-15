from django.shortcuts import render
from .models import Banner

# Create your views here.


def home_page(req):
    currentBanner = Banner.objects.get(is_featured=True)
    context = {
        'banner': currentBanner
    }
    return render(req, 'test.html', context=context)
