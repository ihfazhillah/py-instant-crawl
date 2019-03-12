import json

import requests
from parsel import Selector


sample_json = """
{
    "tip-of-day": {
        "expression": "//div[@class='tip-of-day']/p/text()",
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

def generate_parse_func(selector, selector_data):
    """TODO: Docstring for generate_parse_func.

    :selector: TODO
    :selector_data: TODO
    :returns: TODO

    """
    stype = selector_data['type']
    expression = selector_data['expression']
    getter = selector_data.get('getter', 'get')
    selectlis = getattr(selector, stype)(expression)
    return getattr(selectlis, getter)()

def parse_json(json_string):
    obj = json.loads(json_string)
    result = {}
    for key in obj:
        result[key] = lambda s: generate_parse_func(s, obj[key])

    return result


if __name__ == "__main__":
    url = "https://pragprog.com"
    resp = requests.get(url)
    selector = Selector(resp.text)

    obj = parse_json(sample_json)
    for o in obj:
        print(obj[o](selector))
    print(obj)

    # parse
    # obj = json.loads(sample_json)
    # for key, val in obj.items():
    #     print(key)
    #     data = generate_parse_func(selector, val)
    #     print(data)


