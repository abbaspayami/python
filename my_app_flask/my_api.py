import requests
import os
from dotenv import load_dotenv
from pprint import pprint

# https://api.restful-api.dev/objects

def get_cellphone():
    load_dotenv()
    id = input("Enter cellphone number: ")
    # print(f"{os.getenv("API_URL")}/objects")
    url = f"{os.getenv("API_URL")}/objects/{id}"
    response = requests.get(url)
    print(response.status_code)
    pprint(response.json())

if __name__ == "__main__":
    get_cellphone()
