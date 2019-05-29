class HomePage():
	def __init__(self,driver):
		self.driver = driver
		self.home_page_by_link_text="smartSQL"
		self.about_page_by_link_text="About"
		self.account_page_by_link_text="Profile"
		self.navbar_id="navbarDropDown"
		self.logout_by_link_text= "Logout"
		self.create_review_by_link_text="New Databae"
		self.new_scheme_page_by_link_text="Create Review"
	def click_home_page(self):
		self.driver.find_element_by_link_text(self.home_page_by_link_text).click()
	
	def click_about_page(self):
		self.driver.find_element_by_link_text(self.about_page_by_link_text).click()
	
	def click_account_page(self):
		self.driver.find_element_by_link_text(self.account_page_by_link_text).click()
	
	def click_logout(self):
		self.driver.find_element_by_link_text(self.logout_by_link_text).click()
	def click_create_review(self):
		self.driver.find_element_by_link_text(self.create_review_by_link_text).click()
	
	def click_new_scheme(self):
		self.driver.find_element_by_link_text(self.new_scheme_page_by_link_text).click()
	
