
import re
import os
from pathlib import Path
from playwright.sync_api import Page, expect
import RequestForm_Locator as L


class M3PPage:
    def __init__(self, page: Page):
        self.page = page

    def goto_home(self):
        self.page.goto(L.BASE_URL, wait_until="domcontentloaded", timeout=60000)
        expect(self.page).to_have_title(re.compile(r"Pharmscript – M3P Letters Process"), timeout=15000)
        print(f'The title is ')
        self.page.wait_for_timeout(800)

    
    def FilterList_and_ValidateCount(self):
        self.page.wait_for_timeout(2000)
        self.page.locator(L.Download_Loaded_File).click()
        self.page.wait_for_timeout(2500)
    
        grid = self.page.locator(L.List_grid)
        expect(grid).to_be_attached(timeout=15000)
    
        self.page.locator(L.Invalid_Count).click()         
        self.page.wait_for_timeout(2000)
        self.page.locator(L.Cancel).click()
        self.page.wait_for_timeout(2500)