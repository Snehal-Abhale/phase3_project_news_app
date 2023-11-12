import requests

class Yahoo:
    def __init__(self) -> None:
        self.urlList = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/news/v2/list"
        self.urlDetails = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/news/v2/get-details"

    def get_news_from_yahoo(self, user_input):

        querystring = {"region":"US", "snippetCount":"28", "user_input":user_input}
        payload = "Pass in the value of uuids field returned right in this endpoint to load the next page, or leave empty to load first page"
        headers = {
            "content-type": "text/plain",
            "X-RapidAPI-Key": "e9a61035e5msh5d51b845b8b019ap19d402jsn60f9b9109b07",
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }
        response = requests.post(self.urlList, data=payload, headers=headers, params=querystring)
     
        return response.json()


    def get_news_details_from_yahoo(self, id):
       
        querystring = {"uuid":id,"region":"US"} 
        headers = {
            "X-RapidAPI-Key": "e9a61035e5msh5d51b845b8b019ap19d402jsn60f9b9109b07",
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }
        response = requests.get(self.urlDetails, headers=headers, params=querystring)
        return response.json()
        