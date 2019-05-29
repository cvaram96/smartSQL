class AccountPage():
    def __init__(self,driver):
        self.driver= driver
        self.username_textbox_id = 'username'
        self.email_textbox_id = 'email'
        self.picture_box_id = 'picture'
        self.upload_button_id = 'submit'
        self.database_xpath = '/html/body/main/div/div[2]/div/div/div[2]/article/div/h2/a'

    def change_username(self,name):
        self.driver.find_element_by_name(self.username_textbox_id).clear()
        self.driver.find_element_by_name(self.username_textbox_id).sendkeys(name)
    
    def change_email(self,email):
        self.driver.find_element_by_email(self.email_textbox_id).clear()
        self.driver.find_element_by_name(self.email_textbox_id).sendkeys(email)
    
    
    def insertPic(self,picture):
        self.driver.find_element_by_name(self.picture_box_id).sendkeys(picture)
    
    def click_upload(self):
        self.driver.find_element_by_id(self.upload_button_id).click()
    