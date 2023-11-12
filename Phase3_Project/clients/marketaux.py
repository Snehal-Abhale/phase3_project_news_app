import json
import http.client, urllib.parse



class MarketAux:

    def __init__(self) -> None:
        api_url = 'api.marketaux.com'
        self.conn = http.client.HTTPSConnection(api_url)
        

    def get_news(self):
        params = urllib.parse.urlencode({
            'api_token': 'HOJtW4nx4uEq1QMDfHTs1SpWJ3jOweQCLFsAdQc5',
            'symbols': 'AAPL,TSLA',
            'limit': 50,
            })

        self.conn.request('GET', '/v1/news/all?{}'.format(params))

        res = self.conn.getresponse()
        data = res.read() # reda from bytes
        data = data.decode('utf-8') # decode bytes to str
        data = json.loads(data) # convert str to dict
        return data