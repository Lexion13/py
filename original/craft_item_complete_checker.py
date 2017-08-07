from bs4 import BeautifulSoup
import urllib.parse
from urllib.parse import urljoin
import urllib.request as req
import re
import time
import datetime

urls = [
"https://www.craft-store.jp/products/3way_mini_wallet",
"https://www.craft-store.jp/products/aka-swing",
"https://www.craft-store.jp/products/camdlelights-beeswax-l",
"https://www.craft-store.jp/products/camdlelights-beeswax-m",
"https://www.craft-store.jp/products/camdlelights-beeswax-mug",
"https://www.craft-store.jp/products/camdlelights-beeswax-stick",
"https://www.craft-store.jp/products/fabrik_bi",
"https://www.craft-store.jp/products/2016-bg-coffeecup-l-black-matt",
"https://www.craft-store.jp/products/2016-bg-coffeecup-s-black-matt",
"https://www.craft-store.jp/products/2016-bg-coffecup-s-white-sprinkle",
"https://www.craft-store.jp/products/2016-bg-coffee-dripper",
"https://www.craft-store.jp/products/2016-bg-black-matt",
"https://www.craft-store.jp/products/2016-bg-white-sprinkle",
"https://www.craft-store.jp/products/2016-ch-teacup",
"https://www.craft-store.jp/products/2016-ch-180",
"https://www.craft-store.jp/products/2016-ch-240",
"https://www.craft-store.jp/products/nagae-collinette",
"https://www.craft-store.jp/products/nagae-collinette-aile",
"https://www.craft-store.jp/products/nagae-collinette-lymph",
"https://www.craft-store.jp/products/futae",
"https://www.craft-store.jp/products/camdlelights-greencandle-12",
"https://www.craft-store.jp/products/camdlelights-greencandle-17",
"https://www.craft-store.jp/products/camdlelights-greencandle-18",
"https://www.craft-store.jp/products/camdlelights-greencandle-38",
"https://www.craft-store.jp/products/camdlelights-greencandle-41",
"https://www.craft-store.jp/products/camdlelights-greencandle-9",
"https://www.craft-store.jp/products/teori-grid-square",
"https://www.craft-store.jp/products/aji-grill-square-ami",
"https://www.craft-store.jp/products/aji-grill-square-mame",
"https://www.craft-store.jp/products/aji-grill-square-shima",
"https://www.craft-store.jp/products/teori-grip-l",
"https://www.craft-store.jp/products/teori-grip-s",
"https://www.craft-store.jp/products/kago-oval-l",
"https://www.craft-store.jp/products/kago-oval-s",
"https://www.craft-store.jp/products/kago-square-m",
"https://www.craft-store.jp/products/kago-square-s",
"https://www.craft-store.jp/products/kago-dahlia",
"https://www.craft-store.jp/products/kago-rose",
"https://www.craft-store.jp/products/fabrik_keycard",
"https://www.craft-store.jp/products/fabrik_key",
"https://www.craft-store.jp/products/fabrik_long",
"https://www.craft-store.jp/products/mirror-1",
"https://www.craft-store.jp/products/isuke-moku-teabox",
"https://www.craft-store.jp/products/isuke-moku-tray-a",
"https://www.craft-store.jp/products/isuke-moku-tray-b",
"https://www.craft-store.jp/products/moku-b-isuke-moku-plate-b",
"https://www.craft-store.jp/products/isuke-moku-cup",
"https://www.craft-store.jp/products/isuke-moku-plate-a",
"https://www.craft-store.jp/products/moku_m",
"https://www.craft-store.jp/products/moku_l",
"https://www.craft-store.jp/products/moku_s",
"https://www.craft-store.jp/products/moku_ll",
"https://www.craft-store.jp/products/isuke-moku-cupsaucer",
"https://www.craft-store.jp/products/much",
"https://www.craft-store.jp/products/najimi_tumbler",
"https://www.craft-store.jp/products/nagae-ratio-square-l",
"https://www.craft-store.jp/products/nagae-ratio-square-m",
"https://www.craft-store.jp/products/nagae-ratio-square-s",
"https://www.craft-store.jp/products/rice-wine-glass-for-sake",
"https://www.craft-store.jp/products/2016-sf-mug-gray",
"https://www.craft-store.jp/products/2016-sf-mug-white",
"https://www.craft-store.jp/products/2016-sf-mug-red",
"https://www.craft-store.jp/products/shigeki-fujishiro-shigeki-fujishiro-shouyusashi-gray",
"https://www.craft-store.jp/products/shigeki-fujishiro-shouyusashi-white",
"https://www.craft-store.jp/products/2016-sf-shouyusashi-red",
"https://www.craft-store.jp/products/shiro-tilt",
"https://www.craft-store.jp/products/sanjotokusyuchukousho-ssc-20",
"https://www.craft-store.jp/products/sanjotokusyuchukousho-ssc-26",
"https://www.craft-store.jp/products/gatomikio-tasai-cup",
"https://www.craft-store.jp/products/gatomikio-tasai-plate-l",
"https://www.craft-store.jp/products/gatomikio-tasai-plate-m",
"https://www.craft-store.jp/products/gatomikio-tasai-plate-s",
"https://www.craft-store.jp/products/gatomikio-tasai-bowl-l",
"https://www.craft-store.jp/products/gatomikio-tasai-bowl-m",
"https://www.craft-store.jp/products/gatomikio-tasai-bowl-s",
"https://www.craft-store.jp/products/2016-ty-200-black",
"https://www.craft-store.jp/products/2016-ty-200-white",
"https://www.craft-store.jp/products/2016-ty-180-black",
"https://www.craft-store.jp/products/2016-ty-180-white",
"https://www.craft-store.jp/products/nagae-tin-breath-20-antiquegold",
"https://www.craft-store.jp/products/nagae-tin-breath-20-gold",
"https://www.craft-store.jp/products/nagae-tin-breath-20-silver",
"https://www.craft-store.jp/products/nagae-tin-breath-40-antiquegold",
"https://www.craft-store.jp/products/nagae-tin-breath-40-gold",
"https://www.craft-store.jp/products/nagae-tin-breath-40-silver",
"https://www.craft-store.jp/products/nagae-tin-breath-ring-10x80-antiquegold",
"https://www.craft-store.jp/products/nagae-tin-breath-ring-10x80-gold",
"https://www.craft-store.jp/products/nagae-tin-breath-ring-10x80-silver",
"https://www.craft-store.jp/products/nagae-tin-breath-ring-15x80-antiquegold",
"https://www.craft-store.jp/products/nagae-tin-breath-ring-15x80-gold",
"https://www.craft-store.jp/products/nagae-tin-breath-ring-15x80-silver",
"https://www.craft-store.jp/products/fabrik_tri",
"https://www.craft-store.jp/products/tsumugi-fuji",
"https://www.craft-store.jp/products/1616-ty-square-165-gray",
"https://www.craft-store.jp/products/1616-ty-square-165-white",
"https://www.craft-store.jp/products/1616-ty-square-gray-set",
"https://www.craft-store.jp/products/1616-ty-square-white-set",
"https://www.craft-store.jp/products/1616-ty-square-235-gray",
"https://www.craft-store.jp/products/1616-ty-square-235-white",
"https://www.craft-store.jp/products/1616aritajapan_typalaceplate_set",
"https://www.craft-store.jp/products/1616aritajapan_typalaceplate_l",
"https://www.craft-store.jp/products/1616aritajapan_typalaceplate_s",
"https://www.craft-store.jp/products/ufufu",
"https://www.craft-store.jp/products/unilloy-22cm",
"https://www.craft-store.jp/products/gatomikio-waqwa-cup-l",
"https://www.craft-store.jp/products/gatomikio-waqwa-cup-s",
"https://www.craft-store.jp/products/zen",
"https://www.craft-store.jp/products/copper-spoon",
"https://www.craft-store.jp/products/copper-spoon-pinkgold",
"https://www.craft-store.jp/products/copper-spoon-set-gold",
"https://www.craft-store.jp/products/copper-spoon-set-silver",
"https://www.craft-store.jp/products/todai-spoon",
"https://www.craft-store.jp/products/suginokicraft_lunchbox",
"https://www.craft-store.jp/products/suginokicraft-lunchbox-twostory",
"https://www.craft-store.jp/products/suginokicraft-lunchbox-set",
"https://www.craft-store.jp/products/suginokicraft-large-lunchbox",
"https://www.craft-store.jp/products/tsunoda-ohitsu-l",
"https://www.craft-store.jp/products/tsunoda-ohitsu-s",
"https://www.craft-store.jp/products/tsuki-cutleryrest",
"https://www.craft-store.jp/products/kingflon_nomake_asagata_18",
"https://www.craft-store.jp/products/suzukou_guinomi",
"https://www.craft-store.jp/products/siwa-clutchbag-l",
"https://www.craft-store.jp/products/siwa-clutchbag-m",
"https://www.craft-store.jp/products/urushiyahayashi_sakura_meotobashi",
"https://www.craft-store.jp/products/siwa-slipper-l",
"https://www.craft-store.jp/products/siwa-slipper-s",
"https://www.craft-store.jp/products/maruhiro_hasami_soakcup_l",
"https://www.craft-store.jp/products/maruhiro_hasami_soakcup_l_set",
"https://www.craft-store.jp/products/maruhiro_hasami_soakcup_m",
"https://www.craft-store.jp/products/maruhiro_hasami_soakcup_m_set",
"https://www.craft-store.jp/products/maruhiro_hasami_soakcup_s",
"https://www.craft-store.jp/products/maruhiro_hasami_soakcup_s_set",
"https://www.craft-store.jp/products/maruhiro-soaktray-l",
"https://www.craft-store.jp/products/osakasuzuki_soleiltumbler",
"https://www.craft-store.jp/products/osakasuzuki_soleiltumbler_s",
"https://www.craft-store.jp/products/aiwashibori_tumbler90_brown",
"https://www.craft-store.jp/products/aiwashibori_tumbler90_6264",
"https://www.craft-store.jp/products/aiwashibori_tumbler90_silky",
"https://www.craft-store.jp/products/newking_18",
"https://www.craft-store.jp/products/macrw-bionmg60",
"https://www.craft-store.jp/products/siwa-shoulderbag",
"https://www.craft-store.jp/products/nosaku_beercup",
"https://www.craft-store.jp/products/nosaku_beercup_l",
"https://www.craft-store.jp/products/nousaku_futae",
"https://www.craft-store.jp/products/tsuki-flatplate-190",
"https://www.craft-store.jp/products/tsuki-flatplate-230",
"https://www.craft-store.jp/products/nakaoarumi_proking",
"https://www.craft-store.jp/products/proking_asagata_saute_18",
"https://www.craft-store.jp/products/proking_18",
"https://www.craft-store.jp/products/maruhiro-blockmug-l",
"https://www.craft-store.jp/products/tsuki-bowl-120",
"https://www.craft-store.jp/products/tsuki-bowl-170",
"https://www.craft-store.jp/products/aiwashibori-bowl120-usucha",
"https://www.craft-store.jp/products/aiwashibori-bowl120-kurocha-ohaguro",
"https://www.craft-store.jp/products/aiwashibori-bowl120-silky",
"https://www.craft-store.jp/products/aiwashibori-bowl150-usucha",
"https://www.craft-store.jp/products/aiwashibori-bowl150-kurocha-ohaguro",
"https://www.craft-store.jp/products/aiwashibori-bowl150-silky",
"https://www.craft-store.jp/products/odakoudouki_moscowmulecup_mat",
"https://www.craft-store.jp/products/odakoudouki_moscowmulecup_tsutime",
"https://www.craft-store.jp/products/siwa-lunchibag",
"https://www.craft-store.jp/products/sansaku_morning-glory_silver",
"https://www.craft-store.jp/products/morning-glory-sansaku_morning-glory_black",
"https://www.craft-store.jp/products/unilloy-24cm-shallow",
"https://www.craft-store.jp/products/makemyday-tray-two",
"https://www.craft-store.jp/products/makemyday-tray-five",
"https://www.craft-store.jp/products/hirotagarasu_shouyusashi_kikkou",
"https://www.craft-store.jp/products/hirotagarasu_shouyusashi_sakura",
"https://www.craft-store.jp/products/hirotagarasu_shouyusashi_kagome",
"https://www.craft-store.jp/products/hirotagarasu-syouwamodernglass-cupsaucer",
"https://www.craft-store.jp/products/hirotagarasu_syouwamodernglass_glass",
"https://www.craft-store.jp/products/hirotagarasu_syouwamodern_tumbler",
"https://www.craft-store.jp/products/syuzangama_itazara",
"https://www.craft-store.jp/products/syuzangama_nagaitazara",
"https://www.craft-store.jp/products/nousaku_chopstickrest_82",
"https://www.craft-store.jp/products/nousaku_chopstickrest_85",
"https://www.craft-store.jp/products/nagae-form-bamboo-set",
"https://www.craft-store.jp/products/nousaku_chopstickrest_sakura",
"https://www.craft-store.jp/products/nousaku_chopstickrest_knot",
"https://www.craft-store.jp/products/urushiyahayashi_lunchbox_l",
"https://www.craft-store.jp/products/urushiyahayashi_lunchbox_s",
"https://www.craft-store.jp/products/urushiyahayashi_lunchbox_long",
"https://www.craft-store.jp/products/tsunoda-cutting-board-angular-l",
"https://www.craft-store.jp/products/tsunoda-lunchbox-round-1",
"https://www.craft-store.jp/products/tsunoda-lunchbox-square",
"https://www.craft-store.jp/products/tsunoda-lunchbox-angular-1",
"https://www.craft-store.jp/products/tsunoda-lunchbox-angular-1-urushi",
"https://www.craft-store.jp/products/tsunoda-lunchbox-angular-2",
"https://www.craft-store.jp/products/tsunoda-meiboku-lunchbox-walnut",
"https://www.craft-store.jp/products/tsunoda-meiboku-lunchbox-blackcherry",
"https://www.craft-store.jp/products/tsunoda-meiboku-lunchbox-whiteash",
"https://www.craft-store.jp/products/100cm-musubi-both-isamonyou-kiku-100",
"https://www.craft-store.jp/products/2016-bg-coffeecup-l-white-sprinkle",
"https://www.craft-store.jp/products/big-game-l-white-sprinkle",
"https://www.craft-store.jp/products/bunzangama-beer-mug",
"https://www.craft-store.jp/products/bunzangama-beer-mug-plain",
"https://www.craft-store.jp/products/bunzangama-glass",
"https://www.craft-store.jp/products/bunzangama-glass-plain",
"https://www.craft-store.jp/products/bunzangama-kakuzara",
"https://www.craft-store.jp/products/bunzangama-kakuzara-plain",
"https://www.craft-store.jp/products/bunzangama-katakuchi",
"https://www.craft-store.jp/products/bunzangama-katakuchi-plain",
"https://www.craft-store.jp/products/bunzangama-kozara",
"https://www.craft-store.jp/products/bunzangama-kozara-plain",
"https://www.craft-store.jp/products/bunzangama-reishu-set",
"https://www.craft-store.jp/products/bunzangama-reishu-set-plain",
"https://www.craft-store.jp/products/bunzangama-rock-glass",
"https://www.craft-store.jp/products/bunzangama-rock-glass-plain",
"https://www.craft-store.jp/products/bunzangama-tumbler",
"https://www.craft-store.jp/products/bunzangama-tumbler-plain",
"https://www.craft-store.jp/products/gosu-mamezarahakoiri-set",
"https://www.craft-store.jp/products/hirotagarasu-honey-set",
"https://www.craft-store.jp/products/isuke-moku-bomboniere",
"https://www.craft-store.jp/products/kyo-marshmallow-bowl-and-plate",
"https://www.craft-store.jp/products/kyo-marshmallow-square-plate-pair",
"https://www.craft-store.jp/products/kyo-marshmallow-square-plate-pair-ww",
"https://www.craft-store.jp/products/musubi-both-musubi-100",
"https://www.craft-store.jp/products/musubi-oborozarashi-70",
"https://www.craft-store.jp/products/musubi-shantan-tsubaki-100",
"https://www.craft-store.jp/products/sobachoko-suzumi",
"https://www.craft-store.jp/products/takumi-no-kura-beer-glass-aurora-blue",
"https://www.craft-store.jp/products/takumi-no-kura-beer-glass-kirameki",
"https://www.craft-store.jp/products/takumi-no-kura-glass-aurora-pink",
"https://www.craft-store.jp/products/takumi-no-kura-glass-deep-green",
"https://www.craft-store.jp/products/takumi-no-kura-glass-kirameki",
"https://www.craft-store.jp/products/teruhiro-yanagihara-bowl-200-white",
"https://www.craft-store.jp/products/tsunoda-cutting-board-angular-s",
"https://www.craft-store.jp/products/yo-u-bianco-petty-knife-120mm",
"https://www.craft-store.jp/products/zoa-sometukeumetorimon-7sunzara"
]

print("admin href,", end="")
print("href,", end="")
print("Brand,", end="")
print("Item_name,", end="")
print("price,", end="")
print("carousel_image_setting,", end="")
print("color_setting,", end="")
print("item_detail,", end="")
print("notes_status,", end="")
print("shipping_date,", end="")
print("tag,", end="")
print("index,", end="")
print("meta_title,", end="")
print("meta_description,", end="")
print("")

for url in urls:
    time.sleep(1)
    res = req.urlopen(url)
    soup = BeautifulSoup(res, "html.parser")
    '''
    get list
        href
        Brand
        Item_name
        price
        carousel_image_setting
        color_setting
        item_detail
        notes
        index
        canocanil_status
        meta_title
        meta_description
        meta_keywords
        shipping_date

    '''

    href = url
    admin_href = url.replace("/products", "/admin/products")

    brand = soup.select_one(".product-main-info h2").string
    item_name = soup.select_one(".product-main-info h1").string
    price = soup.select_one(".product-main-info .product-price").text
    price = re.split(r'円', price)
    price = price[0]
    price = price.strip()
    price = price.replace(",", "")
    carousel_image_setting = soup.select("#slick img")
    carousel_image_setting = len(carousel_image_setting)
    color_settings = soup.select(".color-pallet-box span")
    color_que = []
    if color_settings != []:
        for color_setting in color_settings:
            color_setting = color_setting.find("i").string
            color_que.append(color_setting)

        color_que = ','.join(color_que)
        color_que = color_que.replace(",", " ")
    else:
        color_que = "no pattern"

    item_detail = soup.select_one("#product-description")
    if item_detail == None:
        item_detail = "nothing article you have to do something it need."
    else:
        item_detail = "Article is ok"

    notes = soup.select_one("#product-annotation-box").text
    notes = notes.replace(",", "")

    shipping_date = soup.select_one("#product-shipping-time").text
    shipping_date = shipping_date.strip()
    shipping_date = shipping_date.replace(",", " ")
    shipping_date = shipping_date.replace("最短", "")
    shipping_date = shipping_date.replace("月", "/")
    shipping_date = re.sub(r'日.*', '', shipping_date)

    tag_list = []
    tags = soup.select(".single-product .tag-item")
    for tag in tags:
        tag = tag.string
        tag_list.append(tag)
    if tag_list != []:
        tag_list = ','.join(tag_list)
        tag_list = tag_list.replace(",", " ")
    else:
        tag_list = "Nothing any tag"

    try:
        index = soup.find(attrs={"name": "robots"}).get('content')
    except:
        index = "index"
    try:
        canonicalstatus = soup.find(attrs={"rel": "canonical"}).get('href')
    except:
        canonicalstatus = "nothing"
    metatitle = soup.select_one("title")
    metadescription = soup.find(attrs={"name": "description"}).get('content')
    metadescription = metadescription.replace(",", "")

    print(admin_href, end=",")
    print(href, end=",")
    print(brand, end=",")
    print(item_name, end=",")
    print(price, end=",")
    print(carousel_image_setting, end=",")
    print(color_que, end=",")
    print(item_detail.replace('\n',''), end=",")
    print(notes.replace('\n',''), end=",")
    print(shipping_date, end=",")
    print(tag_list, end=",")
    print(index, end=",")
    print(metatitle, end=",")
    print(metadescription, end=",")
    print("")
