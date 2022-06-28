from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import datetime


### -------------------------最新可订时间：当前日期+8  当前时间向后取整半小时再减1h--------------------------------
'''
selector需要元素可见
shell version1: 手动提取预定时间第一个位置selector 最快
功能：1、预定最新可订实验室（续至3h） 2、截胡（慎用） 3、中途续至3h

说明：1、填写自定义区即可运行（需下载浏览器驱动：https://chromedriver.storage.googleapis.com/index.html）  
      2、抢第二天早晨当天晚上11点后运行即可，抢下午/晚上，上午运行即可。
      3、截胡时间选当前时间向后取整后减去1h即可。   
      4、选择房间  0:206   1:208   2:308   3:310    4:107   5:402

                                                                                             by：CC
'''
##----------------------------------选择房间  0:206   1:208   2:308   3:310-------------------------------------

#自定义区
room_num = int(input('请输入0~5选择预定lab ( 0:206   1:208   2:308   3:310    4:107   5:402): '))
your_book_time = input('请输入预定时间(格式 XX:00 or XX:30): ')
username, password = '曹聪', 'cc'
your_book_message = input('请输入预定信息(一般填名字即可): ')
talble_pos = input('请输入预定位置selector: ')
column = int(input('请输入上面信息第二个数字(new则随意输入一个数字): '))
#example：
# talble_pos = '#week_main > tbody > tr:nth-child(6) > td:nth-child(5) > div > a'
# column = 5


#--------------------------------------------------------------------------------------------------------#

option = webdriver.ChromeOptions()
# 隐藏窗口
option.add_argument('--headless')
# 防止打印一些无用的日志
option.add_experimental_option("excludeSwitches", ['enable-logging'])
# option.add_experimental_option("excludeSwitches", ['enable-automation','enable-logging'])
# option.add_experimental_option("excludeSwitches", ['enable-automation'])
wd = webdriver.Chrome(r'd:\Google驱动\chromedriver.exe', chrome_options=option) # 将配置文件加载进webdriver
# wd = webdriver.Chrome(r'd:\Google驱动\chromedriver.exe')
# wd.maximize_window()
wd.get('http://172.27.14.4:5010/labs/admin.php')
print('开始预定......')

# first_pull_time = your_book_time + 1:30
hour_temp = int(your_book_time[0:2])
minute_temp = int(your_book_time[3:5])
if(minute_temp == 0):
    hour_temp += 1
    pull_down_time = [str(hour_temp) + ':29:58', str(hour_temp) + ':59:58', str(hour_temp+1) + ':29:58',
                    str(hour_temp+1) + ':59:58', str(hour_temp+2) + ':29:58']
else:
    hour_temp += 2
    pull_down_time = [str(hour_temp - 1) + ':59:58', str(hour_temp) + ':29:58', str(hour_temp) + ':59:58', 
                    str(hour_temp+1) + ':29:58', str(hour_temp+1) + ':59:58']

for i in range(len(pull_down_time)):
    if(len(pull_down_time[i]) < 8):
        pull_down_time[i] = '0' + pull_down_time[i]

book_time = { 
            '06:00' : '06:59:58', '06:30' : '07:29:58',
            '07:00' : '07:59:58', '07:30' : '08:29:58', '08:00' : '08:59:58', '08:30' : '09:29:58', '09:00' : '09:59:58',
            '09:30' : '10:29:58', '10:00' : '10:59:58', '10:30' : '11:29:58', '11:00' : '11:59:58', '11:30' : '12:29:58',
            '12:00' : '12:59:58', '12:30' : '13:29:58', '13:00' : '13:59:58', '13:30' : '14:29:58', '14:00' : '14:59:58',
            '14:30' : '15:29:58', '15:00' : '15:59:58', '15:30' : '16:29:58', '16:00' : '16:59:58', '16:30' : '17:29:58',
            '17:00' : '17:59:58', '17:30' : '18:29:58', '18:00' : '18:59:58', '18:30' : '19:29:58', '19:00' : '19:59:58',
            '19:30' : '20:29:58', '20:00' : '20:59:58', '20:30' : '21:29:58', '21:00' : '21:59:58', '21:30' : '22:29:58',
            '22:00' : '22:59:58', '22:30' : '23:29:58'
            }

book_time_row = {
                '07:00' :  3, '07:30' :  4, '08:00' :  5, '08:30' :  6,
                '09:00' :  7, '09:30' :  8, '10:00' :  9, '10:30' : 10,
                '11:00' : 11, '11:30' : 12, '12:00' : 13, '12:30' : 14,
                '13:00' : 15, '13:30' : 16, '14:00' : 17, '14:30' : 18,
                '15:00' : 19, '15:30' : 20, '16:00' : 21, '16:30' : 22,
                '17:00' : 23, '17:30' : 24, '18:00' : 25, '18:30' : 26,
                '19:00' : 27, '19:30' : 28, '20:00' : 29, '20:30' : 30,
                '21:00' : 31, '21:30' : 32, '22:00' : 33, '22:30' : 34,
                '23:00' : 35, '23:30' : 36, '06:00' :  1, '06:30' :  2,
                }
#week_main > tbody > tr:nth-child(1) > td:nth-child(2)
dayOfWeek = datetime.datetime.now().isoweekday()
book_week_num = (dayOfWeek + 1) % 7

##--------------------------------登录账号-----------------------------

element = wd.find_element_by_id('username').send_keys(username)
element = wd.find_element_by_id('password').send_keys(password)
element = wd.find_element_by_css_selector("#logon > fieldset > div:nth-child(4) > input[type=submit]").click()
element = wd.find_element_by_css_selector("body > header > nav > ul > li:nth-child(1) > div > div.mrbs > a").click()

##-----------------------------跳转最新可订周---------------------------

room_pos = ["#dwm_rooms > ul > li:nth-child(4) > a > span", "#dwm_rooms > ul > li:nth-child(5) > a > span", 
            "#dwm_rooms > ul > li:nth-child(6) > a > span", "#dwm_rooms > ul > li:nth-child(7) > a > span",
            "#dwm_rooms > ul > li:nth-child(2) > a > span", "#dwm_rooms > ul > li:nth-child(8) > a > span"]
element = wd.find_element_by_css_selector(room_pos[room_num]).click()
if dayOfWeek == 7:
    element = wd.find_element_by_css_selector("body > div.contents > nav:nth-child(3) > a.date_after").click()
element = wd.find_element_by_css_selector("body > div.contents > nav:nth-child(3) > a.date_after").click()
if(your_book_time >= '13:30'):
    wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")

##-------------------------------订实验室------------------------------

book_hour = int(your_book_time[0:2]) + 1
book_minute = int(your_book_time[3:5])

now = datetime.datetime.now()
hour, minute, second = now.hour, now.minute, now.second
if(hour >= 23 and book_hour >= 23):   ##睡觉前运行，预定第二天上午 
    time.sleep(5 * 60 * 60)
    now = datetime.datetime.now()
    hour, minute, second = now.hour, now.minute, now.second

if(book_minute < minute):
    wait_minute = 60 - minute
    book_hour -= 1
    wait_minute += (book_hour - hour) * 60
else:
    wait_minute = book_minute - minute
    wait_minute += (book_hour - hour) * 60

if(wait_minute > 0):
    print('首次预定还需等待', wait_minute, '分钟。')
    time.sleep((wait_minute - 1) * 60)  ##等至最后一分钟循环判断

#---------------------判断账号是否被注销----------------------------

try:
    wd.refresh() # 刷新方法 refresh
    if(your_book_time >= '13:30'):
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    element = wd.find_element_by_css_selector('#logon_box > form:nth-child(2) > input[type=submit]:nth-child(6)')
    print('当前账户登录中。')
except:
    print ("账户已注销，重新登入成功。")
    wd.get('http://172.27.14.4:5010/labs/admin.php')
    element = wd.find_element_by_id('username').send_keys(username)
    element = wd.find_element_by_id('password').send_keys(password)
    element = wd.find_element_by_css_selector("#logon > fieldset > div:nth-child(4) > input[type=submit]").click()
    element = wd.find_element_by_css_selector("body > header > nav > ul > li:nth-child(1) > div > div.mrbs > a").click()
    element = wd.find_element_by_css_selector(room_pos[room_num]).click()
    if dayOfWeek == 7:
        element = wd.find_element_by_css_selector("body > div.contents > nav:nth-child(3) > a.date_after").click()
    element = wd.find_element_by_css_selector("body > div.contents > nav:nth-child(3) > a.date_after").click()
    if(your_book_time >= '13:30'):
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")

now_time = time.strftime('%H:%M:%S', time.localtime())
while(now_time < book_time[your_book_time]):
    now_time = time.strftime('%H:%M:%S', time.localtime())

time.sleep(1.8) #night
# time.sleep(1.4)
# time.sleep(1.35)
# time.sleep(1.3)  


#处理续订情况
try:
    element = wd.find_element_by_css_selector(talble_pos).click()   #slots > 2报警告 :不报可订
    try:
        element = wd.find_element_by_css_selector("#name")
        element.send_keys(your_book_message)
        element = wd.find_element_by_css_selector("#edit_entry_submit_save > input").click()    
    except:
        element = wd.find_element_by_css_selector('#returl > a').click()
except:
    pass

###------------------------------下拉延迟2小时-------------------------------
'''
该周预定超过一天位置增加列元素
例： #week_main > tbody > tr:nth-child(15) > td:nth-child(7) > div > div.celldiv.slots2.clone.ui-resizable > div.ui-resizable-handle.ui-resizable-s
否则只需行元素定位： #week_main > tbody > tr:nth-child(15) > td.I.writable > div > div.celldiv.slots2.clone.ui-resizable > div.ui-resizable-handle.ui-resizable-s
slots2/3/4 表示当前预定时间 2：1h， 3： 1.5h
'''

pull_down_pos = []
if 'new' in talble_pos:
    pulldown_pos1 = '#week_main > tbody > tr:nth-child(' + str(book_time_row[your_book_time]) + ') > td.I.writable > div > div.celldiv.slots2.clone.ui-resizable > div.ui-resizable-handle.ui-resizable-s'
    pulldown_pos2 = '#week_main > tbody > tr:nth-child(' + str(book_time_row[your_book_time]) + ') > td.I.writable > div > div.celldiv.slots3.clone.ui-resizable > div.ui-resizable-handle.ui-resizable-s'
    pulldown_pos3 = '#week_main > tbody > tr:nth-child(' + str(book_time_row[your_book_time]) + ') > td.I.writable > div > div.celldiv.slots4.clone.ui-resizable > div.ui-resizable-handle.ui-resizable-s'
    pulldown_pos4 = '#week_main > tbody > tr:nth-child(' + str(book_time_row[your_book_time]) + ') > td.I.writable > div > div.celldiv.slots5.clone.ui-resizable > div.ui-resizable-handle.ui-resizable-s'
    pulldown_pos5 = '#week_main > tbody > tr:nth-child(' + str(book_time_row[your_book_time]) + ') > td.I.writable > div > div.celldiv.slots6.clone.ui-resizable > div.ui-resizable-handle.ui-resizable-s'
else:
    pulldown_pos1 = '#week_main > tbody > tr:nth-child(' + str(book_time_row[your_book_time]) + ') > td:nth-child(' + str(column) + ')' + ' > div > div.celldiv.slots2.clone.ui-resizable > div.ui-resizable-handle.ui-resizable-s'
    pulldown_pos2 = '#week_main > tbody > tr:nth-child(' + str(book_time_row[your_book_time]) + ') > td:nth-child(' + str(column) + ')' + ' > div > div.celldiv.slots3.clone.ui-resizable > div.ui-resizable-handle.ui-resizable-s'
    pulldown_pos3 = '#week_main > tbody > tr:nth-child(' + str(book_time_row[your_book_time]) + ') > td:nth-child(' + str(column) + ')' + ' > div > div.celldiv.slots4.clone.ui-resizable > div.ui-resizable-handle.ui-resizable-s'
    pulldown_pos4 = '#week_main > tbody > tr:nth-child(' + str(book_time_row[your_book_time]) + ') > td:nth-child(' + str(column) + ')' + ' > div > div.celldiv.slots5.clone.ui-resizable > div.ui-resizable-handle.ui-resizable-s'
    pulldown_pos5 = '#week_main > tbody > tr:nth-child(' + str(book_time_row[your_book_time]) + ') > td:nth-child(' + str(column) + ')' + ' > div > div.celldiv.slots6.clone.ui-resizable > div.ui-resizable-handle.ui-resizable-s'
pull_down_pos.append(pulldown_pos1), pull_down_pos.append(pulldown_pos2), pull_down_pos.append(pulldown_pos3), pull_down_pos.append(pulldown_pos4), pull_down_pos.append(pulldown_pos5)

##-----------------------------------下拉五次-------------------------------

time.sleep(0.5)

for i in range(len(pull_down_time)):

    book_hour = int(pull_down_time[i][0:2])
    book_minute = int(pull_down_time[i][3:5])
    now = datetime.datetime.now()
    hour, minute, second = now.hour, now.minute, now.second

    if(book_minute < minute):
        wait_minute = 60 - minute
        book_hour -= 1
        wait_minute += (book_hour - hour) * 60
    else:
        wait_minute = book_minute - minute
        wait_minute += (book_hour - hour) * 60

    if(wait_minute > 0):
        print('距离第', i+1, '次续订还需等待', wait_minute, '分钟(当前已预定', (i+1)*30, '分钟)。')
        time.sleep((wait_minute - 1) * 60)  ##等至最后一分钟循环判断

    #---------------------判断账号是否被注销----------------------------

    try:
        wd.refresh() # 刷新方法 refresh
        if(your_book_time >= '13:30'):
            wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        element = wd.find_element_by_css_selector('#logon_box > form:nth-child(2) > input[type=submit]:nth-child(6)')
        print('当前账户登录中。')
    except:
        print ("账户已注销，重新登入成功。")
        wd.get('http://172.27.14.4:5010/labs/admin.php')
        element = wd.find_element_by_id('username').send_keys(username)
        element = wd.find_element_by_id('password').send_keys(password)
        element = wd.find_element_by_css_selector("#logon > fieldset > div:nth-child(4) > input[type=submit]").click()
        element = wd.find_element_by_css_selector("body > header > nav > ul > li:nth-child(1) > div > div.mrbs > a").click()
        element = wd.find_element_by_css_selector(room_pos[room_num]).click()
        if dayOfWeek == 7:
            element = wd.find_element_by_css_selector("body > div.contents > nav:nth-child(3) > a.date_after").click()
        element = wd.find_element_by_css_selector("body > div.contents > nav:nth-child(3) > a.date_after").click()
        if(your_book_time >= '13:30'):
            wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    now_time = time.strftime('%H:%M:%S', time.localtime())
    while(now_time < pull_down_time[i]):
        now_time = time.strftime('%H:%M:%S', time.localtime())

    # time.sleep(1.5)
    time.sleep(1.5)

    try:
        element = wd.find_element_by_css_selector(pull_down_pos[i]) 
        # wd.execute_script("arguments[0].scrollIntoView();",element)
        if(your_book_time < '13:30'):
            wd.execute_script('window.scrollBy(0,100)')
            if(your_book_time >= '10:30'):
                wd.execute_script('window.scrollBy(0,80)')
                if(your_book_time == '13:00'):
                    wd.execute_script('window.scrollBy(0,50)')
        ActionChains(wd).move_to_element_with_offset(element, 0, 0).perform()
        ActionChains(wd).click_and_hold().move_by_offset(xoffset=0,yoffset=10).perform()
        ActionChains(wd).release().perform()
    except:
        pass


    time.sleep(0.5)
# wd.close()
print('Book over!')