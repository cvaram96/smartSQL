class RegisterPage():
    def __init__(self,driver):
        self.driver = driver
        self.username_id ="username"
        self.email_textbox_id = "email"
        self.password_textbox_id = "password"
        self.confirm_password_id = 'confirm_password'
        self.signup_button_id= "submit"
    def enter_username(self,username):
        self.driver.find_element_by_id(self.username_id).clear()		
        self.driver.find_element_by_id(self.username_id).send_keys(username)
    def enter_confirm_password(self,password):
        self.driver.find_element_by_id(self.confirm_password_id).clear()		
        self.driver.find_element_by_id(self.confirm_password_id).send_keys(password)    
    def enter_email(self,email):
        self.driver.find_element_by_id(self.email_textbox_id).clear()		
        self.driver.find_element_by_id(self.email_textbox_id).send_keys(email)
    def enter_password(self,password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()		
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)
    def click_signup(self):
        self.driver.find_element_by_id(self.signup_button_id).click()

