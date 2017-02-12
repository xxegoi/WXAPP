#coding
import basemsg

class picmsg(basemsg):

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