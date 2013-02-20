# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render_to_response
from lol.models import Snippet, Language

def index(request):
    random = Snippet.objects.order_by('?')[0]
    return render_to_response('index.html', {'snippet': random})

def upload(request):
        return HttpResponse("Hello, world. You're at the upload page.")
