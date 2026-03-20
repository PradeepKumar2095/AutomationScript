
import re
from pathlib import Path
from playwright.sync_api import Page, expect
import RequestForm_Locator as L


class CollectionTrackerPage:
    def __init__(self, page: Page):
        self.page = page

    def _see(self, locator_str: str, timeout: int = 15000):
        """Small helper to assert a locator is visible."""
        expect(self.page.locator(locator_str)).to_be_visible(timeout=timeout)

    def goto_home(self):
        self.page.goto(L.BASE_URL, wait_until="domcontentloaded", timeout=60000)
        expect(self.page).to_have_title(re.compile(r"Collections"), timeout=15000)
        self._see(L.List_Grid)
        # self._see(L.APP_READY_CELL)
        self.page.wait_for_timeout(1500)

    def click_first_report_and_download(self, download_dir: Path, timeout_ms: int = 60000) -> Path:
        self._see(L.List_Grid)
        link = self.page.locator(L.FIRST_ROW_REPORT_LINK).first
        expect(link).to_be_visible(timeout=15000)

        self.page.wait_for_timeout(800)

        with self.page.expect_download(timeout=timeout_ms) as d:
            link.click()
        download = d.value

        saved_path = Path(download.path())

        self.page.wait_for_timeout(1500)

        # Integrity checks (kept minimal but meaningful)
        
        if not saved_path.exists() or saved_path.stat().st_size == 0:
            raise AssertionError(f"Download failed/empty: {saved_path}")

        return saved_path