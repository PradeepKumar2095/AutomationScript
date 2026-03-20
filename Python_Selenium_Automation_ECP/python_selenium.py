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
        time.sleep(5)       
        assert 'Existing Customer Profitability' == self.driver.title
        self.driver.close()
   
    def test_add_new_queue(self):
        driver=self.driver
        driver.implicitly_wait(10)
        time.sleep(10)
        CurrentQueuid = driver.find_element(By.XPATH,'/html/body/app-root/app-starter/div/div/reportqueue/section/div[1]/drag-scroll/div/div[1]/div/div/p-panel/div/div[2]/div/div/div/div[1]/div/ig-grid/div/div[4]/table/tbody/tr[1]/td[1]').text
        driver.find_element(By.XPATH,'//*[@id="btnAddReportQueue"]').click()
        driver.implicitly_wait(10)
        time.sleep(5)
        driver.find_element(By.XPATH,'/html/body/app-root/app-starter/div/div/reportqueue/section/div[1]/drag-scroll/div/div[2]/div/reportqueuedetails/section/p-panel/div/div[2]/div/form/div[2]/div[2]/ng-select/div/div/div[2]/input').send_keys('PharmID')
        time.sleep(2)
        driver.find_element(By.XPATH,'/html/body/app-root/app-starter/div/div/reportqueue/section/div[1]/drag-scroll/div/div[2]/div/reportqueuedetails/section/p-panel/div/div[2]/div/form/div[2]/div[2]/ng-select/ng-dropdown-panel/div[2]/div[2]/div/a/div/div[1]').click()
        time.sleep(2)
        self.driver.implicitly_wait(10)
        driver.find_element(By.XPATH,'/html/body/app-root/app-starter/div/div/reportqueue/section/div[1]/drag-scroll/div/div[2]/div/reportqueuedetails/section/p-panel/div/div[2]/div/form/div[4]/div[2]/ng-select/div/div/div[2]/input').send_keys('FacGroup')
        time.sleep(2)
        driver.find_element(By.XPATH,'/html/body/app-root/app-starter/div/div/reportqueue/section/div[1]/drag-scroll/div/div[2]/div/reportqueuedetails/section/p-panel/div/div[2]/div/form/div[4]/div[2]/ng-select/ng-dropdown-panel/div/div[2]/div[2]/a/div/div[1]').click()
        time.sleep(2)
        driver.find_element(By.XPATH,'/html/body/app-root/app-starter/div/div/reportqueue/section/div[1]/drag-scroll/div/div[2]/div/reportqueuedetails/section/p-panel/div/div[2]/div/form/div[6]/div[1]/div/label').click()
        driver.find_element(By.XPATH,'//*[@id="chkselectAll"]').click()
        time.sleep(2)
        driver.find_element(By.XPATH,'/html/body/app-root/app-starter/div/div/reportqueue/section/div[1]/drag-scroll/div/div[2]/div/reportqueuedetails/section/p-panel/div/div[2]/div/form/div[7]/div[2]/div/div/div/div[2]/div/div[1]/input').click()
        time.sleep(2)
        driver.find_element(By.XPATH,'//*[@id="radReportByBill"]').click()
        time.sleep(2)
        driver.find_element(By.XPATH,'//*[@id="a2eStartTime"]').send_keys('StartDate')
        self.driver.implicitly_wait(10)
        driver.find_element(By.XPATH,'//*[@id="a2eEndDate"]').send_keys('EndDate')
        driver.find_element(By.XPATH,'//*[@id="btnUpdateQueue"]').click()
        #driver.find_element(By.XPATH,'//*[@id="btnCancel"]').click()
        time.sleep(5)
        # driver.find_element(By.XPATH,'//*[@id="btnReset"]').click()
        # time.sleep(5)
        CurrentQueuidafteradd = driver.find_element(By.XPATH,'/html/body/app-root/app-starter/div/div/reportqueue/section/div[1]/drag-scroll/div/div[1]/div/div/p-panel/div/div[2]/div/div/div/div[1]/div/ig-grid/div/div[4]/table/tbody/tr[1]/td[1]').text
        #driver.find_element(By.XPATH,'//*[@id="DownloadExcel"]').click()
        time.sleep(5)
        CurrentQueuid = int(CurrentQueuid)
        CurrentQueuidafteradd = int (CurrentQueuidafteradd)
        assert CurrentQueuid + 1 == CurrentQueuidafteradd
        self.driver.close()

   


# if __name__ == '__main__':
#     runner = HTMLTestRunner(
#         report_filepath="ReportFilePath",
#         title="ECP Automation Test report",
#         description="ECP Automation Test report",
#         open_in_browser=True
#     )

#     # run the test
#     unittest.main(testRunner=runner)