import pytest
from NCR_Page import NCRPage

@pytest.fixture(scope="function", autouse=True)
def go_home(request,page):
    request.cls.page=page
    request.cls.ncr=NCRPage(page)

@pytest.mark.usefixtures("go_home")
class Test_NCRPage:

    def test_header(self,page):
        self.ncr.goto_home()

    def test_listfilter_report(self,page):
        self.ncr.goto_home()
        self.ncr.FilterList_and_Validate()