import selenium
import unittest
import os
import pathlib  
import selenium
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse, resolve
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)
# from selenium.webdriver.common.keys import Keys
import time

# Setup
#driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")

#Functiona Testing with Selenium  

class Test_functional(StaticLiveServerTestCase):
  def setUp(self):
    driver.get(self.live_server_url)


  @classmethod
  def tearDownClass(self):
    print("tests end")
    time.sleep(2)
    driver.close()

 
  def test_url_login(self):
    driver.get(self.live_server_url)
    driver.find_element_by_id("Login_awy").click()
    current = self.live_server_url + reverse("login")
    self.assertEqual(driver.current_url,current)