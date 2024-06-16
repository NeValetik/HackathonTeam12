from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Load JSON data
with open('products_with_scores.json', 'r', encoding='utf-8') as f:
    products_with_scores = json.load(f)

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products_with_scores)

@app.route('/findIt', methods=['POST'])
def get_product():
    data = request.get_json()
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

    if not current_product_name:
        return jsonify({"error": "Product not found"}), 404

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


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
