import requests
import pandas as pd

def get_json(url):
    response = requests.get(url)
    print(type(response))
    data_json = response.json()  # Parses the JSON data
    print(type(data_json))  # Prints "<class 'list'>"

    # Create a DataFrame from the JSON data
    data_new = pd.DataFrame(data_json)

    print(data_new.head())  # Print the first few rows of the DataFrame
    return data_new

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/posts'
    get_json(url)
