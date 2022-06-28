from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import datetime

username, password = '曹聪', 'cc'
wd = webdriver.Chrome(r'd:\Google驱动\chromedriver.exe')
# wd.set_window_size(1400,900)
wd.get('http://172.27.14.4:5010/labs/admin.php')

element = wd.find_element_by_id('username').send_keys(username)
element = wd.find_element_by_id('password').send_keys(password)
element = wd.find_element_by_css_selector("#logon > fieldset > div:nth-child(4) > input[type=submit]").click()
element = wd.find_element_by_css_selector("body > header > nav > ul > li:nth-child(1) > div > div.mrbs > a").click()
#滑动至底端
wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
