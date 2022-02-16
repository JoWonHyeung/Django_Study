from django.test import TestCase

# Create your tests here.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def exam1(request):
    name = request.GET.get('name', "유니코")  #request.GET['name'] => key값 없으면 오류난다.
    context = {'result': name}              #request.GET.get(key,default value) => 없으면 nonereturn
    return render(request, 'exam2.html', context)