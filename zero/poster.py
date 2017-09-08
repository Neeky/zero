import requests

class Poster(object):
    server_url="http://www.financedatas.com/component/"
    api=""

    def __init__(self,item):
        self._item=item

    @property
    def http_api(self):
        return self.server_url+self.api

    def post(self):
        response=requests.post(self.http_api,data=self._item.convert())
        print(response.text)


class ShiborItemPoster(Poster):
    #server_url="http://127.0.0.1:8000/component/"
    api="market/add/shiborrate/"

class InvestorSituationItemPoster(Poster):
    #server_url="http://127.0.0.1:8000/component/"
    api="market/add/investorsituation/"
    
