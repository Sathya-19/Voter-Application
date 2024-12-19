from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/check-fact', methods=['POST'])
def check_fact():
    data = request.get_json()
    claim = data.get('claim', '')
    
    # Simulated response (replace with API logic)
    fact_checks = {
        "Voting is mandatory in some countries": "True",
        "You can vote without registering": "False",
        "Election Day is always a weekend": "False"
    }
    result = fact_checks.get(claim, "Claim not found in the database.")
    
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)

    !pip install Flask

    python app.py
