import os

import click


@click.command()
@click.argument("url")
def main(url):
    """Get the blog slug for a given URL."""
    from urllib.parse import urlparse

    parsed_url = urlparse(url)
    path_parts = parsed_url.path.strip("/").split("/")
    blog_type = path_parts[0]
    blog_title = path_parts[-1]
    click.echo(os.path.sep.join([blog_type, blog_title]))


if __name__ == "__main__":
    main()
