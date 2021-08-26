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
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options 
import time 
import unittest 

class ChromeDemoTest(unittest.TestCase):

    def setUp(self):
        coptions = Options()
        coptions.headless=True 
        coptions.add_argument("--incognito") # incognito mode 
        coptions.add_argument("--window-size=1920x1080") # window size settings 
        self.cdriver = webdriver.Chrome( r'E:\\awase-harddisk\\CT\\Selenium\\PythonSelenium\\Selenium\\01crawldemo\\01crawlprj\\drivers\\chromedriver.exe',options=coptions)
        time.sleep(3)

    #inserting input data into the forms and fetching the results 
    def test_initiateQuery(self):
        ypUrl='https://www.yellowpages.ca/'
        chromedriver=self.cdriver 
        chromedriver.maximize_window()
        chromedriver.get(ypUrl)
        #approach 1 
        elone =chromedriver.find_element_by_id("whatwho")
        #approach 2 
        eltwo = chromedriver.find_element_by_id("where")
        #approach 3 
        elthree = chromedriver.find_element_by_xpath("//input[@id='whatwho']")
        #approach 3
        elfour = chromedriver.find_element_by_xpath("//input[@id='where']")
        whatelement = 'pharmacies'
        where_element ='Toronto, ON'
        #sending values to the input elements 
        elthree.send_keys(whatelement)
        elfour.send_keys(where_element)
        #submit approaches 
        sbl_btn=chromedriver.find_element_by_name('search_button')
        sbl_btn.click()
        # #alternatively we can use 
        # sbl_chrome = chromedriver.find_element_by_name('search_button')
        # sbl_chrome.submit()
        time.sleep(5)

        result_list = chromedriver.find_elements_by_class_name("listing_right_top_section")
        print("no of records fetched from yellow pages are:" +str(len(result_list)))
        for list in result_list:
            print(list.text)    


        #getting the phone records 
        phone_list = chromedriver.find_elements_by_xpath("//a[@class='mlr__item_cta jsMlrMenu']")
        for phone in phone_list:
            print(phone.get_attribute('data-phone'))
    

   


    
    def tearDown(self):
        self.cdriver.close()



if __name__ =='__main__':
    ChromeDemoTest()