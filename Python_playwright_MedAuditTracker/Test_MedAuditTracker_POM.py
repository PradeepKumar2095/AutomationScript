import pytest
from MedAuditTracker_Page import MedAuditTrackerPage

@pytest.fixture(scope="function", autouse=True)
def go_home(request,page):
    request.cls.page=page
    request.cls.tit=MedAuditTrackerPage(page)

@pytest.mark.usefixtures("go_home")
class Test_MedAuditTrackerPage:

    def test_header(self,page):
        self.tit.goto_home()

    def test_listfilter_report(self,page):
        self.tit.goto_home()
        self.tit.FilterList_and_Validate()