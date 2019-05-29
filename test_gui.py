from selenium import webdriver
import time, unittest,HtmlTestRunner
from loginpage import LoginPage
from Homepage import  HomePage
class LoginTest(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.driver= webdriver.Firefox(executable_path="/home/kadavul/Desktop/FlaskProject/driver/geckodriver")
		cls.driver.set_page_load_timeout(10)
		cls.driver.maximize_window()
	def test_mail_fail_login(self):
		driver = self.driver
		driver.get('http://localhost:5000/login')
		login = LoginPage(driver)
		login.enter_email("sdfsd")
		login.enter_password("sdf")
		login.click_login()
		time.sleep(2)
		login.click_login()
	
	def test_password_fail_login(self):
		driver = self.driver
		driver.get('http://localhost:5000/login')
		login = LoginPage(driver)
		login.enter_email("thalapathy@gmail.com")
		login.enter_password("sdfdfsdfds")
		login.click_login()
		time.sleep(2)
		login.click_login()	
	def test_pass_login(self):
		driver = self.driver
		driver.get('http://localhost:5000/login')
		login = LoginPage(driver)
		login.enter_email("thalapathy@gmail.com")
		login.enter_password("12345")
		login.click_login()
		home =HomePage(driver)
		home.click_home_page()
		home.click_logout()
		time.sleep(2)
	
	
	@classmethod
	def tearDownClass(cls):
		cls.driver.close()
		cls.driver.quit()
		print("Test is completed")
if __name__ == '__main__':
	 unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/home/kadavul/Desktop/FlaskProject/driver/"))
