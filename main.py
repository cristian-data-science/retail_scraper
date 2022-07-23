import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from funciones.func import funciones_globales

#import sys
#sys.path.append("variables")
from variables import var as v

class base_test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= r'C:\chrome_driver\chromedriver.exe')
        # driver=webdriver.Firefox(executable_path="C:\Drivers\geckodriver.exe")
        driver = self.driver
        # este implicity contrala el time out de la función scann multipaginas
        driver.implicitly_wait(5)
        driver.maximize_window()
        #driver.get("https://patagonia-testpos.sandbox.operations.dynamics.com/")        

    def test1(self):
        driver = self.driver
        f = funciones_globales(driver)
        f.scann(v.url_north_h)
        f.scann(v.url_north_m)
        f.scann(v.url_north_n)
        f.scann(v.url_north_e)



    def tearDown(self):
        driver = self.driver
        driver.close()
        

if __name__ == '__main__':
    unittest.main()
