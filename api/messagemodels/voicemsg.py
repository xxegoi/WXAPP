#coding=utf-8

import basemsg


class voicemsg(basemsg):

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
