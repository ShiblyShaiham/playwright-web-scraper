import json
from playwright.sync_api import sync_playwright


def scrape():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto('http://quotes.toscrape.com/', wait_until='domcontentloaded', timeout=30000)
        page.wait_for_selector('.quote', timeout=10000)

        quotes = page.evaluate("""
            () => Array.from(document.querySelectorAll('.quote')).map(quote => {
                return {
                    text: quote.querySelector('.text').innerText,
                    author: quote.querySelector('.author').innerText
                };
            })
        """)

        print('Quotes:')
        for quote in quotes:
            print(f"{quote['text']} — {quote['author']}")

        # Save to JSON file
        with open('quotes.json', 'w') as f:
            json.dump(quotes, f, indent=4)

        browser.close()


if __name__ == "__main__":
    scrape()
