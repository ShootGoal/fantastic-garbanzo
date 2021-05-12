from retry import retry
import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "https://suumo.jp/jj/chintai/ichiran/FR301FC001/?ar=030&ta=11&bs=040&ekInput=02060&tj=60&nk=0&ct=9999999&cb=0.0&md=01&md=02&ts=1&ts=2&et=20&mt=9999999&mb=0&cn=9999999&shkr1=03&shkr2=03&shkr3=03&shkr4=03&fw2=&pc=30"


@retry(tries=3, delay=10, backoff=2)
def get_html(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    return soup


all_data = []
max_page = 181

for page in range(1, max_page + 1):
    # define url
    url = base_url.format(page)

    # get html
    soup = get_html(url)

    # extract all items
    items = soup.findAll("div", {"class": "cassetteitem"})
    print("page", page, "items", len(items))

    # process each item
    for item in items:
        stations = item.findAll("div", {"class": "cassetteitem_detail-text"})

        # process each station
        for station in stations:
            # define variable
            base_data = {}

            # collect base information
            base_data["名称"] = item.find("div", {"class": "cassetteitem_content-title"}).getText().strip()
            base_data["カテゴリー"] = item.find("div", {"class": "cassetteitem_content-label"}).getText().strip()
            base_data["アドレス"] = item.find("li", {"class": "cassetteitem_detail-col1"}).getText().strip()
            base_data["アクセス"] = station.getText().strip()
            base_data["築年数"] = item.find("li", {"class": "cassetteitem_detail-col3"}).findAll("div")[
                0].getText().strip()
            base_data["構造"] = item.find("li", {"class": "cassetteitem_detail-col3"}).findAll("div")[1].getText().strip()

            # process for each room
            tbodys = item.find("table", {"class": "cassetteitem_other"}).findAll("tbody")

            for tbody in tbodys:
                data = base_data.copy()

                data["階数"] = tbody.findAll("td")[2].getText().strip()

                data["家賃"] = tbody.findAll("td")[3].findAll("li")[0].getText().strip()
                data["管理費"] = tbody.findAll("td")[3].findAll("li")[1].getText().strip()

                data["敷金"] = tbody.findAll("td")[4].findAll("li")[0].getText().strip()
                data["礼金"] = tbody.findAll("td")[4].findAll("li")[1].getText().strip()

                data["間取り"] = tbody.findAll("td")[5].findAll("li")[0].getText().strip()
                data["面積"] = tbody.findAll("td")[5].findAll("li")[1].getText().strip()

                data["URL"] = "https://suumo.jp" + tbody.findAll("td")[8].find("a").get("href")

                all_data.append(data)

            # convert to dataframe
df = pd.DataFrame(all_data)
print(df)
df.to_csv("building_data.csv")
