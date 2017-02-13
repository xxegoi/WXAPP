#coding=utf-8
import basemsg
from xml.dom import minidom as mini

class textmsg(basemsg):

    def __init__(self,data):
        basemsg.__init(self,data)
        self.Content=self.getnodesvalue('Content')

    @property
    def Content(self):
        return self.Content

    @Content.setter
    def Content(self,value):
        self.Content=value
