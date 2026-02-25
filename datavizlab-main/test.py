import requests

API_KEY = "AIzaSyDeekmlauHml7rJfi6XCSAGTrV7sV-oFNY"  # <-- Put your Gemini API key here
PROMPT = "simple python code for barchart nothing else"  # <-- Edit your prompt here

# Gemini API endpoint (example, update if needed)
url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent?key=" + API_KEY

headers = {
    "Content-Type": "application/json"
}

data = {
    "contents": [{"parts": [{"text": PROMPT}]}]
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    result = response.json()
    try:
        print("Gemini:", result["candidates"][0]["content"]["parts"][0]["text"])
    except Exception as e:
        print("Could not parse Gemini response:", result)
else:
    print("Error:", response.status_code, response.text)
