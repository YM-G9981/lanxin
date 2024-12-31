import time

import pandas as pd
import requests
import os
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=chrome_options)

class company:
    def __init__(self, name, organizational_code,unified_social_credit_code):
        self.name = name
        self.unified_social_credit_code = str(unified_social_credit_code)
        self.organizational_code = str(organizational_code)
    def greet(self):
        return self.name+" "+self.organizational_code

def save_img(img_src):
    response = requests.get(img_src)
    with open('tmp.jpg', 'wb') as file_obj:
        file_obj.write(response.content)
        file_obj.close()

def read(excel_file_name):
    data = pd.read_excel(excel_file_name)
    object_list = [company(row['公司名称'],row['组织机构代码'],row['统一社会信用代码']) for index, row in data.iterrows()]
    return object_list

def search_zxgk(item):
    name = item.name
    driver.get('https://www.qcc.com/')
    time.sleep(2)
    input = driver.find_element(By.XPATH,'//*[@id="searchKey"]')
    # input.clear()
    input.send_keys(name)
    time.sleep(1)
    button = driver.find_element(By.XPATH,'/html/body/div/div[2]/section[1]/div/div/div/div[1]/div/div/span/button')
    button.click()
    time.sleep(1)
    frist_a = driver.find_element(By.XPATH,'/html/body/div/div[2]/div[2]/div[3]/div/div[2]/div/table/tr[1]/td[3]/div/span/span[1]/a')
    href = frist_a.get_attribute('href')
    driver.get(href)
    time.sleep(1)
    # report_Button = driver.find_element(By.XPATH,'/html/body/div/div[2]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[2]/div/a[1]')
    # report_Button.click()
    # try:
    #     download_Button = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[3]/div/div[1]/div[2]/div[2]/div/div/div[2]/div[2]/a')
    #     download_Button.click()
    # catch:
    #     /html/body/div[2]/div/div/div/div[3]/div/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/div[3]/a[2]
    # # driver.get(href)

    # relation_Pic = driver.find_element(By.XPATH,'//*[@id="qccgraph"]/div/a[4]')
    # relation_Pic.click()

    time.sleep(1)
def zxgk(list):
    for i in range(41,90):
        item = list[i]
        if(item.name.endswith('公司')):
            search_zxgk(item)
    driver.quit()

if __name__=="__main__":
    list = read('C:\\Users\\abcde\\Desktop\\脚本Excel.xlsx')
    zxgk(list)

# 关闭浏览器
