from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    for browser_type in [p.chromium, p.firefox, p.webkit]:
        browser = browser_type.launch()
        print(browser_type.name, 'test started')
        page = browser.new_page()
        page.goto("https://develop.dev.clusters.cyber.bet/en/")
        page.wait_for_timeout(1000)
        page.click("xpath=//div[contains(@class, 'sc-ewSSRw fDTLhF')]")
        page.wait_for_timeout(1000)
        check_visibility = page.is_visible("xpath=//div[contains(@class, 'sc-fIISuV khekgI')]")
        if check_visibility:
            print('Success')
        browser.close()
    print('All tests are finished')
