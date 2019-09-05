class DatabasePage():
	def __init__(self,driver):
		self.driver = driver
		self.query_id = "userQuery"
		self.submit_button_id= "submit"
		self.sql_id = "systemQuery"


	
	def enter_query(self,query):
		self.driver.find_element_by_id(self.query_id).clear()		
		self.driver.find_element_by_id(self.query_id).send_keys(query)

	def click_submit(self):
		self.driver.find_element_by_id(self.submit_button_id).click()

	def check_query(self,sql):
		if sql ==self.driver.find_element_by_id(self.submit_button_id).text:
			self.click_submit()





