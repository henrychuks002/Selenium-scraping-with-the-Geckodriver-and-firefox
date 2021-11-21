#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 11:35:00 2021

@author: bluearc
"""
import time
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import ElementNotInteractableException


opt = Options()
opt.add_argument("--headless")

driver = webdriver.Firefox(executable_path=GeckoDriverManager(cache_valid_range=1).install(), options=opt) 
driver.maximize_window()

driver.get("https://www.konga.com/")
driver.implicitly_wait(40)
time.sleep(5)

try:
# =============================================================================
#     element = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/section/div[4]/section/main/section[3]/div/svg'))
#         )
#     driver.execute_script("arguments[0].clicks()", element)
#     #print("x out successful")
# =============================================================================
    
    element = WebDriverWait(driver, 180).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="NC_CLOSE_ICON"]'))
        )
    driver.execute_script("arguments[0].click()", element)
    print("x out successful")
except ElementNotInteractableException as e:
   print(e)

driver.find_element(By.XPATH, '//input[@id="jsSearchInput"]').send_keys("samsung phones")
driver.find_element(By.XPATH, "/html/body/div[1]/div/section/div[2]/nav/div[2]/div/div/div[2]/div/form/button").click()

driver.find_element(By.XPATH, "/html/body/div[1]/div/section/div[3]/section/main/section[2]/section/section/section[2]/section/ul/li[1]/div/div").click()

#testing table info collection
descriptionList = []

description = driver.find_element(By.XPATH, "//*[@id='mainContent']/div/div[2]/div[3]/div[2]/div[2]/div[2]/div")

descriptionList = descriptionList.append(description.text)
print(descriptionList)
