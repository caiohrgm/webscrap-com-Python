#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on ter Jan  21 10:40:23 2020

Pg. 60 - Web Scraping com python, Capítulo 3

@author: Caio Medeiros
"""
from urllib import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
#Função GetLinks (pega todos os links dentro de um link):

def getLinks(pageUrl):
    global pages # Conjunto, sem tamanho definido;
    html = urlopen ('http://en.wikipedia.org{}'.format(pageUrl))
    bs = BeautifulSoup(html,'html.parser')

    try:
        print(bs.h1.get_text()) # Vai tentar printar o header 1, se existe;
        print(bs.find(id = 'mw-content-text').find_all('p')[0]) # vai tentar printar o conteudo, se existir;
        print(bs.find(id = 'ca-edit').find('span').find('a').attrs['href']) # vai tentar printar o botão editar, se existir;
    except: # Ao não especificar o tipo de erro, a mensagem irá aparecer para qualquer erro encontrado, e irá continuar o programa;
        print('This page is missing something! Continuing.')


    
    for link in bs.find_all('a',href = re.compile('^(/wiki/)')): # Encontra os links com /wiki/ no começo do texto ("^");
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages: # verifica se o link encontrado não está no conjunto;
                # Encontramos uma página nova;
                newPage = link.attrs['href']
                print('-'*20)
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks('')