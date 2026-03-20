import pytest
from RevenueAnalytics_Page import RevenueAnalyticsPage

@pytest.fixture(scope="function", autouse=True)
def go_home(request,page):
    request.cls.page=page
    request.cls.dms=RevenueAnalyticsPage(page)

@pytest.mark.usefixtures("go_home")
class Test_RevenueAnalyticsPage:

    def test_header(self,page):
        self.dms.goto_home()

    def test_listfilter_report(self,page):
        self.dms.goto_home()
        self.dms.FilterList_and_Validate()