import pytest
from PDP_Formulary_Page import PDPFormularyPage

@pytest.fixture(scope="function", autouse=True)
def go_home(request,page):
    request.cls.page=page
    request.cls.dms=PDPFormularyPage(page)
    request.cls.dms.goto_home()

@pytest.mark.usefixtures("go_home")
class Test_PDPFormularyPage:

    def test_header(self,page):
        self.dms.goto_home()

    def test_listfilter_report(self,page):
        self.dms.FilterList_and_ValidateCount()