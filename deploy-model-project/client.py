import requests

# Define the URL of the FastAPI endpoint
url = "http://localhost:8000/predict"

# Define the client record
client = {
    "lead_source": "organic_search",
    "number_of_courses_viewed": 4,
    "annual_income": 80304.0
}

# Send POST request and get response
response = requests.post(url, json=client)

# Parse the JSON response
result = response.json()
print(f"Probability of subscription: {result['probability']:.3f}")