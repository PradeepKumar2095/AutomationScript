
import os
from pathlib import Path
import re

import pytest
from playwright.sync_api import sync_playwright

DOWNLOADS_DIR = Path("downloads")
BROWSER_TYPE = "chromium"
BROWSER_CHANNEL = "msedge"
HEADLESS = False
BROWSER_ARGS = ["--start-maximized"]


def _ensure_downloads_dir():
    DOWNLOADS_DIR.mkdir(parents=True, exist_ok=True)


@pytest.fixture(scope="session")
def playwright_instance():
    pw = sync_playwright().start()
    yield pw
    pw.stop()


@pytest.fixture(scope="session")
def browser(playwright_instance):
    browser = getattr(playwright_instance, BROWSER_TYPE).launch(
        channel=BROWSER_CHANNEL,
        headless=HEADLESS,
        args=BROWSER_ARGS,
    )
    yield browser
    browser.close()


@pytest.fixture(scope="session")
def context(browser):
    _ensure_downloads_dir()
    context = browser.new_context(no_viewport=True, accept_downloads=True)

    def _on_download(download):
        suggested = download.suggested_filename
        target_path = DOWNLOADS_DIR / suggested
        counter = 1
        stem = target_path.stem
        suffix = target_path.suffix
        while target_path.exists():
            target_path = DOWNLOADS_DIR / f"{stem} ({counter}){suffix}"
            counter += 1
        download.save_as(str(target_path))
    context.on("download", _on_download)

    yield context
    context.close()


@pytest.fixture(scope="function")
def page(context):
    pg = context.new_page()
    yield pg
