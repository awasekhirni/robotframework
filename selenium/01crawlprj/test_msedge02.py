"""
 Copyright 2021 Awase Khirni Syed awase008@gmail.com 
 Elain Technologies Inc Canada.
 awasekhirni@gmail.com 
 ORIGINAL WORKING CODE PREPARED FOR ALPHAFACTORY BOOTCAMP 

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

      https://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 """
from selenium.webdriver.opera.options import Options 
from selenium.webdriver.chrome.options import Options as ChromeOptions 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from selenium import webdriver 
import time 
import unittest 

class MSEdgeTest(unittest.TestCase):
    def setUp(self):
        self.msdriver=webdriver.Edge(r"E:\\awase-harddisk\\CT\\Selenium\\PythonSelenium\\Selenium\\01crawldemo\\01crawlprj\\drivers\\msedgedriver.exe")
        self.msdriver.maximize_window()
        
        time.sleep(5)

    
    def test_CitiesUrl(self):
        edgeBrowser = self.msdriver
        edgeBrowser.get('https://www.areavibes.com/bc/')
        cities= edgeBrowser.find_elements_by_tag_name("a")
        
        for city in cities:
            print(city.text)
        
        print("no of records in arealinks:"+ str(len(cities)))

    
    def test_Headings(self):
        edgeBrowser = self.msdriver
        edgeBrowser.get('https://www.areavibes.com/bc/')
        hsets= edgeBrowser.find_elements_by_class_name("columnize-container")
        for h in hsets:
            print(h.text)


    def test_FetchUrl(self):
        edgeBrowser = self.msdriver
        edgeBrowser.get('https://www.areavibes.com/bc/')
        links = edgeBrowser.find_elements_by_xpath('.//a')

        for link in links:
            print(link.get_attribute('href'))


    def tearDown(self):
        self.msdriver.close()


if __name__ =='__main__':
    MSEdgeTest()
