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
    def __init__(self, name, organizational_code,unified_social_credit_code,group_name):
        self.name = name
        self.unified_social_credit_code = str(unified_social_credit_code)
        self.organizational_code = str(organizational_code)
        self.group_name = str(group_name)
    def greet(self):
        return self.name+" "+self.organizational_code
def create_folder(folder_path):
    try:
        os.mkdir(folder_path)
        print(f"Folder '{folder_path}' created successfully.")
    except FileExistsError:
        return


def read(excel_file_name):
    data = pd.read_excel(excel_file_name)
    object_list = [company(row['公司名称'],row['组织机构代码'],row['统一社会信用代码'],row['系列名字']) for index, row in data.iterrows()]
    return object_list

def search_zxgk(item):
    text = item.name + "_" + item.organizational_code
    name = item.name
    group_name = item.group_name
    organizational_code = item.organizational_code
    name_input = driver.find_element(By.XPATH,'//*[@id="pName"]')
    organizational_code_input = driver.find_element(By.XPATH, '//*[@id="pCardNum"]')
    organizational_code_input.clear()
    organizational_code_input.send_keys(organizational_code)
    name_input.clear()
    name_input.send_keys(name)
    try:
        tab = driver.find_element(By.XPATH,'//*[@id="yzm-group"]/div[5]')
    except NoSuchElementException:
        print("no such element")
    # button = driver.find_element(By.XPATH,'//*[@id="yzm-group"]/div[6]/button')
    # driver.execute_script("arguments[0].scrollIntoView();", button)
    # driver.execute_script("arguments[0].click();", button)    time.sleep(2)
    create_folder(group_name)
    driver.maximize_window()
    driver.save_screenshot(group_name+"\\"+text + "-全国法院被执行人信息网.png")
    print(text + "已截图")
def zxgk(list):
    for i in range(0,90):
        item = list[i]
    # for item in list:
        search_zxgk(item)
    driver.quit()

if __name__=="__main__":
    list = read('C:\\Users\\abcde\\Desktop\\脚本Excel.xlsx')
    zxgk(list)

# 关闭浏览器
