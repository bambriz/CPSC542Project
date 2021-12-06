from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import unittest
import dummytest
# #All this stuff makes it so we can use in repl
# chrome_options = Options()
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')

# driver = webdriver.Chrome(options=chrome_options)

# #The website we will do tests on
# driver.get("https://podington.oksocial.net/")
'''Define Test class below
   An Example is Provided We should create our own
   note that setUp and tearDown is called for each test
   so to make it easier we will just print stuff in them and isntead only setup the page opening in first test'''
class dummytest(unittest.TestCase):
	def setUp(self):
		print("Setting up Test")
		chrome_options = Options()
		chrome_options.add_argument('--no-sandbox')
		chrome_options.add_argument('--disable-dev-shm-usage')
		driver = webdriver.Chrome(options=chrome_options)
		driver.get("https://podington.oksocial.net/")
	def test_openDiaspora(self):
		#All this stuff makes it so we can use in repl
		
		print("test 1")
		
		assert True
	
	def tearDown(self):
		print("Tearing down")


if __name__ == "__main__":
	unittest.main()
