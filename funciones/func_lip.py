import time
import unittest
from datetime import date
from time import sleep

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
    def scann(self, url_lip_h):
        self.driver.get(url_lip_h)
        driver = self.driver

        #disable_nextb = driver.find_element(By.CLASS_NAME, value='navButton-icon-yS-')
       # val = disable_nextb.get_attribute("class")


        # iteramos todas las páginas hasta que llegamos al final de las opciones con el atributo "disabled" del tagg button next
        # En cada vuelta se recolectan los datos
        sleep(1)
        driver.execute_script("window.scrollTo(0, 3000)") 

        #next_button_value = driver.find_element(By.CLASS_NAME, value= 'arrow-paginador-right')
        #print(next_button_value.text)
        pagina = 1
        #name_df = []
        df_final = pd.DataFrame(columns=['nombre producto', 'precio', 'link'])
        
        val = "right"
        while val == "right" :
            #print(next_button_value.text)

            print(f"############ Pagina {pagina} ###############")
            name_product = driver.find_elements(By.XPATH, value= '//*[@id="plp_products_init"]/div[2]/ol/li[*]/div/div[1]/strong/a')
            name_list = [name.text for name in name_product]
            #print(name_list)

            price_product = driver.find_elements(By.XPATH, value = '//*[@data-price-type="finalPrice"]/span')
            price_list = [price.text for price in price_product]
            #print(price_list)

            link_product = driver.find_elements(By.XPATH, value= '//*[@id="plp_products_init"]/div[2]/ol/li[*]/div/a')
            link_list = [link.get_attribute("href") for link in link_product]
            #print(link_list)
            

            df = pd.DataFrame(list(zip(name_list, price_list, link_list)), columns=['nombre producto', 'precio', 'link'])
            df_final = df_final.append(df)
            if url_lip_h == 'https://www.lippioutdoor.com/hombres.html':
                cat = "hombre"
            if url_lip_h == 'https://www.lippioutdoor.com/mujeres.html':
                cat = "mujer" 
            if url_lip_h == 'https://www.lippioutdoor.com/kids.html':
                cat = "niño" 
            if url_lip_h == 'https://www.lippioutdoor.com/equipamiento.html':
                cat = "equipamiento"    
            
            df_final =df_final.assign(categoria = cat)

            today = date.today()
            df_final =df_final.assign(fecha = date.today())

            df_final = df_final.reset_index(drop=True)
          
            print(df_final) 








            try:
                next_button_value = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#plp_products_init > div:nth-child(5) > div.pages > ul > li.item.pages-item-next > a")))
                next_button_value.click()
                pagina = pagina + 1
                sleep(2)
                driver.execute_script("window.scrollTo(0, 3000)")

            except TimeoutException as ex:
                print(ex.msg)
                print("TimeOut")
                val = "notright"
                sleep(2)
                print("saliendo del while")
            
        df_final.to_csv(f"./resultados/lippi/{cat}.csv",index = False, encoding= "utf-8")        
            

    def clean_data(self):
        
        df_hombre = pd.read_csv("./resultados/lippi/hombre.csv",encoding="utf-8")
        df_equipamiento = pd.read_csv("./resultados/lippi/equipamiento.csv",encoding="utf-8")
        df_mujer = pd.read_csv("./resultados/lippi/mujer.csv",encoding="utf-8")
        df_niño = pd.read_csv("./resultados/lippi/niño.csv",encoding="utf-8")
        

        final = df_hombre.append(df_mujer, ignore_index=True).append(df_niño, ignore_index=True).append(df_equipamiento, ignore_index=True)
        #final = final.reset_index()
        final.to_excel("./resultados/lippi/lippi_final.xlsx", index = False)    









"""
            driver.execute_script("window.scrollTo(0, 2700)")
            sleep(1) 
            driver.execute_script("window.scrollTo(0, 4800)")
           #sleep(1) 


            try:
                close_popup = next_button_value = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="leadinModal-3135968"]/div[2]/button')))
                close_popup.click()
                print("cerrando popup")
                sleep(2)
                
            except TimeoutException as ex:
                    print(ex.msg)
                    print("No hay popup")

            name_product = driver.find_elements(By.XPATH, value= '/html/body/div[3]/div/div[1]/div/div[4]/div/div[2]/section/div[2]/div/div[5]/div/div[2]/div/div[2]/div/div/div/div[3]/div[*]/section/a/article/div[3]/h3/span')
            name_list = [name.text for name in name_product]
            price_product = driver.find_elements(By.XPATH, value = '/html/body/div[3]/div/div[1]/div/div[4]/div/div[2]/section/div[2]/div/div[5]/div/div[2]/div/div[2]/div/div/div/div[3]/div[*]/section/a/article/div[6]/div/div[2]/span/span/span')
            price_list = [price.text for price in price_product]
            link_product = driver.find_elements(By.XPATH, value= '/html/body/div[3]/div/div[1]/div/div[4]/div/div[2]/section/div[2]/div/div[5]/div/div[2]/div/div[2]/div/div/div/div[3]/div[*]/section/a')
            link_list = [link.get_attribute("href") for link in link_product]
            

            df = pd.DataFrame(list(zip(name_list, price_list, link_list)), columns=['nombre producto', 'precio', 'link'])
            df_final = df_final.append(df)
            if url_col_h == 'https://www.columbiachile.cl/Hombre':
                cat = "hombre"
            if url_col_h == 'https://www.columbiachile.cl/mujer':
                cat = "mujer" 
            if url_col_h == 'https://www.columbiachile.cl/155?map=productClusterIds':
                cat = "footwear" 
            if url_col_h == 'https://www.columbiachile.cl/ninos':
                cat = "niño"    
            
            df_final =df_final.assign(categoria = cat)

            today = date.today()
            df_final =df_final.assign(fecha = date.today())

            df_final = df_final.reset_index(drop=True)
            print(f"################################# Pagina: {pagina}#########################################")
            print(df_final)
            
                    
            try:
                next_button_value = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CLASS_NAME, "arrow-paginador-right")))
                next_button_value.click()
                pagina = pagina + 1
                sleep(3)

            except TimeoutException as ex:
                print(ex.msg)
                print("TimeOut")
                val = "notright"
                sleep(2)
                print("saliendo del while")

        df_final.to_csv(f"./resultados/columbia/{cat}.csv",index = False, encoding= "utf-8")    
            
            
    def clean_data(self):
        
        df_hombre = pd.read_csv("./resultados/columbia/hombre.csv",encoding="utf-8")
        df_footwear = pd.read_csv("./resultados/columbia/footwear.csv",encoding="utf-8")
        df_mujer = pd.read_csv("./resultados/columbia/mujer.csv",encoding="utf-8")
        df_niño = pd.read_csv("./resultados/columbia/niño.csv",encoding="utf-8")
        

        final = df_hombre.append(df_mujer, ignore_index=True).append(df_niño, ignore_index=True).append(df_footwear, ignore_index=True)
        #final = final.reset_index()
        final.to_excel("./resultados/columbia/columbia_final.xlsx", index = False)

        """