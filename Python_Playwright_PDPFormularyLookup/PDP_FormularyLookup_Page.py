
import re
import os
from pathlib import Path
from playwright.sync_api import Page, expect
import RequestForm_Locator as L


class PDPFormularyLookupPage:
    def __init__(self, page: Page):
        self.page = page

    def goto_home(self):
        self.page.goto(L.BASE_URL, wait_until="domcontentloaded", timeout=60000)
        expect(self.page).to_have_title(re.compile(r"PDP Formulary Lookup"), timeout=15000)
        self.page.wait_for_timeout(800)

    
    def FilterList_and_ValidateCount(self):
        #pharmacy select
        self.page.wait_for_timeout(2000)
        self.page.locator(L.Pharmacy_Field).click()
        self.page.wait_for_timeout(800)
        self.page.locator(L.Pharmacy_Field).fill(L.Pharmacy_Fill)
        dropdown_options = self.page.locator(L.Pharmacy_Dropdown)
        
        option = dropdown_options.locator(".ng-option")
        exact = option.filter(has_text=re.compile(rf"\b{re.escape(L.Pharmacy_Fill)}\b", re.IGNORECASE))
        expect(exact).to_have_count(1)
        exact.nth(0).click()

        #rxno select
        self.page.wait_for_timeout(800)
        self.page.locator(L.RxNo_Field).click()
        self.page.wait_for_timeout(800)
        self.page.locator(L.RxNo_Field).fill(L.Rxno_Fill)
        self.page.wait_for_timeout(800)

        #checkbox select
        self.page.locator(L.ViewNonMatchedMB_GPI_Checkbox).click()
        self.page.wait_for_timeout(800)
        loader = self.page.locator(".loading-spinner")
        self.page.locator(L.Serach_Button).click()
        
        expect(loader).to_be_hidden()
        self.page.wait_for_timeout(20000)

        
        
        def to_locator(selector: str):
            if isinstance(selector, str) and (selector.startswith("/") or selector.startswith("//")):
                return self.page.locator(f"xpath={selector}")
            return self.page.locator(selector)

        def safe_text(selector_or_loc) -> str:
            loc = selector_or_loc if hasattr(selector_or_loc, "text_content") else to_locator(selector_or_loc)
            try:
                txt = loc.first.text_content(timeout=3000)
                return (txt or "").strip()
            except Exception:
                return ""

        mimd_text = safe_text(L.MOP)
        plan_id_text = safe_text(L.Plan_ID)

        has_mimd = "MOP" in (mimd_text or "").upper()
        is_mimd_absent = not has_mimd

        plan_value = re.sub(r"(?i)\bplan\s*id\b[:]?\s*", "", plan_id_text or "").strip()
        is_plan_id_blank = (plan_value == "")

        # --- Note validation only ---
        NOTE_TEXT = L.Note_Text 
        note_by_text = self.page.get_by_text(NOTE_TEXT, exact=True)
        note_loc = to_locator(L.Note) 

        if is_mimd_absent and is_plan_id_blank:
            expect(note_by_text).to_be_visible(timeout=35000)
            expect(loader).to_be_hidden()
            expect(note_by_text).to_have_text(NOTE_TEXT, timeout=35000)
        else:
            if note_by_text.count() > 0:
                try:
                    expect(note_by_text).to_be_hidden(timeout=7000)
                except Exception:
                    try:
                        expect(note_loc).to_be_hidden(timeout=7000)
                    except Exception:
                        assert safe_text(L.Note) == "", \
                            "Note should not be present when MIMD is present or Plan ID has value."

        self.page.wait_for_timeout(10000)

    def FilterList_and_Validate2(self):
        #pharmacy select
        self.page.wait_for_timeout(2000)
        self.page.locator(L.Pharmacy_Field).click()
        self.page.wait_for_timeout(800)
        self.page.locator(L.Pharmacy_Field).fill(L.Pharmacy_Fill2)
        dropdown_options = self.page.locator(L.Pharmacy_Dropdown)
        
        option = dropdown_options.locator(".ng-option")
        exact = option.filter(has_text=re.compile(rf"\b{re.escape(L.Pharmacy_Fill2)}\b", re.IGNORECASE))
        expect(exact).to_have_count(1)
        exact.nth(0).click()

        #rxno select
        self.page.wait_for_timeout(800)
        self.page.locator(L.RxNo_Field).click()
        self.page.wait_for_timeout(800)
        self.page.locator(L.RxNo_Field).fill(L.Rxno_Fill2)
        self.page.wait_for_timeout(800)

        #checkbox select
        self.page.locator(L.ViewNonMatchedMB_GPI_Checkbox).click()
        self.page.wait_for_timeout(800)
        loader = self.page.locator(".loading-spinner")
        self.page.locator(L.Serach_Button).click()
        
        expect(loader).to_be_hidden()
        self.page.wait_for_timeout(20000)

        
        
        def to_locator(selector: str):
            if isinstance(selector, str) and (selector.startswith("/") or selector.startswith("//")):
                return self.page.locator(f"xpath={selector}")
            return self.page.locator(selector)

        def safe_text(selector_or_loc) -> str:
            loc = selector_or_loc if hasattr(selector_or_loc, "text_content") else to_locator(selector_or_loc)
            try:
                txt = loc.first.text_content(timeout=3000)
                return (txt or "").strip()
            except Exception:
                return ""

        mimd_text = safe_text(L.MOP)
        plan_id_text = safe_text(L.Plan_ID)

        has_mimd = "MIMD" in (mimd_text or "").upper()
        is_mimd_absent = not has_mimd

        plan_value = re.sub(r"(?i)\bplan\s*id\b[:]?\s*", "", plan_id_text or "").strip()
        is_plan_id_blank = (plan_value == "")

        # --- Note validation only ---
        NOTE_TEXT = L.Note_Text 
        note_by_text = self.page.get_by_text(NOTE_TEXT, exact=True)
        note_loc = to_locator(L.Note) 

        if is_mimd_absent and is_plan_id_blank:
            expect(note_by_text).to_be_visible(timeout=35000)
            expect(loader).to_be_hidden()
            expect(note_by_text).to_have_text(NOTE_TEXT, timeout=35000)
        else:
            if note_by_text.count() > 0:
                try:
                    expect(note_by_text).to_be_hidden(timeout=7000)
                except Exception:
                    try:
                        expect(note_loc).to_be_hidden(timeout=7000)
                    except Exception:
                        assert safe_text(L.Note) == "", \
                            "Note should not be present when MIMD is present or Plan ID has value."

        self.page.wait_for_timeout(10000)