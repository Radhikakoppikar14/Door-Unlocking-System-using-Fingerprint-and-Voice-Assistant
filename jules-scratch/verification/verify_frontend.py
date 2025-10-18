from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('http://localhost:3000')
    page.fill('input[placeholder="Project name"]', 'My New Project')
    page.fill('input[placeholder="Project description"]', 'This is a new project.')
    page.click('button[type="submit"]')
    page.wait_for_timeout(1000) # Wait for the project to be created
    page.screenshot(path='jules-scratch/verification/verification.png')
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
