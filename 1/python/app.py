from flask import Flask, request, jsonify
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
# from transformers import AutoTokenizer, AutoModelForSequenceClassification
# import torch.nn.functional as F
# from transformers import pipeline
import json

app = Flask(__name__)

# def search_product(driver,query):
#     # Find the search input field
#     search_input = driver.find_element(By.ID, 'twotabsearchtextbox')

#     # Clear any existing text in the search input field
#     search_input.clear()

#     # Enter the search query
#     time.sleep(3)
#     search_input.send_keys(query)

#     # Submit the search (you can also simulate pressing Enter)
#     time.sleep(3)
#     search_input.submit()

# def extract_links(driver):
#     # Wait for the elements to be present
#     WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(
#         (By.CSS_SELECTOR, 'a.a-link-normal.s-underline-text.s-underline-link-text.s-link-style.a-text-normal')))
#     # Extract all anchor tags with the specific class
#     links = driver.find_elements(By.CSS_SELECTOR,
#                                  'a.a-link-normal.s-underline-text.s-underline-link-text.s-link-style.a-text-normal')

#     total_links = []
#     # Print the href attribute of each anchor tag
#     for link in links:
#         href = link.get_attribute('href')
#         if href:
#             # print(href)
#             total_links.append(href)
#             if len(total_links):
#                 flag = True
#                 return (total_links,flag)
# absa_tokenizer = None
# absa_model = None
# sentiment_model = None
# models_loaded = False

# def load_models():
#     global absa_tokenizer, absa_model, sentiment_model, models_loaded
#     if not models_loaded:
#         # Load Aspect-Based Sentiment Analysis model
#         absa_tokenizer = AutoTokenizer.from_pretrained("yangheng/deberta-v3-base-absa-v1.1")
#         absa_model = AutoModelForSequenceClassification.from_pretrained("yangheng/deberta-v3-base-absa-v1.1")

#         # Load a traditional Sentiment Analysis model
#         sentiment_model_path = "cardiffnlp/twitter-xlm-roberta-base-sentiment"
#         sentiment_model = pipeline("sentiment-analysis", model=sentiment_model_path,
#                                    tokenizer=sentiment_model_path)
#         models_loaded = True

# @app.before_request
# def ensure_models_loaded():
#     load_models()


# def map_score_to_word(score):
#     if score < 0.2:
#         return "bad"
#     elif score < 0.4:
#         return "below average"
#     elif score < 0.6:
#         return "average"
#     elif score < 0.8:
#         return "above average"
#     else:
#         return "good"

# Load JSON data
with open('products_with_scores.json', 'r', encoding='utf-8') as f:
    products_with_scores = json.load(f)

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products_with_scores)

@app.route('/findIt', methods=['POST'])
def get_product():
    data = request.get_json()
    print(data)
    if not data:
        return jsonify({"error": "Invalid input, expecting JSON payload"}), 400

    keywords = data.get('name')
    if not keywords:
        return jsonify({"error": "Missing 'name' in JSON payload"}), 400

    current_product_name = None
    current_product_details = None

    # Find the current product in products_with_scores
    for product_name, details in products_with_scores.items():
        if all(keyword.lower() in product_name.lower() for keyword in keywords.split()):
            current_product_name = product_name
            current_product_details = details
            break

    # if not current_product_name:
    #     chrome_options = Options()
    #     chrome_options.add_argument("--headless")  # Comment out to run in regular mode
    #     chrome_options.add_argument("--window-size=1920x1080")  # Set window size
    #     # Set up the WebDriver (use the path to your WebDriver)
    #     driver_path = 'D:\\chrome_extension\\1\\chromedriver-win64\\chromedriver.exe'
    #     service = Service(driver_path)
    #     driver = webdriver.Chrome(service=service, options=chrome_options)

    #     # Define the URL you want to scrape
    #     url = 'https://www.amazon.com/s?k=iphone&ref=nb_sb_noss'

    #     # Open the URL
    #     driver.get(url)

    #     total_links = []
    #     flag = False

    #     search_product(driver,'iphone')
    #     total_links=[]
    #     while True:
    #         total_links.append(extract_links(driver)[0])
    #         if flag[1]:
    #             break
    #         time.sleep(3)

    #         try:
    #             next_button = driver.find_element(By.CSS_SELECTOR, 'a.s-pagination-item.s-pagination-next.s-pagination-button.s-pagination-separator')
    #             next_button.click()
    #             time.sleep(3)
    #         except:
    #             print("Last page reached.")
    #             break
        
    #     driver.quit()
    #     return jsonify({"error": "Product not found"}), 404

    # Determine the price range for similar products (e.g., +/- 10% of current price)
    current_product_price = float(str(current_product_details['price']).replace('$', ''))
    price_tolerance_percentage = 10  # Adjust this as needed
    price_tolerance = current_product_price * (price_tolerance_percentage / 100.0)

    # Find top 3 similar products based on price and overall score criteria
    similar_products = []
    for product_name, details in products_with_scores.items():
        if product_name != current_product_name:  # Exclude the current product
            if details['price'] is None: continue
            product_price = float(str(details['price']).replace('$', ''))

            # Check if price is within the tolerance range
            if abs(product_price - current_product_price) <= price_tolerance:
                overall_score = details['scores']['overall']
                # Check if overall score is better or equal to the current product
                if overall_score >= current_product_details['scores']['overall']:
                    similar_products.append({
                        "name": product_name,
                        "url": details['url'],
                        "price": product_price,
                        "scores": details['scores']
                    })

    # Sort similar products by overall score (descending)
    similar_products.sort(key=lambda x: x['scores']['overall'], reverse=True)

    # Limit to top 3 similar products
    top_3_similar_products = similar_products[:3]

    # Prepare the response JSON containing both current product and top 3 similar products
    response = {
        "current_product": {
            "name": current_product_name,
            "details": current_product_details
        },
        "similar_products": top_3_similar_products
    }

    return jsonify(response)


# @app.route('/process', methods=['POST'])
# def process_json():
#     data = request.get_json()
#     if not data:
#         return jsonify({"error": "Invalid input, expecting JSON payload"}), 400

#     name = data['name']
#     url = data['url']
#     price = data['price']
#     sentences = data['content']

#     aspects = ["camera", "battery", "screen", "performance", "quality", "value"]
#     aspect_scores = {aspect: [] for aspect in aspects}

#     # Compute scores for each sentence
#     for sentence in sentences:
#         for aspect in aspects:
#             # Perform Aspect-Based Sentiment Analysis
#             inputs = absa_tokenizer(f"[CLS] {sentence} [SEP] {aspect} [SEP]", return_tensors="pt")
#             outputs = absa_model(**inputs)
#             probs = F.softmax(outputs.logits, dim=1).detach().numpy()[0]

#             # Calculate single score for the aspect
#             aspect_score = probs[2] - probs[0]  # Weighted average: positive - negative
#             aspect_scores[aspect].append(aspect_score)

#     average_aspect_scores = {aspect: (sum(scores) / len(scores) + 1) / 2 if scores else 0 for aspect, scores in aspect_scores.items()}
#     overall_score = sum(average_aspect_scores.values()) / len(average_aspect_scores.keys())
#     average_aspect_scores["overall"] = overall_score

#     product_details = {
#         "url": url,
#         "price": price,
#         "scores": {
#             "camera": map_score_to_word(average_aspect_scores["camera"]),
#             "battery": map_score_to_word(average_aspect_scores["battery"]),
#             "screen": map_score_to_word(average_aspect_scores["screen"]),
#             "performance": map_score_to_word(average_aspect_scores["performance"]),
#             "quality": map_score_to_word(average_aspect_scores["quality"]),
#             "value": map_score_to_word(average_aspect_scores["value"]),
#             "overall": map_score_to_word(average_aspect_scores["overall"])
#         }
#     }

#     products_with_scores[name] = product_details

#     with open('products_with_scores.json', 'w', encoding='utf-8') as f:
#         json.dump(products_with_scores, f, indent=4)

#     return jsonify({"message": "Product processed and scores updated"}), 200


if __name__ == '__main__':
    app.debug = True
    app.run(debug=True, host='0.0.0.0', port=5000)






# Perform the search for 'iphone'

# Function to extract and print links


