import pytest
from top50 import Top50Page

@pytest.fixture(scope="function", autouse=True)
def go_home(request,page):
    request.cls.page=page
    request.cls.ncr=Top50Page(page)

@pytest.mark.usefixtures("go_home")
class Test_Top50Page:

    def test_header(self,page):
        self.ncr.goto_home()

    def test_listfilter_report(self, page):
        self.ncr.goto_home()
        self.ncr.FilterList_and_Validate()