import os
import time
import unittest

from selenium import webdriver
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
        assert 'Compliance Dashboard' == self.driver.title
   
    def test_inventory_list_validation(self):
        driver=self.driver
        driver.implicitly_wait(10)
        time.sleep(10)
        driver.find_element(By.XPATH,'/html/body/app-root/app-starter/div/div/app-compliancetraining-dashboard-list/drag-scroll/div/div/div/div[2]/div[1]/div/form/div/div/div/div/div[1]/daterangepicker/div/input').click()
        time.sleep(1)
        driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/ul/li[4]').click()
        time.sleep(1)
        driver.find_element(By.ID,'btnSearch').click()
        time.sleep(5)
        driver.find_element(By.XPATH,'//*[@id="generatedFiles"]').click()
        driver.implicitly_wait(6)
        complianceheader = driver.find_element(By.XPATH,'/html/body/app-root/app-starter/div/div/app-compliancetraining-dashboard-list/drag-scroll/div/div/div/div[1]/h5').text
        compliancegridheader = driver.find_element(By.XPATH,'/html/body/app-root/app-starter/div/div/app-compliancetraining-dashboard-list/drag-scroll/div/div/div/div[2]/div[2]/div[2]/div[2]/app-generatefiles-list/div/p-panel/div/div[1]/p-header/div/div[1]/h5').text
        driver.find_element(By.XPATH,'/html/body/app-root/app-starter/div/div/app-compliancetraining-dashboard-list/drag-scroll/div/div/div/div[2]/div[2]/div[2]/div[2]/app-generatefiles-list/div/p-panel/div/div[2]/div/form/div/div/ig-grid/div/div[4]/table/tbody/tr[1]/td[5]/div/a/u').click()
        time.sleep(2)
        assert 'Compliance Training Dashboard List' == complianceheader
        assert 'Generated Files' == compliancegridheader
        self.driver.close()


# if __name__ == '__main__':
#     runner = HTMLTestRunner(
#         report_filepath="ReportFilePath",
#         title="Compliance Dashboard Automation Test report",
#         description="Control substance Audit tracker Automation Test report",
#         open_in_browser=True
#     )

#     # run the test
#     unittest.main(testRunner=runner)