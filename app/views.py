from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *

#-------------------------------------------------------------------------

def insert_topic(request):
    ETFO = Topicform()
    d = {'ETFO':ETFO}
    if request.method=='POST':
        TFDO = Topicform(request.POST)
        if TFDO.is_valid():
            TFDO.save()
            return HttpResponse('inserted topic')
    return render(request,'insert_topic.html',d)

#-------------------------------------------------------------------------

def insert_webpage(request):
    EWFO = Webpageform()
    d = {'EWFO':EWFO}
    if request.method=='POST':
        EWWO = Webpageform(request.POST)
        if EWWO.is_valid():
            EWWO.save()
            return HttpResponse('webpage inserted')
    return render(request,'insert_webpage.html',d)

#----------------------------------------------------------------------------

def insert_accesrecord(request):
    EAFO = Accessrecordform()
    d = {'EAFO':EAFO}
    if request.method=='POST':
        WADO = Accessrecordform(request.POST)
        if WADO.is_valid():
            WADO.save()
            return HttpResponse('accesrecord inserted')
    return render(request,'insert_accesrecord.html',d)


#-------------------------------------------------------------------------------