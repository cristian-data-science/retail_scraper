import time
import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

import sys
sys.path.append("variables")
from variables import var as v


class funciones_globales():
    
    def __init__(self, driver):
        self.driver = driver

    def scann(self, url_north_h):
        self.driver.get(url_north_h)
        driver = self.driver
        vermas = driver.find_element(By.CLASS_NAME, value = 'category-loadMore-yau')
        sleep(1)
        vermas.click()
        sleep(1)
        disable_nextb = driver.find_element(By.CLASS_NAME, value='navButton-icon-yS-')
        val = disable_nextb.get_attribute("class")
        # iteramos todas las paginas hasta que llegamos al final de las opciones con el atributo "disabled" del tagg button next
        vuelta = 2
        x = 0
        while val == "navButton-icon-yS-" or val == "navButton-icon-yS-":

            
            
            next_button = driver.find_elements(By.CLASS_NAME, value='navButton-icon-yS-')
            #print(next_button[1])
            #print(next_button[1])
            next_button[x].click()
            sleep(1)

            print("justo antes del if ver mas")
           
            try:
                if WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CLASS_NAME, "category-loadMore-yau"))):
                    print("ver mas existe")
                    vermas = driver.find_element(By.CLASS_NAME, value = 'category-loadMore-yau')
                    vermas.click()
                    print(vuelta)
                    vuelta = vuelta + 1
                    disable_nextb = driver.find_element(By.CLASS_NAME, value='navButton-icon-yS-')
                    val = disable_nextb.get_attribute("class")
                    print(val)
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
                print("TimeOut!!!!")