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
        sleep(2)
        vermas.click()
        sleep(2)

        disable_nextb = driver.find_element(By.XPATH, value='//*[@id="root"]/main/div/article/div[3]/div/div[4]/div/button[7]/span')
        val = disable_nextb.get_attribute("class")
        print("###################### this ###############################")
        print(val)
        print("###################### thos ###############################")

        # iteramos todas las paginas hasta que llegamos al final de las opciones con el atributo "disabled" del tagg button next

        while val == "navButton-icon-yS-":
            next_button = driver.find_element(By.XPATH, value='//*[@id="root"]/main/div/article/div[3]/div/div[4]/div/button[7]')
            next_button.click()
            sleep(1)
            vermas = driver.find_element(By.CLASS_NAME, value = 'category-loadMore-yau')
            vermas.click()
            sleep(1)
            

            
            
            

#navButton-icon_disabled-UGx

        sleep(10)
