import time
import os

import pandas as pd
import requests
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver

options = webdriver.ChromeOptions()
options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"  # 指定自定义Chrome浏览器路径
driver = webdriver.Chrome(options=options)
def create_folder(folder_path):
    try:
        os.mkdir(folder_path)
        print(f"Folder '{folder_path}' created successfully.")
    except FileExistsError:
        return

class company:
    def __init__(self, name, organizational_code,unified_social_credit_code,group_name):
        self.name = name
        self.unified_social_credit_code = str(unified_social_credit_code)
        self.organizational_code = str(organizational_code)
        self.group_name = str(group_name)
    def greet(self):
        return self.name+" "+self.organizational_code

def save_img(img_src):
    response = requests.get(img_src)
    with open('tmp.jpg', 'wb') as file_obj:
        file_obj.write(response.content)
        file_obj.close()

def read(excel_file_name):
    data = pd.read_excel(excel_file_name)
    object_list = [company(row['公司名称'],row['组织机构代码'],row['统一社会信用代码'],row['系列名字']) for index, row in data.iterrows()]
    return object_list

def open_lawxin_chrome():
    # 打开目标网页
    driver.get('https://www.lawxin.com/')
    driver.fullscreen_window()
    time.sleep(1)
    button = driver.find_element(By.XPATH, '//*[@id="header"]/div[1]/div[2]/div/ul/li[3]/button')
    driver.execute_script("arguments[0].scrollIntoView();", button)
    button.click()
    tab = driver.find_element(By.XPATH,
                              '/html/body/div[1]/div/div[4]/div/div/div[2]/div/div[2]/div[1]/div[1]/div/div/div/div[3]')
    driver.execute_script("arguments[0].scrollIntoView();", tab)
    tab.click()
    username_box = driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div/div[4]/div/div/div[2]/div/div[2]/div[1]/div[2]/div[2]/div/form/div[1]/div/div/input')
    username_box.send_keys('gdhx_jmfh')
    password_box = driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div/div[4]/div/div/div[2]/div/div[2]/div[1]/div[2]/div[2]/div/form/div[2]/div/div/input')
    password_box.send_keys('gdhx_jmfh')
    loggin_button = driver.find_element(By.XPATH,
                                        '/html/body/div[1]/div/div[4]/div/div/div[2]/div/div[2]/div[1]/div[2]/div[2]/div/form/div[3]/div/button')
    driver.execute_script("arguments[0].click();", loggin_button)
def search_lawxin(item):
    text= "广东华兴银行股份有限公司江门分行"
    driver.get('https://www.lawxin.com/lookupjq/'+text+'/0')
    time.sleep(1)
    text = item.name + " " + item.organizational_code
    group_name = item.group_name
    input_tab =driver.find_element(By.XPATH, '//*[@id="pane-second"]/div/input')
    # time.sleep(1)
    input_tab.clear()
    input_tab.send_keys(text)
    search_button = driver.find_element(By.XPATH, '//*[@id="pane-second"]/div/div/button')
    driver.execute_script("arguments[0].click();", search_button)
    time.sleep(1)
    try:
        li = driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[1]/div/div/div[1]/div[2]/div[5]/ul/li')
        li.click()
    except NoSuchElementException:
        print("no such element")
    time.sleep(2)
    try:
        if_button = driver.find_element(By.XPATH,
                                        '//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[1]/div[3]/div[3]/span')
        if_button.click()
    except NoSuchElementException:
        print("no such element")
    driver.maximize_window()
    driver.execute_script("document.body.style.zoom='50%'")
    time.sleep(1)
        # 截取屏幕截图
    create_folder(group_name)
    driver.save_screenshot(group_name+"\\"+text + "-汇法风控宝.png")
    print(text+"已截图")


def lan_xin(list):
    open_lawxin_chrome()
    time.sleep(2)
    for i in range(88,90):
        item = list[i]
        search_lawxin(item)
    # for item in list:
    #     search_lawxin(item)
    #     time.sleep(2)

if __name__=="__main__":
    list = read('C:\\Users\\abcde\\Desktop\\脚本Excel.xlsx')
    driver.maximize_window()
    lan_xin(list)

# 关闭浏览器
