# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response, get_object_or_404, redirect
from lol.models import Snippet, Language

def index(request):
    random = Snippet.objects.order_by('?')[0]
    return render_to_response('index.html', {'snippet': random})

def upload(request):
    languages = Language.objects.all().order_by('name')
    return render_to_response('upload.html', {'languages': languages}, context_instance=RequestContext(request))

def rate(request, snippet_id):
    #log it
    return redirect('index')

def new(request):
    lang = get_object_or_404(Language, pk=request.POST['language'])
    s = Snippet(code=request.POST['code'], language=lang)
    s.save()
    return redirect('index')

