#coding=utf-8
import basemsg
from xml.dom import minidom as mini

class textmsg(basemsg):

    def __int__(self,data):
        '''
        暂时未知道怎样继承父类属性
        :param data:
        :return:
        '''
        pass

    @property
    def Content(self):
        return self.Content

    @Content.setter
    def Content(self,value):
        self.Content=value
