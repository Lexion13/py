import requests

image_url = "https://www.cryptocompare.com/media/352312/xci.png"

def download(image_url):
  res = requests.get(image_url)
  if res.status_code == 200:
    image_name = image_url.split("/")[-1]
    with open(image_name, 'wb') as file:
      file.write(res.content)

download(image_url)