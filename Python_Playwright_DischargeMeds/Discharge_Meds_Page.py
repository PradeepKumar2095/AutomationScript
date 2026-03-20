
import re
from pathlib import Path
from playwright.sync_api import Page, expect
import RequestForm_Locator as L


class DischargeMedsPage:
    def __init__(self, page: Page):
        self.page = page

    def goto_home(self):
        self.page.goto(L.BASE_URL, wait_until="domcontentloaded", timeout=60000)
        expect(self.page).to_have_title(re.compile(r"Pharmscript - Discharge Meds"), timeout=15000)
        self.page.wait_for_timeout(800)

    def FilterList_and_ValidateCount (self):
        self.page.wait_for_timeout(2000)
        self.page.locator(L.Date_Range_Field).click()
        self.page.wait_for_timeout(800)
        self.page.locator(L.Last_Month_Option_DateRange).click()
        self.page.wait_for_timeout(2000)
        self.page.locator(L.Filter_List).click()
        self.page.wait_for_timeout(6000)
        self.page.locator(L.ReportUI).click()
        self.page.wait_for_timeout(1500)
        # self.page.locator(L.Facility).click()
        # self.page.wait_for_timeout(800)    
        self.page.locator(L.Report_Type_Field).click()
        self.page.wait_for_timeout(800)
        dropdown_options = self.page.locator(L.Report_Type)
        
        option = dropdown_options.locator(".ng-option")
        exact = option.filter(has_text=re.compile(rf"\b{re.escape("Account Balance Report")}\b", re.IGNORECASE))
        expect(exact).to_have_count(1)
        exact.nth(0).click()
        self.page.wait_for_timeout(1200)

        self.page.locator(L.Generate_Report).click()
        self.page.wait_for_timeout(6000)