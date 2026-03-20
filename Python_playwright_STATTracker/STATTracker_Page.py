
import re
from playwright.sync_api import Page, expect
import RequestForm_Locator as L


class STATTrackerPage:
    def __init__(self, page: Page):
        self.page = page

    def goto_home(self):
        self.page.goto(L.BASE_URL, wait_until="domcontentloaded", timeout=60000)
        expect(self.page).to_have_title(re.compile(r"STAT Tracker"), timeout=15000)
        self.page.wait_for_timeout(1500)

    def FilterList_and_Validate (self):
        locator = self.page.locator(L.request_form_menu)
        locator.wait_for(state="visible")
        locator.hover()
        self.page.wait_for_timeout(300)
        locator.click()
        self.page.wait_for_timeout(1500)
        req_field = self.page.locator(L.Request_By)
        req_field.wait_for(state="visible")
        req_field.fill(L.req_by)
        self.page.wait_for_timeout(800)
    
        # Fill and Select Facility
        fac_input = self.page.locator(L.Facility_Field)
        fac_input.wait_for(state="visible")
        fac_input.click()
        self.page.wait_for_timeout(500)
        fac_input.fill(L.Facility)
        self.page.wait_for_timeout(1200)
    
        dropdown_options = self.page.locator(L.Facility_Dropdown)
        
        option = dropdown_options.locator(".ng-option")
        exact = option.filter(has_text=re.compile(rf"\b{re.escape(L.Facility)}\b", re.IGNORECASE))
        expect(exact).to_have_count(1)
        exact.nth(0).click()
        self.page.wait_for_timeout(1200)

        # Fill and Select Patient
        Pat_Input=self.page.locator(L.Patient_Field)
        Pat_Input.wait_for(state="visible")
        Pat_Input.click()
        self.page.wait_for_timeout(800)
        Pat_Input.fill(L.Patient)
        self.page.wait_for_timeout(1500)

        Patient_Dropdown_Option = self.page.locator(L.Patient_Dropdown)
        Patient_Dropdown_List=Patient_Dropdown_Option.locator(".ng-option")
        exact_Patient = Patient_Dropdown_List.filter(has_text=L.Patient)
        expect(exact_Patient).to_have_count(1)
        exact_Patient.nth(0).click()
        self.page.wait_for_timeout(1200)

        # Select MedType
        self.page.locator(L.MedType_Remove).click()
        self.page.wait_for_timeout(1200)
        self.page.locator(L.MedType_Field).click()
        self.page.wait_for_timeout(800)
        MedType_Droplist=self.page.locator(L.MedType_Dropdown)
        MedType_Option=MedType_Droplist.locator(".ng-option")
        exact_MedType_Option=MedType_Option.filter(has_text=L.MedType)
        exact_MedType_Option.nth(0).click()
        self.page.wait_for_timeout(1200)

        # Select Reason Of STAT
        self.page.locator(L.Reason_Of_STAT_Field).click()
        self.page.wait_for_timeout(1200)
        ReasonForSTAT_Droplist=self.page.locator(L.Reason_Of_STAT_Dropdown)
        ReasonForSTAT_Option=ReasonForSTAT_Droplist.locator(".ng-option")
        exact_ReasonForSTAT_Option=ReasonForSTAT_Option.filter(has_text=L.Reason_For_STAT)
        exact_ReasonForSTAT_Option.nth(0).click()
        self.page.wait_for_timeout(1200)

        # Select Dose Due Time
        self.page.locator(L.Dose_Due_Field).click()
        Dose_Due_Droplist=self.page.locator(L.Dose_Due_Dropdown)
        DropOption=Dose_Due_Droplist.locator(".ng-option")
        exact_DropOption=DropOption.filter(has_text=L.Dose_Due)
        exact_DropOption.nth(0).click()
        self.page.wait_for_timeout(1200)

        rx_raw = str(L.Rx_Validate).strip()
 
        # Conditions that mean "NO RX present"
        if not rx_raw or rx_raw.lower() == "nan":
            print("⚠️ No RX number provided in DDT file. Skipping RX selection...")
        else:
            # Build RX list safely
            rx_list = [r.strip() for r in rx_raw.split(",") if r.strip()]
        
            if not rx_list:
                print("⚠️ RX list is empty after parsing. Skipping RX selection...")
            else:
                print(f"📌 RX numbers to validate: {rx_list}")
        
                # Ensure IGX grid renders all rows
                self.page.keyboard.press("End")
                self.page.wait_for_timeout(400)
                self.page.keyboard.press("Home")
                self.page.wait_for_timeout(400)
        
                # Validate grid **is present** before selection
                try:
                    grid = self.page.locator(L.patient_Drug_GridContainer)
                    grid.wait_for(state="visible", timeout=5000)
                    print("✔ Grid container located successfully")
                except:
                    print("❌ Grid container NOT found. RX validation skipped.")
                    rx_list = []  # stop further selection
        
                # Loop RX numbers only if grid exists
                for rx in rx_list:
                    print(f"🔍 Searching for RX: {rx}")
        
                    try:
                        # Locate RX in column 4
                        rx_cell = self.page.locator(
                            f'igx-grid-cell[aria-colindex="4"]:has-text("{rx}")'
                        )
                        rx_cell.wait_for(state="visible", timeout=7000)
        
                        # Row containing RX
                        row = rx_cell.locator("xpath=ancestor::igx-grid-row")
        
                        # Checkbox in same row, col 1
                        checkbox = row.locator(
                            'igx-grid-cell[aria-colindex="1"] input[type="checkbox"]'
                        )
                        checkbox.wait_for(state="visible", timeout=5000)
                        checkbox.click(force=True)
        
                        print(f"✔ Successfully selected RX: {rx}")
        
                    except Exception as error:
                        print(f"❌ Failed to select RX '{rx}' → {error}")
        
                    self.page.wait_for_timeout(800)

        locator = self.page.locator(L.STAT_Order_List)
        locator.wait_for(state="visible")
        locator.hover()
        self.page.wait_for_timeout(300)
        locator.click()
        self.page.wait_for_timeout(6000)

        self.page.locator(L.Board_Menu).click()
        self.page.wait_for_timeout(1200)

        self.page.locator(L.Board_Filter).click()
        self.page.wait_for_timeout(1000)

        Facility_Filter = self.page.locator(L.Board_Filter_Facility)
        Facility_Filter.click()
        self.page.wait_for_timeout(800)
        Facility_Filter.fill(L.Facility)
        self.page.wait_for_timeout(1500)

        dropdown_options = self.page.locator(L.Board_Facility_Filter_Dropdown)
        option = dropdown_options.locator(".ng-option")
        exact = option.filter(has_text=L.Facility)
        # expect(exact).to_have_count(1)
        exact.nth(0).click()
        self.page.wait_for_timeout(1200)

        self.page.locator(L.Click_Outside).click()
        self.page.locator(L.Filter_Search).click()
        self.page.wait_for_timeout(5000)