# textpand-for-kgs
Retrieve text data for enriching biomedical knowledge graphs.

# The general idea
Given one or more CURIEs from a set of namespaces recognized by [Biolink](https://biolink.github.io/biolink-model/), 
return a flat mapping and [KGX](https://github.com/biolink/kgx)-compatible graph node list containing text from the following sources:
* UniProtKB (specific to gene/protein)
* Wikipedia
* Wikidata
* PubMed abstracts, as per PubTator term mentions and MeSH

This text will be concatenated and will be used to assemble language model (e.g., BERT) applications in producing more informative node embeddings of knowledge graphs.

# Related projects
* [agr_genedescriptions](https://github.com/alliance-genome/agr_genedescriptions)
