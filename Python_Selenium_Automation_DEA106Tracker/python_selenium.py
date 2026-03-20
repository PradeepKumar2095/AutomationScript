import os
import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService

dir = os.getcwd()
from xml.dom import minidom

path = ("ConfigPath")
Config =minidom.parse(path)
item = Config.getElementsByTagName('item')

class Pytest(unittest.TestCase):

    def setUp(self):
        service = EdgeService(executable_path='EdgeDriverPath')
        options = EdgeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Edge(service=service, options=options)
        pageUrl = item[0].childNodes[0].data
        driver=self.driver
        driver.maximize_window()
        driver.get(pageUrl) 
        

    def test_page_title(self):
        time.sleep(3)       
        assert 'Pharmscript - DEA 106 Tracker' == self.driver.title
   
    def test__list_dea106_LIST_Validation(self):
        driver=self.driver
        driver.implicitly_wait(10)
        time.sleep(20)
        driver.find_element(By.XPATH,'//*[@id="txtDateofTheftndLossRange"]').click()
        driver.find_element(By.XPATH,'/html/body/div[6]/div[1]/ul/li[3]').click()
        time.sleep(5)
        driver.find_element(By.XPATH,'//*[@id="btnGo"]').click()
        time.sleep(2)
        time.sleep(30)
        driver.implicitly_wait(10)
        connlastmonthcount = driver.find_element(By.XPATH,'//*[@id="grddetr_DEA106Form_pager_label"]').text
        connlastmonthcount =connlastmonthcount.split(' ')
        assert '1' in connlastmonthcount
        self.driver.close()


# if __name__ == '__main__':
#     runner = HTMLTestRunner(
#         report_filepath="ReportFilePath",
#         title="DEA 106 tracker Automation Test report",
#         description="DEA 106 tracker Automation Test report",
#         open_in_browser=True
#     )

#     # run the test
#     unittest.main(testRunner=runner)