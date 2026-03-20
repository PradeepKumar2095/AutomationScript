import pytest
from STATTracker_Page import STATTrackerPage

@pytest.fixture(scope="function", autouse=True)
def go_home(request,page):
    request.cls.page=page
    request.cls.dms=STATTrackerPage(page)

@pytest.mark.usefixtures("go_home")
class Test_STATTrackerPage:

    def test_header(self,page):
        self.dms.goto_home()

    def test_listfilter_report(self,page):
        self.dms.goto_home()
        self.dms.FilterList_and_Validate()