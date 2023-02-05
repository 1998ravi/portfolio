from typing import FrozenSet
from django.http.response import FileResponse
from django.shortcuts import render
from  django.shortcuts import  HttpResponse
from .models import pr,c

# Create your views here.
def index(request):
    if request.method=='POST':
        n=request.POST['n']
        e=request.POST['e']
        cmnt=request.POST['c']
        cm=c(com=cmnt,n=n,e=e)
        cm.save()


        return render(request,'index.html')
    j=pr.objects.all()
    print(j)
    for i in j:
        print(i.Tech)
    
    return render(request,'index.html',{'j':j})