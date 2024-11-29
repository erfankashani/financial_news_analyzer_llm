from bs4 import BeautifulSoup
import requests

class Website:
    """
    A utility class to represent a Website that we have scraped
    """

    def __init__(self, url):
        self.url = url
        response = requests.get(url)
        self.body = response.content
        soup = self.get_soup(body=self.body)
        self.title = soup.title.string if soup.title else "No title found"
        self.text = soup.body.get_text(strip=True) if soup.body else ""
        self.links = self.get_links(soup=soup)


    def get_soup(self, body , page_type: str = 'html.parser') -> BeautifulSoup:
        soup = BeautifulSoup(body, page_type)
        if soup.body:
            for irrelevant in soup.body(["script", "style", "img", "input"]):
                irrelevant.decompose()
        return soup


    def get_links(self, soup: BeautifulSoup) -> list:
        return [link.get('href') for link in soup.find_all('a')]


    def get_contents(self) -> str:
        return f"Webpage Title:\n{self.title}\nWebpage Contents:\n{self.text}\n\n"


# # represent the News page based on the URL
# class NewsPage():
#     def __init__(self, url):
#         self.url = url
#         response = requests.get(url)
#         soup = BeautifulSoup(response.content, 'html.parser')
#         self.title = soup.title.string if soup.title else "No title found"
#         for irrelevant_tag in soup.body(["script", "style", "img", "input"]):
#             irrelevant_tag.decompose()
#         self.text = soup.body.get_text(strip=True)