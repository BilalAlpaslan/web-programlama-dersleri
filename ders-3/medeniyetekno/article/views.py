from django.shortcuts import render
from django.http import HttpResponse
from .models import article


# def home(request):
#     return HttpResponse("hello world")


def home(request):
    makaleler = article.objects.all()
    return render(request,"main.html",{"makaleler":makaleler})

def detail(request,slug):
    makale=article.objects.get(title=slug)
    return render(request,"detail.html",{"makale":makale})