import pytest
from PSCalendar_Page import PSCalendarPage

@pytest.fixture(scope="function", autouse=True)
def go_home(request,page):
    request.cls.page=page
    request.cls.dms=PSCalendarPage(page)

@pytest.mark.usefixtures("go_home")
class Test_PSCalendarPage:

    def test_header(self,page):
        self.dms.goto_home()

    def test_listfilter_report(self,page):
        self.dms.goto_home()
        self.dms.FilterList_and_Validate()