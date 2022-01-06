#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
from textpand import download as source_download
#from textpand.enrich import DATA_SOURCES

@click.group()
def cli():
    pass


@cli.command()
@click.option("output_dir", "-o", required=True, default="data/raw")
@click.option("snippet_only", "-x", is_flag=True, default=False,
              help='Download only the first 5 kB of each (uncompressed) source, for testing and file checks [false]')
@click.option("ignore_cache", "-i", is_flag=True, default=False,
              help='ignore cache and download files even if they exist [false]')
def download(*args, **kwargs) -> None:
    """Downloads data files from list of URLs (default: download.yaml) into data
    directory (default: data/raw).

    Args:
        output_dir: A string pointing to the directory to download data to.
        snippet_only: Downloads only the first 5 kB of each uncompressed source, for testing and file checks.
        ignore_cache: If specified, will ignore existing files and download again.

    Returns:
        None.

    """

    source_download(*args, **kwargs)

    return None


@cli.command()
@click.option("input_dir", "-d", default="data/raw", type=click.Path(exists=True))
@click.option("input_nodelist", "-i", required=True)
@click.option("output_dir", "-o", default="data/enriched")
#@click.option("sources", "-s", default=None, multiple=True,
#              type=click.Choice(DATA_SOURCES.keys()))
def enrich(*args, **kwargs) -> None:
    """ Produces enriched text description for each node.

    Args:
        input_dir: A string pointing to the directory to import data from.
        input_nodelist: A KGX-format nodelist
        output_dir: A string pointing to the directory to output data to.
        sources: A list of sources to use for enrichment.

    Returns:
        None.

    """

    # Doesn't do anything yet
    pass

    return None

if __name__ == "__main__":
    cli()
