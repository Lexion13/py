from selenium import webdriver

USER = "JS-TESTER"
PASS = "ipCU12ySxI"

browser = webdriver.PhantomJS()
browser.implicitly_wait(10)

# access to login page
url_login = "http://uta.pw/sakusibbs/users.php?action=login"
browser.get(url_login)
print("success login")

#input into textbox
e = browser.find_element_by_id("user")
e.clear()
e.send_keys(USER)
e = browser.find_element_by_id("pass")

# to send form
frm = browser.find_element_by_css_selector("#loginForm form")
frm.submit()
print("input login information and push down return key")



#get mypage url
a = browser.find_element_by_css_selector(".islogin a")

url_mypage = a.get_attribute('href')
print("mypage url is ", url_mypage)

#display mypage
browser.get(url_mypage)

links = browser.find_elements_by_css_selector("#favlist li > a")
for a in links:
    href = a.get_attribute('href')
    title = a.title
    print("-", title, ">", href)
    