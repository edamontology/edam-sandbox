"""
edamdiff.py
Author: Alban Gaignard
Email: alban.gaignard@univ-nantes.fr
Date: 2023-05-31
Description: This script compares two RDF files and outputs the differences.

The MIT License (MIT)
"""

from rdflib import ConjunctiveGraph
from rdflib.compare import to_isomorphic, graph_diff, to_canonical_graph
from rdflib.util import guess_format
import difflib
import sys

from rich.progress import Progress
from rich.console import Console

import click

_UNSTABLE_EDAM = "https://edamontology.org/EDAM_unstable.owl"
_STABLE_EDAM = "https://edamontology.org/EDAM.owl"

#kg_ref = ConjunctiveGraph().parse(_STABLE_EDAM)
#to_canonical_graph(kg_ref).serialize("edam_ref.ttl", format="turtle")
#to_canonical_graph(kg_ref).serialize("edam_ref.owl", format="xml")
#sys.exit(0)

console = Console()

def reformat_edam_txt(input_file, output_file):
    console.print(f"Reformatting {input_file}")
    kg = ConjunctiveGraph().parse(input_file)
    kg.serialize(format="turtle")
    
    

def diff_edam_txt(rdf_1, rdf_2):
    console.print(f"Diffing {rdf_1} with {rdf_2}")
    with Progress() as progress:
        task1 = progress.add_task("[red]Computing diff ...", total=5)
        while not progress.finished:
            kg_1 = ConjunctiveGraph().parse(rdf_1)
            progress.update(task1, advance=1)
            progress.refresh()
            
            kg_2 = ConjunctiveGraph().parse(rdf_2)
            progress.update(task1, advance=2)
            progress.refresh()
            
            kg_1_ttl = to_canonical_graph(kg_1).serialize(format="turtle")
            progress.update(task1, advance=3)
            progress.refresh()
            
            kg_2_ttl = to_canonical_graph(kg_2).serialize(format="turtle")
            progress.update(task1, advance=4)
            progress.refresh()
        
            diff_output = difflib.unified_diff(kg_1_ttl.splitlines(keepends=True), kg_2_ttl.splitlines(keepends=True), n=3)
            progress.update(task1, advance=5)
            progress.refresh()
            
        for line in diff_output:
            if line.startswith("+"):
                console.print("[green]"+line.strip())
            elif line.startswith("-"):
                console.print("[red]"+line.strip())
            else: 
                console.print("[white]"+line.strip())
            
    
    #_ , in_first, in_second = graph_diff(kg_1, kg_2)
    #console.print("[bold]In first version:")
    #console.print(in_first.serialize(format="turtle"))   
    #console.print("[bold]In second version:")
    #console.print(in_second.serialize(format="turtle"))   

@click.command()
@click.option('--src', required=True, help='your input EDAM ontology.')
@click.option('--ref', required=True, help='the reference EDAM ontology.')
def diff_command(src, ref):
    """Simple program that prints a diff between two EDAM ontologies."""
    console.print("[bold]EDAM Diff Tool")
    console.print("[bold]-----------------")
    
    guess_format('src') 
    diff_edam_txt(src, ref)

@click.command("black")
@click.option('--check', is_flag=True, help='...')
@click.option('--diff', is_flag=True, help='...')
@click.argument('filename',  type=click.Path(exists=True))
def black_command(check, diff, filename):
    """Simple program that prints a diff between two EDAM ontologies."""
    #console.print("[bold]EDAM Diff Tool")
    #console.print("[bold]-----------------")
    
    rdf_format = guess_format(filename) 
    console.print(f"{filename} format: {rdf_format}") 
    if not rdf_format in ["xml", "turtle"]:
        exit(1)
    else:
        console.print(f"Checking {filename}")
        with open(filename, "r") as f:
            content = f.readlines()
            kg = ConjunctiveGraph().parse(filename)
            kg_normalized_txt = to_canonical_graph(kg).serialize(format=rdf_format)
        
            diff_output = difflib.unified_diff(content, kg_normalized_txt.splitlines(keepends=True), n=3)
        
            #if check:
                #console.print("[bold]Checking "+filename)
                #console.print(f"{len(list(diff_output))} differences found")
            
            if diff:
                console.print("[bold]Diff "+filename)
                for line in diff_output:
                    if line.startswith("+"):
                        console.print("[green]"+line.strip())
                    elif line.startswith("-"):
                        console.print("[red]"+line.strip())
                    else: 
                        console.print("[white]"+line.strip())
        
    #diff_edam_txt(src, ref)

@click.group()
def entry_point():
    pass

entry_point.add_command(black_command)
entry_point.add_command(diff_command)

if __name__ == '__main__':
    entry_point()