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

   
    def test_patient_demographics_details(self):
        driver=self.driver
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH,'/html/body/app-root/div/app-layout-shell/div/div/div/main/app-admin-dashboard1/div/section[2]/div/div[2]/div/ng-select/div[1]/div/div[2]/input').send_keys("values")
        time.sleep(10)
        driver.find_element(By.XPATH,'/html/body/app-root/div/app-layout-shell/div/div/div/main/app-admin-dashboard1/div/section[2]/div/div[2]/div/ng-select/ng-dropdown-panel/div[2]/div[2]/div/div').click()
        time.sleep(5)
        Get_PatientPharmID = driver.find_element(By.XPATH,'/html/body/app-root/div/app-layout-shell/div/div/div/main/app-patientinfo-list/div[1]/section/div/div/div[2]/div[1]/table[1]/tr[1]/td[2]/label').text
        Get_PatientFacilityID = driver.find_element(By.XPATH,'/html/body/app-root/div/app-layout-shell/div/div/div/main/app-patientinfo-list/div[1]/section/div/div/div[2]/div[1]/table[1]/tr[2]/td[2]/label').text
        Get_PatientDOB = driver.find_element(By.XPATH,'/html/body/app-root/div/app-layout-shell/div/div/div/main/app-patientinfo-list/div[1]/section/div/div/div[2]/div[1]/table[1]/tr[5]/td[2]/label').text
        Get_Patientzip = driver.find_element(By.XPATH,'/html/body/app-root/div/app-layout-shell/div/div/div/main/app-patientinfo-list/div[1]/section/div/div/div[2]/div[1]/table[1]/tr[9]/td[2]/label').text
        Get_PatientState = driver.find_element(By.XPATH,'/html/body/app-root/div/app-layout-shell/div/div/div/main/app-patientinfo-list/div[1]/section/div/div/div[2]/div[1]/table[1]/tr[9]/td[4]/label').text
        time.sleep(10)
        assert Get_PatientFacilityID == ': FacID'
        assert Get_PatientPharmID == ': PharmID'
        assert Get_PatientDOB == ': DOB'
        assert Get_Patientzip == ': PatientZip'
        assert Get_PatientState == ': State'
        driver.close()

    def test_page_title(self):
        time.sleep(3)       
        assert 'Collections' == self.driver.title
        self.driver.close()




# if __name__ == '__main__':
#     runner = HTMLTestRunner(
#         report_filepath="ReportFilePath",
#         title="Collection Automation Test report",
#         description="Collection Automation Test report",
#         open_in_browser=True
#     )

#     # run the test
#     unittest.main(testRunner=runner)