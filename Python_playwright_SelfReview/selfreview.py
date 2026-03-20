import re
from playwright.sync_api import Page, expect
import RequestForm_Locator as L
import conftest 
 
class SelfReviewPage:
    def __init__(self, page: Page):
        self.page = page
 
    def goto_home(self):
        print("Navigating to Self-Review Tracker home page...")
        self.page.goto(L.BASE_URL, wait_until="domcontentloaded", timeout=60000)
        expect(self.page).to_have_title(re.compile(r"Self-Review Tracker"), timeout=15000)
        print("Page Loaded Successfully...")
        self.page.wait_for_timeout(1500)

    def select_facility_go_and_reset(self):
    # Activate dropdown
        self.page.wait_for_timeout(40000)
        print(" Select Facility: {L.FACILITYID}") 
        facility_input = self.page.locator(L.FACILITY_INPUT)
        expect(facility_input).to_be_visible()
        facility_input.click()
        facility_input.fill(L.FACILITYID)
        print("Facility selected Successfully...")
        self.page.wait_for_timeout(3000)
    
        #  EXACT MATCH: select only "FacID" (not FacID)
        exact_option = self.page.locator(
            "ng-dropdown-panel .ng-option .col-sm-3",
            has_text=L.FACILITYID.upper()
        ).first
 
        expect(exact_option).to_be_visible(timeout=5000)
 
    # Click the parent ng-option
        exact_option.locator("xpath=ancestor::div[contains(@class,'ng-option')]").click()
 
    # Click Go
        print("Go button is clicked and records are loaded into the grid Successfully...")
        go_btn = self.page.locator(L.GO_BUTTON)
        expect(go_btn).to_be_enabled()
        go_btn.click()
 
        # Wait for results
        self.page.wait_for_timeout(6000)

        #Excel Export
        print("Excel button is clicked and records are exported Successfully...")
        excel_btn = self.page.locator(L.EXCEL_BUTTON)
        expect(excel_btn).to_be_enabled()
        excel_btn.click()
        self.page.wait_for_timeout(5000)
    
        # # Click Reset
        # print("Reset button is clicked and applied filter is removed Successfully...")
        # reset_btn = self.page.locator(L.RESET_BUTTON)
        # expect(reset_btn).to_be_enabled()
        # reset_btn.click()
        # self.page.wait_for_timeout(40000)

        # #Excel Export
        # excel_btn = self.page.locator(L.EXCEL_BUTTON)
        # expect(excel_btn).to_be_enabled()
        # excel_btn.click()
        # self.page.wait_for_timeout(6000)

    def click_edit_first_row(self):
        # Wait until at least one edit icon is visible
        print("Edit icon is clicked and edit UI is loaded into the Successfully...")
        edit_icon = self.page.locator(L.EDIT_ICON).first
        edit_icon.wait_for(state="visible", timeout=30000)
        edit_icon.click()
        self.page.wait_for_timeout(5000)


