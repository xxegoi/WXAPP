#coding=utf-8
from xml.dom import minidom

class basemsg():

    def __int__(self,data):
        root=minidom.parseString(data)
        self.ToUserName=root.getElementsByTagName('ToUserName')[0].firstChild.wholeText
        self.MsgID=root.getElementsByTagName('MsgID')[0].firstChild.wholeText
        self.MsgType=root.getElementsByTagName('MsgType')[0].firstChild.wholeText
        self.CreateTime=root.getElementsByTagName('CreateTime')[0].firstChild.wholeText
        self.FromUserName=root.getElementsByTagName('FromUserName')[0].firstChild.wholeText

    def getnodesvalue(self,tagName,root):
        return root.getElementsByTagName(tagName)[0].firstChild.wholeText


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
