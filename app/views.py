from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.

def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']

        to=Topic.objects.get_or_create(topic_name=tn)[0]
        to.save()
        return HttpResponse('insert_topic sucessfully!!!')
    return render(request,'insert_topic.html')


def insert_webpage(request):
    LTO=Topic.objects.all()
    d={'topic':LTO}
    if request.method=='POST':
        tn=request.POST['topic']
        Name=request.POST['nm']
        url=request.POST['ur']
        Email=request.POST['em']

        to=Topic.objects.get_or_create(topic_name=tn)[0]
        to.save()
        wo=Webpage.objects.get_or_create(topic_name=to,name=Name,url=url,email=Email)[0]
        wo.save()
        return HttpResponse('inserted_webpage data sucessfully!!!')

    return render(request,'insert_webpage.html',context=d)


def insert_access(request):
        lwo=Webpage.objects.all()
        d={'web':lwo}
        if request.method=='POST':
            name=request.POST['name']
            author=request.POST['au']
            date=request.POST['dt']

            wo=Webpage.objects.get_or_create(name=name)[0]   
            ao=AccessRecord.objects.get_or_create(name=wo,author=author,date=date)[0]
            ao.save()

            return HttpResponse('insert_access data sucessfully!!!')

        return render(request,'insert_access.html',context=d)
def display_webpage(request):
    low=Webpage.objects.all()
    d={'webpage':low}
    return render(request,'display_webpage.html',d)