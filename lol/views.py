# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader, RequestContext
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from lol.models import Snippet, Language
from django.core.exceptions import ValidationError
from lol.forms import UploadForm

def index(request):
    if request.method == 'GET':
        random = Snippet.objects.order_by('?')[0]
        return render_to_response('index.html', {'snippet': random}, context_instance=RequestContext(request))
    elif request.method == 'POST':
        bias = request.POST['submitButton']
        snippet_id = request.POST['snippet_id']
        s = get_object_or_404(Snippet, pk=snippet_id)
        if (bias == 'Leet'):
            s.leet += 1
        elif(bias == 'Lame'):
            s.lame += 1
        s.save()
        return redirect('index')


def upload(request):
    if request.method == 'GET':
        #default_lang = Language.objects.get(name='Python')
        #form = UploadForm(initial = {'language': default_lang.pk})
        form = UploadForm()
        return render(request, 'upload.html', {
            'form': form
        })
    elif request.method == 'POST':
        form = UploadForm(request.POST) 
        if form.is_valid():
            desc = form.cleaned_data['description']
            formCode = form.cleaned_data['inputCode']
            lang = form.cleaned_data['language']
            gistId = form.cleaned_data['gist_id']
            if(gistId):
                s = Snippet(code=formCode.strip(), description=desc.strip(), gist_id=gistId, language=lang)
            else:
                s = Snippet(code=formCode.strip(), description=desc.strip(), language=lang)
            if s.validate():
                s.save()
            else:
                return render(request, 'upload.html', {
                    'form':                form,
                    'error_message':       "Looks like we already have that code in our system." ,
                    'error_message_title': "Oops sorry!"
                })
            return redirect('view', snippet_id=s.id)
        else:
            return render(request, 'upload.html', {
                'form': form
            })

def top(request, limit):
    limit = int(limit)
    top = sorted(Snippet.objects.all(), key=lambda a: a.score, reverse=True)[:limit]
    return render_to_response('top.html', {'top': top, 'limit': limit})

def view(request, snippet_id):
    snippetList = Snippet.objects.filter(pk=snippet_id)
    if len(snippetList) == 1:
        return render_to_response('view.html', {'snippet': snippetList[0]})
    else:
        return redirect('index')
        
    #snippet = get_object_or_404(Snippet, pk=snippet_id)
    #return render_to_response('view.html', {'snippet': snippet})

def bylang(request, language_name):
    lang = get_object_or_404(Language, name=language_name)
    snippet = Snippet.objects.filter(language=lang).order_by('?')[0]
    return render_to_response('index.html', {'snippet': snippet})

