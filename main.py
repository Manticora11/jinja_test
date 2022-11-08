import jinja2
import requests


def get_catfacts_data():
    response = requests.get('https://catfact.ninja/facts')
    return response.json()['data']


def main():
    catfacts = get_catfacts_data()
    print(catfacts)


if __name__ == "__main__":
    main()
