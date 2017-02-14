#coding=utf-8
from xml.dom import minidom

class basemsg():

    def __int__(self,data):
        self.root=minidom.parseString(data)
        self.ToUserName=self.getnodesvalue('ToUserName')
        self.MsgID=self.getnodesvalue('MsgID')
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
