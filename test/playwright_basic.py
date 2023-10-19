import time

from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('https://console.stg.intelcloud.cnvrg.io/')
    time.sleep(5)
    page.reload()
    time.sleep(10)
    assert "https://intelcloudstg.b2clogin.com/" in page.url
    page.locator("//input[@id='signInName']").fill("kaustubhcnvrgsep21@team152640.testinator.com")
    page.locator("//input[@id='password']").fill("Cnvrg@123")
    page.locator("//button[@id='next']").click()
    time.sleep(5)
    page.reload()
    time.sleep(10)
    assert "https://console.stg.intelcloud.cnvrg.io/overview" in page.url
