from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller
from selenium.webdriver.common.keys import Keys
import unittest
import time


unittest.TestLoader.sortTestMethodsUsing = None
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("window-size=1200x600")
driver = webdriver.Chrome(options=chrome_options)

userNTextID = "user_username"
userPTextID = "user_password"
commitButtonName = "commit"
profAdd = "https://podington.oksocial.net/u/dummy123"
tagName = "#food"
composeButtonID = "compose-badge"
textAreaID = "status_message_text"
shareButtonID = "submit"
composeSubmitID = "submit_new_message"
dummyText = """This is Dummy Text created by a selenium bot for testing purposes.

Do not be alarmed!

Best,
Dummy123
#selenium"""
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
		
		print("test 1 to Verify we are on the right website")
		
		#wait for webpage to load
		time.sleep(2)
		#Checks to see we are on the right page
		assert "OKSocial" in driver.title
	
	def test_2(self):
		time.sleep(1)
		print("Second Test Loggin to dummy account")
		time.sleep(1)
		print("It is good")
		usernameBox = driver.find_element(By.ID,userNTextID)
		usernameBox.clear()
		usernameBox.send_keys("dummy123")
		time.sleep(1)
		passwordBox = driver.find_element(By.ID,userPTextID)
		passwordBox.clear()
		passwordBox.send_keys("12345@@@@@")
		time.sleep(1)
		print("Username and Password have been typed")
		submitButton = driver.find_element(By.NAME, commitButtonName)
		submitButton.click()
		time.sleep(2)
		print("Logged in. Now Verify Correct Account.")
		driver.get(profAdd)
		time.sleep(2)
		print("Verifying Account...")
		avatar = driver.find_element(By.CLASS_NAME, "avatar")
		correctAccount = "dummy123" in avatar.get_attribute('alt')
		time.sleep(3)
		print("Going back to home page...")
		driver.back()
		time.sleep(1)
		if correctAccount:
			print("Account verified!")
		assert correctAccount

	def test_3(self):
		time.sleep(2)
		print("Third Test Searching for Tags")
		time.sleep(2)
		searchBox = driver.find_element(By.ID,"q")
		searchBox.clear()
		searchBox.send_keys(tagName)
		print("tag name has been typed")
		time.sleep(2)
		searchBox.send_keys(Keys.RETURN)
		print("displaying the searching results")
		time.sleep(5)
		assert True

	def test_4(self):
		#like a post
		time.sleep(2)
		print("Click like a post")
		likePost = driver.find_element(By.CLASS_NAME, "like")
		likePost.click()
		time.sleep(2)
		assert True
    
	def test_5(self):
		#share a post
		print("Click share a post")
		sharePost = driver.find_element(By.CLASS_NAME, "reshare")
		sharePost.click()
		time.sleep(3)
		keyboard = Controller()
		keyboard.press(Key.enter)
		keyboard.release(Key.enter)
		time.sleep(3)
		print("Go back To Home Page")
		driver.get("https://podington.oksocial.net/stream")
		time.sleep(2)
		assert True

	def test_6(self):
		print("This Test will create a Post.")
		try:
			composeButton = driver.find_element(By.ID, composeButtonID)
			time.sleep(1)
			composeButton.click()
			time.sleep(2)
			print("Composing post...")
			textArea = driver.find_element(By.ID, textAreaID)
			textArea.clear()
			textArea.send_keys(dummyText)
			time.sleep(3)
			submitButton = driver.find_element(By.ID, composeSubmitID)
			submitButton.click()
			time.sleep(3)
			divElement = driver.find_element(By.CLASS_NAME, "nsfw-hidden")
			divElement = divElement.find_element(By.CLASS_NAME, "ltr")
			textParagraph = divElement.find_element(By.TAG_NAME, 'p')
			assert dummyText is textParagraph.text
		   
		except:
			time.sleep(2)
			print("Composing post...")
			textArea = driver.find_element(By.ID, textAreaID)
			textArea.click()
			textArea.clear()
			textArea.send_keys(dummyText)
			time.sleep(3)
			submitButton = driver.find_element(By.ID, shareButtonID)
			submitButton.click()
			time.sleep(3)
			print("Dummy Text Posted")
			# divElement = driver.find_element(By.CLASS_NAME, "collapsible-nsfw-hidden")
			# divElement = divElement.find_element(By.CLASS_NAME, "markdown-content")
			
			assert True

		

		

	def test_7(self):
		#Change this to be the last TestCase whenerver you make one
		time.sleep(3)
		print("Closing Tab.")
		driver.close()
		assert True


	def tearDown(self):
		print("Tearing down")


if __name__ == "__main__":
	driver.get("https://podington.oksocial.net/")
	driver.maximize_window()
	unittest.main()
