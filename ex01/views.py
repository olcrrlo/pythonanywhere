from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from ex01.models import ExResult
from django.utils import timezone
import random

# Create your views here.
def intro(request):
      return render(request, 'ex01/intro.html')

def p1(request):
      type = random.randrange(1, 3)
      # ex.result.type 의 갯수 가져와서
      p = ExResult.objects.create(type=type, starttime=timezone.now(), endtime=timezone.now())
      return render(request, 'ex01/p1.html')

def p2(request):
      return render(request, 'ex01/p2.html')

def p3(request):
      return render(request, 'ex01/p3.html')


def p4(request):
      return render(request, 'ex01/p4.html')


def p5(request):
      return render(request, 'ex01/p5.html')


def p6(request):
      return render(request, 'ex01/p6.html')