from selenium import webdriver

#get driver from PhantomJS
browser =  webdriver.PhantomJS()
browser.implicitly_wait(3)

#get web site
browser.get("https://google.com")

r = browser.execute_script("return 100 + 50")
print(r)
