from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils.crawler import Crawler
from .utils.calendar import Calender


def index(request):
    return HttpResponse('Hello!\nThis is a site of Apis for JHRL.\nIngore if you have no idea.')


@api_view(['GET'])
def getStart(request):
   try:
       crawler = Crawler()
       data = {
           'jsid': crawler.getJsid(),
           'yzmUrl': crawler.getYzm(),
           # 'yzmHeader' : crawler.getYzmHeader()
       }
       return Response(data)
   except:
       return HttpResponse(status=404)


@api_view(['GET'])
def getYzm(request):
    try:
        jsid = request.GET.get('jsid')
        crawler = Crawler(jsid)
        return HttpResponse(crawler.getYzmBin(), content_type="image/png")
    except:
        return HttpResponse(status=404)


@api_view(['POST'])
def login(request):
    try:
        username = request.POST.get('username')
        password = request.POST.get('password')
        yzm = request.POST.get('yzm')
        jsid = request.POST.get('jsid')
        crawler = Crawler(jsid)
        resl = crawler.login(username, password, yzm)
        return Response(resl)
    except:
        #return Response(resl)
        return HttpResponse(status=404)


@api_view(['GET'])
def getSettings(request):
    try:
        #jsid = request.GET.get('username')
        res = {
            'schoolStartDate': "2019-9-16",
            'schoolTotalWeeks': "16"
        }
        return Response(res)
    except:
        return HttpResponse(status=404)


@api_view(['GET'])
def getKb(request):
    try:
        xq = request.GET.get('xq')
        xn = request.GET.get('xn')
        jsid = request.GET.get('jsid')
        crawler = Crawler(jsid)
        res = crawler.getKb(xn, xq)
        return HttpResponse(res)
    except:
        return HttpResponse(status=404)


@api_view(['GET'])
def getIcs(request):
    try:
        xq = request.GET.get('xq', '2')
        xn = request.GET.get('xn', '2019')
        jsid = request.GET.get('jsid')
        crawler = Crawler(jsid)
        kb = crawler.getKb(xn, xq)
        res = crawler.getIcs(kb)
        calender = Calender()
        calender.fomateCalender(res)
        return HttpResponse(calender.getIcs())
    except:
        return HttpResponse(status=404)


@api_view(['GET'])
def getIcsDashboard(request):
    rep = render(request, 'kbDashboard.html')
    return rep