import os
import ollama
import re
from helper.utils import Website

# NOTE: you would need the ollama model running locally to execute this code
# constants
OLLAMA_API = "http://localhost:11434/api/chat"
HEADERS = {"Content-Type": "application/json"}
MODEL = "llama3.2"


# generate prompts
def user_prompt_for_news(web_page: Website) -> str:
    user_prompt = "You are an investment analyst, your role is to read the provided news article, provide a summary, and point out the top three company names or stock tickers that get impacted by this news. \
provide your reasoning. \
ignoring text that might be navigation related. \
respond in markdown."
    user_prompt += f"you are looking at a news article titled '{web_page.title}'."
    user_prompt += "The content of the website is as follows;\n\n"
    user_prompt += web_page.text
    return user_prompt

def messages_for_news(web_page: Website) -> list:
    return [
        {
            "role": "user",
            "content": user_prompt_for_news(web_page)
        }
    ]

def analyze_news_ollama(url: str):
    # web_page = NewsPage(url)
    web_page = Website(url)
    response = ollama.chat(
        model = MODEL,
        messages = messages_for_news(web_page)
    )
    return response['message']['content']


if __name__ == "__main__":
    # ask user for the URL
    url = input("Please enter the URL of the news article you'd like to analyze: ")
    # url = "https://finance.yahoo.com/news/trump-picks-scott-bessent-the-investor-favorite-for-treasury-secretary-000710469.html"
    print(analyze_news_ollama(url=url))
