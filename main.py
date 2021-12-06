from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import unittest
import time
unittest.TestLoader.sortTestMethodsUsing = None
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=chrome_options)

userNTextID = "user_username"

# #All this stuff makes it so we can use in repl
# chrome_options = Options()
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')

# driver = webdriver.Chrome(options=chrome_options)

# #The website we will do tests on
# driver.get("https://podington.oksocial.net/")
'''Define Test class below
   Started the namng convention for sequential testing
   Right now it does things in separate sections but we will combine test 1 and 2 as they are part of logging in'''
class DiasporaTest(unittest.TestCase):
	def setUp(self):
		print("Setting up Test")

	

	def test_1(self):
		#All this stuff makes it so we can use in repl
		
		print("test 1")
		
		#wait for webpage to load
		time.sleep(2)
		#Checks to see we are on the right page
		assert "OKSocial" in driver.title
	
	def test_2(self):
		time.sleep(1)
		print("Second Test")
		time.sleep(1)
		print("It is good")
		usernameBox = driver.find_element(By.ID,userNTextID)
		usernameBox.clear()
		usernameBox.send_keys("dummy123")
		time.sleep(2)

		assert "dummy123" in usernameBox.get_attribute('value')

	def test_3(self):
		print("Closing Tab.")
		driver.close()
		assert True
	def tearDown(self):
		print("Tearing down")


if __name__ == "__main__":
	driver.get("https://podington.oksocial.net/")
	unittest.main()
