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
from selenium.webdriver import Firefox 
from selenium.webdriver.firefox.options import Options as FoxOptions
from selenium.webdriver.support.select import Select #microsoft edge web driver 
from msedge.selenium_tools import Edge, EdgeOptions

import time 
import unittest 

#chrome driver testing 
class ScrapeYC_ChromeTest(unittest.TestCase):

    #scaffolding the required drivers, configurring options and opening the browser
    def setUp(self):
        coptions = Options()
        coptions.headless=True 
        coptions.add_argument("--incognito") # incognito mode 
        coptions.add_argument("--window-size=1920x1080") # window size settings 
        self.cdriver = webdriver.Chrome( r'E:\\awase-harddisk\\CT\\Selenium\\PythonSelenium\\Selenium\\01crawldemo\\01crawlprj\\drivers\\chromedriver.exe',options=coptions)
        time.sleep(3)


    #register user validation 
    #ycombinator form elements do not have id or css hence it becomes difficult to excute these 
    # we need to mark this test as pytest.mark.xfail
    def test_registerUser(self):
        prl='http://news.ycombinator.com/login'
        user_name ="Millena.Polo@EasyOnlineMail.net"
        password="Xv1hytF#8SSORUFhg"
        chromedriver = self.cdriver
        element = chromedriver.find_element_by_partial_link_text('account')
        element.send_keys(user_name)
        element = chromedriver.find_element_by_partial_link_text('password')
        element.send_keys(password)
        element.submit() # using element submit instead of click event
        time.sleep(3)
        

    #login validation and secure web access
    #ycombinator form elements do not have id or css hence it becomes difficult to excute these 
    # we need to mark this test as pytest.mark.xfail
    def test_loginField(self):
        pageUrl='https://news.ycombinator.com/login'
        user_name ="Millena.Polo@EasyOnlineMail.net"
        password="Xv1hytF#8SSORUFhg"
        chromedriver=self.cdriver 
        chromedriver.maximize_window()
        chromedriver.get(pageUrl)
        element = chromedriver.find_element_by_partial_link_text('acct')
        element.send_keys(user_name)
        element = chromedriver.find_element_by_partial_link_text('pwd')
        element.send_keys(password)
        el = chromedriver.find_element_by_name("submit")
        el.click() # using click to submit the login form
        time.sleep(5)


    #scraping news articles 
    def test_scrapeYNews(self):
        pnUrl='https://news.ycombinator.com/'
        chromedriver=self.cdriver 
        chromedriver.maximize_window()
        chromedriver.get(pnUrl)
        elements = chromedriver.find_elements_by_css_selector(".storylink")
        storyTitles = [el.text for el in elements]
        storyUrls=[el.get_attribute("href") for el in elements]

        elements=chromedriver.find_elements_by_css_selector(".score")
        scores = [el.text for el in elements]
        print(str(len(scores)))

        elements=chromedriver.find_elements_by_css_selector('.sitebit a')
        sites =[el.get_attribute("href") for el in elements]
        print(str(len(sites)))

        for s in sites:
            print(s)


    
    #closing the driver and browser 
    def tearDown(self):
        self.cdriver.close()


# #firefoxdriver testing 
class ScrapeYC_FoxTest(unittest.TestCase):

    #scaffolding the required drivers, configurring options and opening the browser
    def setUp(self):
        foxOpts = FoxOptions()
        foxOpts.add_argument("--headless")
        #assert foxOpts.headless # operating in headless mode
        foxcaps = webdriver.DesiredCapabilities().FIREFOX
        foxcaps["marionette"] = True
        self.foxdriver = webdriver.Firefox(firefox_options=foxOpts,capabilities=foxcaps, executable_path="E:\\awase-harddisk\\CT\\Selenium\\PythonSelenium\\Selenium\\01crawldemo\\01crawlprj\\drivers\\geckodriver.exe")
        time.sleep(3)


    #register user validation 
    def test_registerUser(self):
        prl='http://news.ycombinator.com/login'
        user_name ="Millena.Polo@EasyOnlineMail.net"
        password="Xv1hytF#8SSORUFhg"
        fxdriver = self.foxdriver 
        element = fxdriver.find_element_by_partial_link_text('account')
        element.send_keys(user_name)
        element = fxdriver.find_element_by_partial_link_text('password')
        element.send_keys(password)
        element.submit() # using element submit instead of click event
        time.sleep(3)
        

    #login validation and secure web access
    def test_loginField(self):
        pageUrl='https://news.ycombinator.com/login'
        user_name ="Millena.Polo@EasyOnlineMail.net"
        password="Xv1hytF#8SSORUFhg"
        fxdriver=self.foxdriver 
        fxdriver.maximize_window()
        fxdriver.get(pageUrl)
        element = fxdriver.find_element_by_partial_link_text('acct')
        element.send_keys(user_name)
        element = fxdriver.find_element_by_partial_link_text('pwd')
        element.send_keys(password)
        el = fxdriver.find_element_by_css_selector("")
        el.click() # using click to submit the login form
        time.sleep(5)


    #scraping news articles 
    def test_scrapeYNews(self):
        pnUrl='https://news.ycombinator.com/'
        fxdriver=self.foxdriver
        fxdriver.maximize_window()
        fxdriver.get(pnUrl)
        elements = fxdriver.find_elements_by_css_selector(".storylink")
        storyTitles = [el.text for el in elements]
        storyUrls=[el.get_attribute("href") for el in elements]

        elements=fxdriver.find_elements_by_css_selector(".score")
        scores = [el.text for el in elements]

        elements=fxdriver.find_elements_by_css_selector('.sitebit a')
        sites =[el.get_attribute("href") for el in elements]
        print("Firefox Scrapping Results are published below:")
        for s in sites:
            print(s)


    
    #closing the driver and browser 
    def tearDown(self):
        self.foxdriver.close()



# #apple safari testing 
# class ScrapeYC_SafariTest(unittest.TestCase):

#     #scaffolding the required drivers, configurring options and opening the browser
#     def setUp(self):
#         coptions = Options()
#         coptions.headless=True 
#         coptions.add_argument("--incognito") # incognito mode 
#         coptions.add_argument("--window-size=1920x1080") # window size settings 
#         self.cdriver = webdriver.Chrome( r'',options=coptions)
#         time.sleep(3)


#     #register user validation 
#     def test_registerUser(self):
#         prl='http://news.ycombinator.com/login'
#         user_name ="Millena.Polo@EasyOnlineMail.net"
#         password="Xv1hytF#8SSORUFhg"
#         chromedriver = self.cdrive 
#         element = chromedriver.find_element_by_id('')
#         element.send_keys(user_name)
#         element = chromedriver.find_element_by_id('')
#         element.send_keys(password)
#         element.submit() # using element submit instead of click event
#         time.sleep(3)
        

#     #login validation and secure web access
#     def test_loginField(self):
#         pageUrl='https://news.ycombinator.com/login'
#         user_name ="Millena.Polo@EasyOnlineMail.net"
#         password="Xv1hytF#8SSORUFhg"
#         chromedriver=self.cdriver 
#         chromedriver.maximize_window()
#         chromedriver.get(pageUrl)
#         element = chromedriver.find_element_by_id('')
#         element.send_keys(user_name)
#         element = chromedriver.find_element_by_id('')
#         element.send_keys(password)
#         el = chromedriver.find_element_by_css_selector("")
#         el.click() # using click to submit the login form
#         time.sleep(5)


#     #scraping news articles 
#     def test_scrapeYNews(self):
#         pnUrl='https://news.ycombinator.com/'
#         chromedriver=self.cdriver 
#         chromedriver.maximize_window()
#         chromedriver.get(pnUrl)
#         elements = chromedriver.find_elements_by_css_selector(".storylink")
#         storyTitles = [el.text for el in elements]
#         storyUrls=[el.get_attribute("href") for el in elements]

#         elements=chromedriver.find_elements_by_css_selector(".score")
#         scores = [el.text for el in elements]

#         elements=chromedriver.find_elements_by_css_selector('.sitebit a')
#         sites =[el.get_attribute("href") for el in elements]


    
#     #closing the driver and browser 
#     def tearDown(self):
#         self.chromedriver.close()


# #microsoft edge driver testing
#edge is not able to create profile at the directory
class ScrapeYC_EdgeTest(unittest.TestCase):

    #scaffolding the required drivers, configurring options and opening the browser
    def setUp(self):
        Eoptions = EdgeOptions()
        Eoptions.use_chromium = True
        Eoptions.add_argument("--user-data-dir=C:\\Users\/sak_s\/AppData\/Local\\Microsoft\\Edge\\User Data\\Default")
        Eoptions.binary_location= r"C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
        self.msdriver=webdriver.Edge(executable_path=r"E:\\awase-harddisk\\CT\\Selenium\\PythonSelenium\\Selenium\\01crawldemo\\01crawlprj\\drivers\\msedgedriver.exe")
        time.sleep(3)


    #register user validation 
    def test_registerUser(self):
        prl='http://news.ycombinator.com/login'
        user_name ="Millena.Polo@EasyOnlineMail.net"
        password="Xv1hytF#8SSORUFhg"
        edgedriver = self.msdriver
        element = edgedriver.find_element_by_partial_link_text('acct')
        element.send_keys(user_name)
        element = edgedriver.find_element_by_partial_link_text('password')
        element.send_keys(password)
        element.submit() # using element submit instead of click event
        time.sleep(3)
        

    #login validation and secure web access
    def test_loginField(self):
        pageUrl='https://news.ycombinator.com/login'
        user_name ="Millena.Polo@EasyOnlineMail.net"
        password="Xv1hytF#8SSORUFhg"
        edgedriver = self.msdriver
        edgedriver.maximize_window()
        edgedriver.get(pageUrl)
        element = edgedriver.find_element_by_partial_link_text('acct')
        element.send_keys(user_name)
        element = edgedriver.find_element_by_partial_link_text('pwd')
        element.send_keys(password)
        el = edgedriver.find_element_by_css_selector("")
        el.click() # using click to submit the login form
        time.sleep(5)


    #scraping news articles 
    def test_scrapeYNews(self):
        pnUrl='https://news.ycombinator.com/'
        edgedriver=self.msdriver 
        edgedriver.maximize_window()
        edgedriver.get(pnUrl)
        elements = edgedriver.find_elements_by_css_selector(".storylink")
        storyTitles = [el.text for el in elements]
        storyUrls=[el.get_attribute("href") for el in elements]

        elements=edgedriver.find_elements_by_css_selector(".score")
        scores = [el.text for el in elements]

        elements=edgedriver.find_elements_by_css_selector('.sitebit a')
        sites =[el.get_attribute("href") for el in elements]


    
    #closing the driver and browser 
    def tearDown(self):
        self.msdriver.close()


# #Internet Explorer driver testing
class ScrapeYC_ExplorerTest(unittest.TestCase):

    #scaffolding the required drivers, configurring options and opening the browser
    def setUp(self):
        
        self.iedriver = webdriver.Ie( r'E:\\awase-harddisk\\CT\\Selenium\\PythonSelenium\\Selenium\\01crawldemo\\01crawlprj\\drivers\\IEDriverServer')
        time.sleep(3)


    #register user validation 
    def test_registerUser(self):
        prl='http://news.ycombinator.com/login'
        user_name ="Millena.Polo@EasyOnlineMail.net"
        password="Xv1hytF#8SSORUFhg"
        idriver = self.iedriver
        element = idriver.find_element_by_id('')
        element.send_keys(user_name)
        element = idriver.find_element_by_id('')
        element.send_keys(password)
        element.submit() # using element submit instead of click event
        time.sleep(3)
        

    #login validation and secure web access
    def test_loginField(self):
        pageUrl='https://news.ycombinator.com/login'
        user_name ="Millena.Polo@EasyOnlineMail.net"
        password="Xv1hytF#8SSORUFhg"
        idriver=self.iedriver 
        idriver.maximize_window()
        idriver.get(pageUrl)
        element = idriver.find_element_by_id('')
        element.send_keys(user_name)
        element = idriver.find_element_by_id('')
        element.send_keys(password)
        el = idriver.find_element_by_css_selector("")
        el.click() # using click to submit the login form
        time.sleep(5)


    #scraping news articles 
    def test_scrapeYNews(self):
        pnUrl='https://news.ycombinator.com/'
        idriver=self.iedriver 
        idriver.maximize_window()
        idriver.get(pnUrl)
        elements = idriver.find_elements_by_css_selector(".storylink")
        storyTitles = [el.text for el in elements]
        storyUrls=[el.get_attribute("href") for el in elements]

        elements=idriver.find_elements_by_css_selector(".score")
        scores = [el.text for el in elements]

        elements=idriver.find_elements_by_css_selector('.sitebit a')
        sites =[el.get_attribute("href") for el in elements]


    
    #closing the driver and browser 
    def tearDown(self):
        self.iedriver.close()



# #Opera driver testing
# class ScrapeYC_OperaTest(unittest.TestCase):

#     #scaffolding the required drivers, configurring options and opening the browser
#     def setUp(self):
#         coptions = Options()
#         coptions.headless=True 
#         coptions.add_argument("--incognito") # incognito mode 
#         coptions.add_argument("--window-size=1920x1080") # window size settings 
#         self.cdriver = webdriver.Chrome( r'',options=coptions)
#         time.sleep(3)


#     #register user validation 
#     def test_registerUser(self):
#         prl='http://news.ycombinator.com/login'
#         user_name ="Millena.Polo@EasyOnlineMail.net"
#         password="Xv1hytF#8SSORUFhg"
#         chromedriver = self.cdrive 
#         element = chromedriver.find_element_by_id('')
#         element.send_keys(user_name)
#         element = chromedriver.find_element_by_id('')
#         element.send_keys(password)
#         element.submit() # using element submit instead of click event
#         time.sleep(3)
        

#     #login validation and secure web access
#     def test_loginField(self):
#         pageUrl='https://news.ycombinator.com/login'
#         user_name ="Millena.Polo@EasyOnlineMail.net"
#         password="Xv1hytF#8SSORUFhg"
#         chromedriver=self.cdriver 
#         chromedriver.maximize_window()
#         chromedriver.get(pageUrl)
#         element = chromedriver.find_element_by_id('')
#         element.send_keys(user_name)
#         element = chromedriver.find_element_by_id('')
#         element.send_keys(password)
#         el = chromedriver.find_element_by_css_selector("")
#         el.click() # using click to submit the login form
#         time.sleep(5)


#     #scraping news articles 
#     def test_scrapeYNews(self):
#         pnUrl='https://news.ycombinator.com/'
#         chromedriver=self.cdriver 
#         chromedriver.maximize_window()
#         chromedriver.get(pnUrl)
#         elements = chromedriver.find_elements_by_css_selector(".storylink")
#         storyTitles = [el.text for el in elements]
#         storyUrls=[el.get_attribute("href") for el in elements]

#         elements=chromedriver.find_elements_by_css_selector(".score")
#         scores = [el.text for el in elements]

#         elements=chromedriver.find_elements_by_css_selector('.sitebit a')
#         sites =[el.get_attribute("href") for el in elements]


    
#     #closing the driver and browser 
#     def tearDown(self):
#         self.chromedriver.close()


if __name__ =="__main__":
    ScrapeYC_ChromeTest()
    ScrapeYC_FoxTest()
    ScrapeYC_EdgeTest()
    # ScrapeYC_ExplorerTest()
    # ScrapeYC_OperaTest()
    # ScrapeYC_SafariTest()