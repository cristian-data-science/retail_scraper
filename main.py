import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from funciones.func_north import funciones_globales
from selenium.webdriver.chrome.options import Options
import pandas as pd

#import sys
#sys.path.append("variables")
from variables import var as v

chrome_options = Options()
#chrome_options.headless = True
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--allow-running-insecure-content')
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--proxy-server='direct://'")
chrome_options.add_argument("--proxy-bypass-list=*")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--no-sandbox')


class base_test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= r'C:\chrome_driver\chromedriver.exe',options=chrome_options)
        # driver=webdriver.Firefox(executable_path="C:\Drivers\geckodriver.exe")
        driver = self.driver
        # este implicity contrala el time out de la función scann multipaginas
        driver.implicitly_wait(7)
        driver.maximize_window()
        #driver.get("https://patagonia-testpos.sandbox.operations.dynamics.com/")        

    def test1(self):
        driver = self.driver
        f = funciones_globales(driver)
        f.scann(v.url_north_h)
        f.scann(v.url_north_m)
        f.scann(v.url_north_n)
        f.scann(v.url_north_e)

    def test2(self):  
        driver = self.driver
        f = funciones_globales(driver)  
        f.clean_data()



    def tearDown(self):
        driver = self.driver
        driver.close()
        

if __name__ == '__main__':
    unittest.main()
