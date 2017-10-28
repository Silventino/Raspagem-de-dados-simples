from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver

url = 'http://seti.ufla.br'

driver = webdriver.PhantomJS()
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser')

divs = soup.findAll('div', {'ng-repeat':'palestrante in palestrantes'})

for div in divs:
	palestrante = div.find('p').text
	empresa = div.find('h4').text
	print(palestrante + " - " + empresa)