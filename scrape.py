import json
from playwright.sync_api import sync_playwright

# Function to save scraped data to a JSON file
def save_to_file(data):
    with open('headlines.json', 'w') as f:
        json.dump(data, f, indent=4)

def scrape():
    with sync_playwright() as p:
        # Launch the browser in non-headless mode for debugging
        browser = p.chromium.launch(headless=False)  # headless=False means we can see the browser
        page = browser.new_page()

        # Go to the BBC News page
        page.goto('https://www.bbc.com/news')

        # Wait for the headlines to be visible
        page.wait_for_selector('.gs-c-promo-heading__title', timeout=10000)  # Wait for headlines

        # Scrape the headlines
        headlines = page.evaluate("""
            () => {
                const elements = Array.from(document.querySelectorAll('.gs-c-promo-heading__title'));  
            }
        """)

        # Print the scraped headlines
        print('Headlines:')
        for headline in headlines:
            print(headline)

        # Save the headlines to a JSON file
        save_to_file(headlines)

        # Close the browser
        browser.close()

if __name__ == '__main__':
    scrape()
