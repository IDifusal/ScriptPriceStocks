import bs4
import requests
from bs4 import BeautifulSoup

#Buscar precio accion Coca Cola
yahoo = requests.get('https://finance.yahoo.com/quote/KO')
soup = bs4.BeautifulSoup(yahoo.text,'html.parser')
actualpriceKO=soup.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
print ("El precio de KO es ->", actualpriceKO)
#Buscar precio accion Facebook
yahoo = requests.get('https://finance.yahoo.com/quote/FB')
soup = bs4.BeautifulSoup(yahoo.text,'html.parser')
actualpricefb=soup.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text

#Buscar precio accion Buen Ventura
yahoo = requests.get('https://finance.yahoo.com/quote/BVN')
soup = bs4.BeautifulSoup(yahoo.text,'html.parser')
actualpriceBVN=soup.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text

#buscar precio de Twitter
yahoo = requests.get('https://finance.yahoo.com/quote/TWTR')
soup = bs4.BeautifulSoup(yahoo.text,'html.parser')
actualpriceTWTR=soup.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text

#Buscar precio de Exxon
yahoo = requests.get('https://finance.yahoo.com/quote/XOM')
soup = bs4.BeautifulSoup(yahoo.text,'html.parser')
actualpricexom=soup.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text

#Buscar precio de BHF
yahoo = requests.get('https://finance.yahoo.com/quote/BHF')
soup = bs4.BeautifulSoup(yahoo.text,'html.parser')
actualpricehfb=soup.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text


#Imprimiendo todos los precios
print("Elprecio actual de KO es ->", actualpriceKO)
print("Elprecio actual de FB es ->", actualpricefb)
print("Elprecio actual de BVN es ->", actualpriceBVN)
print("Elprecio actual de TWTR es ->", actualpriceTWTR)
print("Elprecio actual de XOM es ->", actualpricexom)
print("Elprecio actual de HFB es ->", actualpricehfb)