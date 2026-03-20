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
        assert 'Prescriber DEA Report Tracker' == self.driver.title
   
    def test_Prescriber_DEA_Report_List(self):
        driver=self.driver
        driver.implicitly_wait(10)
        time.sleep(10)
        appheader=driver.find_element(By.XPATH,'/html/body/app-root/app-starter/div/div/app-prescriber-dea-report/div/div[1]/h5/span/b').text
        time.sleep(2)  
        driver.find_element(By.XPATH,'/html/body/app-root/app-starter/div/app-header/nav/ul[2]/li[1]/app-filter/div/ul/li[3]/a/i').click()
        time.sleep(2)
        driver.find_element(By.XPATH,'/html/body/app-root/app-starter/div/app-header/nav/ul[2]/li[1]/app-filter/div/ul/li[3]/form/div[2]/div/div[1]/div[1]/daterangepicker/div/input').click()
        time.sleep(1)
        driver.find_element(By.XPATH,'/html/body/div[5]/div[1]/ul/li[3]').click()
        time.sleep(2)
        driver.find_element(By.XPATH,'/html/body/app-root/app-starter/div/app-header/nav/ul[2]/li[1]/app-filter/div/ul/li[3]/form/div[4]/div/button[1]').click()
        time.sleep(3)
        driver.find_element(By.XPATH,'/html/body/app-root/app-starter/div/div/app-prescriber-dea-report/div/div[2]/div[2]/div/ig-grid/div/div[4]/table/tbody/tr[1]/td[5]/div/center/a/u').click()
        driver.implicitly_wait(10)
        gridfirstheadername = driver.find_element(By.XPATH,'/html/body/app-root/app-starter/div/div/app-prescriber-dea-report/div/div[2]/div[2]/div[2]/app-dea-tracking-details/div/div[1]/div/ig-grid/div/div[2]/table/thead/tr[1]/th[1]/span[1]').text
        assert gridfirstheadername == 'Date Ordered'
        assert 'Prescriber DEA Report List' == appheader
        self.driver.close()


# if __name__ == '__main__':
#     runner = HTMLTestRunner(
#         report_filepath="ReportFilePath",
#         title="DEAPrescriber Automation Test report",
#         description="DEAPrescriber Automation Test report",
#         open_in_browser=True
#     )

#     # run the test
#     unittest.main(testRunner=runner)