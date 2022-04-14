from selenium import webdriver
iimport time2

#1

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()
chrome.get("http://walla.co.il")
firefox.get("http://www.ynet.co.il")

#2
firefox = webdriver.Firefox()
firefox.get("http://www.ynet.co.il")
title = firefox.title
firefox.refresh()
name = firefox.name
assert name == title

#3
chrome.get("https://github.com")
firefox.get("https://github.com")
chrome.find_element_by_id('user_email').send_keys('ofir')
firefox.find_element_by_id('user_email').send_keys('ofir')
#yes, it have the same locators

#4 + 6
chrome.get("https://translate.google.com/")
input1 = chrome.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea')
input1.send_keys('משהו בעברית\n')
input1.send_keys('xpath\n')
input2 = chrome.find_element_by_class_name('er8xn')
input2.send_keys('CSS_class_name\n')
input3 = chrome.find_elements_by_tag_name('textarea')
input3[0].send_keys('HTML_tag_name')
print(input3)
print(input2)
print(input1)

#5
firefox.get("https://www.youtube.com")
searchbox = firefox.find_element_by_xpath('//input[@id="search"]')
searchbox.send_keys("Baby Shark Dance")
time.sleep(1)
searchbutton = firefox.find_element_by_xpath('//*[@id="search-icon-legacy"]') 
searchbutton.click()

#7
chrome.get("https://www.facebook.com/")
chrome.find_element_by_id("email").send_keys('username')
chrome.find_element_by_id("pass").send_keys('password')
time.sleep(2)
chrome.find_element_by_name("login").click()

#8
chrome.get("https://github.com/")
print(chrome.get_cookies())
time.sleep(1)
chrome.delete_all_cookies()
print(chrome.get_cookies())

#9
from selenium.webdriver.common.keys import Keys
chrome.get("https://github.com/")
chrome.find_element_by_xpath('/html/body/div[1]/header/div/div[1]/div[2]/button').click()
input = chrome.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[2]/div[1]/div/div/form/label/input[1]')
input.send_keys('selenium')
input.send_keys(Keys.ENTER)

#10
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome = webdriver.Chrome(chrome_options=chrome_options)
from selenium.webdriver.firefox.options import Options as foptions
firefox_options = foptions()
firefox_options.add_argument("--disable-extensions")
firefox = webdriver.Firefox(options=firefox_options)
from selenium.webdriver.edge.options import Options
edge_options = Options()
edge_options.add_argument("--disable-extensions")
edge = webdriver.Edge(options = edge_options)
edge.get('github.com')
