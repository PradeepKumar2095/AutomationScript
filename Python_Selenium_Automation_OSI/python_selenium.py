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
        assert 'OSI App' == self.driver.title
        self.driver.close()
   
    def test_OSI_Board_validation(self):
        driver=self.driver
        time.sleep(5)
        driver.implicitly_wait(10)
        element_to_hover = driver.find_element(By.XPATH, '/html/body/app-root/app-starter/div/app-menu-sidebar/aside/div/nav/ul/li[7]/a/i')
        actions = ActionChains(driver)
        actions.move_to_element(element_to_hover).perform()
        actions.click(element_to_hover).perform()
        time.sleep(5)
        driver.implicitly_wait(10)
        barcodequeue = driver.find_element(By.XPATH,'/html/body/app-root/app-starter/div/div/gtm-board/div/div[2]/div/drag-scroll/div/div[1]/div/div[1]/gtm-column/div/div[1]/span[1]').text
        rphreview = driver.find_element(By.XPATH,'/html/body/app-root/app-starter/div/div/gtm-board/div/div[2]/div/drag-scroll/div/div[1]/div/div[4]/gtm-column/div/div[1]/span[1]').text
        time.sleep(2)
        assert rphreview== '   Review'
        assert barcodequeue== '   Queue'
        self.driver.close()

# if __name__ == '__main__':
#     runner = HTMLTestRunner(
#         report_filepath="ReportFilePath",
#         title="OSI Automation Test report",
#         description="OSI Automation Test report",
#         open_in_browser=True
#     )

#     # run the test
#     unittest.main(testRunner=runner)