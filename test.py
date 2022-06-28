from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import datetime

### -------------------------最新可订时间：当前日期+8  当前时间向后取整半小时再减1h--------------------------------
'''
功能：1、预定最新可订实验室（续至3h） 2、截胡（慎用） 

说明：1、填写自定义区即可运行（需下载浏览器驱动：https://chromedriver.storage.googleapis.com/index.html）  
      2、抢第二天早晨当天晚上11点后运行即可，抢下午/晚上，上午运行即可。
      3、截胡时间选当前时间向后取整后减去1h即可。   
      4、选择房间  0:206   1:208   2:308   3:310    4:107   5:402

                                                                                             by：CC
'''
##----------------------------------选择房间  0:206   1:208   2:308   3:310-------------------------------------

#自定义区
room_num = 1
your_book_time = '08:00'
username, password = '曹聪', 'cc'
your_book_message = '曹聪'

#--------------------------------------------------------------------------------------------------------#

now_time = time.strftime('%H:%M:%S', time.localtime())
print(now_time)
