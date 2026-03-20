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
        assert 'Pharmscript - Writeoff Tracker' == self.driver.title
        self.driver.close()
   
    def test_writeoff_tracker_list_validation(self):
        driver=self.driver
        time.sleep(5)
        driver.find_element(By.XPATH,'/html/body/app-root/div/app-layout-shell/div/app-header/header/div[3]/app-filter/div/ul/div/form/div/div[1]/div[1]/div[1]/app-date-range-selector/div/input').click()
        driver.find_element(By.XPATH,'/html/body/div/div/div/igx-calendar-container/div/div/button[3]').click()
        time.sleep(2)
        driver.find_element(By.XPATH,'/html/body/app-root/div/app-layout-shell/div/app-header/header/div[3]/app-filter/div/ul/div/form/div/div[1]/div[1]/div[2]/ng-select/div[1]/div/div[2]/input').click()
        time.sleep(2)
        driver.find_element(By.XPATH,'/html/body/app-root/div/app-layout-shell/div/app-header/header/div[3]/app-filter/div/ul/div/form/div/div[1]/div[1]/div[2]/ng-select/ng-dropdown-panel/div/div[2]/div[2]').click()
        time.sleep(2)
        driver.find_element(By.XPATH,'/html/body/app-root/div/app-layout-shell/div/app-header/header/div[3]/app-filter/div/ul/div/form/div/div[1]/div[1]/div[5]/ng-select/div[1]/div/div[2]/input').click()
        time.sleep(2)
        driver.find_element(By.XPATH,'/html/body/app-root/div/app-layout-shell/div/app-header/header/div[3]/app-filter/div/ul/div/form/div/div[1]/div[1]/div[5]/ng-select/ng-dropdown-panel/div/div[2]/div[5]').click()
        time.sleep(2)
        driver.find_element(By.XPATH,'/html/body/app-root/div/app-layout-shell/div/app-header/header/div[3]/app-filter/div/ul/div/form/div/div[2]/button[1]').click()
        time.sleep(10)
        writeoffgridheader = driver.find_element(By.XPATH,'/html/body/app-root/div/app-layout-shell/div/div/div/main/app-queue/div[1]/div/form/div/div/div/igx-grid/igx-grid-toolbar/igx-grid-toolbar-title').text
        assert  writeoffgridheader == 'Write-off List'
        self.driver.close()

# if __name__ == '__main__':
#     runner = HTMLTestRunner(
#         report_filepath="ReportFilePath",
#         title="WriteOff tracker Automation Test report",
#         description="WriteOff tracker Automation Test report",
#         open_in_browser=True
#     )

#     # run the test
#     unittest.main(testRunner=runner)