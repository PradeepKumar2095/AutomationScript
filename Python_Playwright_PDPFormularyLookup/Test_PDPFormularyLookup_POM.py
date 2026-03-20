import pytest
from PDP_FormularyLookup_Page import PDPFormularyLookupPage

@pytest.fixture(scope="function", autouse=True)
def go_home(request,page):
    request.cls.page=page
    request.cls.dms=PDPFormularyLookupPage(page)
    request.cls.dms.goto_home()

@pytest.mark.usefixtures("go_home")
class Test_PDPFormularyLookupPage:

    def test_header(self,page):
        self.dms.goto_home()

    def test_listfilter_report(self,page):
        self.dms.FilterList_and_ValidateCount()
    
    def test_listfilter_report2(self,page):
        self.dms.FilterList_and_Validate2()