from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
# Create your views here.

def posts_home(request):
	return HttpResponse("<h1>Hello</h1>")