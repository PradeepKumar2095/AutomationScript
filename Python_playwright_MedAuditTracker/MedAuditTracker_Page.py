
import re
from playwright.sync_api import Page, expect
import RequestForm_Locator as L
from pathlib import Path
from datetime import datetime


def _save_screenshot(page, name: str, directory: Path = Path("ScreenshotPath"), full_page: bool = False):
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / f"{name}.png"
    page.screenshot(path=str(path), full_page=full_page)


class MedAuditTrackerPage:
    def __init__(self, page: Page):
        self.page = page

    def goto_home(self):
        self.page.goto(L.BASE_URL, wait_until="domcontentloaded", timeout=60000)
        expect(self.page).to_have_title(re.compile(r"Pharmscript - Non Control Drugs"), timeout=45000)
        self.page.wait_for_timeout(1500)

    def FilterList_and_Validate (self):
        loader = self.page.locator(".loading-spinner")
        expect(loader).to_be_hidden()
        self.page.wait_for_timeout(3000)
        # self.page.locator(L.Filter_Icon).click()
        # self.page.wait_for_timeout(800)
        self.page.locator(L.Pharmacy_Filter_Field).click()
        self.page.wait_for_timeout(800)
        self.page.locator(L.Pharmacy_Filter_Field).fill("PharmID")
        
        self.page.keyboard.press("Enter")
        self.page.wait_for_timeout(1200)

        self.page.locator(L.GPI_Field).click()
        self.page.wait_for_timeout(800)
        self.page.locator(L.GPI_Search_Field).fill('97052000000000')
        dropdown_options = self.page.locator(L.GPI_Field_DD)
        
        option = dropdown_options#.locator(".ng-option")
        exact = option.filter(has_text=re.compile(rf"\b{re.escape("97052000000000")}\b", re.IGNORECASE))
        expect(exact).to_have_count(1)
        exact.nth(0).click()

        self.page.locator(L.Search).click()
        expect(loader).to_be_hidden(timeout=10000)
        self.page.wait_for_timeout(10000)
        _save_screenshot(self.page, "Search_Results_FullPage", full_page=True)

        # Addendum_Menu = self.page.locator(L.Addendum)
        # Addendum_Menu.hover()
        # self.page.wait_for_timeout(800)
        # Addendum_Menu.click()
        self.page.wait_for_timeout(1500)
