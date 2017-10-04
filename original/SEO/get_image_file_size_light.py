from bs4 import BeautifulSoup
import requests
import urllib.request as req
import urllib.parse
from urllib.parse import urlparse as urlparse
import urllib.request
from urllib.parse import urljoin
from os import makedirs
import os.path, time, re
from html.parser import HTMLParser

base_url = "https://www.craft-store.jp"

urls=[
"https://www.craft-store.jp",
"https://www.craft-store.jp/products/1616aritajapan_typalaceplate_s",
"https://www.craft-store.jp/products/kidate-sokomaru-koboshi",
"https://www.craft-store.jp/features/staff-pick-ideyasuhiro",
"https://www.craft-store.jp/t/tableware",
"https://www.craft-store.jp/products/suginokicraft_lunchbox",
"https://www.craft-store.jp/products/sanjotokusyuchukousho-ssc-20",
"https://www.craft-store.jp/t/kitchenware",
"https://www.craft-store.jp/cart",
"https://www.craft-store.jp/t/goods",
"https://www.craft-store.jp/products?utf8=✓&keywords=",
"https://www.craft-store.jp/products/osakasuzuki_soleiltumbler_s",
"https://www.craft-store.jp/features/difference-of-sake-by-glass",
"https://www.craft-store.jp/products/kidate-sokomaru-rocks",
"https://www.craft-store.jp/products/unilloy-22cm-shallow",
"https://www.craft-store.jp/products/todai-spoon",
"https://www.craft-store.jp/features/present-to-men",
"https://www.craft-store.jp/about",
"https://www.craft-store.jp/products/yasudagawara-cup-80",
"https://www.craft-store.jp/products/kidate-kuki-rocks",
"https://www.craft-store.jp/t/tableware?page=2",
"https://www.craft-store.jp/t/bathroom-supplies",
"https://www.craft-store.jp/features/gift-liquor-glass",
"https://www.craft-store.jp/ranks",
"https://www.craft-store.jp/products/fabrik_bi",
"https://www.craft-store.jp/products/suginoki-runchbox-set",
"https://www.craft-store.jp/products/2016-bg-coffeecup-l-white-sprinkle",
"https://www.craft-store.jp/products/suginokicraft-large-lunchbox",
"https://www.craft-store.jp/t/tableware?page=3",
"https://www.craft-store.jp/features/wedding-present-tableware",
"https://www.craft-store.jp/products/suginokicraft-lunchbox-twostory",
"https://www.craft-store.jp/t/goods?page=2",
"https://www.craft-store.jp/features/fabrik-introduction",
"https://www.craft-store.jp/products/takakuwakinzoku-curryspoon",
"https://www.craft-store.jp/t/tableware?page=4",
"https://www.craft-store.jp/features",
"https://www.craft-store.jp/products/gosu-mamezarahakoiri-set",
"https://www.craft-store.jp/t/tableware?page=6",
"https://www.craft-store.jp/t/tableware?page=5",
"https://www.craft-store.jp/scenes/reward-yourself",
"https://www.craft-store.jp/checkout/address",
"https://www.craft-store.jp/products/rice-wine-glass-for-sake",
"https://www.craft-store.jp/products/sghr-awaglass-champagne",
"https://www.craft-store.jp/features/nagae-plus-introduction",
"https://www.craft-store.jp/products/keepware-plate-16",
"https://www.craft-store.jp/products/najimi_tumbler",
"https://www.craft-store.jp/features/modern-aritayaki",
"https://www.craft-store.jp/products/soil-soap-dish-circle",
"https://www.craft-store.jp/products/shiro-tilt",
"https://www.craft-store.jp/scenes/birthday-gifts",
"https://www.craft-store.jp/products/takakuwakinzoku-desertspoon",
"https://www.craft-store.jp/products/soil-bath-mat-30cm",
"https://www.craft-store.jp/products/takakuwa-dessert-set",
"https://www.craft-store.jp/scenes/wedding-gifts",
"https://www.craft-store.jp/products/fabrik_long",
"https://www.craft-store.jp/products/nagae-collinette",
"https://www.craft-store.jp/t/tableware?page=7",
"https://www.craft-store.jp/galleries",
"https://www.craft-store.jp/law",
"https://www.craft-store.jp/products/kimuraglass-waterglass",
"https://www.craft-store.jp/products/siwa-clutchbag-m",
"https://www.craft-store.jp/contact",
"https://www.craft-store.jp/products/kimuraglass-table-soysauce",
"https://www.craft-store.jp/products/urushiyahayashi_lunchbox_s",
"https://www.craft-store.jp/features/how-to-choose-wine-glass",
"https://www.craft-store.jp/features/history-furoshiki",
"https://www.craft-store.jp/features/usual-dishes-1616-arita",
"https://www.craft-store.jp/products?price=0-5000",
"https://www.craft-store.jp/products/2016-sf-mug-red",
"https://www.craft-store.jp/products/sanjotokusyuchukousho-ssc-26",
"https://www.craft-store.jp/tags/弁当箱",
"https://www.craft-store.jp/brands/tsuki",
"https://www.craft-store.jp/features/difference-of-sake-by-ice",
"https://www.craft-store.jp/products/3way_mini_wallet",
"https://www.craft-store.jp/products/aiwashibori_tumbler90_silky",
"https://www.craft-store.jp/brands/1616aritajapan",
"https://www.craft-store.jp/products?keywords=有田&utf8=✓",
"https://www.craft-store.jp/products/nagae-tin-breath-ring-10x80-silver",
"https://www.craft-store.jp/products/sansaku_morning-glory_silver",
"https://www.craft-store.jp/brands/gatomikiosyouten",
"https://www.craft-store.jp/features/evening_drink",
"https://www.craft-store.jp/products/2016-bg-coffee-dripper",
"https://www.craft-store.jp/products/hirotagarasu-syouwamodernglass-cupsaucer",
"https://www.craft-store.jp/products/much",
"https://www.craft-store.jp/checkout/delivery",
"https://www.craft-store.jp/features/type-of-coffee-dripper",
"https://www.craft-store.jp/products/hirotagarasu_shouyusashi_kagome",
"https://www.craft-store.jp/features/small-and-convenient-wallet",
"https://www.craft-store.jp/products/osashimi-set",
"https://www.craft-store.jp/features/soak_1",
"https://www.craft-store.jp/products/makemyday-tray-five",
"https://www.craft-store.jp/products/soil-toothbrush-stand",
"https://www.craft-store.jp/products/suginokicraft-lunchbox-set",
"https://www.craft-store.jp/scenes/reward-yourself?page=3",
"https://www.craft-store.jp/brands/nousaku",
"https://www.craft-store.jp/brands/tsunoda-seibee",
"https://www.craft-store.jp/features/suginoki-brand",
"https://www.craft-store.jp/products/takakuwakinzoku-milkpan-straight",
"https://www.craft-store.jp/products/urushiyahayashi_sakura_meotobashi",
"https://www.craft-store.jp/checkout/payment",
"https://www.craft-store.jp/features/rwg-experiment",
"https://www.craft-store.jp/guide",
"https://www.craft-store.jp/products?keywords=有田&page=2&utf8=✓",
"https://www.craft-store.jp/products/2016-bg-coffecup-s-white-sprinkle",
"https://www.craft-store.jp/products/siwa-lunchibag",
"https://www.craft-store.jp/scenes/birthday-gifts?page=2",
"https://www.craft-store.jp/products/maruhiro-blockmug-l",
"https://www.craft-store.jp/products/nagae-ratio-square-m",
"https://www.craft-store.jp/scenes/birthday-gifts?page=3",
"https://www.craft-store.jp/features/beeswax-candle",
"https://www.craft-store.jp/features/roll-pencilcase",
"https://www.craft-store.jp/products/aiwashibori_tumbler90_6264",
"https://www.craft-store.jp/products/cooloff-set-koushi-en",
"https://www.craft-store.jp/products/sobachoko-suzumi",
"https://www.craft-store.jp/scenes/reward-yourself?page=2",
"https://www.craft-store.jp/brands/hasami",
"https://www.craft-store.jp/brands/unilloy",
"https://www.craft-store.jp/features/beautiful-arita-yaki-for-gift",
"https://www.craft-store.jp/features/lunchbox-gift",
"https://www.craft-store.jp/products/takakuwakinzoku-ladle",
"https://www.craft-store.jp/brands/barbar",
"https://www.craft-store.jp/brands/nagae-plus",
"https://www.craft-store.jp/brands/suginokicraft",
"https://www.craft-store.jp/brands/tashirotoukiten",
"https://www.craft-store.jp/checkout/confirm",
"https://www.craft-store.jp/products?keywords=&page=2&utf8=✓",
"https://www.craft-store.jp/products/1616aritajapan_typalaceplate_l",
"https://www.craft-store.jp/products/musubi-oborozarashi-70",
"https://www.craft-store.jp/products/nousaku-guinomi",
"https://www.craft-store.jp/products/takakuwakinzoku-teaspoon",
"https://www.craft-store.jp/products/unilloy-22cm",
"https://www.craft-store.jp/brands/osakasuzuki",
"https://www.craft-store.jp/brands/urushiyahayashi",
"https://www.craft-store.jp/features/white-dishes",
"https://www.craft-store.jp/login",
"https://www.craft-store.jp/products/1616aritajapan_typalaceplate_set",
"https://www.craft-store.jp/products/fabrik_keycard",
"https://www.craft-store.jp/products/hirotagarasu_syouwamodernglass_glass",
"https://www.craft-store.jp/products/nosaku_beercup",
"https://www.craft-store.jp/products/urushiyahayashi_lunchbox_l",
"https://www.craft-store.jp/scenes/housewarming",
"https://www.craft-store.jp/scenes/wedding-gifts?page=2",
"https://www.craft-store.jp/scenes/wedding-gifts?page=3",
"https://www.craft-store.jp/brands/nakaoarumiseisakusyo",
"https://www.craft-store.jp/products",
"https://www.craft-store.jp/products/nousaku_chopstickrest_knot",
"https://www.craft-store.jp/brands/fabrik",
"https://www.craft-store.jp/brands/siwa",
"https://www.craft-store.jp/features/ideas",
"https://www.craft-store.jp/products/copper-spoon",
"https://www.craft-store.jp/products/copper-spoon-set-gold",
"https://www.craft-store.jp/products/sghr-ginette-old",
"https://www.craft-store.jp/products/siwa-shoulderbag",
"https://www.craft-store.jp/products/ufufu",
"https://www.craft-store.jp/features/herashibori",
"https://www.craft-store.jp/features/soak_2",
"https://www.craft-store.jp/products?utf8=✓&keywords=soil",
"https://www.craft-store.jp/products/fabrik_tri",
"https://www.craft-store.jp/products/kago-oval-s",
"https://www.craft-store.jp/products/tsumugi-fuji",
"https://www.craft-store.jp/brands/candle-lights",
"https://www.craft-store.jp/brands/hirotagarasu",
"https://www.craft-store.jp/features/what-is-hera-sibori",
"https://www.craft-store.jp/products/bunzangama-kozara-plain",
"https://www.craft-store.jp/products/macrw-bionmg60",
"https://www.craft-store.jp/products/siwa-clutchbag-l",
"https://www.craft-store.jp/products/teori-grid-square",
"https://www.craft-store.jp/tags/漆屋はやし",
"https://www.craft-store.jp/tags/陶磁器",
"https://www.craft-store.jp/brands/copper-the-cutlery",
"https://www.craft-store.jp/features/how-to-make-good-wiskey-soda",
"https://www.craft-store.jp/features/urushiya-hayashi",
"https://www.craft-store.jp/products?page=3&price=0-5000",
"https://www.craft-store.jp/products/nagae-tin-breath-ring-10x80-antiquegold",
"https://www.craft-store.jp/products/sghr-duo-old",
"https://www.craft-store.jp/products/soil-coaster-large-circle",
"https://www.craft-store.jp/products/takakuwakinzoku-desertfork",
"https://www.craft-store.jp/brands/elfin",
"https://www.craft-store.jp/features/how-to-choose-knife",
"https://www.craft-store.jp/products?page=2&price=0-5000",
"https://www.craft-store.jp/products?utf8=✓&keywords=弁当",
"https://www.craft-store.jp/products/celebrate-set-bamboo",
"https://www.craft-store.jp/products/hayashi-runchbox-set",
"https://www.craft-store.jp/products/osakasuzuki_soleiltumbler",
"https://www.craft-store.jp/products/urushiyahayashi_lunchbox_long",
"https://www.craft-store.jp/brands/sansaku",
"https://www.craft-store.jp/features/gift-tin-tumbler",
"https://www.craft-store.jp/products?price=25000-999999",
"https://www.craft-store.jp/products?price=5001-10000",
"https://www.craft-store.jp/products/camdlelights-greencandle-41",
"https://www.craft-store.jp/products/keepware-bowl-16",
"https://www.craft-store.jp/products/kingflon_nomake_asagata_18",
"https://www.craft-store.jp/products/nagae-tin-breath-40-silver",
"https://www.craft-store.jp/products/nousaku_chopstickrest_82",
"https://www.craft-store.jp/products/nousaku_futae",
"https://www.craft-store.jp/products/takakuwakinzoku-toriwakespoon-l",
"https://www.craft-store.jp/products/tsunoda-cutting-board-angular-s",
"https://www.craft-store.jp/scenes/housewarming?page=2",
"https://www.craft-store.jp/tags/ナガエプリュス",
"https://www.craft-store.jp/brands/zoa",
"https://www.craft-store.jp/features/tablecordinate-with-wooden-dishes",
"https://www.craft-store.jp/features/wood_items",
"https://www.craft-store.jp/products?utf8=✓&keywords=弁当箱",
"https://www.craft-store.jp/products/hirotagarasu_syouwamodern_tumbler",
"https://www.craft-store.jp/products/kago-rose",
"https://www.craft-store.jp/products/kimuraglass-droplet",
"https://www.craft-store.jp/products/nagae-collinette-aile",
"https://www.craft-store.jp/products/nakaoarumi_proking",
"https://www.craft-store.jp/products/sghr-kirameki-rocks-grid",
"https://www.craft-store.jp/products/soil-dispenser-tray",
"https://www.craft-store.jp/products/tsunoda-ohitsu-l",
"https://www.craft-store.jp/products/tsunoda-ohitsu-s",
"https://www.craft-store.jp/products/yasudagawara-cup-45",
"https://www.craft-store.jp/products/yasudagawara-cup-65",
"https://www.craft-store.jp/signup",
"https://www.craft-store.jp/tags/木工品",
"https://www.craft-store.jp/tags/田代陶器店",
"https://www.craft-store.jp/features/fabrik",
"https://www.craft-store.jp/features/gift-dish",
"https://www.craft-store.jp/products?page=2&price=5001-10000",
"https://www.craft-store.jp/products?page=4&price=0-5000",
"https://www.craft-store.jp/products?utf8=✓&keywords=sghr",
"https://www.craft-store.jp/products/2016-bg-coffeecup-l-black-matt",
"https://www.craft-store.jp/products/aji-grill-square-shima",
"https://www.craft-store.jp/products/celebrate-set-plum",
"https://www.craft-store.jp/products/futae",
"https://www.craft-store.jp/products/maruhiro_hasami_soakcup_m",
"https://www.craft-store.jp/products/odakoudouki_moscowmulecup_mat",
"https://www.craft-store.jp/products/zen",
"https://www.craft-store.jp/tags/酒器",
"https://www.craft-store.jp/features/no-liquid-spill-soy-source-bottle",
"https://www.craft-store.jp/features/tin-interior-kago",
"https://www.craft-store.jp/features/wine-glass",
"https://www.craft-store.jp/products?keywords=&page=3&utf8=✓",
"https://www.craft-store.jp/products?utf8=✓&keywords=安田",
"https://www.craft-store.jp/products/copper-spoon-pinkgold",
"https://www.craft-store.jp/products/first-knife-set",
"https://www.craft-store.jp/products/kimuraglass-lotus-goblet-10oz",
"https://www.craft-store.jp/products/makemyday-tray-two",
"https://www.craft-store.jp/products/maruhiro-soaktray-l",
"https://www.craft-store.jp/products/nagae-ratio-square-l",
"https://www.craft-store.jp/products/proking_18",
"https://www.craft-store.jp/products/sghr-natsu-17-circle",
"https://www.craft-store.jp/products/soil-amenity-tray",
"https://www.craft-store.jp/products/suzukou_guinomi",
"https://www.craft-store.jp/products/takakuwakinzoku-minibutterknife",
"https://www.craft-store.jp/products/takakuwakinzoku-turner",
"https://www.craft-store.jp/products/tsunoda-lunchbox-angular-1",
"https://www.craft-store.jp/products/unilloy-24cm-shallow",
"https://www.craft-store.jp/products/yo-u-bianco-small-santoku-knife-165mm",
"https://www.craft-store.jp/scenes/housewarming?page=3",
"https://www.craft-store.jp/scenes/housewarming?page=4",
"https://www.craft-store.jp/tags/elfin",
"https://www.craft-store.jp/tags/陶磁器?page=2",
"https://www.craft-store.jp/tags/革製品",
"https://www.craft-store.jp/term",
"https://www.craft-store.jp/brands/gosu",
"https://www.craft-store.jp/products?keywords=&page=4&utf8=✓",
"https://www.craft-store.jp/products?keywords=&page=5&utf8=✓",
"https://www.craft-store.jp/products?page=2",
"https://www.craft-store.jp/products?page=3&price=5001-10000",
"https://www.craft-store.jp/products?page=5&price=0-5000",
"https://www.craft-store.jp/products?utf8=✓&keywords=kidate",
"https://www.craft-store.jp/products?utf8=✓&keywords=ティー",
"https://www.craft-store.jp/products?utf8=✓&keywords=能作",
"https://www.craft-store.jp/products?utf8=✓&keywords=高桑",
"https://www.craft-store.jp/products/2016-ty-180-black",
"https://www.craft-store.jp/products/aka-swing",
"https://www.craft-store.jp/products/camdlelights-beeswax-stick",
"https://www.craft-store.jp/products/celebrate-set-pine",
"https://www.craft-store.jp/products/fabrik_key",
"https://www.craft-store.jp/products/gatomikio-waqwa-cup-l",
"https://www.craft-store.jp/products/hannari-kokoharecup",
"https://www.craft-store.jp/products/kago-dahlia",
"https://www.craft-store.jp/products/kimuraglass-crumple-wine-s-set",
"https://www.craft-store.jp/products/morning-glory-sansaku_morning-glory_black",
"https://www.craft-store.jp/products/nagae-tin-breath-20-silver",
"https://www.craft-store.jp/products/newking_18",
"https://www.craft-store.jp/products/soil-soap-dish-bath-circle",
"https://www.craft-store.jp/products/takakuwakinzoku-cakefork",
"https://www.craft-store.jp/features/event-report",
"https://www.craft-store.jp/features/relax-home-café",
"https://www.craft-store.jp/features/types-of-sake",
"https://www.craft-store.jp/privacy",
"https://www.craft-store.jp/products?page=4",
"https://www.craft-store.jp/products?page=9&utf8=✓",
"https://www.craft-store.jp/products?utf8=✓&keywords=tin+breath",
"https://www.craft-store.jp/products?utf8=✓&keywords=TYパレスプレート",
"https://www.craft-store.jp/products?utf8=✓&keywords=アヅマ",
"https://www.craft-store.jp/products?utf8=✓&keywords=トーダイ",
"https://www.craft-store.jp/products?utf8=✓&keywords=ホーロー",
"https://www.craft-store.jp/products/1616-ty-square-165-gray",
"https://www.craft-store.jp/products/2016-ch-teacup",
"https://www.craft-store.jp/products/2016-sf-mug-white",
"https://www.craft-store.jp/products/2016-ty-180-white",
"https://www.craft-store.jp/products/bunzangama-tumbler-plain",
"https://www.craft-store.jp/products/camdlelights-beeswax-l",
"https://www.craft-store.jp/products/gatomikio-waqwa-cup-s",
"https://www.craft-store.jp/products/kago-square-m",
"https://www.craft-store.jp/products/keepware-plate-25",
"https://www.craft-store.jp/products/musubi-chirimen-ume-70",
"https://www.craft-store.jp/products/nagae-collinette-lymph",
"https://www.craft-store.jp/products/nagae-form-bamboo-set",
"https://www.craft-store.jp/products/soil-umbrella-stand",
"https://www.craft-store.jp/products/suginokicraft_lunchbox_b",
"https://www.craft-store.jp/products/unilloy-20cm",
"https://www.craft-store.jp/products/zoa-kacho-7sunzara",
"https://www.craft-store.jp/tags/丸三安田瓦",
"https://www.craft-store.jp/tags/陶磁器?page=3",
"https://www.craft-store.jp/features?page=2",
"https://www.craft-store.jp/features?page=3",
"https://www.craft-store.jp/features/gift-liquor-glass-feature",
"https://www.craft-store.jp/features/nousaku-tin-chopstick-rest",
"https://www.craft-store.jp/features/unilloy",
"https://www.craft-store.jp/features/wedding-present",
"https://www.craft-store.jp/products?keywords=&utf8=✓",
"https://www.craft-store.jp/products?page=10&utf8=✓",
"https://www.craft-store.jp/products?page=4&price=5001-10000",
"https://www.craft-store.jp/products?utf8=✓&keywords=RATIO",
"https://www.craft-store.jp/products?utf8=✓&keywords=スピーカー",
"https://www.craft-store.jp/products?utf8=✓&keywords=蕎麦猪口",
"https://www.craft-store.jp/products?utf8=✓&keywords=風呂敷",
"https://www.craft-store.jp/products/2016-sf-mug-gray",
"https://www.craft-store.jp/products/bunzangama-reishu-set-plain",
"https://www.craft-store.jp/products/maruhiro_hasami_soakcup_s",
"https://www.craft-store.jp/products/nagae-ratio-square-s",
"https://www.craft-store.jp/products/odakoudouki_moscowmulecup_tsutime",
"https://www.craft-store.jp/products/sghr-crystaledge",
"https://www.craft-store.jp/products/sghr-nightcarafe",
"https://www.craft-store.jp/products/takumi-no-kura-glass-kirameki",
"https://www.craft-store.jp/products/tsuki-flatplate-230",
"https://www.craft-store.jp/products/tsunoda-lunchbox-angular-2",
"https://www.craft-store.jp/products/tsunoda-runchbox-set",
"https://www.craft-store.jp/products/yo-u-bianco-dimple-180mm",
"https://www.craft-store.jp/products/zoa-fuyoude-7sunzara",
"https://www.craft-store.jp/tags/TSUKI",
"https://www.craft-store.jp/tags/カップ",
"https://www.craft-store.jp/tags/杉の木クラフト",
"https://www.craft-store.jp/tags/能作",
"https://www.craft-store.jp/tags/錫製品",
"https://www.craft-store.jp/brands/soil",
"https://www.craft-store.jp/features/mothers-day-nousaku",
"https://www.craft-store.jp/features/vegetable-leather",
"https://www.craft-store.jp/orders/R094774702",
"https://www.craft-store.jp/products?page=3",
"https://www.craft-store.jp/products?page=5",
"https://www.craft-store.jp/products?page=5&utf8=✓",
"https://www.craft-store.jp/products?page=7",
"https://www.craft-store.jp/products?price=10001-15000",
"https://www.craft-store.jp/products?price=15001-20000",
"https://www.craft-store.jp/products?utf8=✓&keywords=FABRIK",
"https://www.craft-store.jp/products?utf8=✓&keywords=keep",
"https://www.craft-store.jp/products?utf8=✓&keywords=NAGAE+",
"https://www.craft-store.jp/products?utf8=✓&keywords=アイスクリーム",
"https://www.craft-store.jp/products?utf8=✓&keywords=カレー",
"https://www.craft-store.jp/products?utf8=✓&keywords=コーヒー",
"https://www.craft-store.jp/products?utf8=✓&keywords=ナガエ",
"https://www.craft-store.jp/products?utf8=✓&keywords=ファブリック",
"https://www.craft-store.jp/products?utf8=✓&keywords=マルヒロ",
"https://www.craft-store.jp/products?utf8=✓&keywords=大阪錫器",
"https://www.craft-store.jp/products?utf8=✓&keywords=木村硝子",
"https://www.craft-store.jp/products?utf8=✓&keywords=見るストーリー",
"https://www.craft-store.jp/products/1616-ty-square-235-gray",
"https://www.craft-store.jp/products/1616-ty-square-gray-set",
"https://www.craft-store.jp/products/2016-bg-coffeecup-s-black-matt",
"https://www.craft-store.jp/products/bunzangama-tumbler",
"https://www.craft-store.jp/products/copper-spoon-set-silver",
"https://www.craft-store.jp/products/gatomikio-tasai-cup",
"https://www.craft-store.jp/products/isuke-moku-plate-b",
"https://www.craft-store.jp/products/isuke-moku-tray-a",
"https://www.craft-store.jp/products/kago-square-s",
"https://www.craft-store.jp/products/keepware-cup-250",
"https://www.craft-store.jp/products/marubun-square-plate-mid",
"https://www.craft-store.jp/products/maruhiro_hasami_soakcup_s_set",
"https://www.craft-store.jp/products/musubi-shantan-tsubaki-90",
"https://www.craft-store.jp/products/nagae-tin-breath-40-antiquegold",
"https://www.craft-store.jp/products/nousaku-chopstickrest-kasane-maru-2",
"https://www.craft-store.jp/products/nousaku-fuurin-rin-silver",
"https://www.craft-store.jp/products/sghr-thebeer-nido",
"https://www.craft-store.jp/products/sobachoko-iroe-axolotl",
"https://www.craft-store.jp/products/soil-sponge-tray",
"https://www.craft-store.jp/products/takakuwa-ladle-turner-set",
"https://www.craft-store.jp/products/tsuki-bowl-170",
"https://www.craft-store.jp/products/tsuki-flatplate-190",
"https://www.craft-store.jp/products/tsunoda-lunchbox-angular-1-urushi",
"https://www.craft-store.jp/products/tsunoda-meiboku-lunchbox-walnut",
"https://www.craft-store.jp/products/zoa-kumowarisansuimon-7sunzara",
"https://www.craft-store.jp/products/zoa-nejiri-7sunzara",
"https://www.craft-store.jp/products/zoa-sannsui-7sunzara",
"https://www.craft-store.jp/tags/木工品?page=2",
"https://www.craft-store.jp/tags/木村硝子店",
"https://www.craft-store.jp/tags/菅原工芸硝子",
"https://www.craft-store.jp/tags/酒器?page=2",
"https://www.craft-store.jp/tags/鍋",
"https://www.craft-store.jp/cart?pid=2016-bg-coffeecup-l-white-sprinkle",
"https://www.craft-store.jp/cart?pid=soil-bath-mat-30cm",
"https://www.craft-store.jp/cart?pid=suginokicraft-large-lunchbox",
"https://www.craft-store.jp/checkout/update/payment",
"https://www.craft-store.jp/features/categories/pick-up",
"https://www.craft-store.jp/features/craft-popup",
"https://www.craft-store.jp/features/how-to-clean-lacqueware",
"https://www.craft-store.jp/features/tin-cup",
"https://www.craft-store.jp/features/yotsukawa-guinomi",
"https://www.craft-store.jp/orders/R765736721",
"https://www.craft-store.jp/products?keywords=&page=6&utf8=✓",
"https://www.craft-store.jp/products?keywords=&page=7&utf8=✓",
"https://www.craft-store.jp/products?keywords=&page=9&utf8=✓",
"https://www.craft-store.jp/products?keywords=ティー&page=2&utf8=✓",
"https://www.craft-store.jp/products?page=2&utf8=✓",
"https://www.craft-store.jp/products?page=3&utf8=✓",
"https://www.craft-store.jp/products?page=6",
"https://www.craft-store.jp/products?page=8",
"https://www.craft-store.jp/products?page=9",
"https://www.craft-store.jp/products?price=20001-25000",
"https://www.craft-store.jp/products?utf8=",
"https://www.craft-store.jp/products?utf8=✓&keywords=2016",
"https://www.craft-store.jp/products?utf8=✓&keywords=BIG-GAME+コーヒーカップL+White+Sprinkle_2016",
"https://www.craft-store.jp/products?utf8=✓&keywords=futae",
"https://www.craft-store.jp/products?utf8=✓&keywords=KEEP WARE",
"https://www.craft-store.jp/products?utf8=✓&keywords=R&W=",
"https://www.craft-store.jp/products?utf8=✓&keywords=rice",
"https://www.craft-store.jp/products?utf8=✓&keywords=TIN-BREATH",
"https://www.craft-store.jp/products?utf8=✓&keywords=TIN+BREATH+&+TIN+BREATH+Ring=",
"https://www.craft-store.jp/products?utf8=✓&keywords=tyパレス",
"https://www.craft-store.jp/products?utf8=✓&keywords=アイスクリーム_アヅマ/トーダイ",
"https://www.craft-store.jp/products?utf8=✓&keywords=スプーン",
"https://www.craft-store.jp/products?utf8=✓&keywords=そば猪口",
"https://www.craft-store.jp/products?utf8=✓&keywords=ドリッパー",
"https://www.craft-store.jp/products?utf8=✓&keywords=ビアカップ",
"https://www.craft-store.jp/products?utf8=✓&keywords=フライパン",
"https://www.craft-store.jp/products?utf8=✓&keywords=三条特殊鋳工所",
"https://www.craft-store.jp/products?utf8=✓&keywords=四津川製作所",
"https://www.craft-store.jp/products?utf8=✓&keywords=日本酒",
"https://www.craft-store.jp/products?utf8=✓&keywords=橋",
"https://www.craft-store.jp/products/1616-ty-square-235-white",
"https://www.craft-store.jp/products/2016-bg-black-matt",
"https://www.craft-store.jp/products/2016-bg-white-sprinkle",
"https://www.craft-store.jp/products/2016-ch-180",
"https://www.craft-store.jp/products/2016-sf-shouyusashi-gray",
"https://www.craft-store.jp/products/camdlelights-beeswax-m",
"https://www.craft-store.jp/products/camdlelights-beeswax-mug",
"https://www.craft-store.jp/products/camdlelights-greencandle-38",
"https://www.craft-store.jp/products/gatomikio-tasai-bowl-m",
"https://www.craft-store.jp/products/gosu-hashiokihakoiri-set",
"https://www.craft-store.jp/products/gosu-kodukehakoiri-set",
"https://www.craft-store.jp/products/hirotagarasu_shouyusashi_kikkou",
"https://www.craft-store.jp/products/hirotagarasu-honey-set",
"https://www.craft-store.jp/products/kago-oval-l",
"https://www.craft-store.jp/products/kyo-marshmallow-bowl-and-plate-py",
"https://www.craft-store.jp/products/kyo-marshmallow-bowl-and-plate-yw",
"https://www.craft-store.jp/products/kyo-marshmallow-square-plate-pair-ww",
"https://www.craft-store.jp/products/marubun-square-plate-large",
"https://www.craft-store.jp/products/marubun-square-plate-small",
"https://www.craft-store.jp/products/nagae-tin-breath-20-antiquegold",
"https://www.craft-store.jp/products/nagae-tin-breath-ring-15x80-antiquegold",
"https://www.craft-store.jp/products/nousaku_chopstickrest_85",
"https://www.craft-store.jp/products/nousaku_chopstickrest_sakura",
"https://www.craft-store.jp/products/nousaku-chopstickrest-tsuki-5",
"https://www.craft-store.jp/products/nousaku-fuurin-heirin-round",
"https://www.craft-store.jp/products/proking_asagata_saute_18",
"https://www.craft-store.jp/products/siwa-slipper-s",
"https://www.craft-store.jp/products/sobachoko-iroe-chameleon",
"https://www.craft-store.jp/products/sobachoko-iroe-short-hair",
"https://www.craft-store.jp/products/takumi-no-kura-glass-aurora-pink",
"https://www.craft-store.jp/products/tasaki-light-s-10oz",
"https://www.craft-store.jp/products/tsunoda-lunchbox-round-1",
"https://www.craft-store.jp/products/tsunoda-lunchbox-square",
"https://www.craft-store.jp/products/tsunoda-meiboku-lunchbox-blackcherry",
"https://www.craft-store.jp/products/tsunoda-meiboku-lunchbox-whiteash",
"https://www.craft-store.jp/products/zoa-fuyoudemon-7sunzara",
"https://www.craft-store.jp/products/zoa-nejirimadorikamon-7sunzara",
"https://www.craft-store.jp/products/zoa-sometukeumetorimon-7sunzara",
"https://www.craft-store.jp/tags/1616aritajapan",
"https://www.craft-store.jp/tags/2016arita",
"https://www.craft-store.jp/tags/SIWA",
"https://www.craft-store.jp/tags/コップ",
"https://www.craft-store.jp/tags/プレート",
"https://www.craft-store.jp/tags/雑貨",
"https://www.craft-store.jp/)",
"https://www.craft-store.jp/cart?pid=kidate-sokomaru-koboshi",
"https://www.craft-store.jp/cart?pid=suginoki-runchbox-set",
"https://www.craft-store.jp/cart?pid=takakuwakinzoku-curryspoon",
"https://www.craft-store.jp/features-tags/モダン",
"https://www.craft-store.jp/features-tags/名刺入れ",
"https://www.craft-store.jp/features-tags/有田焼",
"https://www.craft-store.jp/features-tags/漆屋はやし",
"https://www.craft-store.jp/features-tags/食器",
"https://www.craft-store.jp/features/fashionable-present-for-girls",
"https://www.craft-store.jp/features/sensitive",
"https://www.craft-store.jp/features/Valentine",
"https://www.craft-store.jp/history-furoshiki",
"https://www.craft-store.jp/orders/R091548097",
"https://www.craft-store.jp/orders/R182961945",
"https://www.craft-store.jp/orders/R337042283",
"https://www.craft-store.jp/orders/R389808420",
"https://www.craft-store.jp/orders/R395749543",
"https://www.craft-store.jp/orders/R493910632",
"https://www.craft-store.jp/orders/R496387906",
"https://www.craft-store.jp/orders/R552770340",
"https://www.craft-store.jp/orders/R595993184",
"https://www.craft-store.jp/orders/R641928226",
"https://www.craft-store.jp/orders/R649480610",
"https://www.craft-store.jp/orders/R664992674",
"https://www.craft-store.jp/orders/R718490947",
"https://www.craft-store.jp/orders/R866918951",
"https://www.craft-store.jp/products?keywords=&page=10&utf8=✓",
"https://www.craft-store.jp/products?keywords=&page=8&utf8=✓",
"https://www.craft-store.jp/products?keywords=Ｌ&page=2&utf8=✓",
"https://www.craft-store.jp/products?keywords=ティー&utf8=✓",
"https://www.craft-store.jp/products?keywords=漆&page=2&utf8=✓",
"https://www.craft-store.jp/products?page=10",
"https://www.craft-store.jp/products?page=2&price=10001-15000",
"https://www.craft-store.jp/products?page=4&utf8=✓",
"https://www.craft-store.jp/products?utf8=✓&keywords=41",
"https://www.craft-store.jp/products?utf8=✓&keywords=arita",
"https://www.craft-store.jp/products?utf8=✓&keywords=bi",
"https://www.craft-store.jp/products?utf8=✓&keywords=big",
"https://www.craft-store.jp/products?utf8=✓&keywords=BIG GAME",
"https://www.craft-store.jp/products?utf8=✓&keywords=BIG++GAME",
"https://www.craft-store.jp/products?utf8=✓&keywords=BIG+GAME+",
"https://www.craft-store.jp/products?utf8=✓&keywords=ceramic",
"https://www.craft-store.jp/products?utf8=✓&keywords=co",
"https://www.craft-store.jp/products?utf8=✓&keywords=e",
"https://www.craft-store.jp/products?utf8=✓&keywords=eflin",
"https://www.craft-store.jp/products?utf8=✓&keywords=elfin",
"https://www.craft-store.jp/products?utf8=✓&keywords=fab",
"https://www.craft-store.jp/products?utf8=✓&keywords=Fabrick",
"https://www.craft-store.jp/products?utf8=✓&keywords=fabrik",
"https://www.craft-store.jp/products?utf8=✓&keywords=kawara",
"https://www.craft-store.jp/products?utf8=✓&keywords=keep+ware",
"https://www.craft-store.jp/products?utf8=✓&keywords=kidateシリーズ",
"https://www.craft-store.jp/products?utf8=✓&keywords=kisen",
"https://www.craft-store.jp/products?utf8=✓&keywords=Ｌ",
"https://www.craft-store.jp/products?utf8=✓&keywords=najimi",
"https://www.craft-store.jp/products?utf8=✓&keywords=ratio",
"https://www.craft-store.jp/products?utf8=✓&keywords=RATIO_ナガエプリュス",
"https://www.craft-store.jp/products?utf8=✓&keywords=SIWA",
"https://www.craft-store.jp/products?utf8=✓&keywords=spar",
"https://www.craft-store.jp/products?utf8=✓&keywords=SSC",
"https://www.craft-store.jp/products?utf8=✓&keywords=tin",
"https://www.craft-store.jp/products?utf8=✓&keywords=TIN BREATH",
"https://www.craft-store.jp/products?utf8=✓&keywords=Tsuki",
"https://www.craft-store.jp/products?utf8=✓&keywords=TSUKI",
"https://www.craft-store.jp/products?utf8=✓&keywords=wine",
"https://www.craft-store.jp/products?utf8=✓&keywords=アイスクリーム_アヅマ",
"https://www.craft-store.jp/products?utf8=✓&keywords=アワ",
"https://www.craft-store.jp/products?utf8=✓&keywords=うるし",
"https://www.craft-store.jp/products?utf8=✓&keywords=うるしの弁当箱",
"https://www.craft-store.jp/products?utf8=✓&keywords=お刺身セット",
"https://www.craft-store.jp/products?utf8=✓&keywords=お弁当",
"https://www.craft-store.jp/products?utf8=✓&keywords=お弁当箱",
"https://www.craft-store.jp/products?utf8=✓&keywords=カメレオン",
"https://www.craft-store.jp/products?utf8=✓&keywords=コーヒーカップ",
"https://www.craft-store.jp/products?utf8=✓&keywords=ジネット",
"https://www.craft-store.jp/products?utf8=✓&keywords=ステンレス",
"https://www.craft-store.jp/products?utf8=✓&keywords=セット",
"https://www.craft-store.jp/products?utf8=✓&keywords=ソープ",
"https://www.craft-store.jp/products?utf8=✓&keywords=そば",
"https://www.craft-store.jp/products?utf8=✓&keywords=そばちょこ",
"https://www.craft-store.jp/products?utf8=✓&keywords=デザート",
"https://www.craft-store.jp/products?utf8=✓&keywords=デザートスプーン",
"https://www.craft-store.jp/products?utf8=✓&keywords=トーダイTIN-BREATH",
"https://www.craft-store.jp/products?utf8=✓&keywords=ナガエプリュス",
"https://www.craft-store.jp/products?utf8=✓&keywords=ふた",
"https://www.craft-store.jp/products?utf8=✓&keywords=べんとう",
"https://www.craft-store.jp/products?utf8=✓&keywords=まるぶん",
"https://www.craft-store.jp/products?utf8=✓&keywords=ユニロイ",
"https://www.craft-store.jp/products?utf8=✓&keywords=ロックグラス",
"https://www.craft-store.jp/products?utf8=✓&keywords=大阪錫器株式会社",
"https://www.craft-store.jp/products?utf8=✓&keywords=小林",
"https://www.craft-store.jp/products?utf8=✓&keywords=小林ミドリ",
"https://www.craft-store.jp/products?utf8=✓&keywords=小林ミドリ竹籠店",
"https://www.craft-store.jp/products?utf8=✓&keywords=小皿",
"https://www.craft-store.jp/products?utf8=✓&keywords=左利き用スプーン",
"https://www.craft-store.jp/products?utf8=✓&keywords=廣田硝子",
"https://www.craft-store.jp/products?utf8=✓&keywords=弁当https://kinarino.jp/cat2-生活雑貨/2613-伝統技術の美しさ。曲げわっぱのお弁当箱が気になる！",
"https://www.craft-store.jp/products?utf8=✓&keywords=新潟精密鋳造",
"https://www.craft-store.jp/products?utf8=✓&keywords=時計",
"https://www.craft-store.jp/products?utf8=✓&keywords=有田",
"https://www.craft-store.jp/products?utf8=✓&keywords=木 弁当",
"https://www.craft-store.jp/products?utf8=✓&keywords=杉の木クラフト",
"https://www.craft-store.jp/products?utf8=✓&keywords=漆",
"https://www.craft-store.jp/products?utf8=✓&keywords=相和",
"https://www.craft-store.jp/products?utf8=✓&keywords=箸置き",
"https://www.craft-store.jp/products?utf8=✓&keywords=紙のいらない",
"https://www.craft-store.jp/products?utf8=✓&keywords=素材感",
"https://www.craft-store.jp/products?utf8=✓&keywords=能作?utm_source=facebook",
"https://www.craft-store.jp/products?utf8=✓&keywords=茶碗",
"https://www.craft-store.jp/products?utf8=✓&keywords=蕎麦",
"https://www.craft-store.jp/products?utf8=✓&keywords=豆皿",
"https://www.craft-store.jp/products?utf8=✓&keywords=財布",
"https://www.craft-store.jp/products?utf8=✓&keywords=醤油差し",
"https://www.craft-store.jp/products/1616-ty-square-165-white",
"https://www.craft-store.jp/products/1616-ty-square-white-set",
"https://www.craft-store.jp/products/2016-ch-240",
"https://www.craft-store.jp/products/2016-sf-shouyusashi-red",
"https://www.craft-store.jp/products/2016-ty-200-black",
"https://www.craft-store.jp/products/3way_mini_wallet_b",
"https://www.craft-store.jp/products/bunzangama-beer-mug-plain",
"https://www.craft-store.jp/products/bunzangama-glass-plain",
"https://www.craft-store.jp/products/bunzangama-kakuzara",
"https://www.craft-store.jp/products/bunzangama-kakuzara-plain",
"https://www.craft-store.jp/products/bunzangama-reishu-set",
"https://www.craft-store.jp/products/bunzangama-rock-glass",
"https://www.craft-store.jp/products/bunzangama-rock-glass-plain",
"https://www.craft-store.jp/products/camdlelights-greencandle-17",
"https://www.craft-store.jp/products/camdlelights-greencandle-18",
"https://www.craft-store.jp/products/gatomikio-tasai-plate-l",
"https://www.craft-store.jp/products/gatomikio-tasai-plate-m",
"https://www.craft-store.jp/products/gatomikio-tasai-plate-s",
"https://www.craft-store.jp/products/ha-65",
"https://www.craft-store.jp/products/hirotagarasu_shouyusashi_sakura",
"https://www.craft-store.jp/products/isuke-moku-bomboniere",
"https://www.craft-store.jp/products/isuke-moku-cup",
"https://www.craft-store.jp/products/isuke-moku-cupsaucer",
"https://www.craft-store.jp/products/isuke-moku-plate-a",
"https://www.craft-store.jp/products/isuke-moku-tray-b",
"https://www.craft-store.jp/products/kimuraglass-porceold",
"https://www.craft-store.jp/products/kyo-marshmallow-square-plate-pair-pw",
"https://www.craft-store.jp/products/kyo-marshmallow-square-plate-pair-yw",
"https://www.craft-store.jp/products/maruhiro_hasami_soakcup_l",
"https://www.craft-store.jp/products/maruhiro_hasami_soakcup_m_set",
"https://www.craft-store.jp/products/mirror-1",
"https://www.craft-store.jp/products/musubi-aquadrop-yellow",
"https://www.craft-store.jp/products/musubi-both-shinme-100",
"https://www.craft-store.jp/products/musubi-kigi-kakitsubata-100",
"https://www.craft-store.jp/products/nagae-tin-breath-20-gold",
"https://www.craft-store.jp/products/nagae-tin-breath-ring-10x80-gold",
"https://www.craft-store.jp/products/nagae-tin-breath-ring-15x80-gold",
"https://www.craft-store.jp/products/nagae-tin-breath-ring-15x80-silver",
"https://www.craft-store.jp/products/najimi_tumbler_t0s0t-b",
"https://www.craft-store.jp/products/sghr-thebeer-likka",
"https://www.craft-store.jp/products/siwa-slipper-l",
"https://www.craft-store.jp/products/sobachoko-madori-mangetsumon",
"https://www.craft-store.jp/products/sobachoko-madori-yotubamon",
"https://www.craft-store.jp/products/soil-coaster-large-square",
"https://www.craft-store.jp/products/suzuko_mug",
"https://www.craft-store.jp/products/suzuko_old",
"https://www.craft-store.jp/products/syuzangama_itazara",
"https://www.craft-store.jp/products/takumi-no-kura-beer-glass-aurora-blue",
"https://www.craft-store.jp/products/tasaki-aging-20oz",
"https://www.craft-store.jp/products/tasaki-cocktail-5oz",
"https://www.craft-store.jp/products/tasaki-liqueur-3oz",
"https://www.craft-store.jp/products/tasaki-port-10oz",
"https://www.craft-store.jp/products/tasaki-sparkling-7oz",
"https://www.craft-store.jp/products/teori-grip-l",
"https://www.craft-store.jp/products/teori-grip-s",
"https://www.craft-store.jp/products/tsuki-bowl-120",
"https://www.craft-store.jp/products/tsuki-flatplate-300",
"https://www.craft-store.jp/products/tsunoda-cutting-board-angular-l",
"https://www.craft-store.jp/products/tsunoda-cutting-board-round",
"https://www.craft-store.jp/products/yo-u-bianco-petty-knife-120mm",
"https://www.craft-store.jp/tags/AJIPROJECT",
"https://www.craft-store.jp/tags/HASAMI",
"https://www.craft-store.jp/tags/ShigekiFujishiro",
"https://www.craft-store.jp/tags/soil",
"https://www.craft-store.jp/tags/SSC",
"https://www.craft-store.jp/tags/カップ?page=2",
"https://www.craft-store.jp/tags/プレート?page=2",
"https://www.craft-store.jp/tags/まるぶん",
"https://www.craft-store.jp/tags/三条特殊鋳工所",
"https://www.craft-store.jp/tags/大阪錫器",
"https://www.craft-store.jp/tags/廣田硝子",
"https://www.craft-store.jp/tags/錫製品?page=2",
"https://www.craft-store.jp/tags/雑貨?page=3",
]

def get_img_size(url):
    try:
        soup = req.urlopen(url)
        soup = BeautifulSoup(soup,"html.parser")
        imges = soup.find_all("img")
        for img in imges:
            img_url = img.get("src")
            if img_url.find("http"):
                img_url = base_url + img_url
            else:
                img_url = img_url
            try:
                img_size = requests.head(img_url)
                img_size.headers
                img_size = int(img_size.headers['content-length'])
                img_size = img_size / 1024
                img_size = int(img_size)
                if img_size >= 300:
                    img_size = str(img_size) + "K"
                    print(img_url,img_size)

            except:
                print("this image is not available")
    except:
        print("nothing")

for url in urls:
    get_img_size(url)

print("it's over. good job.")
