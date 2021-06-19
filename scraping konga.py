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


opt = Options()
opt.add_argument("--headless")

driver = webdriver.Firefox(executable_path=GeckoDriverManager(cache_valid_range=1).install(), options=opt)
driver.maximize_window()

driver.get("https://www.konga.com/")
driver.implicitly_wait(40)
time.sleep(5)
driver.find_element(By.XPATH, '//input[@id="jsSearchInput"]').send_keys("samsung phones")
driver.find_element(By.XPATH, "/html/body/div[1]/div/section/div[2]/nav/div[2]/div/div/div[2]/div/form/button").click()

driver.find_element(By.XPATH, "/html/body/div[1]/div/section/div[3]/section/main/section[2]/section/section/section[2]/section/ul/li[1]/div/div").click()

#testing table info collection
descriptionList = []

description = driver.find_element(By.XPATH, "//*[@id='mainContent']/div/div[2]/div[3]/div[2]/div[2]/div[2]/div")

descriptionList = descriptionList.append(description.text)
print(descriptionList)
