
import re
from playwright.sync_api import Page, expect, TimeoutError as PlaywrightTimeoutError
import RequestForm_Locator as L


class RevenueAnalyticsPage:
    def __init__(self, page: Page):
        self.page = page

    def goto_home(self):
        self.page.goto(L.BASE_URL, wait_until="domcontentloaded", timeout=60000)
        expect(self.page).to_have_title(re.compile(r"Pharmscript - Revenue Analytics"), timeout=15000)
        self.page.wait_for_timeout(1500)

    def FilterList_and_Validate (self, row_selector: str = "tr"):
        self.page.wait_for_timeout(2000)
        # self.page.locator(L.Billing_Date_GFilter).click()
        # self.page.wait_for_timeout(800)
        # self.page.locator(L.Previous_Month).click()
        # self.page.wait_for_timeout(800)
        # self.page.locator(L.Start_Date).click()
        # self.page.wait_for_timeout(1000)
        self.page.wait_for_selector (L.Grid_List, state="visible", timeout=30000)
        self.page.locator(L.Grid_List)
        self.page.wait_for_timeout(2000)
        
        grid = self.page.locator(L.Grid_List)
        self.page.wait_for_selector(L.Grid_List, state="visible", timeout=30000)

        pharm_row = grid.locator(row_selector).filter(has_text=L.PharmID).first

        try:
            pharm_row.wait_for(state="visible", timeout=15000)
        except PlaywrightTimeoutError:
            grid_el = grid.element_handle()
            if not grid_el:
                raise RuntimeError("Grid element handle not found for scrolling.")
            for _ in range(40):  # adjust passes if needed
                self.page.evaluate("(el) => el.scrollTop = el.scrollTop + el.clientHeight", grid_el)
                    
                pharm_row = grid.locator(row_selector).filter(has_text=L.PharmID).first
                if pharm_row.count() > 0:
                    try:
                        pharm_row.wait_for(state="visible", timeout=3000)
                        break
                    except PlaywrightTimeoutError:
                        pass
            else:
                raise RuntimeError(f"Could not find a row containing '{L.PharmID}' in the grid.")
        pharm_row.click(force=True)

        try:
            if getattr(L.Download_Excel,None):
                download_btn_in_row = pharm_row.locator(L.Download_Excel)
                if download_btn_in_row.count() > 0:
                    with self.page.expect_download() as di:
                        download_btn_in_row.first.click()
                    dl = di.value
                    final_name = dl.suggested_filename or f"{L.PharmID}_report.xlsx"
                    dl.save_as(final_name)
                    print(f"[OK] Downloaded to: {final_name}")
                    return
        except Exception as e:
            print(f"[WARN] Per-row download icon attempt failed: {e}")

        with self.page.expect_download() as di:
            self.page.click(L.Download_Excel)
        dl = di.value
        final_name = dl.suggested_filename or f"{L.PharmID}_report.xlsx"
        dl.save_as(final_name)
        print(f"[OK] Downloaded to: {final_name}")   
        self.page.wait_for_timeout(3000)