#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 10:57:33 2019

@author: caiom
"""
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from selenium import webdriver
from selenium.webdriver import Geckodriver



my_url = "https://www.resultados.com/futebol/brasil/serie-a/classificacao/"

web_r = uReq(my_url)

driver = webdriver.Chrome(executable_path=r"/home/caiom/anaconda3/pkgs/geckodriver-0.24.0-hf484d3e_1/bin/geckodriver.bin")
driver.get(my_url)
souppage_soup = soup(web_r,'html.parser')
html = driver.execute_script("return document.documentElement.outerHTML")

#print

html_page_soup = soup(html,"html.parser")
container = html_page_soup.findAll("div",{"class":"table__row"})
len(container)



