from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import urllib.request

class cragslist_scrapper(object):
    def __init__(self,min,max,location):
        self.min_price = min
        self.max_price = max
        self.location = location
        self.driver = webdriver.Chrome()
        self.url = f"https://{self.location}.craigslist.org/search/sss?min_price={self.min_price}&max_price={self.max_price}"
        self.delay = 3

    def get_driver(self):
        self.driver.get(self.url)
        try:
            wait = WebDriverWait(self.driver,self.delay)
            wait.until(EC.presence_of_element_located((By.ID,"searchform")))
            print("Page is ready")
        except TimeoutException:
            print("Loading took too much time")

    def extract_post_titles(self):
        all_posts = self.driver.find_elements_by_class_name("result-row")
        all_post_titles = []
        for post in all_posts:
            all_post_titles.append(post.text)
            print(post.text)

    def extract_urls(self):
        url_list = []
        html_page = urllib.request.urlopen(self.url)
        soup = BeautifulSoup(html_page,features="html.parser")
        for link in soup.findAll("a",{"class":"result-title hdrlnk"}):
            url_list.append(link["href"])
            print(link["href"])


    def quit(self):
        self.driver.close()

min_price ="2000"
max_price = "200000"
location = "jaipur"


scrape = cragslist_scrapper(min_price,max_price,location)
scrape.get_driver()
scrape.extract_post_titles()
scrape.extract_urls()
scrape.quit()