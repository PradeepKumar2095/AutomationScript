import pytest
from Discharge_Meds_Page import DischargeMedsPage

@pytest.fixture(scope="function", autouse=True)
def go_home(request,page):
    request.cls.page=page
    request.cls.dms=DischargeMedsPage(page)
    request.cls.dms.goto_home()

@pytest.mark.usefixtures("go_home")
class Test_DischargeMeds:

    def test_header(self,page):
        self.dms.goto_home()

    def test_listfilter_report(self,page):
        self.dms.FilterList_and_ValidateCount()