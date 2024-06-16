import requests

def walmart_request_and_save():
    url = 'https://aliexpress.ru/wholesale?SearchText=iphone&g=y&page=1&searchInfo=A%2FsRthprYtZRN8knpjRC4FBy4Wz0erUYgHqSNWSU6DVyNiBX9RkvOZulLy%2FQTwHXqHuwtpNjU3KZkWE8JJ5FXk0rjT3gj8pZ08V4vRkKsWwc3OBa%2FGUdzsC0VXthuYH791niW3P4G0TzoKTCtp0LgRxpZm9adlyKoNp0xjfbpGiFk0%2FYmlX8d3a4xiUDCxdq1KasjSJeBrQ7Y%2FCOJpvfec8KVQu%2FJb7kA4gRxzoy%2FVQjYRsGUCowFW0i9fAPYj03ZvroPYpDNXOAdvYDX6kbPNcJJbY%2FO21LBrqUHfc%3D'  # URL of Walmart's homepage
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

    try:
        response = requests.get(url, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            print('Request to Walmart successful!')
            # Save the response text into a file
            with open('walmart_homepage.html', 'w', encoding='utf-8') as f:
                f.write(response.text)
            print('Walmart homepage saved as walmart_homepage.html')
        else:
            print(f'Failed to retrieve data from Walmart. Status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'An error occurred: {e}')

if __name__ == '__main__':
    walmart_request_and_save()
