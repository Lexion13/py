import requests
from bs4 import BeautifulSoup
import urllib.parse
from urllib.parse import urljoin
import urllib.request as req
import re
import time
import datetime
from pprint import pprint


urls = ['https://www.craft-store.jp/products/soil-sponge-tray', 'https://www.craft-store.jp/products/1616aritajapan_typalaceplate_set', 'https://www.craft-store.jp/products/maruhiro-blockmug-l', 'https://www.craft-store.jp/products/copper-spoon-pinkgold', 'https://www.craft-store.jp/products/gatomikio-tasai-bowl-m', 'https://www.craft-store.jp/products/hirotagarasu_shouyusashi_kikkou', 'https://www.craft-store.jp/products/1616-ty-square-165-gray', 'https://www.craft-store.jp/products/tsuki-flatplate-300', 'https://www.craft-store.jp/products/soil-coaster-large-circle', 'https://www.craft-store.jp/products/soil-coaster-large-square', 'https://www.craft-store.jp/products/first-knife-set', 'https://www.craft-store.jp/products/nagae-collinette', 'https://www.craft-store.jp/products/nousaku-fuurin-rin-silver', 'https://www.craft-store.jp/products/keepware-plate-16', 'https://www.craft-store.jp/products/teori-grid-square', 'https://www.craft-store.jp/products/2016-bg-white-sprinkle', 'https://www.craft-store.jp/products/fabrik_bi', 'https://www.craft-store.jp/products/nagae-tin-breath-ring-10x80-gold', 'https://www.craft-store.jp/products/suginokicraft-large-lunchbox', 'https://www.craft-store.jp/products/2016-bg-coffeecup-l-white-sprinkle', 'https://www.craft-store.jp/products/todai-spoon', 'https://www.craft-store.jp/products/cooloff-set-koushi-en', 'https://www.craft-store.jp/products/sghr-crystaledge', 'https://www.craft-store.jp/products/celebrate-set-plum', 'https://www.craft-store.jp/products/fabrik_key', 'https://www.craft-store.jp/products/gatomikio-tasai-plate-m', 'https://www.craft-store.jp/products/takakuwakinzoku-desertspoon', 'https://www.craft-store.jp/products/takakuwakinzoku-desertfork', 'https://www.craft-store.jp/products/takakuwakinzoku-turner', 'https://www.craft-store.jp/products/takakuwakinzoku-ladle', 'https://www.craft-store.jp/products/nakaoarumi_proking', 'https://www.craft-store.jp/products/unilloy-22cm', 'https://www.craft-store.jp/products/proking_asagata_saute_18', 'https://www.craft-store.jp/products/proking_18', 'https://www.craft-store.jp/products/gosu-mamezarahakoiri-set/', 'https://www.craft-store.jp/products/takakuwakinzoku-curryspoon', 'https://www.craft-store.jp/products/takakuwakinzoku-cakefork', 'https://www.craft-store.jp/products/takakuwakinzoku-minibutterknife', 'https://www.craft-store.jp/products/takakuwakinzoku-milkpan-straight', 'https://www.craft-store.jp/products/takakuwakinzoku-teaspoon', 'https://www.craft-store.jp/products/takakuwakinzoku-toriwakespoonbig', 'https://www.craft-store.jp/products/kidate-sokomaru-rocks', 'https://www.craft-store.jp/products/keepware-cup-250', 'https://www.craft-store.jp/products/gatomikio-tasai-plate-s', 'https://www.craft-store.jp/products/2016-bg-coffeecup-l-black-matt', 'https://www.craft-store.jp/products/siwa-clutchbag-m', 'https://www.craft-store.jp/products/sghr-ginette-old', 'https://www.craft-store.jp/products/odakoudouki_moscowmulecup_tsutime', 'https://www.craft-store.jp/products/copper-spoon-set-gold', 'https://www.craft-store.jp/products/tasaki-sherry-8oz', 'https://www.craft-store.jp/products/odakoudouki_moscowmulecup_mat', 'https://www.craft-store.jp/products/nosaku_beercup', 'https://www.craft-store.jp/products/sobachoko-madori-kamon', 'https://www.craft-store.jp/products/nagae-tin-breath-40-antiquegold', 'https://www.craft-store.jp/products/sghr-kirameki-rocks-storm', 'https://www.craft-store.jp/products/sghr-kirameki-rocks-nejiri', 'https://www.craft-store.jp/products/sghr-duo-old', 'https://www.craft-store.jp/products/kimuraglass-crumple-wine-s', 'https://www.craft-store.jp/products/kimuraglass-crumple-wine-s-frost', 'https://www.craft-store.jp/products/kimuraglass-table-soysauce', 'https://www.craft-store.jp/products/kimuraglass-droplet', 'https://www.craft-store.jp/products/tasaki-aging-30oz', 'https://www.craft-store.jp/products/tasaki-young-l-24oz', 'https://www.craft-store.jp/products/tasaki-light-l-20oz', 'https://www.craft-store.jp/products/tasaki-light-m-15oz', 'https://www.craft-store.jp/products/tasaki-prototype-l-30oz', 'https://www.craft-store.jp/products/tasaki-prototype-m-20oz', 'https://www.craft-store.jp/products/tasaki-sparkling-9oz', 'https://www.craft-store.jp/products/kimuraglass-karuta-1x1', 'https://www.craft-store.jp/products/kimuraglass-karuta-1x2', 'https://www.craft-store.jp/products/kimuraglass-crumple-wine-s-set', 'https://www.craft-store.jp/products/tsuki-flatplate-190', 'https://www.craft-store.jp/products/fabrik_long', 'https://www.craft-store.jp/products/macrw-bionmg60', 'https://www.craft-store.jp/products/suginokicraft-lunchbox-twostory', 'https://www.craft-store.jp/products/tsuki-flatplate-230', 'https://www.craft-store.jp/products/aka-swing', 'https://www.craft-store.jp/products/gatomikio-tasai-bowl-s', 'https://www.craft-store.jp/products/aiwashibori-bowl150-silky', 'https://www.craft-store.jp/products/tsuki-bowl-170', 'https://www.craft-store.jp/products/sobachoko-madori-mangetsumon', 'https://www.craft-store.jp/products/sobachoko-madori-yotubamon', 'https://www.craft-store.jp/products/suginoki-runchbox-set', 'https://www.craft-store.jp/products/yo-u-bianco-petty-knife-120mm', 'https://www.craft-store.jp/products/yo-u-bianco-small-santoku-knife-165mm', 'https://www.craft-store.jp/products/1616aritajapan_typalaceplate_l', 'https://www.craft-store.jp/products/nousaku_chopstickrest_knot_b', 'https://www.craft-store.jp/products/urushiyahayashi_lunchbox_s', 'https://www.craft-store.jp/products/kago-square-m', 'https://www.craft-store.jp/products/futae', 'https://www.craft-store.jp/products/camdlelights-beeswax-stick', 'https://www.craft-store.jp/products/2016-bg-coffecup-s-white-sprinkle', 'https://www.craft-store.jp/products/morning-glory-sansaku_morning-glory_black', 'https://www.craft-store.jp/products/shiro-tilt', 'https://www.craft-store.jp/products/teruhiro-yanagihara-180', 'https://www.craft-store.jp/products/hirotagarasu_syouwamodernglass_glass', 'https://www.craft-store.jp/products/nousaku_chopstickrest_sakura', 'https://www.craft-store.jp/products/big-game-black-matt', 'https://www.craft-store.jp/products/maruhiro_hasami_soakcup_s', 'https://www.craft-store.jp/products/newking_18', 'https://www.craft-store.jp/products/tsuki-bowl-120', 'https://www.craft-store.jp/products/big-game-l-black-matt', 'https://www.craft-store.jp/products/1616-ty-square-165-white', 'https://www.craft-store.jp/products/much', 'https://www.craft-store.jp/products/maruhiro_hasami_soakcup_s_set', 'https://www.craft-store.jp/products/gatomikio-waqwa-cup-s', 'https://www.craft-store.jp/products/musubi-both-musubi-100', 'https://www.craft-store.jp/products/bunzangama-reishu-set-plain', 'https://www.craft-store.jp/products/camdlelights-beeswax-mug', 'https://www.craft-store.jp/products/aiwashibori_tumbler90_6264', 'https://www.craft-store.jp/products/bunzangama-rock-glass', 'https://www.craft-store.jp/products/sobachoko-iroe-chameleon', 'https://www.craft-store.jp/products/hirotagarasu-syouwamodernglass-cupsaucer', 'https://www.craft-store.jp/products/sobachoko-iroe-parakeet', 'https://www.craft-store.jp/products/aiwashibori_tumbler90_brown', 'https://www.craft-store.jp/products/suginokicraft-lunchbox-set', 'https://www.craft-store.jp/products/tsuki-cutleryrest', 'https://www.craft-store.jp/products/tsumugi-fuji', 'https://www.craft-store.jp/products/kingflon_nomake_asagata_18', 'https://www.craft-store.jp/products/hannari-kokoharecup', 'https://www.craft-store.jp/products/kago-rose', 'https://www.craft-store.jp/products/keepware-cup-700', 'https://www.craft-store.jp/products/camdlelights-greencandle-12', 'https://www.craft-store.jp/products/siwa-shoulderbag', 'https://www.craft-store.jp/products/gatomikio-tasai-cup', 'https://www.craft-store.jp/products/kyo-marshmallow-bowl-and-plate-yw', 'https://www.craft-store.jp/products/hirotagarasu_shouyusashi_sakura', 'https://www.craft-store.jp/products/bunzangama-tumbler', 'https://www.craft-store.jp/products/keepware-plate-25', 'https://www.craft-store.jp/products/siwa-slipper-s', 'https://www.craft-store.jp/products/musubi-kigi-tsubaki-70', 'https://www.craft-store.jp/products/siwa-clutchbag-l', 'https://www.craft-store.jp/products/2016-sf-mug-red', 'https://www.craft-store.jp/products/bunzangama-kozara', 'https://www.craft-store.jp/products/bunzangama-tumbler-plain', 'https://www.craft-store.jp/products/zen', 'https://www.craft-store.jp/products/takakuwa-dessert-set', 'https://www.craft-store.jp/products/bunzangama-kakuzara-plain', 'https://www.craft-store.jp/products/musubi-kigi-kakitsubata-100', 'https://www.craft-store.jp/products/1616-ty-square-235-white', 'https://www.craft-store.jp/products/kago-oval-l', 'https://www.craft-store.jp/products/tsunoda-lunchbox-angular-1', 'https://www.craft-store.jp/products/kago-dahlia', 'https://www.craft-store.jp/products/camdlelights-greencandle-41', 'https://www.craft-store.jp/products/isuke-moku-bomboniere', 'https://www.craft-store.jp/products/nousaku-chopstickrest-kasane-maru-2', 'https://www.craft-store.jp/products/nagae-tin-breath-ring-10x80-antiquegold', 'https://www.craft-store.jp/products/nousaku-chopstickrest-tsuki-5', 'https://www.craft-store.jp/products/tsunoda-lunchbox-angular-2', 'https://www.craft-store.jp/products/isuke-moku-plate-a', 'https://www.craft-store.jp/products/2016-ty-180-white', 'https://www.craft-store.jp/products/camdlelights-beeswax-l', 'https://www.craft-store.jp/products/bunzangama-kakuzara', 'https://www.craft-store.jp/products/2016-bg-black-matt', 'https://www.craft-store.jp/products/suzukou_guinomi', 'https://www.craft-store.jp/products/bunzangama-reishu-set', 'https://www.craft-store.jp/products/camdlelights-greencandle-18', 'https://www.craft-store.jp/products/kyo-marshmallow-square-plate-pair-pw', 'https://www.craft-store.jp/products/yasudagawara-cup-65', 'https://www.craft-store.jp/products/tsunoda-meiboku-lunchbox-walnut', 'https://www.craft-store.jp/products/sanjotokusyuchukousho-ssc-26', 'https://www.craft-store.jp/products/2016-sf-mug-gray', 'https://www.craft-store.jp/products/tsunoda-cutting-board-round', 'https://www.craft-store.jp/products/nagae-tin-breath-ring-15x80-silver', 'https://www.craft-store.jp/products/tsunoda-cutting-board-angular-s', 'https://www.craft-store.jp/products/nagae-tin-breath-40-gold', 'https://www.craft-store.jp/products/nousaku_chopstickrest_85', 'https://www.craft-store.jp/products/2016-sf-shouyusashi-red', 'https://www.craft-store.jp/products/gatomikio-tasai-plate-l', 'https://www.craft-store.jp/products/tsunoda-cutting-board-angular-l', 'https://www.craft-store.jp/products/nagae-collinette-lymph', 'https://www.craft-store.jp/products/2016-sf-shouyusashi-white', 'https://www.craft-store.jp/products/100cm-musubi-both-isamonyou-kiku-100', 'https://www.craft-store.jp/products/camdlelights-greencandle-9', 'https://www.craft-store.jp/products/copper-spoon-set-silver', 'https://www.craft-store.jp/products/bunzangama-beer-mug', 'https://www.craft-store.jp/products/camdlelights-greencandle-38', 'https://www.craft-store.jp/products/kyo-marshmallow-bowl-and-plate-pw', 'https://www.craft-store.jp/products/nagae-ratio-square-l', 'https://www.craft-store.jp/products/bunzangama-kozara-plain', 'https://www.craft-store.jp/products/kago-oval-s', 'https://www.craft-store.jp/products/camdlelights-greencandle-17', 'https://www.craft-store.jp/products/musubi-both-shinme-100', 'https://www.craft-store.jp/products/bunzangama-beer-mug-plain', 'https://www.craft-store.jp/products/sobachoko-iroe-pug', 'https://www.craft-store.jp/products/sobachoko-iroe-short-hair', 'https://www.craft-store.jp/products/sobachoko-iroe-axolotl', 'https://www.craft-store.jp/products/sobachoko-suzumi', 'https://www.craft-store.jp/products/maruhiro-soaktray-l', 'https://www.craft-store.jp/products/nousaku_futae', 'https://www.craft-store.jp/products/fabrik_keycard', 'https://www.craft-store.jp/products/sansaku_morning-glory_silver', 'https://www.craft-store.jp/products/2016-ty-180-black', 'https://www.craft-store.jp/products/isuke-moku-cup', 'https://www.craft-store.jp/products/2016-bg-coffeecup-s-black-matt', 'https://www.craft-store.jp/products/2016-ch-teacup', 'https://www.craft-store.jp/products/nosaku_beercup_l', 'https://www.craft-store.jp/products/tsunoda-lunchbox-angular-1-urushi', 'https://www.craft-store.jp/products/2016-ty-200-black', 'https://www.craft-store.jp/products/urushiyahayashi_lunchbox_l', 'https://www.craft-store.jp/products/2016-ch-180', 'https://www.craft-store.jp/products/tsunoda-ohitsu-s', 'https://www.craft-store.jp/products/urushiyahayashi_lunchbox_long', 'https://www.craft-store.jp/products/musubi-aquadrop-yellow', 'https://www.craft-store.jp/products/moku_s', 'https://www.craft-store.jp/products/nagae-tin-breath-20-antiquegold', 'https://www.craft-store.jp/products/tsunoda-meiboku-lunchbox-whiteash', 'https://www.craft-store.jp/products/takumi-no-kura-beer-glass-kirameki', 'https://www.craft-store.jp/products/1616-ty-square-235-gray', 'https://www.craft-store.jp/products/2016-ch-240', 'https://www.craft-store.jp/products/tsunoda-lunchbox-round-1', 'https://www.craft-store.jp/products/aiwashibori-bowl120-silky', 'https://www.craft-store.jp/products/teruhiro-yanagihara-rim-plate-180-white', 'https://www.craft-store.jp/products/teruhiro-yanagihara-200', 'https://www.craft-store.jp/products/moku_m', 'https://www.craft-store.jp/products/teruhiro-yanagihara-bowl-200-white', 'https://www.craft-store.jp/products/shigeki-fujishiro-shouyusashi-white', 'https://www.craft-store.jp/products/shigeki-fujishiro-shigeki-fujishiro-shouyusashi-gray', 'https://www.craft-store.jp/products/shigeki-fujishiro-shigeki-fujishiro-shouyusashi-red', 'https://www.craft-store.jp/products/shigeki-fujishiro-mug-white', 'https://www.craft-store.jp/products/shigeki-fujishiro', 'https://www.craft-store.jp/products/shigeki-fujishiro-mug-red', 'https://www.craft-store.jp/products/teori-grip-s', 'https://www.craft-store.jp/products/christian-haas-180', 'https://www.craft-store.jp/products/big-game-s-white-sprinkle', 'https://www.craft-store.jp/products/teori-grip-l', 'https://www.craft-store.jp/products/big-game-s-black-matt', 'https://www.craft-store.jp/products/big-game-l-white-sprinkle', 'https://www.craft-store.jp/products/isuke-moku-cupsaucer', 'https://www.craft-store.jp/products/2016-sf-mug-white', 'https://www.craft-store.jp/products/siwa-slipper-l', 'https://www.craft-store.jp/products/makemyday-giftbox', 'https://www.craft-store.jp/products/aiwashibori-bowl120-kurocha-ohaguro', 'https://www.craft-store.jp/products/aiwashibori-bowl150-kurocha-ohaguro', 'https://www.craft-store.jp/products/moku_l', 'https://www.craft-store.jp/products/moku_ll', 'https://www.craft-store.jp/products/gatomikio-tasai-bowl-l', 'https://www.craft-store.jp/products/aji-grill-square-ami', 'https://www.craft-store.jp/products/aji-grill-square-mame', 'https://www.craft-store.jp/products/1616-ty-square-white-set', 'https://www.craft-store.jp/products/tsunoda-lunchbox-square', 'https://www.craft-store.jp/products/aiwashibori-bowl120-usucha', 'https://www.craft-store.jp/products/kago-square-s', 'https://www.craft-store.jp/products/aiwashibori-bowl150-usucha', 'https://www.craft-store.jp/products/maruhiro_hasami_soakcup_m_set', 'https://www.craft-store.jp/products/maruhiro_hasami_soakcup_l', 'https://www.craft-store.jp/products/maruhiro_hasami_soakcup_l_set', 'https://www.craft-store.jp/products/unilloy-24cm-shallow', 'https://www.craft-store.jp/products/unilloy-22cm-shallow', 'https://www.craft-store.jp/products/tsunoda-runchbox-set', 'https://www.craft-store.jp/products/soil-umbrella-stand', 'https://www.craft-store.jp/products/soil-toothbrush-stand', 'https://www.craft-store.jp/products/takakuwa-ladle-turner-set', 'https://www.craft-store.jp/products/osashimi-set', 'https://www.craft-store.jp/products/takakuwakinzoku-toriwakespoon-l', 'https://www.craft-store.jp/products/sghr-kirameki-rocks-grid', 'https://www.craft-store.jp/products/sghr-natsu-17-circle', 'https://www.craft-store.jp/products/sghr-nightcarafe', 'https://www.craft-store.jp/products/kimuraglass-lotus-goblet-10oz', 'https://www.craft-store.jp/products/kimuraglass-porceold', 'https://www.craft-store.jp/products/tasaki-young-s-12oz', 'https://www.craft-store.jp/products/tasaki-light-s-10oz', 'https://www.craft-store.jp/products/tasaki-liqueur-3oz', 'https://www.craft-store.jp/products/tasaki-port-10oz', 'https://www.craft-store.jp/products/tasaki-prototype-s-12oz', 'https://www.craft-store.jp/products/tasaki-cocktail-5oz', 'https://www.craft-store.jp/products/marubun-square-plate-small', 'https://www.craft-store.jp/products/marubun-square-plate-mid', 'https://www.craft-store.jp/products/gosu-hashiokihakoiri-set', 'https://www.craft-store.jp/products/gosu-kodukehakoiri-set', 'https://www.craft-store.jp/products/nousaku-fuurin-horn-gold', 'https://www.craft-store.jp/products/nousaku-fuurin-heirin-round', 'https://www.craft-store.jp/products/nagae-tin-breath-40-silver', 'https://www.craft-store.jp/products/keepware-cup-500', 'https://www.craft-store.jp/products/yasudagawara-cup-80', 'https://www.craft-store.jp/products/yasudagawara-cup-45', 'https://www.craft-store.jp/products/nousaku-guinomi', 'https://www.craft-store.jp/products/kyo-marshmallow-square-plate-pair-ww', 'https://www.craft-store.jp/products/yo-u-bianco-small-santoku-knife-145mm', 'https://www.craft-store.jp/products/yo-u-bianco-dimple-180mm', 'https://www.craft-store.jp/products/yo-u-bianco-chef-knife-210mm', 'https://www.craft-store.jp/products/kyo-marshmallow-bowl-and-plate-py', 'https://www.craft-store.jp/products/kyo-marshmallow-square-plate-pair-yw', 'https://www.craft-store.jp/products/bunzangama-rock-glass-plain', 'https://www.craft-store.jp/products/bunzangama-glass-plain', 'https://www.craft-store.jp/products/bunzangama-glass', 'https://www.craft-store.jp/products/bunzangama-katakuchi-plain', 'https://www.craft-store.jp/products/bunzangama-katakuchi', 'https://www.craft-store.jp/products/tsunoda-ohitsu-l', 'https://www.craft-store.jp/products/musubi-both-karacho-100', 'https://www.craft-store.jp/products/musubi-shantan-tsubaki-90', 'https://www.craft-store.jp/products/musubi-chirimen-ume-70', 'https://www.craft-store.jp/products/musubi-kohare-kaze-70', 'https://www.craft-store.jp/products/takumi-no-kura-glass-kirameki', 'https://www.craft-store.jp/products/takumi-no-kura-glass-deep-green', 'https://www.craft-store.jp/products/takumi-no-kura-glass-aurora-pink', 'https://www.craft-store.jp/products/takumi-no-kura-beer-glass-aurora-blue', 'https://www.craft-store.jp/products/nagae-tin-breath-ring-15x80-antiquegold', 'https://www.craft-store.jp/products/nagae-tin-breath-ring-15x80-gold', 'https://www.craft-store.jp/products/nagae-tin-breath-20-gold', 'https://www.craft-store.jp/products/isuke-moku-plate-b', 'https://www.craft-store.jp/products/isuke-moku-tray-b', 'https://www.craft-store.jp/products/isuke-moku-tray-a', 'https://www.craft-store.jp/products/zoa-sannsui-7sunzara', 'https://www.craft-store.jp/products/zoa-nejiri-7sunzara', 'https://www.craft-store.jp/products/zoa-kacho-7sunzara', 'https://www.craft-store.jp/products/zoa-fuyoude-7sunzara', 'https://www.craft-store.jp/products/zoa-fuyoudemon-7sunzara', 'https://www.craft-store.jp/products/zoa-nejirimadorikamon-7sunzara', 'https://www.craft-store.jp/products/zoa-kumowarisansuimon-7sunzara', 'https://www.craft-store.jp/products/zoa-sometukeumetorimon-7sunzara']

for url in urls:
    res = req.urlopen(url)
    soup = BeautifulSoup(res, "html.parser")
    images = soup.find_all("img")
    for image in images:
        image = image.get('src')
        if image is not None:
            if image.find('http'):
                image = "https://www.craft-store.jp" + image
            else:
                image = image
            try:
                image_res = requests.head(image)
                if image_res.status_code != 200 :
                    print(url,image,image_res.status_code)
            except:
                print(url,"something error occurred")
