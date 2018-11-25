import requests
from bs4 import BeautifulSoup
import Scraper
from Utils import isInt

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
#Find max product page
def findMaxPage():
    baseURL = 'https://www.adidas.com/us/men-shoes'
    res = requests.get(baseURL,headers=headers)
    page = BeautifulSoup(res.text,'lxml')
    pageindex = page.find_all('li',{'class':'gl-dropdown__option'})
    pagenumbers = []
    pages = []
    for index in pageindex:
        if isInt(index.text):
            pagenumbers.append(int(index.text))

    for i in range(0,len(pagenumbers)):
        if i == 0:
            pages.append(baseURL)
        else:
            index = "?start=" + str(i * 48)
            pages.append(baseURL + index)
    return pages

#Find all products href
def findProducts():
    pages = findMaxPage()
    res = []
    page = []
    products = []
    for i in range(0,len(pages)):
        res.append(requests.get(pages[i],headers=headers))
        page.append( BeautifulSoup(res[i].text,'lxml') )
        products = page[i].find_all('div',{'class':'gl-product-card__details'})
        for a in products:
            b = a.find('a',href=True)
            products.append(b['href'])
    
    return products

findProducts()