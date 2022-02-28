from os import uname
import sys
import time
import requests
from rich.console import Console
from rich.table import Table
from rich.text import Text
from argparse import ArgumentParser, RawTextHelpFormatter
from collections import OrderedDict
from rdflib import ConjunctiveGraph, Namespace, URIRef
from rdflib.namespace import RDF, RDFS, OWL
import jellyfish


def download_EDAM():
    r = requests.get("http://edamontology.org/EDAM.owl")
    with open("EDAM.owl", "wb") as f:
        f.write(r.content)


# a single function to load EDAM and get the graph object as a result
def load_EDAM():

    g = ConjunctiveGraph()
    try:
        g.load("./EDAM.owl", format="xml")
    except FileNotFoundError:
        download_EDAM()
        g.load("./EDAM.owl", format="xml")
    g.bind("edam", Namespace("http://edamontology.org#"))
    g.bind("oboInOwl", Namespace("http://www.geneontology.org/formats/oboInOwl#"))
    return g


class LimitedSizeDict(OrderedDict):
    def __init__(self, *args, **kwds):
        self.size_limit = kwds.pop("size_limit", None)
        OrderedDict.__init__(self, *args, **kwds)
        self._check_size_limit()

    def __setitem__(self, key, value):
        OrderedDict.__setitem__(self, key, value)
        self._check_size_limit()

    def _check_size_limit(self):
        if self.size_limit is not None:
            while len(self) > self.size_limit:
                self.popitem(last=False)


def index_EDAM(edam_kg):
    index_label_to_uri = {}
    for subject, predicate, obj in edam_kg.triples((None, RDFS.label, None)):
        index_label_to_uri[str(obj)] = str(subject)

    for subject, predicate, obj in edam_kg.triples(
        (
            None,
            URIRef("http://www.geneontology.org/formats/oboInOwl#hasExactSynonym"),
            None,
        )
    ):
        index_label_to_uri[str(obj)] = str(subject)
    return index_label_to_uri


def get_edam_top_10_jaro(l, index):
    max_sim = 0
    min_dist = 100
    top_10 = LimitedSizeDict(size_limit=5)
    for label in index.keys():
        s = jellyfish.jaro_winkler(l, label)
        if s > max_sim:
            max_sim = s
            top_10[label] = s
            top_10.move_to_end(label, last=False)
    return top_10


def get_edam_top_10_jaro_ci(l, index):
    max_sim = 0
    min_dist = 100
    top_10 = LimitedSizeDict(size_limit=5)
    for label in index.keys():
        s = jellyfish.jaro_winkler(l.lower(), label.lower())
        if s > max_sim:
            max_sim = s
            top_10[label] = s
            top_10.move_to_end(label, last=False)
    return top_10


def get_edam_top_10(l, index):
    max_sim = 0
    min_dist = 100
    top = {}
    for label in index.keys():
        top[label] = jellyfish.jaro_winkler(l.lower(), label.lower())

    sorted_hits = dict(sorted(top.items(), key=lambda item: item[1], reverse=True))
    top_10 = {k: sorted_hits[k] for k in list(sorted_hits)[:10]}

    return top_10


parser = ArgumentParser(
    description="""
text2edam recommend EDAM term URIs based on syntactic similarity.   

Usage examples :
    python text2edam.py -l
    
Please report any issue to alban.gaignard@univ-nantes.fr
""",
    formatter_class=RawTextHelpFormatter,
)

parser.add_argument(
    "-u",
    "--update",
    help="download or update the EDAM ontology",
)

parser.add_argument(
    "labels",
    metavar="label",
    type=str,
    nargs="+",
    help="input labels",
)

if __name__ == "__main__":

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()
    console = Console()

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Label", justify="left")
    table.add_column("Matched term", justify="right")
    table.add_column("Confidence score", justify="right")
    table.add_column("Term URI", justify="right", style="green")

    if args.update:
        download_EDAM()
    elif args.labels:
        s1 = time.time()
        G = load_EDAM()
        ts1 = round((time.time() - s1), 2)
        console.print(f"Loaded {len(G)} triples from EDAM")
        console.print(f"EDAM ontology loaded in {ts1} s")

        s2 = time.time()
        index = index_EDAM(G)
        ts2 = round((time.time() - s2), 2)
        console.print(f"EDAM ontology indexed in {ts2} s")

        s3 = time.time()
        for label in args.labels:
            # top_10 = get_edam_top_10_jaro_ci(label, index=index)
            top_10 = get_edam_top_10(label, index=index)
            for hit in top_10.keys():
                table.add_row(
                    label,
                    hit,
                    str(top_10[hit]),
                    f"[link={index[hit]}]{index[hit]}[/link]",
                )
        ts3 = round((time.time() - s3), 2)
        console.print(f"Approximate term search in {ts3} s")
        console.print(table)
