import requests as req

r = req.get("https://www.google.co.jp/?gfe_rd=cr&ei=kyY8WbL6F4XR8gfV1ZPYDA")

text = r.text
print(text)

bin = r.content
print(bin)