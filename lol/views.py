# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader, RequestContext
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from lol.models import Snippet, Language
from django.core.exceptions import ValidationError
from lol.forms import UploadForm

def index(request):
    if request.method == 'GET':
        random = Snippet.objects.filter(approved=True).order_by('?')[0]
        thanks = False
        if request.session.get('thanks', False):
            request.session['thanks'] = False
            thanks = True
        return render_to_response('index.html', {'snippet': random, 'thanks': thanks},
                                  context_instance=RequestContext(request))
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
            userName = form.cleaned_data['userName']
            if(gistId):
                s = Snippet(code=formCode.strip(), description=desc.strip(), gist_id=gistId, language=lang,userName=userName.strip())
            else:
                s = Snippet(code=formCode.strip(), description=desc.strip(), language=lang, userName=userName.strip())
            if s.validate():
                s.save()
            else:
                return render(request, 'upload.html', {
                    'form':                form,
                    'error_message':       "Looks like we already have that code in our system." ,
                    'error_message_title': "Oops sorry!"
                })
            request.session['thanks'] = True
            return redirect('index')
        else:
            return render(request, 'upload.html', {
                'form': form
            })

def top(request, limit):
    limit = int(limit)
    top = sorted(Snippet.objects.filter(approved=True), key=lambda a: a.score, reverse=True)[:limit]
    return render_to_response('top.html', {'top': top, 'limit': limit},
                              context_instance=RequestContext(request))

def view(request, snippet_id):
    snippetList = Snippet.objects.filter(pk=snippet_id).filter(approved=True)
    if len(snippetList) == 1:
        return render_to_response('view.html', {'snippet': snippetList[0]},context_instance=RequestContext(request))
    else:
        return redirect('index')

def bylang(request, language_name):
    lang = get_object_or_404(Language, name=language_name)
    snippet = Snippet.objects.filter(language=lang).filter(approved=True).order_by('?')[0]
    return render_to_response('index.html', {'snippet': snippet},context_instance=RequestContext(request))

