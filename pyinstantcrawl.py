import json

import requests
from parsel import Selector


sample_json = """
{
    "tip-of-day": {
        "expression": "string(//div[@class='tip-of-day'])",
        "type": "xpath",
        "getter": "get"
    },
    "testimonial": {
        "expression": ".testimonial",
        "type": "css",
        "getter": "getall"
    }
}
"""

sample_with_child = """
{
    "contents": {
        "expression": "//section[@id='content']/ul/li",
        "type": "xpath",
        "children": {
            "datetime": {
                "expression": "./time/text()",
                "type": "xpath",
                "getter": "get"
            },
            "url": {
                "expression": "./a/@href",
                "type": "xpath",
                "getter": "get"
            },
            "title": {
                "expression": "./a/text()",
                "type": "xpath",
                "getter": "get"
            }
        }
    }
}
"""


def parse_node(selector, selector_data):
    """ Parse the node

    :selector: parsel.Selector instance
    :selector_data: a dictionary object contains expression, type, and getter
    :returns: string

    """
    stype = selector_data['type']
    expression = selector_data['expression']
    getter = selector_data.get('getter', 'get')
    selectlis = getattr(selector, stype)(expression)
    return getattr(selectlis, getter)()


def parse(selector, json_ob):
    """doing real parsing

    :selector: parsel.Selector instance
    :json_string: the whole json scraper template
    :returns: dict

    """
    # obj = json.loads(json_string)
    result = {}

    for key, selector_data in json_ob.items():
        result[key] = parse_node(selector, selector_data)

    return result


def fetch(url, template):
    """Do actual fetch and return the selected data

    :url: TODO
    :template: TODO
    :returns: TODO

    """
    resp = requests.get(url)
    selector = Selector(resp.text)
    json_ob = json.loads(template)
    parsed = parse(selector, json_ob)
    return parsed


if __name__ == "__main__":
    print(fetch("https://pragprog.com", sample_json))
    print("nested")
    print(fetch("https://blog.ihfazh.com/archives.html", sample_with_child))
