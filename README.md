# py-instant-crawl
python library for scrape websites by specifying template in json


## Installation

```
pip install pyinstantcrawl
```

## Quickstart

1. create the template like below and save is as `sample.json`

```
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
```

2. call the command below
```python
python main.py https://pragprog.com sample.json
```

now its work with parent + child structure. Check it at examples folder.


