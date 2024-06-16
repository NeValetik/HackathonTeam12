from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import pyautogui



chrome_options = Options()
chrome_options.add_argument("--headless")  # Comment out to run in regular mode
chrome_options.add_argument("--window-size=1920x1080")  # Set window size

def switch_virtual_desktop(desktop_number):
    # Hotkey to switch virtual desktop
    if desktop_number == 1:
        pyautogui.hotkey('win', 'ctrl', 'left')
    elif desktop_number == 2:
        pyautogui.hotkey('win', 'ctrl', 'right')
# switch_virtual_desktop(2)



# Set up the WebDriver (use the path to your WebDriver)
driver_path = 'D:\\chrome_extension\\1\\chromedriver-win64\\chromedriver.exe'
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Define the URL you want to scrape
url = 'https://www.amazon.com/s?k=iphone&ref=nb_sb_noss'

# Open the URL
driver.get(url)

total_links = []
flag = 0


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
            # print(href)
            total_links.append(href)
            if len(total_links):
                flag = True
                return


# Loop to go through all pages
while True:
    # Extract and print links from the current page
    extract_links()
    if flag:
        break


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

# switch_virtual_desktop(1)
print(total_links)
# Close the browser
driver.quit()
