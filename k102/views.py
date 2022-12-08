from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, Http404
from k102.models import Score
import random
from .forms import IdForm

# Create your views here.
def check(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = IdForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
          new_id = form.cleaned_data['c_id']
          try:
            score_list = Score.objects.get(c_id=new_id)
            return render(request, 'k102/check2.html', {'score_list': score_list})
          except:
            return render(request, 'k102/check2.html', {'new_id': new_id})


    else:
        form = IdForm()
        return render(request, 'k102/check.html', {'form': form})
