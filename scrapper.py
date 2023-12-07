import requests
from bs4 import BeautifulSoup


def scrapper(link: str):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")  # html.parser
    data_all = soup.find_all("div", class_="w-full rounded border")  # Поиск всех данных с тэгом
    for i in data_all:
        name = i.find("h4").text
        price = i.find("h5").text
        url_img = "https://scrapingclub.com" + i.find("img", class_="card-img-top img-fluid").get("src")
        print(name, price, url_img)


"""url = "https://scrapingclub.com/exercise/list_basic/?page=1"
scrapper(url)"""
for count in range(1, 8):
    url = f"https://scrapingclub.com/exercise/list_basic/?page={count}"
    scrapper(url)