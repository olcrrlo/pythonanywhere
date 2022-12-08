from django.db import models

# Create your models here.
class ExResult(models.Model):
    type = models.CharField(max_length=10)
    em1 = models.IntegerField(default=0)
    em2 = models.IntegerField(default=0)
    em3 = models.IntegerField(default=0)
    em4 = models.IntegerField(default=0)
    em5 = models.IntegerField(default=0)
    em6 = models.IntegerField(default=0)
    em7 = models.IntegerField(default=0)
    clt1 = models.IntegerField(default=0)
    clt2 = models.IntegerField(default=0)
    clt3 = models.IntegerField(default=0)
    clt4 = models.IntegerField(default=0)
    clt5 = models.IntegerField(default=0)
    dist1 = models.IntegerField(default=0)
    dist2 = models.IntegerField(default=0)
    dist3 = models.IntegerField(default=0)
    pana1 = models.IntegerField(default=0)
    pana2 = models.IntegerField(default=0)
    pana3 = models.IntegerField(default=0)
    pana4 = models.IntegerField(default=0)
    pana5 = models.IntegerField(default=0)
    pana6 = models.IntegerField(default=0)
    pana7 = models.IntegerField(default=0)
    pana8 = models.IntegerField(default=0)
    pana9 = models.IntegerField(default=0)
    pana10 = models.IntegerField(default=0)
    pana11 = models.IntegerField(default=0)
    pana12 = models.IntegerField(default=0)
    pana13 = models.IntegerField(default=0)
    pana14 = models.IntegerField(default=0)
    pana15 = models.IntegerField(default=0)
    pana16 = models.IntegerField(default=0)
    pana17 = models.IntegerField(default=0)
    pana18 = models.IntegerField(default=0)
    pana19 = models.IntegerField(default=0)
    pana20 = models.IntegerField(default=0)
    check1 = models.IntegerField(default=0)
    check2 = models.IntegerField(default=0)
    check3 = models.IntegerField(default=0)
    phone = models.CharField(max_length=15)
    Snum = models.CharField(max_length=9)
    Cname = models.CharField(max_length=50)
    starttime = models.DateTimeField('date published')
    endtime = models.DateTimeField('date published')

    def __unicode__(self):  # __str__ on Python 3
        return self.ExResult_id







