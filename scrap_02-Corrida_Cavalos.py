
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from selenium import webdriver
from pyvirtualdisplay import Display
import pandas as pd
import pandas as to_csv
import pandas as DataFrame

display = Display(visible=0, size=(800, 800))
display.start()

my_url = "https://www.sportinglife.com/racing/results/2019-09-30/hamilton/545168/channel-finance-scotland-finance-made-simple-handicap-gentleman-amateur-riders"
web_r = uReq(my_url)

driver = webdriver.Chrome(executable_path="/home/caiom/Downloads/chromedriver_linux64/chromedriver")
driver.get(my_url)

souppage_soup = soup(web_r,'html.parser')
html = driver.execute_script("return document.documentElement.outerHTML") # pequisar


html_page_soup = soup(html,"html.parser")

#Pega posição:
position = html_page_soup.find_all("span",{"class":"ordinal"})
posicoes = []
for i in range(len(position)):
	txt = soup.get_text(position[i])
	if(txt[0] == "1" or txt[0] == "2" or txt[0] =="3"):
		posicoes.append(txt[0]) #Adicionando as 3 posições, se elas estiverem presente, na lista de posições.


# Pega Hora,Data e Corrida: De fevereiro/2005 até 2019 nomenclatura das tags está igual
lugar = html_page_soup.find("div",{"class":"hr-racing-racecard-heading-text"})
text = soup.get_text(lugar)
listaTexto = text.split(":")
lista2 = listaTexto[1].split(" ")
lista3 = lista2[0].split("\xa0")

datas = []

#Pega 1º,2º,3º e odds:
names = html_page_soup.find_all("span",{"class":"hr-racing-runner-horse-name"})
nomes = []
for i in range(len(names)):
	if i > 2:
		break
	txt = soup.get_text(names[i])
	nomes.append(txt)
print(nomes)

chances = html_page_soup.find_all("span",{"class":"hr-racing-runner-betting-info"})
odds = []
for odd in odds:
	txt = soup.get_text(odd)
	print(txt)


#df = pd.DataFrame({'Data': datas,
					#'Pista': pistas,
					#'Horário': horarios,
					#'odd 1º Lugar': odd1,
					#'odd 2º Lugar': odd2,
					#'odd 3º Lugar': odd3})

#df.to_csv('resultadosBrasileirao.csv',index=False,header=True) #Salva o arquivo em .csv sem Index(Indice da lista);
#print(df)


#for elm in html_page_soup.find_all("div",{"class":"hr-racing-racecard-heading-text"}):
	
	#txt = soup.get_text(elm) #converte o retorno da busca do html em texto(String)
	#print(txt)
	#text = txt.strip("\n\n\t")
	#text2 = text.strip(".\n\n")


#text = txt.strip("\n\n\t")
#text2 = text.strip(".\n\n")


