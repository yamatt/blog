import json

import click
import mf2py
import mf2util
import requests


@click.command()
@click.argument("url")
@click.argument("target")
@click.argument("destination")
def main(url, target, destination):

    resp = requests.get(url, timeout=10, headers={"User-Agent": "Webmention-Bot/1.0"})
    parsed = mf2py.parse(doc=resp.text, url=url)

    # This automatically identifies likes, replies, etc.
    entry = mf2util.interpret_comment(parsed["items"][0], target)

    if destination == "-":
        print(json.dumps(entry))

    with open(destination, "w") as f:
        json.dump(entry, f, indent=2)


if __name__ == "__main__":
    main()
