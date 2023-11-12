# # from polygon import RESTClient

# # client =  RESTClient(api_key="JgOzexEspWFss74lkoZGm2y4xqp1CFOR")

# # ticker = "AAPL"

# # # List Aggregates (Bars)
# # aggs = []
# # for a in client.list_aggs(ticker=ticker, multiplier=1, timespan="minute", from_="2023-06-01", to="2023-06-13", limit=5):
# #     aggs.append(a)

# # print(aggs)


# """
# https://rapidapi.com/apidojo/api/ms-finance
# list news
# """
# # import http.client

# # conn = http.client.HTTPSConnection("ms-finance.p.rapidapi.com")

# # headers = {
# #     'X-RapidAPI-Key': "be029279a0msh0d04ed52e30425ap1b697ejsn551bf12cccc5",
# #     'X-RapidAPI-Host': "ms-finance.p.rapidapi.com"
# # }

# # conn.request("GET", "/news/list?performanceId=0P0000OQN8", headers=headers)

# # res = conn.getresponse()
# # data = res.read()

# # print(data.decode("utf-8"))

# """
# get news details
# """
# # import http.client

# # conn = http.client.HTTPSConnection("ms-finance.p.rapidapi.com")

# # headers = {
# #      'X-RapidAPI-Key': "be029279a0msh0d04ed52e30425ap1b697ejsn551bf12cccc5",
# #      'X-RapidAPI-Host': "ms-finance.p.rapidapi.com"
# #  }

# # conn.request("GET", "/news/get-details?id=20231028282&sourceId=marketwatch", headers=headers)
# # res = conn.getresponse()
# # data = res.read()

# # print(data.decode("utf-8"))


# """
# get news headlines for given news url
# """
# # IMPORT ALL THE REQUIRED LIBRARIES
# # from bs4 import BeautifulSoup as BS
# # import requests as req
 
# # url = "https://www.businesstoday.in/latest/economy"
 
# # webpage = req.get(url)
# # trav = BS(webpage.content, "html.parser")
# # M = 1
# # for link in trav.find_all('a'):
   
# #     # PASTE THE CLASS TYPE THAT WE GET
# #     # FROM THE ABOVE CODE IN THIS AND
# #     # SET THE LIMIT GREATER THAN 35
# #     if(str(type(link.string)) == "<class 'bs4.element.NavigableString'>"
# #        and len(link.string) > 35):
 
# #         print(str(M)+".", link.string)
# #         M += 1


# # import requests
# # from bs4 import BeautifulSoup
# # from gensim.summarization import summarize

# # # Step 1: Choose a news source and stock ticker
# # news_source_url = "https://www.businesstoday.in/latest/economy"  # Replace with your news source URL
# # stock_ticker = "AAPL"  # Replace with the stock ticker you're interested in

# # # Step 2: Fetch News Articles
# # response = requests.get(news_source_url)
# # soup = BeautifulSoup(response.content, 'html.parser')
# # articles = soup.find_all('a', class_='article-link')  # Adjust based on the structure of the website

# # # Step 3: Preprocess Text Data (if needed)

# # # Step 4: Summarize News Articles
# # for article in articles:
# #     article_url = article['href']
# #     article_title = article.text
# #     article_response = requests.get(article_url)
# #     article_soup = BeautifulSoup(article_response.text, 'html.parser')
# #     article_text = article_soup.find('div', class_='article-content').text  # Adjust based on the structure of the article page
# #     summary = summarize(article_text, word_count=100)  # Adjust the word count as needed
# #     print(f"Title: {article_title}")
# #     print(f"Summary: {summary}")
# #     print("-" * 50)
