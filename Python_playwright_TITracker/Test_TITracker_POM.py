import pytest
from TITracker_Page import TITrackerPage

@pytest.fixture(scope="function", autouse=True)
def go_home(request,page):
    request.cls.page=page
    request.cls.tit=TITrackerPage(page)

@pytest.mark.usefixtures("go_home")
class Test_TITrackerPage:

    def test_header(self,page):
        self.tit.goto_home()

    def test_listfilter_report(self,page):
        self.tit.goto_home()
        self.tit.FilterList_and_Validate()