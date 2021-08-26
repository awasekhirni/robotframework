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
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
#events 
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select



class ChromeFileTest(unittest.TestCase):

    #setUp
    def setUp(self):
        coptions = Options()
        coptions.headless=True 
        coptions.add_argument("--disable-infobars")
        #coptions.add_argument("start-maximized")
        #coptions.add_argument("--disable-extensions")
        #coptions.add_argument("--start-maximized")
        coptions.add_argument("no-sandbox")
        #coptions.add_argument("--disable-gpu")
        coptions.add_argument("--disable-dev-shm-usage")
          
        coptions.add_argument("--disable-xss-auditor")
        coptions.add_argument("--disable-web-security")
        coptions.add_argument("--allow-running-insecure-content")
        coptions.add_argument("--disable-setuid-sandbox")
        #coptions.add_argument("--disable-webgl")
        coptions.add_argument("--disable-popup-blocking")
        #avoid getting the permission prompt 
        coptions.add_argument("--use-fake-ui-for-media-stream")
        #setting a default directory for downloading files 
        prefs={"download.default_directory": "E:\\awase-harddisk\\CT\\Selenium\\PythonSelenium\\Selenium\\01crawldemo\\01crawlprj\\"}
        coptions.add_experimental_option("prefs", prefs)
        # Pass the argument 1 to allow and 2 to block
        coptions.add_experimental_option("prefs", {
            "profile.default_content_setting_values.media_stream_mic": 2,
            "profile.default_content_setting_values.media_stream_camera": 2,
            "profile.default_content_setting_values.geolocation": 2,
            "profile.default_content_setting_values.notifications": 2
        })
        coptions.add_argument("--incognito") # incognito mode 
        coptions.add_argument("--window-size=1920x1080") # window size settings 
        self.cdriver = webdriver.Chrome( r'E:\\awase-harddisk\\CT\\Selenium\\PythonSelenium\\Selenium\\01crawldemo\\01crawlprj\\drivers\\chromedriver.exe',options=coptions)
        time.sleep(3)


    def test_fileUploading(self):
        pgUrl='https://blueimp.github.io/jQuery-File-Upload/'
        chromedriver=self.cdriver 
        chromedriver.maximize_window()
        chromedriver.get(pgUrl)
        
        file_path= 'E:\\awase-harddisk\\CT\\Selenium\\PythonSelenium\\Selenium\\01crawldemo\\01crawlprj\\samplesyed.csv'
        upi=chromedriver.find_element_by_xpath("//input[@type='file']")
        upi.send_keys(file_path)
        sblbtn=chromedriver.find_element_by_xpath("//button[@type='submit']")
        sblbtn.submit()


    def test_fileDownloading(self):
        try:
            pUrl="https://www.browserstack.com/test-on-the-right-mobile-devices"
            chromedriver = self.cdriver 
            xd = chromedriver.find_element_by_id('accept-cookie-notification')
            xd.click()
            dsv=chromedriver.find_element_by_css_selector('.icon-csv')
            dsv.click()
            time.sleep(5)
        except:
            print("Invalid URL")


    def test_dragDropGoat(self):
        dUrl='https://beej.us/blog/data/drag-n-drop/'
        chromedriver = self.cdriver 
        chromedriver.implicitly_wait(30)
        chromedriver.set_page_load_timeout(50)
        goatMove = ActionChains(chromedriver)
        source = chromedriver.find_element_by_id('goat0')
        target = chromedriver.find_element_by_id('dropzone0')
        goatMove.drag_and_drop(source,target).perform()
        time.sleep(5)
        print(target.text)
        el=chromedriver.switch_to_alert()
        el_msg = el.text
        assert "goat0 was just dropped on dropzone0" in el.text
        time.sleep(3)
        el.accept()
        

    def tearDown(self):
        self.cdriver.close()




if __name__=='__main__':
    ChromeFileTest()