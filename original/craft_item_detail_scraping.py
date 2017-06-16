from bs4 import BeautifulSoup
import urllib.parse
from urllib.parse import urljoin
import urllib.request as req
import re


urls = [
	"https://www.craft-store.jp/products/nagae-form-bamboo-set",
	"https://www.craft-store.jp/products/nagae-ratio-square-l",
	"https://www.craft-store.jp/products/nagae-ratio-square-m",
	"https://www.craft-store.jp/products/nagae-ratio-square-s",
	"https://www.craft-store.jp/products/suginokicraft-lunchbox-twostory",
	"https://www.craft-store.jp/products/teori-grip-l",
	"https://www.craft-store.jp/products/teori-grip-s",
	"https://www.craft-store.jp/products/teori-grid-square",
	"https://www.craft-store.jp/products/macrw-bionmg60",
	"https://www.craft-store.jp/products/aka-swing",
	"https://www.craft-store.jp/products/shiro-tilt",
	"https://www.craft-store.jp/products/sanjotokusyuchukousho-ssc-26",
	"https://www.craft-store.jp/products/isuke-moku-cupsaucer",
	"https://www.craft-store.jp/products/isuke-moku-cup",
	"https://www.craft-store.jp/products/gatomikio-waqwa-cup-s",
	"https://www.craft-store.jp/products/gatomikio-waqwa-cup-l",
	"https://www.craft-store.jp/products/aji-grill-square-ami",
	"https://www.craft-store.jp/products/aji-grill-square-mame",
	"https://www.craft-store.jp/products/aji-grill-square-shima",
	"https://www.craft-store.jp/products/1616-ty-square-white-set",
	"https://www.craft-store.jp/products/1616-ty-square-gray-set",
	"https://www.craft-store.jp/products/1616-ty-square-235-white",
	"https://www.craft-store.jp/products/1616-ty-square-235-gray",
	"https://www.craft-store.jp/products/1616-ty-square-165-white",
	"https://www.craft-store.jp/products/1616-ty-square-165-gray",
	"https://www.craft-store.jp/products/hirotagarasu-syouwamodernglass-cupsaucer",
	"https://www.craft-store.jp/products/suginokicraft-lunchbox-set",
	"https://www.craft-store.jp/products/gatomikio-tasai-cup",
	"https://www.craft-store.jp/products/gatomikio-tasai-bowl-l",
	"https://www.craft-store.jp/products/gatomikio-tasai-bowl-m",
	"https://www.craft-store.jp/products/gatomikio-tasai-bowl-s",
	"https://www.craft-store.jp/products/gatomikio-tasai-plate-l",
	"https://www.craft-store.jp/products/gatomikio-tasai-plate-m",
	"https://www.craft-store.jp/products/gatomikio-tasai-plate-s",
	"https://www.craft-store.jp/products/sanjotokusyuchukousho-ssc-20",
	"https://www.craft-store.jp/products/aiwashibori-bowl150-usucha",
	"https://www.craft-store.jp/products/aiwashibori-bowl150-kurocha-ohaguro",
	"https://www.craft-store.jp/products/aiwashibori-bowl150-silky",
	"https://www.craft-store.jp/products/aiwashibori-bowl120-usucha",
	"https://www.craft-store.jp/products/aiwashibori-bowl120-kurocha-ohaguro",
	"https://www.craft-store.jp/products/aiwashibori-bowl120-silky",
	"https://www.craft-store.jp/products/hirotagarasu_shouyusashi_kagome",
	"https://www.craft-store.jp/products/hirotagarasu_shouyusashi_kikkou",
	"https://www.craft-store.jp/products/hirotagarasu_shouyusashi_sakura",
	"https://www.craft-store.jp/products/todai-spoon",
	"https://www.craft-store.jp/products/copper-spoon-pinkgold",
	"https://www.craft-store.jp/products/copper-spoon-set-silver",
	"https://www.craft-store.jp/products/copper-spoon-set-gold",
	"https://www.craft-store.jp/products/copper-spoon",
	"https://www.craft-store.jp/products/urushiyahayashi_lunchbox_s",
	"https://www.craft-store.jp/products/urushiyahayashi_lunchbox_long",
	"https://www.craft-store.jp/products/urushiyahayashi_lunchbox_l",
	"https://www.craft-store.jp/products/suginokicraft-large-lunchbox",
	"https://www.craft-store.jp/products/fabrik_keycard",
	"https://www.craft-store.jp/products/fabrik_tri",
	"https://www.craft-store.jp/products/maruhiro-blockmug-l",
	"https://www.craft-store.jp/products/maruhiro-soaktray-l",
	"https://www.craft-store.jp/products/kago-dahlia",
	"https://www.craft-store.jp/products/kago-rose",
	"https://www.craft-store.jp/products/kago-square-s",
	"https://www.craft-store.jp/products/kago-oval-l",
	"https://www.craft-store.jp/products/kago-oval-s",
	"https://www.craft-store.jp/products/nosaku_beercup_l",
	"https://www.craft-store.jp/products/nousaku_futae",
	"https://www.craft-store.jp/products/nosaku_beercup",
	"https://www.craft-store.jp/products/najimi_tumbler",
	"https://www.craft-store.jp/products/nousaku_chopstickrest_sakura",
	"https://www.craft-store.jp/products/nousaku_chopstickrest_85",
	"https://www.craft-store.jp/products/nousaku_chopstickrest_82",
	"https://www.craft-store.jp/products/nousaku_chopstickrest_knot_b",
	"https://www.craft-store.jp/products/kingflon_nomake_asagata_18",
	"https://www.craft-store.jp/products/newking_18",
	"https://www.craft-store.jp/products/proking_18",
	"https://www.craft-store.jp/products/proking_asagata_saute_18",
	"https://www.craft-store.jp/products/fabrik_bi",
	"https://www.craft-store.jp/products/fabrik_long",
	"https://www.craft-store.jp/products/fabrik_key",
	"https://www.craft-store.jp/products/1616aritajapan_typalaceplate_set",
	"https://www.craft-store.jp/products/maruhiro_hasami_soakcup_s_set",
	"https://www.craft-store.jp/products/maruhiro_hasami_soakcup_m_set",
	"https://www.craft-store.jp/products/maruhiro_hasami_soakcup_l_set",
	"https://www.craft-store.jp/products/urushiyahayashi_sakura_meotobashi",
	"https://www.craft-store.jp/products/moku_ll",
	"https://www.craft-store.jp/products/moku_l",
	"https://www.craft-store.jp/products/moku_m",
	"https://www.craft-store.jp/products/moku_s",
	"https://www.craft-store.jp/products/1616aritajapan_typalaceplate_l",
	"https://www.craft-store.jp/products/1616aritajapan_typalaceplate_s",
	"https://www.craft-store.jp/products/syuzangama_itazara",
	"https://www.craft-store.jp/products/syuzangama_nagaitazara",
	"https://www.craft-store.jp/products/ufufu",
	"https://www.craft-store.jp/products/futae",
	"https://www.craft-store.jp/products/maruhiro_hasami_soakcup_l",
	"https://www.craft-store.jp/products/maruhiro_hasami_soakcup_s",
	"https://www.craft-store.jp/products/maruhiro_hasami_soakcup_m",
	"https://www.craft-store.jp/products/much",
	"https://www.craft-store.jp/products/3way_mini_wallet",
	"https://www.craft-store.jp/products/zen",
	"https://www.craft-store.jp/products/morning-glory-sansaku_morning-glory_black",
	"https://www.craft-store.jp/products/sansaku_morning-glory_silver",
	"https://www.craft-store.jp/products/odakoudouki_moscowmulecup_mat",
	"https://www.craft-store.jp/products/odakoudouki_moscowmulecup_tsutime",
	"https://www.craft-store.jp/products/suzukou_guinomi",
	"https://www.craft-store.jp/products/kago-square-m",
	"https://www.craft-store.jp/products/unilloy-22cm",
	"https://www.craft-store.jp/products/rice-wine-glass-for-sake",
	"https://www.craft-store.jp/products/hirotagarasu_syouwamodernglass_glass",
	"https://www.craft-store.jp/products/tsumugi-fuji",
	"https://www.craft-store.jp/products/aiwashibori_tumbler90_brown",
	"https://www.craft-store.jp/products/aiwashibori_tumbler90_6264",
	"https://www.craft-store.jp/products/nakaoarumi_proking",
	"https://www.craft-store.jp/products/suginokicraft_lunchbox",
	"https://www.craft-store.jp/products/osakasuzuki_soleiltumbler",
	"https://www.craft-store.jp/products/osakasuzuki_soleiltumbler_s",
	"https://www.craft-store.jp/products/hirotagarasu_syouwamodern_tumbler",
	"https://www.craft-store.jp/products/aiwashibori_tumbler90_silky",
	"https://www.craft-store.jp/products/suginokicraft_lunchbox_b"
]

print("href", ",", end="")
print("title", ",", end="")
print("brand", ",", end="")
print("price", ",", end="")
print("shippingdate", ",", end="")
print("indexstatus", ",", end="")
print("canonicalstatus", ",", end="")
print("metatitle", ",", end="")
print("metadescription", ",", end="")
print("")

for url in urls:
	res = req.urlopen(url)
	soup = BeautifulSoup(res, "html.parser")
	'''
	get list
	href
	title
	brand
	price
	shipping date
	index status
	canonical status
	meta title
	meta description
	
	'''
	href = url
	title = soup.select_one(".product-main-info h1").string
	brand = soup.select_one(".product-main-info h2").string
	price = soup.select_one(".product-main-info .product-price").text
	price = re.split(r'円', price)
	price = price[0]
	price = price.strip()
	price = price.replace(",", "")
	shippingdate = soup.select_one("#product-shipping-time").text
	shippingdate = shippingdate.strip()
	try:
		indexstatus = soup.find(attrs={"name":"robots"}).get('content')
	except:
		indexstatus = "index"
	try:
		canonicalstatus = soup.find(attrs={"rel":"canonical"}).get('href')
	except:
		canonicalstatus = "nothing"
	metatitle = soup.select_one("title")
	metadescription = soup.find(attrs={"name": "description"}).get('content')

	print(href, ",", end="")
	print(title, ",", end="")
	print(brand, ",", end="")
	print(price, ",", end="")
	print(shippingdate, ",", end="")
	print(indexstatus, ",", end="")
	print(canonicalstatus, ",", end="")
	print(metatitle, ",", end="")
	print(metadescription, ",", end="")
	print("")



'''
If you wanna get only url,
Please be commentout line 21.
'''
# like that
