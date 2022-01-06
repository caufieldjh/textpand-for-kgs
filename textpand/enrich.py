#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from typing import List
import sys

from textpand.enrich.uniprot.uniprot import UniProtEnrich
from textpand.enrich.wikipedia.wikipedia import WikipediaEnrich
from textpand.enrich.wikidata.wikidata import WikidataEnrich


DATA_SOURCES = {
    'UniProtEnrich': UniProtEnrich,
    'WikipediaEnrich': WikipediaEnrich,
    'WikidataEnrich': WikidataEnrich
}


def enrich(input_dir: str, output_dir: str, sources: List[str] = None) -> None:
    """Call scripts in textpand/enrich/[source name]/ to 
    prepare each source and search it for node IDs.

    Args:
        input_dir: A string pointing to the directory to import data from.
        output_dir: A string pointing to the directory to output data to.
        sources: A list of sources to use for enrichment.

    Returns:
        None.

    """
    if not sources:
        # run all sources
        sources = list(DATA_SOURCES.keys())

    for source in sources:
        try:
            if source in DATA_SOURCES:
                logging.info(f"Parsing {source}")
                enrichment = DATA_SOURCES[source](input_dir, output_dir)
                enrichment.run()
        except Exception as e:
            logging.error(f"Encountered error: {e}")
            sys.exit(1)
