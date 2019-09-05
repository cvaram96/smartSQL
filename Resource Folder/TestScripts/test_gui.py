from selenium import webdriver
import time, unittest,HtmlTestRunner
from loginpage import LoginPage
from Homepage import  HomePage
from accountpage import AccountPage
from databasepage import DatabasePage
from selenium.webdriver.support.ui import Select

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
	
	def test_pass_login(self):
		driver = self.driver
		driver.get('http://localhost:5000/login')
		login = LoginPage(driver)
		login.enter_email("user@uom.lk")
		login.enter_password("12345")
		time.sleep(2)
		login.click_login()
		home =HomePage(driver)
		home.click_account_page()
		time.sleep(2)
		
	def test_query_pass(self):
		driver = self.driver
		account = AccountPage(driver)
		account.click_database()
		time.sleep(3)
		database =DatabasePage(driver)
		database.enter_query('what is the image of the products which productCode is 333')
		time.sleep(3)
		database.click_submit()
		time.sleep(4)
		database.check_query(str("SELECT productlines.image FROM products INNER JOIN productlines ON products.productLine = productlines.productLine WHERE products.productCode = '333';"))
		time.sleep(4)


	@classmethod
	def tearDownClass(cls):
		cls.driver.close()
		cls.driver.quit()
		print("Test is completed")
if __name__ == '__main__':
	 unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/home/kadavul/Desktop/FlaskProject/driver/"))
