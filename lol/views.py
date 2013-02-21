# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response, get_object_or_404, redirect
from lol.models import Snippet, Language
import requests, json

def index(request):
    if request.method == 'GET':
        random = Snippet.objects.order_by('?')[0]
        return render_to_response('index.html', {'snippet': random}, context_instance=RequestContext(request))
    elif request.method == 'POST':
        return redirect('index')

def rate(request, snippet_id):
    s = get_object_or_404(Snippet, pk=snippet_id)
    bias = request.POST['submitButton']
    if (bias == 'Leet'):
        s.leet += 1
    elif(bias == 'Lame'):
        s.lame += 1
    s.save()
    return redirect('index')


def upload(request):
    if request.method == 'GET':
        languages = Language.objects.all().order_by('name')
        return render_to_response('upload.html', {'languages': languages}, context_instance=RequestContext(request))
    elif request.method == 'POST':
        lang = get_object_or_404(Language, pk=request.POST['language_id'])
        s = Snippet(code=request.POST['code'], description=request.POST['description'], language=lang)
        s.save()
        return redirect('index')

def top(request, limit):
    limit = int(limit)
    top = sorted(Snippet.objects.all(), key=lambda a: a.score)[:limit]
    return render_to_response('top.html', {'top': top, 'limit': limit})

def view(request, snippet_id):
    snippet = get_object_or_404(Snippet, pk=snippet_id)
    return render_to_response('view.html', {'snippet': snippet})

def import_gist(request):
    if request.method == 'POST':
        gist_id = request.POST['gist_id']
        r = requests.get("https://api.github.com/gists/%s" % gist_id)
        data = json.loads(r.content)
        description = data['description']
        files = data['files'].keys()
        first = data['files'][files[0]]
        #lang = first['language']
        raw_url = first['raw_url']
        file_request = requests.get(raw_url)
        code = file_request.content
        lang = get_object_or_404(Language, pk=request.POST['language_id'])
        s = Snippet(code=code, description=description, language=lang)
        s.save()
        return redirect('index')
        #return HttpResponse("%s." % code)

    elif request.method == 'GET':
        languages = Language.objects.all().order_by('name')
        return render_to_response('import_gist.html', {'languages': languages}, context_instance=RequestContext(request))

