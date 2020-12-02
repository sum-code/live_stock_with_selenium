import re
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
def calculate(stock):
    try:
        link = "https://www.nseindia.com/get-quotes/equity?symbol="+stock  #link for go into web page
        web_driver = webdriver.Chrome(executable_path=r'chromedriver.exe')      #selenium web_driver
        web_driver.set_page_load_timeout(30)                                     #for time out page
        
        web_driver.get(link)                                                       #get link
        time.sleep(15)

        l = web_driver.find_element_by_id("priceInfoTable").get_attribute('outerHTML')  #for finding value of table in web page
        s = (re.search('dy class', a)).end()                                            #regular expression for finding index
        open_ = l[s+12:s+20]                                                              
        close_ = l[s+29:s+37]                                                            #we get value for open and close

        low = web_driver.find_element_by_id('gq-e-idhlMin').get_attribute('innerHTML')    #find value with id in web page
        high = web_driver.find_element_by_id('gq-e-idhlMax').get_attribute('innerHTML')     #same for high
        total_volume = web_driver.find_element_by_id('orderBookTradeVol').get_attribute('innerHTML')  #same for valume
        Delivery_data = web_driver.find_element_by_id('securityWiseDQ').get_attribute('innerHTML')
        Delivery_percentage =web_driver.find_element_by_id('securityWiseDQTQ').get_attribute('innerHTML')  #for finding delivery data
        print('Data Retrieved')
        web_driver.quit()                   #closing web driver
        return(open_,close_,low,high,total_volume,Delivery_data,Delivery_percentage)
    except:     #for any error occured
        print('Internet timeout while Retrieving data')
        return(['-','-','-','-','-','-','-'])
symbol=['RELIANCE','HDFCBANK','ADANIPORTS','ITC','SBIN','IOC','RBLBANK']

all_stocklist=[]
cou=0
for i in symbol:
    cou+=1
    print('calculating : '+str(cou)+'-'+i)
    all_stocklist.append(calculate(i))

import sys
import pandas as pd
print('List of '+str(sys.getsizeof(all_stocklist))+' bits')
print(pd.DataFrame(all_stocklist,columns=['Open','High','Low','Close','Volume','Delivery Data','Delivery Percentage']))
