
class Poster(object):
    server_url="http://www.financedatas.com/component/"
    api=""

    def __init__(self,item):
        self._item=item

    @property
    def http_api(self):
        return self.server_url+self.api

    def post(self):
        raise NotImplemented()


class ShiborItemPoster(Poster):
    def post(self):
        print(self._item.convert())

class InvestorSituationItemPoster(Poster):
    def post(self):
        print(self._item.convert())
    
