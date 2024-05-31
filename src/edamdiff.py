
from rdflib import ConjunctiveGraph
from rdflib.compare import to_isomorphic, graph_diff, to_canonical_graph
import difflib

from rich.progress import Progress
from rich.console import Console

import click

_UNSTABLE_EDAM = "https://edamontology.org/EDAM_unstable.owl"
_STABLE_EDAM = "https://edamontology.org/EDAM.owl"

console = Console()

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
    diff_edam_txt(src, ref)

if __name__ == '__main__':
    #ref_edam = ConjunctiveGraph().parse(_STABLE_EDAM)
    #ref_edam.serialize("edam_ref.ttl", format="turtle")
    #ref_edam.serialize("edam_ref.owl", format="xml")
    diff_command()