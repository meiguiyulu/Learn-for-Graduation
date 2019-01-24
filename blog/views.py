from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, RequestContext
from blog.models import BlogPost
from datetime import datetime


def index(request):
    return render(request, 'index.html')

def archive(request):
    posts = BlogPost.objects.all().order_by('-timestamp')
    t = loader.get_template('archive.html')
    return HttpResponse(t.render({'posts': posts}))
    #return render_to_response('archive.html', {'posts': posts,},RequestContext(request))

def create_blogpost(request):
    if request.method == 'POST':
        BlogPost(
            title=request.POST.get('title'),
            body=request.POST.get('body'),
            timestamp=datetime.now()
        ).save()
    return HttpResponseRedirect('/blog/')

# Create your views here.
