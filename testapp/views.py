from django.shortcuts import render
from testapp.crawling import crawling

# Create your views here.
from django.http import HttpResponse

def exam1(request):
     return render(request,'index.html',None)

def exam2(request):
     tmp = crawling()
     context = {
          'images': tmp[0],
          'urls': tmp[1],
          'n': range(len(tmp[0])),
     }
     return render(request, 'exam1.html',context)
