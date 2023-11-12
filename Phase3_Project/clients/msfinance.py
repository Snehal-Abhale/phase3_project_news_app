import requests
import json

class MsFinance:
    def __init__(self) -> None:
        self.urlList = "https://ms-finance.p.rapidapi.com/articles/list"
        self.urlDetails = "https://ms-finance.p.rapidapi.com/articles/get-details"

    def getListOfNewsArticles(self):
        querystring = {"performanceId":"0P0000OQN8"}

        headers = {
            "X-RapidAPI-Key": "be029279a0msh0d04ed52e30425ap1b697ejsn551bf12cccc5",
            "X-RapidAPI-Host": "ms-finance.p.rapidapi.com"
        }

        response = requests.get(self.urlList, headers=headers, params=querystring)
        return response.json()
        
    def getDetailsOfNewsArticles(self)  :
       
            querystring = {"id":"981538"}

            headers = {
                "X-RapidAPI-Key": "be029279a0msh0d04ed52e30425ap1b697ejsn551bf12cccc5",
                "X-RapidAPI-Host": "ms-finance.p.rapidapi.com"
            }

            response = requests.get(self.urlDetails, headers=headers, params=querystring)            
          
            data = response.__dict__
            return data
           