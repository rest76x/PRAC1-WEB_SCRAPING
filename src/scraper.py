#!/usr/bin/env python
# coding: utf-8

import urllib.request
import urllib.error
import time
import re
from bs4 import BeautifulSoup
from datetime import date
DELAY=10

class ACO_Scraper():
    lastDownloadTime=0
    #Inicialitzar el web scraper
    def __init__(self):
        self.url="https://www.aco.es"
        self.subdomain="/es/producto"
        self.data=[]
    
    #descarregar la pagina web i retornar error si no pot
    def __download_html(self,url):
        #print ('Downloading:',url)
        currentTime=time.time()
        currentdelay=(currentTime-self.lastDownloadTime)*1000
        if(currentdelay<DELAY):
            sleep(DELAY-currentdelay)
        self.lastDownloadTime=currentTime
        try:
            html = urllib.request.urlopen(url).read()
        except urllib.error.URLError as e:
            print ('Download error:',e.reason)
            html=None
        return html
    
    #Buscar tots els productes
    def __get_families_links(self,url):
        #navegar per les families fins a les taules
        html=self.__download_html(url)
        if(html is None):
            return None
        bs=BeautifulSoup(html,"html.parser")
        #Buscar families, si no, som a la pagina principal
        page = bs.find("div",class_="view-pagefamilia-block2")
        if(page is None):
            #Mirar si es pagina principal
            page = bs.find("div",class_="view-id-home_familias")
        if(page is not None):    
            families = page.findAll("div",class_="views-field-name")
            for familia in families:
                link=familia.find("a",href=True)["href"]
                self.__get_families_links(self.url+link) 
        #Buscar taules
        self.__get_product_link(bs)
        return True
    
    def __get_product_link(self,bs):
        #Trobar el link a les pagines dels productes de les taules
        #buscar productes
        filas = bs.findAll("div",class_="aco-lista-productos-titulo")
        if filas is not None:
            for fila in filas:
                #Buscar link a la página del producte
                link = fila.find("a",href=True)["href"]
                self.__get_product_info(self.url+link) 
            #comprovar si hi ha més pagines i anar a la seguent
            pages =bs.find("ul",class_="pagination")
            llista=[]
            if(pages is not None):
                pages=pages.find("li",class_="next")
                if(pages is not None):
                    #Hi ha página seguent
                    html=self.__download_html(self.url+pages.find("a",href=True)["href"])
                    if(html is None):
                        return None
                    bs=BeautifulSoup(html,"html.parser")
                    self.__get_product_link(bs)   
        return True
    
    def __get_product_info(self,url):
        #agafar la info de les families
        html=self.__download_html(url)
        if(html is None):
            return None
        bs=BeautifulSoup(html,"html.parser")
        #buscar productes
        info=[None]*6
        campos=bs.find("div",class_="product-code")
        if(campos is not None):
            info[0]=date.today().strftime('%Y/%m/%d')
            info[1]='"'+bs.find("div",class_="product-code").text.split()[1]+'"'
            info[2] = '"'+bs.find("div",class_="field-name-field-product-preciopvp").find("div",class_="field-item even").text+'"'
            campos=bs.find("div",id="field_product_encabezados").findAll(['h1','h2','h3'])
            for campo in campos:
                if campo.name=='h1':
                    info[3]='"'+campo.text+'"'
                elif campo.name=='h2':
                    info[4]='"'+campo.text+'"'
                else:
                    info[5]='"'+campo.text+'"'
            if(len(self.data)==0):
                #Posar els noms de les dades
                self.data.append(["Date","Code","PVP","Description1","Description2","Type"])
            self.data.append(info)
        return True
    
    def data2csv(self,filename):
        #Crear arxiu si no existeix
        file = open("../csv/" + filename, "w+")
        #Ficar tota la informació
        for row in range(len(self.data)):
            for value in range(len(self.data[row])):
                file.write(self.data[row][value]+";");
            file.write("\n");
        
    #Scrapper
    def scrape(self):
        print ("Startig info scrapping from " + "'"+self.url+"'...")
        #el proces pot tardar aproximadament 1h i mitja
        #começar el temps
        time_start=time.time()
        #Trobar els links dels productes
        self.__get_families_links(self.url+self.subdomain)
        #temps final
        time_end=time.time()
        print ("\nelapsed time: " + str(round(((time_end - time_start) / 60) , 2)) + " minutes")
            






