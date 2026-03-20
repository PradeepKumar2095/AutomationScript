
import re
from playwright.sync_api import Page, expect
import RequestForm_Locator as L


class PSCalendarPage:
    def __init__(self, page: Page):
        self.page = page

    def goto_home(self):
        self.page.wait_for_timeout(10000)
        self.page.goto(L.BASE_URL, wait_until="domcontentloaded", timeout=60000)
        expect(self.page).to_have_title(re.compile(r"PS Calendar"), timeout=15000)
        self.page.wait_for_timeout(15000)

    def FilterList_and_Validate (self):
        self.page.wait_for_timeout(2000)
        self.page.locator(L.Week_Button).click()
        self.page.wait_for_timeout(800)
        self.page.locator(L.Next_Button).click()
        self.page.wait_for_timeout(800)
        self.page.locator(L.Today_Button).click()
        self.page.wait_for_timeout(1000)
        self.page.locator(L.Month_Button).click()
        self.page.wait_for_timeout(2000)

        self.page.locator(L.Excel_Export).click()
        self.page.wait_for_timeout(2000)
        container = self.page.locator(L.Export)
        container.get_by_role("button", name="Export").click()
        self.page.wait_for_timeout(2000)


        self.page.locator(L.New_Start).click()
        self.page.wait_for_timeout(1000)
        self.page.locator(L.New_Start).click()
        self.page.wait_for_timeout(2000)

        loader = self.page.locator(".loading-spinner")

        self.page.locator(L.User_Menu).click()
        expect(loader).to_be_hidden()
        self.page.wait_for_timeout(5000)

        # Hover_Completed_Menu=self.page.locator(L.Completed_List_Menu)
        # Hover_Completed_Menu.hover()
        # self.page.wait_for_timeout(800)
        # Hover_Completed_Menu.click()
        # self.page.wait_for_timeout(10000)
        # expect(loader).to_be_hidden()
        # self.page.locator(L.Completed_List_Filter).click()
        # self.page.wait_for_timeout(800)    
        # self.page.locator(L.Pharmacy_Filter_Field).click()
        # self.page.wait_for_timeout(800)
        # self.page.locator(L.Pharmacy_Filter_Field).fill("PHARMID")
        # dropdown_options = self.page.locator(L.Pharmacy_Filter_DD)
        
        # option = dropdown_options.locator(".ng-option")
        # exact = option.filter(has_text=re.compile(rf"\b{re.escape("PHARMID")}\b", re.IGNORECASE))
        # expect(exact).to_have_count(1)
        # exact.nth(0).click()
        # self.page.wait_for_timeout(1200)

        # self.page.locator(L.Search).click()
        # self.page.wait_for_timeout(10000)