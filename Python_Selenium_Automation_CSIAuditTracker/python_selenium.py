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
        assert 'Pharmscript - CSIAuditTracker' == self.driver.title
   
    def test_CSIAudit_list_validation(self):
        driver=self.driver
        time.sleep(5)
        driver.implicitly_wait(10)
        element_to_hover = driver.find_element(By.XPATH, '/html/body/app-root/app-admin/div/app-admin-left-side/aside/section/ul/li[3]/a/i')
        actions = ActionChains(driver)
        actions.move_to_element(element_to_hover).perform()
        actions.click(element_to_hover).perform()
        time.sleep(15)
        driver.implicitly_wait(10)
        
        CSIAudittitle = driver.find_element(By.XPATH,'/html/body/app-root/app-admin/div/app-auditlog-list/div[1]/div/section/div/div/p-panel/div/div[1]/p-header/div/span').text
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH,'//*[@id="txtAuditLogDateRange"]').click()
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH,'/html/body/div[4]/div[1]/ul/li[3]').click()
        time.sleep(2)
        driver.implicitly_wait(10)

        driver.find_element(By.XPATH,'//*[@id="btnsearch"]').click()
        time.sleep(15)
        driver.implicitly_wait(10)
        connlastmonthcount = driver.find_element(By.XPATH,'//*[@id="grdAuditLogList_pager_label"]').text
        connlastmonthcount =connlastmonthcount.split(' ')
        assert 'ID' in connlastmonthcount
        assert CSIAudittitle == 'Audit List'
        self.driver.close()


# if __name__ == '__main__':
#     runner = HTMLTestRunner(
#         report_filepath="ReportFilePath",
#         title="CSI Audit tracker Automation Test report",
#         description="CSI Audit tracker Automation Test report",
#         open_in_browser=True
#     )

#     # run the test
#     unittest.main(testRunner=runner)