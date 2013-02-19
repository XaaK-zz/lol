from django.db import models

class Language(models.Model):
    name = models.CharField(max_length=200)

class snippet(models.Model):
    code = models.TextField()
    language = models.ForeignKey(Language)
    leet = models.IntegerField()
    lame = models.IntegerField()
# Create your models here.
#CREATE TABLE snippets (id INTEGER PRIMARY KEY, code text, lang_id INTEGER, leet_count INTEGER DEFAULT 0, lame_count INTEGER DEFAULT 0);
