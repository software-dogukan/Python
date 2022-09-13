import time
from User_Password import e_mail,password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
class Linkedln:
    def __init__(self,e_mail,password):
        self.browser=webdriver.Chrome()
        self.e_mail=e_mail
        self.password=password
    def signIn(self):
        self.browser.get("https://www.linkedin.com/login/tr")
        self.browser.maximize_window()
        mailInput= self.browser.find_element(By.XPATH,"//*[@id='username']")
        passwordInput=self.browser.find_element(By.XPATH,"//*[@id='password']")
        mailInput.send_keys(self.e_mail)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
login=Linkedln(e_mail,password)
login.signIn()