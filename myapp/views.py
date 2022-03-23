from django.shortcuts import render
from collections import namedtuple
from django.db.models.fields import EmailField
from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from .models import *


# Create your views here.
class MeView(View):
    def get(self, request):
        return render(request, 'justme.html',{})

def index(request):
    return HttpResponse("Ronald S. Pocong,  BSIT -3  ")