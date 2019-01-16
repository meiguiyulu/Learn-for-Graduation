from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context
from blog.models import BlogPost


def index(request):
    return render(request, 'index.html')

def archive(request):
    posts = BlogPost.objects.all()
    t = loader.get_template('archive.html')
    return HttpResponse(t.render({'posts': posts}))


# Create your views here.
