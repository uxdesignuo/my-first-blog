from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# def home(request):
#   return HttpResponse('<h1>Blog2 Home</h1>')

# def about(request):
#   return HttpResponse('<h1>Blog2: About</h1>')

def post_list(request):
  return render(request, 'blog_2/post_list.html')