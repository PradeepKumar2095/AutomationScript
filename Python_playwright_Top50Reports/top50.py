
import re
from playwright.sync_api import Page, expect
import RequestForm_Locator as L
from pathlib import Path
from datetime import datetime


def _save_screenshot(page, name: str, directory: Path = Path(r"ScreenshotPath"), full_page: bool = False):
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / f"{name}.png"
    page.screenshot(path=str(path), full_page=full_page)


class Top50Page:
    def __init__(self, page: Page):
        self.page = page

    def goto_home(self):
        self.page.goto(L.BASE_URL, wait_until="domcontentloaded", timeout=60000)
        expect(self.page).to_have_title(re.compile(r"Pharmscript - Report Module"), timeout=15000)
        self.page.wait_for_timeout(3000)
        actual_title = self.page.title()
        print(f"Page title displayed: {actual_title}")
        return actual_title

    def FilterList_and_Validate(self):
        print("Locating report checkbox...")
    
        # Locate the leaf <li> that has exact report text
        report_li = self.page.locator(
            "//li[contains(@class,'ui-igtree-node-nochildren')]"
            "//a[normalize-space()='Top 50 Brands and Generics Report']/ancestor::li[1]"
        ).first
    
        # Locate the checkbox inside that <li>
        checkbox = report_li.locator("span[data-role='checkbox']").first
    
        # Ensure the checkbox is checked
        data_chk = checkbox.get_attribute("data-chk")
        if data_chk != "on":
            checkbox.click()
            print("Checkbox checked for Top 50 Brands and Generics Report")
        else:
            print("Checkbox already checked")
    
        self.page.wait_for_timeout(1000)
    
        # Fill the start date
        print("Filling start date...")
        date_input = self.page.locator(L.Start_Date)
        expect(date_input).to_be_visible()
        date_input.click()
        date_input.fill("")
        date_input.fill(L.Start_Date_Fill)
        print(f"Start date filled with: {L.Start_Date_Fill}")
        self.page.wait_for_timeout(1000)
    
        # Click Submit
        print("Clicking Submit button...")
        submit = self.page.locator(L.Submit)
        expect(submit).to_be_enabled()
        submit.click()
        self.page.wait_for_timeout(1000)
    
        # Wait for confirmation
        print("Waiting for confirmation dialog...")
        confirmation = self.page.locator(L.Confirmation_Message)
        expect(confirmation).to_be_visible(timeout=10000)
        message_text = confirmation.inner_text().strip()
        print(f"Confirmation text: {message_text}")
        assert L.Confirmation_Message_Text.lower() in message_text.lower(), (
            f"Expected confirmation message not found.\nExpected: {L.Confirmation_Message_Text}\nActual: {message_text}"
        )
    
        # Click OK button
        ok_button = confirmation.get_by_role("button", name="Ok")
        expect(ok_button).to_be_visible()
        ok_button.click()
    
        # Validate Report History header
        print("Validating Report History header...")
        header = self.page.locator(L.Report_History)
        expect(header).to_be_visible()
        actual_header = header.inner_text().strip()
        assert actual_header == L.Report_History_Header, (
            f"Header mismatch!\nExpected: {L.Report_History_Header}\nFound: {actual_header}"
        )
        print("Report History header validated successfully")
        self.page.wait_for_timeout(3000)
        # Take screenshot
        _save_screenshot(self.page, "Top50_Report_Success", full_page=True)
        print("Screenshot saved")
        self.page.wait_for_timeout(2000)