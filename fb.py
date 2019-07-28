from selenium import webdriver
from getpass import getpass

usr = input("Enter your username::")
pwd = getpass("password::")

drv = webdriver.Chrome()
drv.get('https://www.facebook.com/')

username_box = drv.find_element_by_id('email')
username_box.send_keys(usr)

password_box = drv.find_element_by_id('pass')
password_box.send_keys(pwd)

login = drv.find_element_by_id('loginbutton')
login.click()
drv.close()