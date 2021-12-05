from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#All this stuff makes it so we can use in repl
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)

#The website we will do tests on
driver.get("https://podington.oksocial.net/")

