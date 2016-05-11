from django.shortcuts import render
from blog.models import Post
from django.utils import timezone

# Create your views here.

def index(request):
    return render(request, 'home/index.html', {})
