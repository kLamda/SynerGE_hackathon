# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 09:22:41 2020

@author: krish
"""

from django.contrib.staticfiles.storage import staticfiles_storage
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')


import time
year = ''


from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def giveDate(page_, num, date_r, month_r):
    date = page_[num].find_elements_by_class_name("text05")[0].text.replace("\n", "")[-10:-8]
    month = page_[num].find_elements_by_class_name("text05")[0].text.replace("\n", "")[-7:-5]
    if (date!='r '):
        print("Date : {}, Month : {}".format(date, month))
        if (int(date)<=date_r) and (int(month)==month_r):
            
            return True
        else:
            return False
    else:
        giveDate(page_, num-1, date_r, month_r)
    
from numba import jit
import csv

def csvGen(post_elems, location, path):
    data_scrapped = []
    for i in range(1, len(post_elems)):
        print("Row {} stored".format(i))
        data_scrapped.append([post_elems[i].find_elements_by_class_name("text03")[0].text.split("\n")[0][-8:],
                         post_elems[i].find_elements_by_class_name("text03")[0].text.split("\n")[1],
                         post_elems[i].find_elements_by_class_name("text04")[0].text.replace("\n", ""),
                         post_elems[i].find_elements_by_class_name("text05")[0].text.replace("\n", "")[-10:],
                         location[i - 1].text.split("\n")[0]])

    print(data_scrapped)
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file)
        for item in data_scrapped:
            writer.writerow(item)

    with open(staticfiles_storage.path("csv/scrapped_backup.csv"), "a+", newline='') as file:
        writer = csv.writer(file)
        for item in data_scrapped:
            writer.writerow(item)

def scrap_data(Threshold_date, Threshold_month, path):
    print("The scraper started")
    browser = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe',chrome_options=chrome_options)
    browser.get("https://www.tender247.com/keyword/Medical+Equipment+Tenders#")
    browser.execute_script("manageTab('3');")
    browser.execute_script("archiveTabYearWise('');")
    time.sleep(5)

    elem = browser.find_element_by_tag_name("body")

    no_of_pagedowns = 1

    while True:
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.2)
        if (no_of_pagedowns % 50 == 0):
            page_ = browser.find_elements_by_class_name("tender_inner_tr")
            num = len(page_) - 1
            if(giveDate(page_, num, Threshold_date, Threshold_month)):
                break
        print("no_of_pagedowns", no_of_pagedowns)
        no_of_pagedowns+=1

    post_elems = browser.find_elements_by_class_name("tender_inner_tr")
    location = browser.find_elements_by_class_name("location_content")
    csvGen(post_elems=post_elems, location=location, path=path)
    print("Scraping Ended")