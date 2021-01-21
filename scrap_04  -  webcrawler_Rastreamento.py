#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 17:39:37 2020

Pg. 60 - Web Scraping com python, Capítulo 3

@author: Caio Medeiros
"""
from urllib import urlopen
from bs4 import BeautifulSoup
import re


pages = set()
#Função GetLinks (pega todos os links dentro de um link):
def getLinks(pageUrl):
    global pages
    html = urlopen ('http://en.wikipedia.org{}'.format(pageUrl))
    bs = BeautifulSoup(html,'html.parser')
    
    for link in bs.find_all('a',href = re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages: # verifica se o link encontrado não está no conjunto;
                # Encontramnos uma página nova;
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks('')