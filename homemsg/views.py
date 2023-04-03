from django.shortcuts import render,redirect
from . import models
from django.shortcuts import HttpResponse
import markdown
# Create your views here.

def getpagelist(request):
	obj=models.articlePags.objects.all()
	return render(request,'../template/homepagev2.html',{'obj':obj,'murl':"/media/"})

def getpages(request,ida):
    obj=None
    try:
    	obj=models.articlePags.objects.get(uuids=ida)
    except Exception:
        return render(request,'../template/404.html')
    article=obj.mdtext
    return render(request,'../template/articlepage.html', {'article': article,"title":obj.title,'time':obj.time})
def getpagesida(request,ida):
    obj=None
    try:
    	obj=models.articlePags.objects.get(id=ida)
    except Exception:
        return render(request,'../template/404.html')
    article=obj.mdtext
    return render(request,'../template/articlepage.html', {'article': article,"title":obj.title,'time':obj.time})