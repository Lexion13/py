from bs4 import BeautifulSoup
html = """
<html><body>
<h1 id="title">スクレイピングとは？</h1>
<p id="body">Webページから任意のデータを抽出する。</p>
</html></body>
"""

soup = BeautifulSoup(html, 'html.parser')

title = soup.find(id="title")
body = soup.find(id="body")

print(title.string + " and " + body.string)
