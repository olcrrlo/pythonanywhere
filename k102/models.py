from django.db import models

# Create your models here.
class Score(models.Model):
    c_id = models.CharField(max_length=9)
    test1 = models.CharField(max_length=10)
    test2 = models.CharField(max_length=10)
    test3 = models.CharField(max_length=10)
    test4 = models.CharField(max_length=10)
    test5 = models.CharField(max_length=10)
    test6 = models.CharField(max_length=10)
    test7 = models.CharField(max_length=10)
    test8 = models.CharField(max_length=10)
    test9 = models.CharField(max_length=10)

    def __unicode__(self): # __str__ on Python 3
        return self.score_text