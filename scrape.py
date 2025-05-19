from playwright.sync_api import sync_playwright


def scrape():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.set_extra_http_headers({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        })

        page.goto('https://www.bbc.com/news')
        page.wait_for_selector('h3', timeout=20000)  # wait for headlines

        headlines = page.evaluate("""
            () => Array.from(document.querySelectorAll('h3')).map(e => e.innerText)
        """)

        print('Headlines:')
        for headline in headlines:
            print(headline)

        browser.close()


if __name__ == "__main__":
    scrape()
