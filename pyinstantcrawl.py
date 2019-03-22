import json

import requests
from parsel import Selector
import pprint


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
    selectlist = getattr(selector, stype)(expression)

    return getattr(selectlist, getter)(), selectlist


def parse(result, selector, json_ob, is_child=False, parent=None):
    """doing real parsing

    :selector: parsel.Selector instance
    :json_string: the whole json scraper template
    :returns: dict

    """
    for key, val in json_ob.items():
        children = val.get('children')

        if not children:
            res, _ = parse_node(selector, val)
            result[key] = res
        else:
            _, p_selector = parse_node(selector, val)
            l_result = []
            for s in p_selector:
                with_child = parse({}, s, children)
                l_result.append(with_child)
            result[key] = l_result

    return result


def fetch(url, template):
    """Do actual fetch and return the selected data

    :url: TODO
    :template: TODO
    :returns: TODO

    """
    result = {}
    resp = requests.get(url)
    selector = Selector(resp.text)
    json_ob = json.loads(template)
    parsed = parse(result, selector, json_ob)
    return parsed


if __name__ == "__main__":
    print(fetch("https://pragprog.com", sample_json))
    print("nested")
    pprint.pprint(
        fetch("https://blog.ihfazh.com/archives.html", sample_with_child))
