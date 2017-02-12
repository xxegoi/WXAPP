from django.shortcuts import render
from WXController import wxcontrol
from django.http import HttpResponse
# Create your views here.

def index(request):

    wx=wxcontrol()

    if request.method=='GET':
        token='xxegoi'
        signature=request.GET['signature']
        timestamp=request.GET['timestamp']
        nonce=request.GET['nonce']
        echostr=request.GET['echostr']

        if wx.signature_check(token,signature,timestamp,nonce):
            return HttpResponse(echostr)
        else:
            pass

    else:
        with open('data.txt','w') as f:
            f.write(request.body)
        return HttpResponse('success')