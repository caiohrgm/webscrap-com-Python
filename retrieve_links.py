from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from selenium import webdriver
from pyvirtualdisplay import Display
import datetime		#
import random		# Importa a biblioteca de
import re 			# Importa a biblioteca de Expresões Regulares(re)


random.seed(datetime.datetime.now())
def getLinks(articleUrl):
	my_url = "http://en.wikipedia.org"+articleUrl
	web_r = uReq(my_url)
	driver = webdriver.Chrome(executable_path="/home/caiom/Downloads/chromedriver_linux64/chromedriver")
	driver.get(my_url)

	souppage_soup = soup(web_r,'html.parser')
	html = driver.execute_script("return document.documentElement.outerHTML") # pequisar

	html_page_soup = soup(html,"html.parser")

	return html_page_soup.find("div",{"id":"bodyContent"}).findAll("a",
								href =  re.compile("^(/wiki/)((?!:).)*$"))

display = Display(visible=0, size=(800, 800))
display.start()

links = getLinks("/wiki/Kevin_Bacon")

while len(links) > 0:
	newArticle = links[random.randint(0,len(links)-1)].attrs["href"] #Pega um elemento aleatorio da lista de links;
	print(newArticle)
	links = getLinks(newArticle)
