import pytest
from selfreview import SelfReviewPage
import conftest 
 
@pytest.fixture(scope="function", autouse=True)
def go_home(request, page):
    request.cls.page = page
    request.cls.dms = SelfReviewPage(page)
 
 
@pytest.mark.usefixtures("go_home")
class Test_DischargeMeds:
 
    def test_header(self,page):
        self.dms.goto_home()

    def test_select_facility_and_reset(self):
        self.dms.goto_home()
        self.dms.select_facility_go_and_reset()
        self.dms.click_edit_first_row()
 