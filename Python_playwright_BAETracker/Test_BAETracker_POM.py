import pytest
from BAETracker_Page import BAETrackerPage

@pytest.fixture(scope="function", autouse=True)
def go_home(request,page):
    request.cls.page=page
    request.cls.dms=BAETrackerPage(page)

@pytest.mark.usefixtures("go_home")
class Test_BAETrackerPage:

    def test_header(self,page):
        self.dms.goto_home()

    def test_listfilter_report(self,page):
        self.dms.goto_home()
        self.dms.FilterList_and_Validate()