import os
from dotenv import load_dotenv
from openai import OpenAI
import re
from helper.utils import Website


def validate_open_ai_api_key(api_key:str):
    if not api_key:
        raise ValueError("No API key was found; please set an OPENAI_API_KEY environment variable")
    elif not api_key.startswith("sk-proj"):
        raise ValueError("An API key was found, but it doesn't start sk-proj-; please check you're using the right key")
    elif api_key.strip() != api_key:
        raise ValueError("An API key was found, but it looks like it might have space or tab characters at the start or end - please remove them")
    else:
        print("API key looks good")


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
validate_open_ai_api_key(api_key)

openai = OpenAI()


# generate prompts
SYSTEM_PROMPT = "You are an investment analyst, your role is to read the provided news article, provide a summary, and point out the top three company names or stock tickers that get impacted by this news. \
provide your reasoning. \
ignoring text that might be navigation related. \
respond in markdown."

def user_prompt_for_news(web_page: Website) -> str:
    user_prompt = f"you are looking at a news article titled '{web_page.title}'."
    user_prompt += "The content of the website is as follows; \
    Please provide a summary of the article in markdown. \
    Point out the top three company names or stock tickers that will get impacted by this news while Provide your reasoning.\n\n"
    user_prompt += web_page.text
    return user_prompt

def messages_for_news(web_page: Website) -> list:
    return [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": user_prompt_for_news(web_page)
        }
    ]

def analyze_news(url: str):
    web_page = Website(url)
    response = openai.chat.completions.create(
        model = "gpt-4o-mini",
        messages = messages_for_news(web_page)
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    # ask user for the URL
    url = input("Please enter the URL of the news article you'd like to analyze: ")
    # url = "https://finance.yahoo.com/news/trump-picks-scott-bessent-the-investor-favorite-for-treasury-secretary-000710469.html"
    print(analyze_news(url=url))
