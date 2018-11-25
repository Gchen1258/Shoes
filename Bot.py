import bs4 
from selenium import webdriver
import os

def render_page(url,agent): #Loads page for processing
    chromedriver = "./chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    options.add_argument('--headless')
    options.add_argument(f'user-agent={agent}')
    driver = webdriver.Chrome(chromedriver)
    driver.get(url)
    r = driver.page_source
    return r

def URLGen(model, size): #Generates URLs
    BaseSize = 580 #For shoe size 6.5
    ShoeSize = float(size) - 6.5
    ShoeSize *= 20 #Generates our size code
    RawSize = ShoeSize + BaseSize
    SizeCode = int(RawSize)
    URL = 'https://www.adidas.com/us/' + str(model) + '.html?forceSelSize=' + str(model) + '_' + str(SizeCode)
    return URL

def GetSizes(url): #Returns all available sizes
    response =  render_page(url)
    page = bs4.BeautifulSoup(response,"lxml")
    print(page.title.string)
    l = page.find_all('div',{"class" : "gl-square-list__cta"})
    sizes = []
    for i in range(0,len(l)):
        print(l[i].text)
        sizes.append(l[i].text)
    return sizes

