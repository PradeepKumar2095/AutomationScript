
import re
from playwright.sync_api import Page, expect
import RequestForm_Locator as L


class BAETrackerPage:
    def __init__(self, page: Page):
        self.page = page

    def goto_home(self):
        self.page.goto(L.BASE_URL, wait_until="domcontentloaded", timeout=60000)
        expect(self.page).to_have_title(re.compile(r"BAE Tracker"), timeout=15000)
        self.page.wait_for_timeout(1500)

    def FilterList_and_Validate (self):
        self.page.wait_for_timeout(2000)
        self.page.locator(L.Request_Page).click()
        self.page.wait_for_timeout(2000)
        self.page.locator(L.Request_Detail_UI).click()
        self.page.wait_for_timeout(1200)
        self.page.locator(L.Facility).click()  # open ng-select
        self.page.locator(L.Facility_Input).fill(L.Facility_ID, timeout=2000)

        options = self.page.locator(L.Facility_DD)
        exact = options.filter(has_text=re.compile(rf"\b{re.escape(L.Facility_ID)}\b", re.IGNORECASE))
        expect(exact).to_have_count(1)
        exact.first.click()
        self.page.wait_for_timeout(1200)
        loader = self.page.locator(".loading-spinner")
        self.page.locator(L.Cancel).click()
        expect(loader).to_be_hidden()

        Pharmacy_Filter=self.page.locator(L.Pharmacy)
        Pharmacy_Filter.click()
        self.page.wait_for_timeout(800)
        self.page.locator(L.Pharmacy_Input).fill(L.Pharmacy_Fill)
        dropdown_options = self.page.locator(L.Pharmacy_DD)

        option = dropdown_options.locator(".ng-option")
        exact = option.filter(has_text=re.compile(rf"\b{re.escape(L.Pharmacy_Fill)}\b", re.IGNORECASE))
        expect(exact).to_have_count(1)
        exact.nth(0).click()
        self.page.wait_for_timeout(1200)
        self.page.locator(L.Go).click()
        self.page.wait_for_timeout(5)

        Hover_Completed_Menu=self.page.locator(L.Board_UI)
        Hover_Completed_Menu.hover()
        self.page.wait_for_timeout(800)
        Hover_Completed_Menu.click()
        self.page.wait_for_timeout(10000)
        expect(loader).to_be_hidden()
        self.page.locator(L.Filter).click()
        self.page.wait_for_timeout(800)    
        self.page.locator(L.Filter_Pharmacy).click()
        self.page.wait_for_timeout(800)
        self.page.locator(L.Filter_Pharmacy_Input).fill(L.Filter_Pharmacy_Fill)
        dropdown_options = self.page.locator(L.Filter_Pharmacy_DD)
        
        option = dropdown_options.locator(".ng-option")
        exact = option.filter(has_text=re.compile(rf"\b{re.escape(L.Filter_Pharmacy_Fill)}\b", re.IGNORECASE))
        expect(exact).to_have_count(1)
        exact.nth(0).click()
        self.page.wait_for_timeout(1200)

        self.page.locator(L.Filter_Search).click()
        expect(loader).to_be_hidden()
        self.page.wait_for_timeout(10000)