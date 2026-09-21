from pathlib import Path
import sys

import click

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from baml_client.sync_client import b


@click.command()
@click.argument("file_path", type=click.Path(exists=True))
@click.option("--language", default="US English", help="Language of the blog post")
def main(file_path: str, language: str):
    """
    Main entry point for the copyeditor CLI.
    """
    click.echo(f"Processing file: {file_path}")

    with open(file_path, "r") as f:
        blog_post = f.read()

    findings = b.Find(blog_post=blog_post, language=language)
    click.echo("Findings:")
    for finding in findings.grammar:
        click.echo(f" - {finding.original_text} -> {finding.suggested_text}")


if __name__ == "__main__":
    main()