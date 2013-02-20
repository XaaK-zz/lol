# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response, get_object_or_404, redirect
from lol.models import Snippet, Language

def index(request):
    random = Snippet.objects.order_by('?')[0]
    return render_to_response('index.html', {'snippet': random}, context_instance=RequestContext(request))

def upload(request):
    languages = Language.objects.all().order_by('name')
    return render_to_response('upload.html', {'languages': languages}, context_instance=RequestContext(request))

def rate(request, snippet_id):
    s = get_object_or_404(Snippet, pk=snippet_id)
    bias = request.POST['submitButton']
    if (bias == 'Leet'):
        s.leet += 1
    elif(bias == 'Lame'):
        s.lame += 1
    s.save()
    return redirect('index')

def new(request):
    lang = get_object_or_404(Language, pk=request.POST['language_id'])
    s = Snippet(code=request.POST['code'], language=lang)
    s.save()
    return redirect('index')

