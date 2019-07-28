from selenium import webdriver
import time
# import gspread
# from oauth2client.service_account import ServiceAccountCredentials
# scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
# creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
# client = gspread.authorize(creds)
# sheet = client.open('product price').sheet1
# stuff = sheet.get_all_records()
# print(stuff)




class AmazonBot(object):
    def __init__(self,item):
        self.item = item
        self.drv = webdriver.Firefox()


    def get_url(self):
        self.drv.get("https://www.amazon.in/")

    def find_item(self):
        for item in self.item:
            search_box = self.drv.find_element_by_id('twotabsearchtextbox')
            search_box.send_keys(item)
            search = self.drv.find_element_by_class_name('nav-input')
            search.click()
            time.sleep(2)
            first_search = self.drv.find_element_by_css_selector("div.s-result-item:nth-child(1)")
            asin = first_search.get_attribute("data-asin")
            url = "https://www.amazon.in/dp/" + asin
            self.get_title(url)
            self.get_price(url)


    def get_title(self,url):
        self.drv.get(url)
        try:
            title = self.drv.find_element_by_id("productTitle").text
        except:
            pass


        print(title)


    def get_price(self,url):
        self.drv.get(url)
        try:
            price = self.drv.find_element_by_id("priceblock_ourprice").text
        except:
            pass
        try:
            price = self.drv.find_element_by_id("priceblock_ourprice").text
        except:
            pass
        print(price)


    def quit(self):
        self.drv.close()







item = input("enter an item you want to purchase separated by / ::").split('/')
amazon = AmazonBot(item)
amazon.get_url()
amazon.find_item()
amazon.quit()