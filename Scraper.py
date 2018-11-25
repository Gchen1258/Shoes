import requests
import bs4 
from selenium import webdriver
import random
import os
import time

agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'

def render_page(url):
    #Grabs our Chrome Driver and sets PATH
    chromedriver = "./chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument(f'user-agent={agent}')
    driver = webdriver.Chrome(chromedriver,options=options)
    driver.get(url)
    #time.sleep(2)
    r = driver.page_source
    return r


#headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
#proxies = {
#    "https": 'https://37.53.83.40:34934',
#    "https": 'https://139.0.23.188:32551'
#}

#url = 'https://www.adidas.com/us/F36156.html?forceSelSize=F36156_600'
#response =  render_page(url)
#page = bs4.BeautifulSoup(response,"lxml")
#print(page.title.string)
#l = page.find_all('div',{"class" : "gl-square-list__cta"})

#sizes = []

#for i in range(0,len(l) - 1):
#    print(l[i].text)
#    sizes.append(l[i].text)

#print(sizes)
