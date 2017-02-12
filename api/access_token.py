import urllib
import json
from django.utils import timezone

class access_token():
    @property
    def token(self):
        return self.token

    @token.setter
    def token(self,value):
        self.token=value

    @property
    def gettime(self):
        return self.gettime

    def update(self,appid,secret):
        try:
            url='https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' % (appid,secret)
            token=urllib.urlopen(url).read()
            token=json.loads(token)
            self.token=token['access_token']
            self.gettime=timezone.now()

        except Exception,e:
            return e



