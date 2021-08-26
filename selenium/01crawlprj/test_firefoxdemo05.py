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
from selenium.webdriver.common.keys import Keys 

class GoogleSearchBarTest(unittest.TestCase):

    def setUp(self):
        foxOpts = FoxOptions()
        foxOpts.add_argument("--headless")
        #assert foxOpts.headless # operating in headless mode
        foxcaps = webdriver.DesiredCapabilities().FIREFOX
        foxcaps["marionette"] = True
        self.foxdriver = webdriver.Firefox(firefox_options=foxOpts,capabilities=foxcaps, executable_path="E:\\awase-harddisk\\CT\\Selenium\\PythonSelenium\\Selenium\\01crawldemo\\01crawlprj\\drivers\\geckodriver.exe")
        #self.foxdriver.implicitly_wait(3)
        #time.sleep(10)



    def test_GoogleSearch(self):
        gUrl='http://www.google.com'
        fundriver = self.foxdriver 
        fundriver.get(gUrl)
        gsearchbar = fundriver.find_element_by_name('q')
        gsearchbar.send_keys("Aliens among us")
        gsearchbar.submit()
        time.sleep(10)
        gsearch_results=fundriver.find_elements_by_class_name("tF2Cxc")
        print(len(gsearch_results))
        for result in gsearch_results:
            print(result.get_attribute('innerHTML'))

    
    def test_AmazonDropDownMenu(self):
        aUrl='http://amazon.com'
        fundriver = self.foxdriver 
        fundriver.get(aUrl)
        aselection = Select(fundriver.find_element_by_id('searchDropdownBox'))
        #selection approaches 
        #aselection.select_by_index(1)
        #aselection.select_by_visible_text("Electronics")
        aselection.select_by_value('search-alias=electronics-intl-ship')
        aselection.submit()
        # asearchbtn= fundriver.find_element_by_id("nav-search-submit-button")
        # asearchbtn.click()
        time.sleep(4)
        resultlinks = fundriver.find_elements_by_class_name("a-link-normal")
        for link in resultlinks:
            link.get_attribute('href')

    
    def test_CheckTabNavigation(self):
        sUrl='https://mdbootstrap.com/docs/standard/navigation/tabs/#docsTabsOverview'
        fundriver = self.foxdriver 
        fundriver.get(sUrl)
        overviewtab= fundriver.window_handles[0]
        overviewtab_title= fundriver.title 
        print(overviewtab_title)
        apitab=fundriver.window_handles[1]
        apitab_title = fundriver.title 
        print(apitab_title)
        

    
    def test_checkAlert(self):
        nUrl='http://demo.guru99.com/test/delete_customer.php'
        fundriver = self.foxdriver 
        fundriver.get(nUrl)
        alertbtn=fundriver.find_element_by_name('cusid').send_keys("72387")
        alertsubmit=fundriver.find_element_by_name('submit')
        alertsubmit.submit()
        # switcht o alert 
        el = fundriver.switch_to.alert()
        el_msg = el.text
        print(el_msg)
        time.sleep(3)
        el.accept()



        





    def tearDown(self):
        self.foxdriver.close()





if __name__ =='__main__':
    GoogleSearchBarTest()
