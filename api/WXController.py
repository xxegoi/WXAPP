#coding=utf-8
import hashlib
import urllib
from access_token import access_token

class wxcontrol():

    def __int__(self,token,appid,secret,encodingaeskey):
        self.token=token
        self.appid=appid
        self.secret=secret
        self.encodingaeskey=encodingaeskey
        self.access_token=access_token()

        self.access_token.update()

    @property
    def access_token(self):
        return self.access_token
    @access_token.setter
    def access_token(self,value):
        self.access_token=value

    def signature_check(self,token,signature,timestamp,nonce):
        '''

        :param token: 微信公众号中填写的Token,不是Access_Token
        :param signature:微信加密签名，signature结合了开发者填写的token参数和请求中的timestamp参数、nonce参数
        :param timestamp:时间戳
        :param nonce:随机数
        :return:
        '''
        ##将token、timestamp、nonce三个参数进行字典序排序
        lst=[token,timestamp,nonce]

        lst.sort()
        #将三个参数字符串拼接成一个字符串
        tmp_str=''.join(lst)
        #进行sha1加密
        tmp_str=hashlib.sha1(tmp_str).hexdigest()
        #加密后的字符串可与signature对比
        if signature==tmp_str:
            return True
        else:
            return False

    def get_access_token(self):




        pass