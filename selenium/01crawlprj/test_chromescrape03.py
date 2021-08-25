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


class ChromeScraperTest(unittest.TestCase):

    def setUp(self):
        coptions = Options()
        coptions.headless=True 
        coptions.add_argument("--incognito") # incognito mode 
        coptions.add_argument("--window-size=1920x1080") # window size settings 
        self.cdriver = webdriver.Chrome( r'E:\\awase-harddisk\\CT\\Selenium\\PythonSelenium\\Selenium\\01crawldemo\\01crawlprj\\drivers\\chromedriver.exe',options=coptions)
        time.sleep(3) 


    def test_FetchListing(self):
        pgUrl='https://www.realtor.ca/map#ZoomLevel=4&Center=54.920828%2C-99.316406&LatitudeMax=66.87403&LongitudeMax=-46.56445&LatitudeMin=37.95286&LongitudeMin=-152.06836&view=list&Sort=6-D&PropertyTypeGroupID=1&PropertySearchTypeId=1&TransactionTypeId=2&Currency=CAD'
        chromedriver=self.cdriver 
        chromedriver.maximize_window()
        chromedriver.get(pgUrl)
       # urllists =chromedriver.find_elements_by_class_name('listingDetailsLink')
        cardPrices = chromedriver.find_elements_by_class_name('listingCardPrice')
        cardAddresses=chromedriver.find_elements_by_class_name('listingCardAddress')
        cardRealtors = chromedriver.find_elements_by_class_name('listingCardOfficeName')
                
        # for card in urllists:
        #     print(card.get_attribute('href'))
        
        for address in cardAddresses:
            print(address.text)

        for realtor in cardRealtors:
            print(realtor.text)
        
        for price in cardPrices:
            print(price.text)

    

    def tearDown(self):
        self.cdriver.close()
    



if __name__=='__main__':
    ChromeScraperTest()

 