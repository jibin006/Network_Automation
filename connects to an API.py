#Write a script that safely connects to an API and handles errors.


import requests

url = "https://api.example.com/data"
time_out_seconds = 5 

try:
    response= requests.get(url,timeout=time_out_seconds)
    response.raise_for_status() #status
    print("API connection successful")
    print("response_data: ",response.json())
except requests.ConnectionError:
    print("Failed to connect to the API. Check the URL or network")
except requests.HTTPError as http_err:
    # Handle HTTP errors (e.g., 404 Not Found, 500 Internal Server Error)
    print(f"HTTP Error: {http_err}")
except requests.RequestException as err:
    # Catch-all for other requests-related errors (e.g., invalid URL)
    print(f"An error occurred during the request: {err}")    
except Exception as err: 
    print(f"Unexpected error: {err}")   
