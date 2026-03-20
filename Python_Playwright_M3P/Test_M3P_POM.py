import pytest
from M3P_Page import M3PPage

@pytest.fixture(scope="function", autouse=True)
def go_home(request,page):
    request.cls.page=page
    request.cls.dms=M3PPage(page)
    request.cls.dms.goto_home()

@pytest.mark.usefixtures("go_home")
class Test_M3PPage:

    def test_App(self,page):
        self.dms.goto_home()
        self.dms.FilterList_and_ValidateCount()