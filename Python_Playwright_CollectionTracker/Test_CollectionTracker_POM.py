import pytest
from pathlib import Path
from Collection_Tracker_Page import CollectionTrackerPage

@pytest.fixture(scope="function", autouse=True)
def go_home(page):
    CollectionTrackerPage(page).goto_home()

def test_smoke(page):
    assert "Collections" in page.title()

def test_download_first_report(page, tmp_path):
    file_path = CollectionTrackerPage(page).click_first_report_and_download(tmp_path)
    assert file_path.exists() and file_path.stat().st_size > 0