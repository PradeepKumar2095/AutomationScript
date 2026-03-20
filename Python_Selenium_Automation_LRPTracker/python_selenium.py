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
        assert 'Pharmscript - LRP Workflow Streamliner' == self.driver.title
   
    def test_LRPBoard_validation(self):
        driver=self.driver
        driver.implicitly_wait(10)
        time.sleep(20)
        driver=self.driver
        driver.implicitly_wait(10)
        Requestreceived = driver.find_element(By.XPATH,'/html/body/app-root/app-admin/div/gtm-board/div/div/section/div[2]/div/div/div/drag-scroll/div/div[1]/div/div[1]/gtm-column/div/div/span[1]').text
        completed = driver.find_element(By.XPATH,'/html/body/app-root/app-admin/div/gtm-board/div/div/section/div[2]/div/div/div/drag-scroll/div/div[1]/div/div[7]/gtm-column/div/div/span[1]').text
        time.sleep(5)
        self.driver.implicitly_wait(10)
        assert '  Request Received' == Requestreceived
        assert '  Complete' == completed
        self.driver.close()

# if __name__ == '__main__':
#     runner = HTMLTestRunner(
#         report_filepath="ReportFilePath",
#         title="LRP Audit tracker Automation Test report",
#         description="LRP Audit tracker Automation Test report",
#         open_in_browser=True
#     )

#     # run the test
#     unittest.main(testRunner=runner)