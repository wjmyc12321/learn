# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

#from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def home(request):
    my_dict = {'site':u'自强学堂','content':u'各种IT技术'}
    return render(request,'home.html',{'List1':my_dict})


def add(request,a,b):
    c = int(a) + int(b)
    return HttpResponse(str(c))