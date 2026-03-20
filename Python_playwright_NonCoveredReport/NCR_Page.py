
import re
from playwright.sync_api import Page, expect
import RequestForm_Locator as L
from pathlib import Path
from datetime import datetime


def _save_screenshot(page, name: str, directory: Path = Path("ScreenshotPath"), full_page: bool = False):
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / f"{name}.png"
    page.screenshot(path=str(path), full_page=full_page)


class NCRPage:
    def __init__(self, page: Page):
        self.page = page

    def goto_home(self):
        self.page.goto(L.BASE_URL, wait_until="domcontentloaded", timeout=60000)
        expect(self.page).to_have_title(re.compile(r"Pharmscript - Report Module"), timeout=15000)
        self.page.wait_for_timeout(1500)
        actual_title = self.page.title()
        print(f"Page title displayed: {actual_title}")
        return actual_title

    def FilterList_and_Validate (self):
        self.page.wait_for_timeout(5000)
        # Reports_detail = self.page.locator(L.Reports)
        Reports_Select = self.page.get_by_role("link", name=L.Report_Name, exact=True)
        Reports_Select.wait_for(state="visible")
        Reports_Select.click()
        self.page.wait_for_timeout(1500)
        self.page.locator(L.Facility_Group).click()
        self.page.wait_for_timeout(500)
        self.page.locator(L.Facility_Group).fill(L.Facility_Group_Fill)
        self.page.wait_for_timeout(800)

        dropdown_options = self.page.locator(L.Facility_Group_Dropdown)
        
        option = dropdown_options.locator(".ng-option")
        exact = option.filter(has_text=re.compile(rf"\b{re.escape(L.Facility_Group_Fill)}\b", re.IGNORECASE))
        expect(exact).to_have_count(1)
        exact.nth(0).click()
        self.page.wait_for_timeout(1200)

        self.page.locator(L.Start_Date).clear()
        self.page.wait_for_timeout(1500)
        self.page.locator(L.Start_Date).fill(L.Start_Date_Fill)
        self.page.wait_for_timeout(1500)
        self.page.locator(L.End_Date).clear()
        self.page.wait_for_timeout(1500)
        self.page.locator(L.End_Date).fill(L.End_Date_Fill)
        self.page.wait_for_timeout(1500)
        self.page.locator (L.Submit).click()
        self.page.wait_for_timeout(800)
        
        confirmation = self.page.locator(L.Confirmation_Message)
        if confirmation.count() > 0:
            confirmation.first.wait_for(state="visible", timeout=5000)
            message_text = (confirmation.first.text_content() or "").strip()
            print(f"Confirmation text: {message_text}")
            
            if getattr(L, "Confirmation_Message_Text", None):
                            expected = L.Confirmation_Message_Text.strip()
                            assert expected.lower() in message_text.lower(), (
                                f"Confirmation text mismatch.\n"
                                f"Expected: {expected}\n"
                                f"Actual:   {message_text}"
                            )
            ok_button = confirmation.first.get_by_role("button", name="Ok")
            # Alternative options:
            # ok_button = confirmation.first.locator('text=ok')          # text engine
            # ok_button = confirmation.first.locator('[data-test="ok"]') # data attribute
            # ok_button = confirmation.first.locator('button:has-text("ok")')

            expect(ok_button).to_be_visible(timeout=5000)
            ok_button.click()
        else:
            print("Confirmation text Not Appeared")
        self.page.wait_for_timeout(1500)

        expected_header = L.Report_History_Header    # <-- change this to the expected text
        
        header_locator = self.page.locator(L.Report_History)
        header_locator.wait_for(state="visible")
        
        actual_text = header_locator.inner_text().strip()
        
        if actual_text != expected_header:
            raise AssertionError(f"❌ Header mismatch! Expected: '{expected_header}', Found: '{actual_text}'")
        
        print(f"✔ Header validated successfully")
        _save_screenshot(self.page, "Search_Results_FullPage", full_page=True)
        self.page.wait_for_timeout(2000)