from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
# chrome_driver = "C:\\Users\\abcde\\anaconda3\\Scripts\\chromedriver.exe"
driver = webdriver.Chrome(options=chrome_options)
print(driver.title)