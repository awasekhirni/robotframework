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

from selenium.webdriver import Firefox 
from selenium.webdriver.firefox.options import Options as FoxOptions
from selenium import webdriver 
import time 
import unittest
from selenium.webdriver.support.ui import Select

class FoxScrapeTest(unittest.TestCase):

    def setUp(self):
        foxOpts = FoxOptions()
        foxOpts.add_argument("--headless")
        #assert foxOpts.headless # operating in headless mode
        foxcaps = webdriver.DesiredCapabilities().FIREFOX
        foxcaps["marionette"] = True
        self.foxdriver = webdriver.Firefox(firefox_options=foxOpts,capabilities=foxcaps, executable_path="E:\\awase-harddisk\\CT\\Selenium\\PythonSelenium\\Selenium\\01crawldemo\\01crawlprj\\drivers\\geckodriver.exe")
        time.sleep(3)
        

    def test_FetchDemographics_By_ZipCode(self):
        pageUrl='https://zipwho.com/?zip=&city=&filters=--_--_--_--&state=&mode=demo'
        fundriver = self.foxdriver
        fundriver.get(pageUrl)
        zipcodes= fundriver.find_elements_by_xpath('.//a')
        
        for code in zipcodes:
            print(code.get_attribute('href'))
            print(code.text)
    

    def test_StateWise_Demographics(self):
        pageUrl='https://zipwho.com/'
        fundriver = self.foxdriver
        fundriver.get(pageUrl)
        selectstate = Select(fundriver.find_element_by_id('state'))
        #select by visible text 
        selectstate.select_by_visible_text('Alabama')
        #alternatively we can use select by value 
        #selectstate.select_by_value('1)
        
        element=fundriver.find_element_by_css_selector(".button[value='Advanced Search']")
        element.click()
        zipcodes = fundriver.find_elements_by_xpath('.//a')

        for code in zipcodes:
            print(code.text)
            print(code.get_attribute('href'))

    
    def test_FetchWealthiestZipcodes(self):
        pageUrl='https://zipwho.com/'
        fundriver = self.foxdriver
        fundriver.get(pageUrl)
        element = fundriver.find_element_by_link_text('Wealthiest 1%')
        element.click()
        time.sleep(5)
        zipcodes = fundriver.find_elements_by_xpath('.//a')
        for code in zipcodes:
            print(code.text)
            print(code.get_attribute('href'))
    
    def test_BigHouse(self):
        pageUrl='https://zipwho.com/'
        fundriver = self.foxdriver
        fundriver.get(pageUrl)
        element = fundriver.find_element_by_link_text('Big House Little Mortgage')
        element.click()
        time.sleep(5)
        zipcodes = fundriver.find_elements_by_xpath('.//a')
        for code in zipcodes:
            print(code.text)
            print(code.get_attribute('href'))




    
    def tearDown(self):
        self.foxdriver.close()


if __name__ =='__main__':
    FoxScrapeTest()