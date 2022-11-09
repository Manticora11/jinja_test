from jinja2 import Environment, FileSystemLoader
import requests


def get_catfacts_data():
    response = requests.get('https://catfact.ninja/facts')
    return response.json()['data']


def main():
    file_loader = FileSystemLoader(".")
    environment = Environment(loader=file_loader)
    template = environment.get_template("base.html")
    output = template.render(catfacts=get_catfacts_data())
    print(output)


if __name__ == "__main__":
    main()
