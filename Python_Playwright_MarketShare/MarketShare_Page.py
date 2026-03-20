
import re
from playwright.sync_api import Page, expect
import RequestForm_Locator as L

class MarketSharePage:
    def __init__(self, page: Page):
        self.page = page

    def goto_home(self):
        self.page.goto(L.BASE_URL, wait_until="domcontentloaded", timeout=60_000)
        expect(self.page).to_have_title(re.compile(r"Pharmscript – RevenueAnalyticsWeb_V1"), timeout=60_000)

    def FilterList_and_ValidateCount(self):
        self.page.wait_for_timeout(1200)
        self.page.get_by_title(L.Exclude_NDC_Option).click()
        self.page.wait_for_timeout(5200)