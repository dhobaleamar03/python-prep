# Handling errors when making an HTTP request
import requests

try:
    #send a GET request to the API
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/1",
        timeout=10
    )

    #raise an error if the response has an unsuccessful status
    response.raise_for_status()

    # Read the returned user details
    user = response.json()
    print("Name:", user["name"])

except requests.exceptions.HTTPError:
    #handle unsuccessful HTTP status codes
    print("HTTP request failed.")

except requests.exceptions.RequestException:
    #handle connection problems and timeouts
    print("Could not connect to the API.")