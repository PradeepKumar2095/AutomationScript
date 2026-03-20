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

@pytest.fixture(scope="session")
def playwright_instance():
    pw = sync_playwright().start()
    yield pw
    pw.stop()

@pytest.fixture(scope="function")
def browser(playwright_instance):
    browser = getattr(playwright_instance, BROWSER_TYPE).launch(
        channel=BROWSER_CHANNEL,
        headless=HEADLESS,
        args=BROWSER_ARGS
    )
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def context(browser):
    context = browser.new_context(no_viewport=True, accept_downloads=True)
    yield context
    context.close()

@pytest.fixture(scope="function")
def page(context):
    pg = context.new_page()
    yield pg
    pg.close()