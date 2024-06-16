from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the WebDriver (use the path to your WebDriver)
driver_path = 'D:\\Folder nou\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe'
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# Define the URL you want to scrape
url = 'https://www.amazon.com/s?k=iphone&ref=nb_sb_noss'

# Open the URL
driver.get(url)


def search_product(query):
    # Find the search input field
    search_input = driver.find_element(By.ID, 'twotabsearchtextbox')

    # Clear any existing text in the search input field
    search_input.clear()

    # Enter the search query
    time.sleep(3)
    search_input.send_keys(query)

    # Submit the search (you can also simulate pressing Enter)
    time.sleep(3)
    search_input.submit()


# Perform the search for 'iphone'
search_product('iphone')

# Function to extract and print links
def extract_links():
    # Wait for the elements to be present
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, 'a.a-link-normal.s-underline-text.s-underline-link-text.s-link-style.a-text-normal')))
    # Extract all anchor tags with the specific class
    links = driver.find_elements(By.CSS_SELECTOR,
                                 'a.a-link-normal.s-underline-text.s-underline-link-text.s-link-style.a-text-normal')

    # Print the href attribute of each anchor tag
    for link in links:
        href = link.get_attribute('href')
        if href:
            print(href)


# Loop to go through all pages
while True:
    # Extract and print links from the current page
    extract_links()

    # Add delay to mimic human behavior and to wait for the page to load
    time.sleep(3)

    try:
        # Find the "Next" button
        next_button = driver.find_element(By.CSS_SELECTOR, 'a.s-pagination-item.s-pagination-next.s-pagination-button.s-pagination-separator')
        # Click the "Next" button to go to the next page
        next_button.click()
        # Wait for the next page to load
        time.sleep(3)
    except:
        # If there's an exception, it means there's no "Next" button (last page reached)
        print("Last page reached.")
        break

# Close the browser
driver.quit()
