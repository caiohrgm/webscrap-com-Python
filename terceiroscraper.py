import requests #FAz o requisito dos dados
import bs4 #Biblioteca do BeautifulSoup #Faz a análise das informações

response = requests.get("https://evaldowolkers.wordpress.com/")
soup = bs4.BeautifulSoup(response.text, "html.parser")

print(soup.find_all('title'))
