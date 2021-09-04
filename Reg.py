from playwright.sync_api import sync_playwright
import random
import string


def random_email(char_sym):
    return ''.join(random.choice(string.ascii_letters) for _ in range(char_sym))


def random_password(char_num):
    return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))


password = random_password(8)

with sync_playwright() as p:
    for browser_type in [p.chromium, p.firefox, p.webkit]:
        email = random_email(7) + "@gmail.com"
        password = random_password(8)
        print(browser_type.name, 'start test')
        browser = browser_type.launch()
        page = browser.new_page(locale='en-GB')
        page.goto("http://cyber.bet")
        page.click("text=Registration")
        page.type("input[name='email']", email.lower())
        page.type("input[name='password']", password)
        page.click("text=Next step")
        page.click("text=Confirm later")
        # check success authorization
        user = page.evaluate("() => window.localStorage.getItem('cyber/user/AUTH')")
        if 'accessToken' in user:
            print('Success authorization')
        browser.close()
        print('end of test')

    print('End of All Tests!')
