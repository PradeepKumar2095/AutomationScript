
import re
import os
from pathlib import Path
from playwright.sync_api import Page, expect
import RequestForm_Locator as L


class PDPFormularyPage:
    def __init__(self, page: Page):
        self.page = page

    def goto_home(self):
        self.page.goto(L.BASE_URL, wait_until="domcontentloaded", timeout=60000)
        expect(self.page).to_have_title(re.compile(r"PDP-Formulary"), timeout=15000)
        self.page.wait_for_timeout(800)

    
    def FilterList_and_ValidateCount(self):
        self.page.wait_for_timeout(2000)
        self.page.locator(L.Date_Range_Field).click()
        self.page.wait_for_timeout(800)
        self.page.locator(L.This_Year_Option_DateRange).click()
        self.page.wait_for_timeout(2000)
        self.page.locator(L.Filter_List).click()
        self.page.wait_for_timeout(5000)
        self.page.locator(L.Excel_Export).click()
        self.page.wait_for_timeout(1500)

        table = self.page.locator(L.List_Grid)
        expect(table).to_be_visible(timeout=5000)

        rows = table.locator("tr")
        expect(rows.first).to_be_visible(timeout=5000)
        assert rows.count() > 0, "No rows found in the table"

        first_row = rows.nth(0)
        download_button = first_row.locator(L.Download_File)
        expect(download_button).to_be_visible(timeout=2000)

        # Use self.page.expect_download()
        with self.page.expect_download() as download_info:
            download_button.click()

        download = download_info.value
        download.save_as("downloaded_file.xlsx")

        assert os.path.exists("downloaded_file.xlsx"), "File was not downloaded"
    
        self.page.wait_for_timeout(2000)