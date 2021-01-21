#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on ter Jan  21 12:11:13 2020

Pg. 64- Web Scraping com python, Capítulo 3

@author: Caio Medeiros
"""
from urllib import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())

#F Obtém uma lista de todos os links internos encontrados em uma página:
def getInternalLinks(bs,includeUrl):
    
    includeURL = '{}://{}'.format(urlparse(includeURL).scheme,urlparse(includeURL).netloc);
    internalLinks = []

    # Encontra todos os links que começam com "/"
    
    for link in bs.find_all('a',href = re.compile('^(/|.*'+includeURL+')')): # Encontra os links com /wiki/ no começo do texto ("^");
        if 'href' is not None:
            if link.attrs['href'] not in internalLinks: # verifica se o link encontrado não está no conjunto;
                if (link.attrs['href'].startwith('/')):
                    internalLinks.append(includeURL+link.attrs['href'])
    return internalLinks

getInternalLinks(bs,'http://igniteshow.com/')