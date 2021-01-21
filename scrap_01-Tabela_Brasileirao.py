#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 10:57:33 2019

@author: caiom
"""
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from selenium import webdriver
from pyvirtualdisplay import Display
import pandas as pd
#import pandas as to_csv
import pandas as to_excel
import pandas as DataFrame

display = Display(visible=0, size=(800, 800))
display.start()

my_url = "https://www.resultados.com/futebol/brasil/serie-a/classificacao/"
web_r = uReq(my_url)

driver = webdriver.Chrome(executable_path="/home/caiom/Downloads/chromedriver_linux64/chromedriver")
driver.get(my_url)

souppage_soup = soup(web_r,'html.parser')
html = driver.execute_script("return document.documentElement.outerHTML") # pequisar


html_page_soup = soup(html,"html.parser")
container = html_page_soup.findAll("div",{"class":"table__row"})


# Pega Classificação:
classif = []
for position in html_page_soup.find_all("div",{"class":"table__cell table__cell--rank table__cell--col_rank table__cell--no table__cell--q1 cell--sorted"}):
	time = []
	txt = soup.get_text(position)
	text = txt.strip("\n\n\t")
	text2 = text.strip(".\n\n")
	classif.append(text2)
for position in html_page_soup.find_all("div",{"class":"table__cell table__cell--rank table__cell--col_rank table__cell--no table__cell--q2 cell--sorted"}):
	time = []
	txt = soup.get_text(position)
	text = txt.strip("\n\n\t")
	text2 = text.strip(".\n\n")
	classif.append(text2)
for position in html_page_soup.find_all("div",{"class":"table__cell table__cell--rank table__cell--col_rank table__cell--no table__cell--q3 cell--sorted"}):
	time = []
	txt = soup.get_text(position)
	text = txt.strip("\n\n\t")
	text2 = text.strip(".\n\n")
	classif.append(text2)
for position in html_page_soup.find_all("div",{"class":"table__cell table__cell--rank table__cell--col_rank table__cell--no table__cell-- cell--sorted"}):
	time = []
	txt = soup.get_text(position)
	text = txt.strip("\n\n\t")
	text2 = text.strip(".\n\n")
	classif.append(text2)
for position in html_page_soup.find_all("div",{"class":"table__cell table__cell--rank table__cell--col_rank table__cell--no table__cell--r1 cell--sorted"}):
	time = []
	txt = soup.get_text(position)
	text = txt.strip("\n\n\t")
	text2 = text.strip(".\n\n")
	classif.append(text2)

# Pega Equipes:
equipes = []
for nome in html_page_soup.find_all("span",{"class":"team_name_span"}):
	txt = soup.get_text(nome)
	text = txt.strip("\n")
	equipes.append(text)
	
# Pega Nº de Jogos:
nJogos = []
for jogos in html_page_soup.find_all("div",{"class":"table__cell table__cell--matches_played table__cell--col_matches_played"}):
	txt = soup.get_text(jogos)
	text = txt.strip("\n\t")
	nJogos.append(text)

# Pega Nº de Vitórias:
nVitorias = []
for vitorias in html_page_soup.find_all("div",{"class":"table__cell table__cell--wins_regular table__cell--col_wins_regular"}):
	txt = soup.get_text(vitorias)
	text = txt.strip("\n\t")
	nVitorias.append(text)

# Pega Nº de Empates:
nEmpates = []
for empates in html_page_soup.find_all("div",{"class":"table__cell table__cell--draws table__cell--col_draws"}):
	txt = soup.get_text(empates)
	text = txt.strip("\n\t")
	nEmpates.append(text)

# Pega Nº de Derrotas:
nDerrotas = []
for derrotas in html_page_soup.find_all("div",{"class":"table__cell table__cell--losses_regular table__cell--col_losses_regular"}):
	txt = soup.get_text(derrotas)
	text = txt.strip("\n\t")
	nDerrotas.append(text)

# Pega Nº de Gols:
nGolsFeitos = []
nGolsSofridos = []
for gols in html_page_soup.find_all("div",{"class":"table__cell table__cell--goals table__cell--col_goals"}):
	txt = soup.get_text(gols)
	text = txt.strip("\n\t")
	quebra = text.split(":")
	nGolsFeitos.append(quebra[0])
	nGolsSofridos.append(quebra[1])

# Pega Nº de Pontos:
nPontos = []
for pontos in html_page_soup.find_all("div",{"class":"table__cell table__cell--points table__cell--col_points"}):
	txt = soup.get_text(pontos)
	text = txt.strip("\n\t")
	nPontos.append(text)

# Coloca no DataFrame:
df = pd.DataFrame({'Classificação': classif,
					'Equipes': equipes,
					'Jogos': nJogos,
					'Vitórias': nVitorias,
					'Empates': nEmpates,
					'Derrotas': nDerrotas,
					'Gols Feitos': nGolsFeitos,
					'Gols Sofridos': nGolsSofridos,
					'Pontos': nPontos})

#df.to_csv('resultadosBrasileirao.csv',index=False,header=True) #Salva o arquivo em .csv sem Index(Indice da lista);
df.to_excel('resultadosBrasileirao.xlsx',index=False,header=True)
print(df)	