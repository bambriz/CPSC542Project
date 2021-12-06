import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options





class dummytest(unittest.TestCase):


	def test_openDiaspora(self):
		print("test")
		#All this stuff makes it so we can use in repl
		chrome_options = Options()
		chrome_options.add_argument('--no-sandbox')
		chrome_options.add_argument('--disable-dev-shm-usage')
		driver = webdriver.Chrome(options=chrome_options)
		driver.get("https://joindiaspora.com/")
		assert True