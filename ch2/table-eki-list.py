from bs4 import BeautifulSoup
import requests as req

url = "table.html"
html = open(url, encoding="utf-8").read()
soup = BeautifulSoup(html, "html.parser")

#analize table
result = []
table = soup.select_one("table")

#get tr tag
tr_list = table.find_all("tr")
for tr in tr_list:
    #get td or th tag
    result_row = []
    td_list = tr.find_all(["td", "th"])
    for td in td_list:
        cell = td.get_text()
        result_row.append(cell)
    result.append(result_row)
    
#output csv file in this list
for row in result:
    print(",".join(row))
    