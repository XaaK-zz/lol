from django.db import models
        
class Language(models.Model):
    name            = models.CharField(max_length=200)
    language_class  = models.CharField(max_length=200)
    
    def __unicode__(self):
        return u'%s' % (self.name)

class Snippet(models.Model):
    description = models.CharField(max_length=200)
    code        = models.TextField(max_length=1000)
    language    = models.ForeignKey(Language)
    parent      = models.ForeignKey('self', null=True)
    leet        = models.IntegerField(default=0)
    lame        = models.IntegerField(default=0)
    gist_id     = models.IntegerField(default=0,null=True)
    
    def __unicode__(self):
        return u'%s' % (self.description)

    def _get_score(self):
        "Returns the diff of leet and lame"
        return self.leet - self.lame

    score = property(_get_score)
