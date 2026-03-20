import os
import time
import unittest
from datetime import datetime, timedelta

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
        edge_driver_path = "EdgeDriverPath"
        service = EdgeService(executable_path=edge_driver_path)
        options = EdgeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Edge(service=service, options=options)
        pageUrl = item[0].childNodes[0].data
        driver=self.driver
        driver.maximize_window()
        driver.get(pageUrl)
        

    def test_page_title(self):
        time.sleep(3)       
        assert 'Admission Tracker' == self.driver.title
        self.driver.close()
   
    def test_Admission_Workflow_validation(self):
        driver=self.driver
        driver.implicitly_wait(10)
        time.sleep(30)
        Cycletimeinformation = driver.find_element(By.XPATH,'/html/body/app-root/app-starter/div/div/app-dashboard/div[1]/div[2]/gridster/gridster-item[3]/div[1]/div[1]/b/span').text
        Workflowdashboard = driver.find_element(By.XPATH,'/html/body/app-root/app-starter/div/div/app-dashboard/div[1]/div[2]/gridster/gridster-item[1]/div[1]/div[1]/b/span').text
        lastupdatetime = driver.find_element(By.XPATH,'/html/body/app-root/app-starter/div/div/app-dashboard/div[1]/div[1]/div[3]/b').text
        print(lastupdatetime)
        # datetime object containing current date and time
        now = datetime.now()
        todaybefore5minutes = now - timedelta(minutes=1)
        todaybefore5minutes = todaybefore5minutes.strftime("%m/%d/%Y %H:%M:%S")
        assert 'Cycle Time Information' == Cycletimeinformation
        assert 'Workflow Dashboard' == Workflowdashboard
        assert todaybefore5minutes <= todaybefore5minutes
        self.driver.close()


# if __name__ == '__main__':
#     runner = HTMLTestRunner(
#         report_filepath="ReportFilePath",
#         title="Admission Streamliner Test report",
#         description="Admission Streamliner Automation Test report",
#         open_in_browser=True
#     )

#     # run the test
#     unittest.main(testRunner=runner)