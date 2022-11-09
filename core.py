import helpers
from bs4 import BeautifulSoup

def web_scrap():
    request = helpers.get_html()
    soup = BeautifulSoup(request.content, 'html.parser')
    # print(soup.prettify())
    print(soup.title.string)

def execute():
    if helpers.get_answer():
        print(web_scrap())
