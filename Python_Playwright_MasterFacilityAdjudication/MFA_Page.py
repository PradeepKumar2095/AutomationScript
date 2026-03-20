
import re
from playwright.sync_api import Page, expect
import RequestForm_Locator as L

class MFAPage:
    def __init__(self, page: Page):
        self.page = page

    def goto_home(self):
        self.page.goto(L.BASE_URL, wait_until="domcontentloaded", timeout=60_000)
        expect(self.page).to_have_title(re.compile(r"Pharmscript - Facility Adjudication"), timeout=60_000)

    def FilterList_and_ValidateCount(self):
        # Dismiss modal/banner if present
        cancel_btn = self.page.locator(L.Cancel)
        if cancel_btn.count() > 0 and cancel_btn.is_visible():
            cancel_btn.click()

        # Open filters
        self.page.locator(L.Filter_Icon).click()
        expect(self.page.locator(L.Pharmacy_Filed)).to_be_visible()
        self.page.locator(L.Pharmacy_Filed).click()

        # 1) Click the Pharmacy display input (readonly)
        pharmacy_display = self.page.locator('igc-input >> css=input[placeholder="Please select Pharmacy"]').first
        expect(pharmacy_display).to_be_visible()
        pharmacy_display.click()

        # 2) Type into the search input in the opened dropdown
        search_box = self.page.locator('igc-input >> css=input[placeholder="Search"]').first
        if search_box.count() > 0:
            expect(search_box).to_be_visible()
            search_box.fill(L.Pharmacy)

        # 3) Pick the option
        items = self.page.locator('igc-combo >> css=igc-combo-item')
        if items.count() == 0:
            # If the dropdown is framework-portal-based or uses ng-select elsewhere
            items = self.page.locator('.ng-option')

        exact = items.filter(has_text=re.compile(rf'^\s*{re.escape(L.Pharmacy)}\s*$', re.IGNORECASE))
        if exact.count() == 0:
            exact = items.filter(has_text=re.compile(re.escape(L.Pharmacy), re.IGNORECASE))

        expect(exact).to_have_count(1)
        exact.first.click()

        # Submit / search
        search_btn = self.page.locator(L.Search)
        expect(search_btn).to_be_enabled()
        search_btn.click()
        self.page.wait_for_timeout(2500)
