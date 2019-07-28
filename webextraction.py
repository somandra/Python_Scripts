from selenium import webdriver

max_page_num = 5
max_dig_num = 3
with open("result.csv",'w') as f:
    f.write("Buyers , Prices \n")

drv = webdriver.Chrome()
for i in range(1,max_page_num+1):
    p = (max_dig_num-len(str(i)))*"0"+str(i)
    url = "http://econpy.pythonanywhere.com/ex/"+p+".html"
    drv.get(url)
    buyers = drv.find_elements_by_xpath('//div[@title = "buyer-name"]')
    prices = drv.find_elements_by_xpath('//span[@class = "item-price"]')
    n = len(buyers)
    with open("result.csv",'a') as f:
        for i in range(n):
            f.write(buyers[i].text + "," + prices[i].text+'\n')

# drv.get("http://econpy.pythonanywhere.com/ex/001.html")

# buyers = drv.find_elements_by_xpath('//div[@title = "buyer-name"]')
# prices = drv.find_elements_by_xpath('//span[@class = "item-price"]')

# n = len(buyers)
#
# for i in range(n):
#     print(buyers[i].text+" : "+prices[i].text)

drv.close()
