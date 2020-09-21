from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Publisher
import json


# Create your views here.


def search_form(request):
    return render(request, 'search_form.html')


# def search(request):
#     error = True
#     if 'q' in request.GET:
#         q = request.GET["q"]
#         if not q:
#             error = True
#         else:
#             error = False
#             message = Publisher.objects.filter(name=q)
#             # return HttpResponse(error)
#             return render(request, "search_form.html", {'message': message, 'key': q})
#     else:
#         error = False
#         # message = f" You must send book name"
#     return render(request, "search_form.html", {"message": error})
def search(request):
    return render(request, "文件.html")


def logon(request):
    return render(request, "Home.html")


def ajax(request):
    return render(request, "图表.html")


def ajaxe(request):
    data = {"1": 1, "2": 2}
    # return render(request,"ajax.html", {"data": data})
    return HttpResponse(data, content_type='application/javascript')


def form(request):
    return render(request, 'test.html')


def classification(request):  # 分类
    return render(request, '分类.html')


def about(request):
    return render(request, 'about.html')
