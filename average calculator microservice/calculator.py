import requests

# API endpoint for primes (Change URL if testing another endpoint)
url = "http://20.244.56.144/evaluation-service/users"

# Your access token
access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiZXhwIjoxNzQzNjAxMTE4LCJpYXQiOjE3NDM2MDA4MTgsImlzcyI6IkFmZm9yZG1lZCIsImp0aSI6ImU5ZWE3MjY1LTBiN2QtNGVjZS04ZGQzLWM4MDRlMTYzOTU5MyIsInN1YiI6InRlcm1pbmFsaXNoZXJlMTI3QGdtYWlsLmNvbSJ9LCJlbWFpbCI6InRlcm1pbmFsaXNoZXJlMTI3QGdtYWlsLmNvbSIsIm5hbWUiOiJhbnViaGF2IG1henVtZGVyIiwicm9sbE5vIjoiMjIwNTExNDUiLCJhY2Nlc3NDb2RlIjoibndwd3JaIiwiY2xpZW50SUQiOiJlOWVhNzI2NS0wYjdkLTRlY2UtOGRkMy1jODA0ZTE2Mzk1OTMiLCJjbGllbnRTZWNyZXQiOiJDZmdta0NZZXRaTkRYR1FGIn0.EvNucLjfa2DqoyoAePAXuZzA6ai3eDCMBwuUQ9Zxs0E"

# Headers with the Authorization token
headers = {
    "Authorization": f"Bearer {access_token}"
}

# Send GET request to API
response = requests.get(url, headers=headers)

# Print response status code
print(f"Status Code: {response.status_code}")

# Print response JSON
try:
    print("Response Data:", response.json())
except ValueError:
    print("Invalid JSON response:", response.text)
