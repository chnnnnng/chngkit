import datetime

from django.http import HttpResponse
from .utils.MailUtil import MailUtil

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .healthreport import doHealthReport


def index(request):
    return HttpResponse('Hello!\nThis is a site of Apis for ZJUT (Third Party).\nIngore if you have no idea (Bullshit).')


@api_view(['POST'])
def healthreport(request):
    try:
        stuno = request.POST.get('stuno')
        password = request.POST.get('password')
        email = request.POST.get('email',None)
        resl = doHealthReport(stuno,password)
        #发送邮件
        if email is not None :
            i = datetime.datetime.now()
            title = ("「小柏」自动健康上报 · %s月%s日" % (i.month, i.day))
            mail = MailUtil()
            mail.setUser(email).setTitle(title).setContent(resl).send()
        return Response(resl)
    except:
        return HttpResponse(status=404)

