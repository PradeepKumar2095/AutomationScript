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

# xml path
path = ("ConfigPath")
# validate the xml file
Config =minidom.parse(path)
# Get the field name
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
        
    # Validate the application title
    def test_page_title(self):
        # set the sleep time for app, to finding the title
        time.sleep(3)
        # validate the application title using assert method       
        assert 'Control Substance Audit Tracker' == self.driver.title
        #close the browser
        self.driver.close()

    # Validate Inventory list and verify the record count
    def test_inventory_list_validation(self):
        driver=self.driver
        driver.implicitly_wait(10)
        # set up the sleep time for List UI loading
        time.sleep(40)
        # Open the TOP Filter using xpath
        driver.find_element(By.XPATH,'/html/body/app-root/app-starter/div/div/app-inventorylist/div/div/section/div/div[1]/div/drag-scroll/div/div[1]/div/div/p-panel/div/div[1]/p-header/div/div[3]/div/inventorylist-filter/div/ul/li[1]/div/div[2]/div/a[2]/i').click()
        PharmacyID=item[2].childNodes[0].data
        # setup the Pharmacy Filter Pharmacy
        driver.find_element(By.XPATH,'/html/body/app-root/app-starter/div/div/app-inventorylist/div/div/section/div/div[1]/div/drag-scroll/div/div[1]/div/div/p-panel/div/div[1]/p-header/div/div[3]/div/inventorylist-filter/div/ul/li[2]/form/div[2]/div[1]/ng-select/div/div/div[2]/input').send_keys(PharmID)
        driver.find_element(By.XPATH,'/html/body/app-root/app-starter/div/div/app-inventorylist/div/div/section/div/div[1]/div/drag-scroll/div/div[1]/div/div/p-panel/div/div[1]/p-header/div/div[3]/div/inventorylist-filter/div/ul/li[2]/form/div[2]/div[1]/ng-select/ng-dropdown-panel/div[2]/div[2]/div/a/div/div').click()
        time.sleep(2)
        # Find and select the date for Date Range Selection
        driver.find_element(By.XPATH,'//*[@id="itemsDatePicker"]').click()
        time.sleep(2)
        # setup the date range
        driver.find_element(By.XPATH,'/html/body/div[5]/div[1]/ul/li[3]').click()
        time.sleep(1)
        # click Go, To filter the data (pharmacy, date range filter)
        driver.find_element(By.XPATH,'//*[@id="btnGo"]').click() 
        time.sleep(30)
        screenshotpath=item[4].childNodes[0].data
        # Take the UI screenshot and store it in common path
        driver.save_screenshot(screenshotpath + 'ControlsubstanceAudittracker_img01.png')
        driver.implicitly_wait(10)
        # Get the UI count
        connlastmonthcount = driver.find_element(By.XPATH,'//*[@id="grdInventoryLogList_pager_label"]').text
        connlastmonthcount =connlastmonthcount.split(' ')
        # Get the value from UI for validation
        transactionrecordcount=item[3].childNodes[0].data
        # Validate the UI count using assert method
        assert transactionrecordcount in connlastmonthcount
        #close the browser
        self.driver.close()

# Call the main function and store the Automation test result in html file.
# if __name__ == '__main__':
#     runner = HTMLTestRunner(
#         report_filepath="ReportFilePath",
#         title="Control substance Audit tracker Automation Test report",
#         description="Control substance Audit tracker Automation Test report",
#         open_in_browser=True
#     )

#     # run the test
#     unittest.main(testRunner=runner)