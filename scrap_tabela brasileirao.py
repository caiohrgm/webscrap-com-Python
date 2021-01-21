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

display = Display(visible=0, size=(800, 800))
display.start()

my_url = "https://www.resultados.com/futebol/brasil/serie-a/classificacao/"
web_r = uReq(my_url)

driver = webdriver.Chrome(executable_path="/home/caiom/Downloads/chromedriver_linux64 (1)/chromedriver")
driver.get(my_url)

souppage_soup = soup(web_r,'html.parser')
html = driver.execute_script("return document.documentElement.outerHTML") # pequisar


html_page_soup = soup(html,"html.parser")
container = html_page_soup.findAll("div",{"class":"table__row"})

times = []

# Pega Classificação:
for position in html_page_soup.find_all("div",{"class":"table__cell table__cell--rank table__cell--col_rank table__cell--no table__cell--q1 cell--sorted"}):
	time = []
	txt = soup.get_text(position)
	text = txt.strip("\n")
	text2 = text.strip(".")
	time.append(text2)
	times.append(time)
for position in html_page_soup.find_all("div",{"class":"table__cell table__cell--rank table__cell--col_rank table__cell--no table__cell--q2 cell--sorted"}):
	time = []
	txt = soup.get_text(position)
	text = txt.strip("\n")
	text2 = text.strip(".")
	time.append(text2)
	times.append(time)
for position in html_page_soup.find_all("div",{"class":"table__cell table__cell--rank table__cell--col_rank table__cell--no table__cell--q3 cell--sorted"}):
	time = []
	txt = soup.get_text(position)
	text = txt.strip("\n")
	text2 = text.strip(".")
	time.append(text2)
	times.append(time)
for position in html_page_soup.find_all("div",{"class":"table__cell table__cell--rank table__cell--col_rank table__cell--no table__cell-- cell--sorted"}):
	time = []
	txt = soup.get_text(position)
	text = txt.strip("\n")
	text2 = text.strip(".")
	time.append(text2)
	times.append(time)
for position in html_page_soup.find_all("div",{"class":"table__cell table__cell--rank table__cell--col_rank table__cell--no table__cell--r1 cell--sorted"}):
	time = []
	txt = soup.get_text(position)
	text = txt.strip("\n")
	text2 = text.strip(".")
	time.append(text2)
	times.append(time)

# Pega Nomes:
count = 0
for nome in html_page_soup.find_all("span",{"class":"team_name_span"}):
	txt = soup.get_text(nome)
	text = txt.strip("\n")
	times[count].append(text)
	count = count + 1

# Pega Nº de Jogos:
count = 0
for jogos in html_page_soup.find_all("div",{"class":"table__cell table__cell--matches_played table__cell--col_matches_played"}):
	txt = soup.get_text(jogos)
	text = txt.strip("\n")
	times[count].append(text)
	count = count + 1

# Pega Nº de Vitórias:
count = 0
for vitorias in html_page_soup.find_all("div",{"class":"table__cell table__cell--wins_regular table__cell--col_wins_regular"}):
	txt = soup.get_text(vitorias)
	text = txt.strip("\n")
	times[count].append(text)
	count = count + 1

# Pega Nº de Empates:
count = 0
for empates in html_page_soup.find_all("div",{"class":"table__cell table__cell--draws table__cell--col_draws"}):
	txt = soup.get_text(empates)
	text = txt.strip("\n")
	times[count].append(text)
	count = count + 1

# Pega Nº de Derrotas:
count = 0
for derrotas in html_page_soup.find_all("div",{"class":"table__cell table__cell--losses_regular table__cell--col_losses_regular"}):
	txt = soup.get_text(derrotas)
	text = txt.strip("\n")
	times[count].append(text)
	count = count + 1

# Pega Nº de Gols:
count = 0
for gols in html_page_soup.find_all("div",{"class":"table__cell table__cell--goals table__cell--col_goals"}):
	txt = soup.get_text(gols)
	text = txt.strip("\n")
	times[count].append(text)
	count = count + 1

# Pega Nº de Pontos:
count = 0
for pontos in html_page_soup.find_all("div",{"class":"table__cell table__cell--points table__cell--col_points"}):
	txt = soup.get_text(pontos)
	text = txt.strip("\n")
	times[count].append(text)
	count = count + 1

# Imprime a lista de times:
for time in times:
	print("NOME: " + time[1] + "\n - Classificação:" + time[0] + "\n - Número de Jogos:" + time[2] + 
		"\n - Número de Vitórias:" + time[3] + "\n - Número de Empates:" + time[4] + "\n - Número de Derrotas:" + time[5] + 
		"\n - Número de Gols:" + time[6] + "\n - Pontos:" + time[7] + "\n")
	
#print(container)
