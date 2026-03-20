import os
import time
import unittest
from datetime import datetime, timedelta

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from xml.dom import minidom

# Load config
CONFIG_PATH = "ConfigPath"
Config = minidom.parse(CONFIG_PATH)
item = Config.getElementsByTagName('item')

class Pytest(unittest.TestCase):

    def setUp(self):
        edge_driver_path = "EdgeDriverPath"
        service = EdgeService(executable_path=edge_driver_path)
        options = EdgeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Edge(service=service, options=options)
        self.wait = WebDriverWait(self.driver, 20)
        pageUrl = item[0].childNodes[0].data
        driver=self.driver
        driver.maximize_window()
        driver.get(pageUrl)

    def test_thirdparty_dashboard_details(self):
        driver=self.driver
        driver.implicitly_wait(20)
        Get_Pharmid = driver.find_element(By.XPATH,'/html/body/app-root/app-admin/div/summary/div[2]/div/section/div/div/div/div/div/div/div/div/div/div/div[2]/table/tbody[1]/tr[5]/td[1]/strong').text
        Get_hubname = driver.find_element(By.XPATH,'/html/body/app-root/app-admin/div/summary/div[2]/div/section/div/div/div/div/div/div/div/div/div/div/div[2]/table/tbody[1]/tr[1]/td[1]/strong').text
        Get_hubcountfor_1st_run_ECS = driver.find_element(By.XPATH,'/html/body/app-root/app-admin/div/summary/div[2]/div/section/div/div/div/div/div/div/div/div/div/div/div[2]/table/tbody[1]/tr[1]/td[6]').text
        time.sleep(15)
        covert_Get_hubcountfor_1st_run_ECS = int(Get_hubcountfor_1st_run_ECS)
        assert Get_Pharmid == 'PharmID'
        assert Get_hubname == 'HubName'
        assert covert_Get_hubcountfor_1st_run_ECS >= 1
        driver.close()

    def test_page_title(self):
        
        expected_title = 'Pharmscript - 3rd Party Dashboard'
        self.wait.until(EC.title_is(expected_title))
        self.assertEqual(expected_title, self.driver.title)

    # if __name__ == '__main__':
#     # ensure reports directory exists
#     reports_dir = "ReportsPath"
#     try:
#         os.makedirs(reports_dir, exist_ok=True)
#     except Exception:
#         pass

#     runner = HtmlTestRunner.HTMLTestRunner(
#         output=reports_dir,
#         report_title="3rdparty dashboard Automation Test report",
#         descriptions="3rdparty dashboard Automation Test report",
#     )

#     # run the tests with the HTML runner
#     unittest.main(testRunner=runner)
