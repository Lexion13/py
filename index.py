# now i try to do scraping code.

from urllib import request
from pyquery import PyQuery as pq

resp = request.urlopen("http://cookpad.com/recipe/1069312")
html = resp.read().decode("utf-8")
query = pq(html)

results = []

# レシピのメイン部を取得
for recipe_main in query.find("div#recipe-main"):
    # レシピのタイトルを取得
    for recipe_title in pq(recipe_main).find("h1.recipe-title"):
        results.append(pq(recipe_title).text())

    # 材料を取得
    for ingredient in pq(recipe_main).find("div.ingredient_name"):
        results.append(pq(ingredient).text())

# 結果を表示
for r in results:
    print(r)