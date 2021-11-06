import requests
from bs4 import BeautifulSoup

URL = "https://www.theguardian.com/football/datablog/2012/dec/24/world-best-footballers-top-100-list"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

table = soup.find("table", class_="in-article sortable")
rows = table.find("tbody").find_all("tr")

for row in rows:
    player = row.find_all("td")
    player_name = player[1].text.strip()
    print(player_name)

