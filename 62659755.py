from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

opts = Options()
opts.headless = True
assert opts.headless  # Operating in headless mode
browser = webdriver.Chrome('Z:/chromedriver.exe', options=opts)

sptct_links =['https://www.macys.com/shop/mens-clothing/mens-blazers-sports-coats/Productsperpage/120?id=16499',
        'https://www.macys.com/shop/mens-clothing/mens-blazers-sports-coats/Pageindex,Productsperpage/2,120?id=16499',
        'https://www.macys.com/shop/mens-clothing/mens-blazers-sports-coats/Pageindex,Productsperpage/3,120?id=16499',
        'https://www.macys.com/shop/mens-clothing/mens-blazers-sports-coats/Pageindex,Productsperpage/4,120?id=16499',
        'https://www.macys.com/shop/mens-clothing/mens-blazers-sports-coats/Pageindex,Productsperpage/5,120?id=16499']


def pull_Brand(url):
    browser.get(url)
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    brand = []
    temp = soup.find_all(class_='productBrand')
    for tag in soup.find_all(class_='productBrand'):
        brand.append(tag.text.strip())
    print(brand)


for i in range(len(sptct_links)):
        pull_Brand(sptct_links[i])

browser.quit()
