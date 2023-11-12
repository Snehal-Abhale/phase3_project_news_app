from Phase3_Project.clients.marketaux import MarketAux
from Phase3_Project.clients.msfinance import MsFinance
from Phase3_Project.clients.yahoo import Yahoo
from Phase3_Project.clients.chatgpt_summary import ChatGptSummary
import json  

class ServiceWorkflow:

    def __init__(self) -> None:
        pass

    def run(self):
        self.yahoo_service_workflow()
            
    
    def yahoo_service_workflow(self):
        yahoo_client = Yahoo()
        user_input = input(">> Enter the search string: ")
        yahoo_news_list = yahoo_client.get_news_from_yahoo(user_input)
        
        data = yahoo_news_list.get('data', {}).get('main', {}).get('stream', [])
        list_of_ids = []
        
        for item in data:
        # Check if 'id' key exists in the dictionary
            if 'id' in item:
                # Access the 'id' value
                id_value = item['id']
                # print(f"ID: {id_value}")
                list_of_ids.append(id_value)
            else:
                print("No 'id' key in the dictionary")
        
        counter = 0
        yahoo_news_details = []
        list_of_news_article_urls = []
        for id in list_of_ids:
            if counter <= 2:
                yahoo_news_details.append(yahoo_client.get_news_details_from_yahoo(id))
            counter += 1

        for news_detail in yahoo_news_details:
            news_detail_contents = news_detail.get('data',{}).get('contents',[]) 

            for item in news_detail_contents:
                content = item.get('content',{})
                print(f'\t>> ID: \n\t\t{content.get("id","")}\n')
                print(f'\t>> News Title: \n\t\t{content.get("title","")}\n')
                if content.get('clickThroughUrl',{}) is not None:
                    list_of_news_article_urls.append(content.get('clickThroughUrl',{}).get('url',''))
                    print(f"\t>> URL: \n\t\t{content.get('clickThroughUrl',{}).get('url','')}\n")
                print(f"\t>> Summary: \n\t\t{content.get('summary','')}\n\n\t\t")

        chatgpt_summary = ChatGptSummary()
        chatgpt_summary.get_chatgpt_news_summary(list_of_news_article_urls)


    def marketaux_service_workflow(self):
        # going To expand later
        # marketaux_client = MarketAux()
        # marketaux_news_data = marketaux_client.get_news()
        pass

    def msfinance_service_workflow(self):
        # going To expand later
        # msfinance_client = MsFinance()
        # msfinance_client.getListOfNewsArticles()
        # msfinance_client.getDetailsOfNewsArticles()
        pass

 
    def save_json(self, json_obj, file_path):
        """
        save json response from API to a json file to analyze it
        """
        with open(file_path, 'w') as file:
            json.dump(json_obj, file, indent = 6)  

       