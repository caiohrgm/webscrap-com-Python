#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 15:35:41 2020

@author: caiom
"""

from urllib import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now()) # Define a seed para o gerador de numeros 
#aleatorios a partir do horário atual do sistema

#Função GetLinks (pega todos os links dentro de um link):
def getLinks(articleUrl):
    html = urlopen ('http://en.wikipedia.org{}'.format(articleUrl))
    bs = BeautifulSoup(html,'html.parser')
    
    return bs.find('div',{'id':'bodyContent'}).find_all('a',href=re.compile ('^(/wiki/)((?!:).)*$'))
    
links = getLinks('/wiki/Kevin_Bacon') 
count = 0 #adapação.Original: "len(links) > 0"
while count < 6:
    newArticle = links[random.randint(0,len(links)-1)].attrs['href'] # Encontra uma tag de link aleatória e extrai o atributo href dela
    print(newArticle)
    links = getLinks(newArticle)
    count+=1