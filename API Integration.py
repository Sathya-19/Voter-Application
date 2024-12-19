import requests

@app.route('/check-fact', methods=['POST'])
def check_fact():
    data = request.get_json()
    claim = data.get('claim', '')

    # Use a real fact-checking API
    api_url = "https://factchecktools.googleapis.com/v1alpha1/claims:search"
    params = {
        "query": claim,
        "key": "YOUR_API_KEY"  # Replace with your API key
    }
    response = requests.get(api_url, params=params)
    
    if response.status_code == 200:
        results = response.json().get('claims', [])
        if results:
            return jsonify({"result": results[0]['text']})
        else:
            return jsonify({"result": "No results found."})
    else:
        return jsonify({"result": "Error connecting to fact-checking service."})
