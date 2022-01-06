#!/usr/bin/env python
# -*- coding: utf-8 -*-


from .utils import download_from_yaml


def download(output_dir: str, snippet_only: bool, ignore_cache: bool = False) -> None:
    """Downloads data files from list of URLs (default: download.yaml) into data directory (default: data/).

    Args:
        output_dir: A string pointing to the location to download data to.
        snippet_only: Downloads only the first 5 kB of the source, for testing and file checks.    
        ignore_cache: Ignore cache and download files even if they exist [false]

    Returns:
        None.
    """

    download_from_yaml(yaml_file="download.yaml", 
                        output_dir=output_dir,
                        snippet_only=snippet_only,
                        ignore_cache=ignore_cache, 
                        verbose=True)

    return None
