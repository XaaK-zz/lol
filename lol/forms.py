from django import forms
from lol.models import Snippet, Language

class UploadForm(forms.Form):
    description = forms.CharField(max_length=200)
    description.widget = forms.TextInput(attrs={"class":"input-block-level","required":""})
    inputCode = forms.CharField(widget=forms.Textarea(attrs={"rows":"10","class":"input-block-level"}))
    language = forms.ModelChoiceField(queryset=Language.objects.all().extra(select={'lower_name': 'lower(name)'}).order_by('lower_name'), empty_label=None)
    gist_id = forms.IntegerField(required=False)