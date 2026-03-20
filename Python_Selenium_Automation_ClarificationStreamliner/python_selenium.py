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
        assert 'Pharmscript - Clarifications Streamliner' == self.driver.title
        self.driver.close()
   
    def test_board_details_validation(self):
        driver=self.driver
        driver.implicitly_wait(10)
        readytowork = driver.find_element(By.XPATH,'/html/body/app-root/app-starter/div/div/gtm-board/div/div[2]/div/drag-scroll/div/div[1]/div/div[2]/gtm-column/div/div[1]/span[1]')
        completed = driver.find_element(By.XPATH,'/html/body/app-root/app-starter/div/div/gtm-board/div/div[2]/div/drag-scroll/div/div[1]/div/div[5]/gtm-column/div/div[1]/span[1]')
        workinprogress = driver.find_element(By.XPATH,'/html/body/app-root/app-starter/div/div/gtm-board/div/div[2]/div/drag-scroll/div/div[1]/div/div[3]/gtm-column/div/div[1]/span[1]')
        backlog = driver.find_element(By.XPATH,'/html/body/app-root/app-starter/div/div/gtm-board/div/div[2]/div/drag-scroll/div/div[1]/div/div[1]/gtm-column/div/div[1]/span[1]')
        backlogcount = driver.find_element(By.XPATH,'/html/body/app-root/app-starter/div/div/gtm-board/div/div[2]/div/drag-scroll/div/div[1]/div/div[1]/gtm-column/div/div[1]/span[2]')
        time.sleep(5)
        self.driver.implicitly_wait(10)
        readytowork = readytowork.text
        completed = completed.text
        workinprogress = workinprogress.text
        backlog = backlog.text
        backlogcount = backlogcount.text
        backlogcount = backlogcount.split('/')
        assert '  Ready To Work' == readytowork
        assert '  Completed' == completed
        assert '  Work In Progress' == workinprogress
        assert '  Backlog' == backlog
        assert count >= int(backlogcount[0])
        driver.implicitly_wait(10)
        self.driver.close()
    
    def test_completed_list_validation(self):
        driver=self.driver
        time.sleep(5)
        driver.implicitly_wait(10)
        element_to_hover = driver.find_element(By.XPATH, '/html/body/app-root/app-starter/div/app-menu-sidebar/aside/div/nav/ul/li[3]/a/i')
        actions = ActionChains(driver)
        actions.move_to_element(element_to_hover).perform()
        actions.click(element_to_hover).perform()
        time.sleep(3)
        driver.implicitly_wait(10)
        driver.find_element(By.NAME, 'dtDate').click()
        time.sleep(2)
        driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/ul/li[3]').click()
        time.sleep(2)
        driver.find_element(By.XPATH,'/html/body/app-root/app-starter/div/div/app-completed-items-list/drag-scroll/div/div[1]/div/div[2]/div[1]/div/form/div/div/div[6]/div/button[1]').click()
        time.sleep(2)
        completedclarificationcount = driver.find_element(By.XPATH,'/html/body/app-root/app-starter/div/div/app-completed-items-list/drag-scroll/div/div[1]/div/div[2]/div[2]/div/ig-grid/div/div[21]/span').text
        self.driver.implicitly_wait(16)
        completedclarificationcount = completedclarificationcount.split(' ')
        assert 24270 == int(completedclarificationcount[4])
        driver.implicitly_wait(16)
        self.driver.close()

    def test_completed_list_validation_incorrectcount(self):
        driver=self.driver
        time.sleep(5)
        driver.implicitly_wait(10)
        element_to_hover = driver.find_element(By.XPATH, '/html/body/app-root/app-starter/div/app-menu-sidebar/aside/div/nav/ul/li[3]/a/i')
        actions = ActionChains(driver)
        actions.move_to_element(element_to_hover).perform()
        actions.click(element_to_hover).perform()
        time.sleep(3)
        driver.implicitly_wait(10)
        driver.find_element(By.NAME, 'dtDate').click()
        time.sleep(2)
        driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/ul/li[3]').click()
        time.sleep(2)
        driver.find_element(By.XPATH,'/html/body/app-root/app-starter/div/div/app-completed-items-list/drag-scroll/div/div[1]/div/div[2]/div[1]/div/form/div/div/div[6]/div/button[1]').click()
        time.sleep(2)
        completedclarificationcount = driver.find_element(By.XPATH,'/html/body/app-root/app-starter/div/div/app-completed-items-list/drag-scroll/div/div[1]/div/div[2]/div[2]/div/ig-grid/div/div[21]/span').text
        self.driver.implicitly_wait(10)
        completedclarificationcount = completedclarificationcount.split(' ')
        assert 1 !=  int(completedclarificationcount[4])
        driver.implicitly_wait(10)



# if __name__ == '__main__':
#     runner = HTMLTestRunner(
#         report_filepath="ReportFilePath",
#         title="Clarification Streamliner Automation Test report",
#         description="Clarification Streamliner Automation Test report",
#         open_in_browser=True
#     )

#     # run the test
#     unittest.main(testRunner=runner)