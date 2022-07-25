import time
import unittest
from time import sleep

from datetime import date

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
import pandas as pd

import sys
sys.path.append("variables")
from variables import var as v


class funciones_globales():
    
    def __init__(self, driver):
        self.driver = driver

    
    # Función para escanear y recolectar nombre, precio, y link de producto. antes de entrar al while la función clickea en "ver más" y cuando entra al while comienza a recolectar y a saltar pagina
    # La recolección de la ultima pagina se genera dentro del except y tambien cambia el valor de val por el atributo de la ultima hoja para que no entre nuevamente a la iteración
    def scann(self, url_north_h):
        self.driver.get(url_north_h)
        driver = self.driver
        vermas = driver.find_element(By.CLASS_NAME, value = 'category-loadMore-yau')
        sleep(1)
        vermas.click()
        sleep(1)
        disable_nextb = driver.find_element(By.CLASS_NAME, value='navButton-icon-yS-')
        val = disable_nextb.get_attribute("class")


        # iteramos todas las páginas hasta que llegamos al final de las opciones con el atributo "disabled" del tagg button next
        # En cada vuelta se recolectan los datos
        vuelta = 2
        x = 0
        name_product = []
        df_final = pd.DataFrame(columns=['nombre producto', 'precio', 'link'])
        #df = pd.DataFrame(columns=['Nombre producto', 'precio', 'link'])
        while val == "navButton-icon-yS-" or val == "navButton-icon-yS-":
            # Comienza la recolección por vuelta    
            name_product = driver.find_elements(By.XPATH, value= '//*[@id="root"]/main/div/article/div[3]/div/section/div/div/div[*]/div[3]/a/span')                        
            name_product = [name.text for name in name_product]
            #print(name_product)
            price_product = driver.find_elements(By.XPATH, value= '//*[@id="root"]/main/div/article/div[3]/div/section/div/div/div[*]/div[3]/div/div/div[1]/div')
            price_product = [price.text for price in price_product]
            #print(price_product)
            link_product = driver.find_elements(By.XPATH, value= '//*[@id="root"]/main/div/article/div[3]/div/section/div/div/div[*]/div[2]/div/a')
            link_product = [link.get_attribute("href") for link in link_product]
            #print(link_product)

            df = pd.DataFrame(list(zip(name_product, price_product, link_product)), columns=['nombre producto', 'precio', 'link'])
            
            df_final = df_final.append(df)

            if url_north_h == 'https://www.thenorthface.cl/hombre?page=1':
                cat = "hombre"
            if url_north_h == 'https://www.thenorthface.cl/mujer?page=1':
                cat = "mujer" 
            if url_north_h == 'https://www.thenorthface.cl/equipamiento?page=1':
                cat = "equipamiento" 
            if url_north_h == 'https://www.thenorthface.cl/ni-os?page=1':
                cat = "niño"    


            df_final =df_final.assign(categoria = cat)
            print(url_north_h)
            df_final = df_final.reset_index(drop=True)
            print(df_final)

            #for name in name_product:
                #print(name.text)

            # logica para clickear pagina siguiente. tanto adelante como  atras comparten el mismo atributo en su clase por eso se crea una lista
            # en la primera vuelta x vale 0 porque solo esta habiliatdo el "siguiente" en la segunda vuelta y demases se activa el "atras" y el "siguiente"

            next_button = driver.find_elements(By.CLASS_NAME, value='navButton-icon-yS-')
            next_button[x].click()
            sleep(1)

            #print("justo antes del if ver mas")
           
            try:
                if WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CLASS_NAME, "category-loadMore-yau"))):
                    #print("ver mas existe")
                    vermas = driver.find_element(By.CLASS_NAME, value = 'category-loadMore-yau')
                    vermas.click()
                    # bajar el scroll
                    driver.execute_script("window.scrollTo(0, 4500)") 
                    #print(vuelta)
                    vuelta = vuelta + 1
                    disable_nextb = driver.find_element(By.CLASS_NAME, value='navButton-icon-yS-')
                    val = disable_nextb.get_attribute("class")
                    #print(val)
                    x = 1

                else:
                    print("else activado")
                    
                    next_button = driver.find_element(By.XPATH, value='//*[@id="root"]/main/div/article/div[3]/div/div[4]/div/button[7]')
                    next_button.click()
                    sleep(1)
                    
            except TimeoutException as ex:
                print(ex.msg)
                disable_nextb = driver.find_element(By.CLASS_NAME, value='navButton-icon_disabled-UGx')
                val = disable_nextb.get_attribute("class")
                
                # Recolección de la ultima página y salida del bucle while
                name_product = driver.find_elements(By.XPATH, value= '//*[@id="root"]/main/div/article/div[3]/div/section/div/div/div[*]/div[3]/a/span')                        
                name_product = [name.text for name in name_product]
                #print(name_product)
                price_product = driver.find_elements(By.XPATH, value= '//*[@id="root"]/main/div/article/div[3]/div/section/div/div/div[*]/div[3]/div/div/div[1]/div')
                price_product = [price.text for price in price_product]
                #print(price_product)
                link_product = driver.find_elements(By.XPATH, value= '//*[@id="root"]/main/div/article/div[3]/div/section/div/div/div[*]/div[2]/div/a')
                link_product = [link.get_attribute("href") for link in link_product]
                #print(link_product)

                # append de la ultima vuelta/pagina por time out. "ver mas" no encontrado
                df = pd.DataFrame(list(zip(name_product, price_product, link_product)), columns=['nombre producto', 'precio', 'link'])

                df_final = df_final.append(df)

                if url_north_h == 'https://www.thenorthface.cl/hombre?page=1':
                    cat = "hombre"
                if url_north_h == 'https://www.thenorthface.cl/mujer?page=1':
                    cat = "mujer" 
                if url_north_h == 'https://www.thenorthface.cl/equipamiento?page=1':
                    cat = "equipamiento" 
                if url_north_h == 'https://www.thenorthface.cl/ni-os?page=1':
                    cat = "niño"    


                df_final =df_final.assign(categoria = cat)
                print(url_north_h)

                today = date.today()
                df_final =df_final.assign(fecha = date.today())

                df_final = df_final.reset_index(drop=True)
                print(df_final)


                #print(vuelta)    
                print("TimeOut!!!!")
        
        df_final.to_csv(f"./resultados/northface/{cat}.csv",index = False)

    def clean_data(self):
        
        df_hombre = pd.read_csv("./resultados/northface/hombre.csv",encoding="utf-8")
        df_equipamiento = pd.read_csv("./resultados/northface/equipamiento.csv",encoding="utf-8")
        df_mujer = pd.read_csv("./resultados/northface/mujer.csv",encoding="utf-8")
        df_niño = pd.read_csv("./resultados/northface/niño.csv",encoding="utf-8")
        

        final = df_hombre.append(df_mujer, ignore_index=True).append(df_niño, ignore_index=True).append(df_equipamiento, ignore_index=True)
        #final = final.reset_index()
        final.to_excel("./resultados/northface/northface_final.xlsx", index = False)