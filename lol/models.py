from django.db import models

# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return u'%s' % (self.name)

class Snippet(models.Model):
    description = models.CharField(max_length=200)
    code = models.TextField()
    language = models.ForeignKey(Language)
    leet = models.IntegerField(default=0)
    lame = models.IntegerField(default=0)
    def __unicode__(self):
        return u'%s' % (self.code[0:10])

    def _get_score(self):
        "Returns the diff of leet and lame"
        return self.leet - self.lame
    score = property(_get_score)
