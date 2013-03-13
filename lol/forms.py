from django import forms
from lol.models import Snippet, Language
from django.core.exceptions import ValidationError
import re

def validate_code(value):
    regex = re.compile("\r\n?|\n")
    match = regex.findall(value)
    
    if len(match) > 30:
        raise ValidationError("Sorry - too many lines.")
        
        
class UploadForm(forms.Form):
    description = forms.CharField(max_length=200)
    description.widget = forms.TextInput(attrs={"class":"input-block-level","required":""})
    inputCode = forms.CharField(widget=forms.Textarea(attrs={"rows":"10","class":"input-block-level"}),
                                validators=[validate_code],
                                max_length=2000)
    language = forms.ModelChoiceField(queryset=Language.objects.all().extra(select={'lower_name': 'lower(name)'}).order_by('lower_name'),
                                      empty_label="Select a language...")
    userName = forms.CharField(max_length=200,required=False)
    
    gist_id = forms.IntegerField(required=False)
    
    
    