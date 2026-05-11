"""
Module 9 API Assignment
Author: Sam Dirr

This program demonstrates how to connect to public APIs with the requests
library, print the raw JSON response, and format selected fields for easier
reading.
"""

import json
from urllib.request import urlopen

try:
    import requests
except ModuleNotFoundError:
    requests = None


ASTRONAUTS_URL = "http://api.open-notify.org/astros.json"
ZIP_CODE_URL = "http://api.zippopotam.us/us/68106"


class SimpleResponse:
    """Small fallback response object used when requests is not installed."""

    def __init__(self, status_code, text):
        self.status_code = status_code
        self.text = text

    def json(self):
        return json.loads(self.text)


def get_response(url):
    """Get a URL with requests, or urllib if requests is unavailable."""
    if requests is not None:
        return requests.get(url, timeout=10)

    with urlopen(url, timeout=10) as response:
        text = response.read().decode("utf-8")
        return SimpleResponse(response.status, text)


def test_connection(url):
    """Send a GET request and print the HTTP status code."""
    response = get_response(url)
    print(f"Connection test for {url}")
    print(f"Status code: {response.status_code}")
    print()
    return response


def print_raw_response(title, response):
    """Print the API response with no special formatting."""
    print(title)
    print(response.text)
    print()


def print_astronauts_formatted(response):
    """Format the current astronauts response from Open Notify."""
    data = response.json()
    print("Formatted Current Astronauts")
    print(f"People in space: {data['number']}")

    for person in data["people"]:
        print(f"{person['name']} is aboard the {person['craft']}.")

    print()


def print_zip_code_formatted(response):
    """Format the response from the Zippopotam.us API."""
    data = response.json()
    print("Formatted ZIP Code Information")
    print(f"Post code: {data['post code']}")
    print(f"Country: {data['country']} ({data['country abbreviation']})")

    for place in data["places"]:
        print(f"Place: {place['place name']}, {place['state abbreviation']}")
        print(f"Latitude: {place['latitude']}")
        print(f"Longitude: {place['longitude']}")

    print()


def print_pretty_json(title, response):
    """Print the same response in an indented JSON format."""
    data = response.json()
    print(title)
    print(json.dumps(data, indent=4))
    print()


def main():
    """Run all API examples required for the assignment."""
    astronauts_response = test_connection(ASTRONAUTS_URL)
    print_raw_response("Raw Current Astronauts Response", astronauts_response)
    print_astronauts_formatted(astronauts_response)

    zip_code_response = test_connection(ZIP_CODE_URL)
    print_raw_response("Raw ZIP Code Response", zip_code_response)
    print_pretty_json("ZIP Code Response Formatted Like Tutorial JSON", zip_code_response)
    print_zip_code_formatted(zip_code_response)


if __name__ == "__main__":
    main()
