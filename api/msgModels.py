#coding=utf-8
from xml.dom import minidom

class basemsg():

    def __init__(self,data):
        self.root=data
        self.ToUserName=self.getnodesvalue('ToUserName')
        self.MsgID=self.getnodesvalue('MsgId')
        self.MsgType=self.getnodesvalue('MsgType')
        self.CreateTime=self.getnodesvalue('CreateTime')
        self.FromUserName=self.getnodesvalue('FromUserName')

    def getnodesvalue(self,tagName):
        return self.root.getElementsByTagName(tagName)[0].firstChild.wholeText


    @property
    def ToUserName(self):
        return self.ToUserName

    @ToUserName.setter
    def ToUserName(self, value):
        self.ToUserName = value

    @property
    def FromUserName(self):
        return self.FromUserName

    @FromUserName.setter
    def FromUserName(self, value):
        self.FromUserName = value

    @property
    def CreateTime(self):
        return self.CreateTime

    @CreateTime.setter
    def CreateTime(self, value):
        self.CreateTime = value

    @property
    def MsgType(self):
        return self.MsgType

    @MsgType.setter
    def MsgType(self, value):
        self.MsgType = value

    @property
    def MsgID(self):
        return self.MsgID

    @MsgID.setter
    def MsgID(self,value):
        self.MsgID=value


class textmsg(basemsg):

    def __init__(self,data):
        basemsg.__init__(self,data)
        self.Content=self.getnodesvalue('Content')

    @property
    def Content(self):
        return self.Content

    @Content.setter
    def Content(self,value):
        self.Content=value

class voicemsg(basemsg):
    '''
    语音消息
    '''
    @property
    def MediaId(self):
        return self.MediaId

    @MediaId.setter
    def MediaId(self,value):
        self.MediaId=value

    @property
    def ThumbMediaId(self):
        return self.ThumbMediaId

    @ThumbMediaId.setter
    def ThumbMediaId(self,value):
        self.ThumbMediaId=value

class picmsg(basemsg):
    '''
    图片消息
    '''
    @property
    def PicUrl(self):
        '''
        图片链接
        :return:
        '''
        return self.PicUrl

    @PicUrl.setter
    def PicUrl(self,value):
        self.PicUrl=value

    @property
    def MediaId(self):
        '''
        图片消息媒体id，可以调用多媒体文件下载接口拉取数据
        :return:
        '''
        return self.MediaId

    @MediaId.setter
    def MediaId(self,value):
        self.MediaId=value

class videomsg(basemsg):
    '''
    视频消息
    '''
    def __init__(self,data):
        basemsg.__init__(data)

    @property
    def MediaId(self):
        return self.MediaId
    @MediaId.setter
    def MediaId(self,value):
        self.MediaId=value

    @property
    def Title(self):
        return self.Title

    @Title.setter
    def Title(self,value):
        self.Title=value

    @property
    def Description(self):
        return self.Description

    @Description.setter
    def Description(self,value):
        self.Description=value
