from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import WebBaseLoader
from langchain.chains.summarize import load_summarize_chain

"""
define a class to call chatgpt API to summarize the news articles
"""
class ChatGptSummary:

    def __init__(self) -> None:
        pass

    def get_chatgpt_news_summary(self, list_of_news_article_urls):
        """
        generate summary of list of news article urls using langchain library
        """
        loader = WebBaseLoader(list_of_news_article_urls)
        docs = loader.load()

        llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-16k")
        chain = load_summarize_chain(llm, chain_type="stuff")

        print(f">> Chatgpt Summary of all above news articles: \n\t\t{chain.run(docs)}")