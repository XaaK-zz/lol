from django.db import models
import hashlib

class Language(models.Model):
    name            = models.CharField(max_length=200)
    language_class  = models.CharField(max_length=200)
    
    def __unicode__(self):
        return u'%s' % (self.name)

class Snippet(models.Model):
    description = models.CharField(max_length=200)
    code        = models.TextField(max_length=1000)
    code_hash   = models.CharField(max_length=40, unique=True)
    language    = models.ForeignKey(Language)
    parent      = models.ForeignKey('self', null=True)
    leet        = models.IntegerField(default=0)
    lame        = models.IntegerField(default=0)
    gist_id     = models.IntegerField(default=0,null=True)
    approved    = models.BooleanField(default=False)
    userName    = models.CharField(max_length=200)
    
    def __unicode__(self):
        return u'%s' % (self.description)

    def _get_score(self):
        "Returns the diff of leet and lame"
        return self.leet - self.lame

    def validate(self):
        self.code_hash = hashlib.sha1(self.code.strip()).hexdigest()
        checkQuery = Snippet.objects.filter(code_hash=self.code_hash)
        
        return len(checkQuery) == 0
    
    score = property(_get_score)
