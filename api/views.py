from django.shortcuts import render
from WXController import wxcontrol
from django.http import HttpResponse
from xml.dom import minidom
import msgModels
from dict_to_xml import dict_to_xml




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

        root=minidom.parseString(request.body)
        msg=msgModels.basemsg(root)

        if msg.MsgType=='text':
            msg=msgModels.textmsg(root)
            msg.Content='Test is OK'
        elif msg.MsgType=='voice':
            msg=msgModels.voicemsg(root)
        elif msg.MsgType=='image':
            msg=msgModels.picmsg(root)
        elif msg.MsgType=='video':
            msg=msgModels.videomsg(root)
        else:
            pass

        msg=dict((name,getattr(msg,name)) for name in dir(msg) if not name.startswith('__'))
        msg=dict_to_xml(msg)


        with open('return.txt','w') as f:
            f.write(msg.__str__())


        return HttpResponse(msg,content_type='application/xml')