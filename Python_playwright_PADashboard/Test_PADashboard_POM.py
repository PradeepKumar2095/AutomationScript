import pytest
from PADashboard_Page import PADashboardPage

@pytest.fixture(scope="function", autouse=True)
def go_home(request,page):
    request.cls.page=page
    request.cls.dms=PADashboardPage(page)

@pytest.mark.usefixtures("go_home")
class Test_DischargeMeds:

    def test_header(self,page):
        self.dms.goto_home()

    def test_listfilter_report(self,page):
        self.dms.goto_home()
        self.dms.FilterList_and_Validate()