import os
import requests
path = requests.get("https://craft-neworld-production.s3.amazonaws.com/uploads/spree/product/image/88/thumbnail_thumb_gold-box.jpg")
path = requests.get("https://pbs.twimg.com/profile_images/378800000220029324/fe66faeca20115da8566e51d83447ead_400x400.jpeg")

with open(path, "wb")

size = os.path.getsize(path)
print (size)
