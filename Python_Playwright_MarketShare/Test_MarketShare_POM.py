import pytest
from MarketShare_Page import MarketSharePage

@pytest.fixture(scope="function", autouse=True)
def go_home(request,page):
    request.cls.page=page
    request.cls.dms=MarketSharePage(page)
    request.cls.dms.goto_home()

@pytest.mark.usefixtures("go_home")
class Test_MarketSharePage:

    def test_header(self,page):
        self.dms.goto_home()

    def test_listfilter_report(self,page):
        self.dms.FilterList_and_ValidateCount()