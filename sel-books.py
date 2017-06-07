from bs4 import BeautifulSoup
fp = open("books.html", ="utf-8")
soup = BeautifulSoup(fp, "html.parser")

sel = lambda q : print(soup.select_one(q).string)
sel("#nu")
sel("li#nu")
sel("ul > li#nu")
sel("#bible #nu")
sel("ül#bible > li#nu")
sel("li[id='nu'")
sel("li:nth-of-type(4)")

print(soup.select("li").string)
print(soup.find_all("li"),string)


