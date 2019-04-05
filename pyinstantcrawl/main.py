import json
import click
import pyinstantcrawl


@click.command()
@click.argument('url', nargs=1)
@click.argument('template', nargs=1, type=click.File('r'))
def fetch(url, template):
    crawled = pyinstantcrawl.fetch(url, template.read())
    print(json.dumps(crawled, indent=4))


if __name__ == "__main__":
    fetch()
