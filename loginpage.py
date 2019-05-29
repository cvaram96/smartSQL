class LoginPage():
	def __init__(self,driver):
		self.driver = driver
		self.email_textbox_id = "email"
		self.password_textbox_id = "password"
		self.login_button_id= "submit"

	def enter_email(self,email):
		self.driver.find_element_by_id(self.email_textbox_id).clear()		
		self.driver.find_element_by_id(self.email_textbox_id).send_keys(email)

	def enter_password(self,password):
		self.driver.find_element_by_id(self.password_textbox_id).clear()		
		self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

	def click_login(self):
		self.driver.find_element_by_id(self.login_button_id).click()

