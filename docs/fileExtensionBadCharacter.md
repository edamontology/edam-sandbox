# EDAM Format concept file extension contains disallowed characters

**Problem:** A file extension specified for an EDAM Format concept contains disallowed characters (they must contain only lowercase alphanumeric characters).

**Solution:** Change the file extension value so that it contains lowercase alphanumeric characters only.

**Further information:** File extensions must not container the period (```.```) or any other disallowed characters. See [EDAM Developers Guide](https://edamontologydocs.readthedocs.io/en/latest/developers_guide.html#optional-attributes) for more information.


**Query:** [fileExtensionBadCharacter.ipynb](https://github.com/edamontology/edamverify/blob/master/queries/fileExtensionBadCharacter.ipynb)

```
import io
import sys
from rdflib import ConjunctiveGraph, Namespace

# Constants for script return value as per https://github.com/edamontology/edamverify.
NOERR = 0
INFO  = 1
WARN  = 2
ERROR = 3

#Load EDAM_dev.owl from GitHub into an RDF graph.
print("Loading graph ...", end="")
g = ConjunctiveGraph()
g.load('https://raw.githubusercontent.com/edamontology/edamontology/master/EDAM_dev.owl', format='xml')
g.bind('edam', Namespace('http://edamontology.org#'))
print("done!")

# Compile SPARQL query
query_term = """
BASE <http://edamontology.org/>
SELECT ?id ?term ?ext WHERE
{
?id rdfs:label ?term .
?id :file_extension ?ext .
}
"""

# Run SPARQL query and collate results
errfound = False    
report = list()
results = g.query(query_term)
for r in results :
    # print(str(r['id']), str(r['term']), str(r['ext']))
    id   = str(r['id'])
    term = str(r['term']) 
    ext  = str(r['ext'])

    if not ext.isalnum() or ext != ext.lower(): 
        errfound = True
        report.append(id +  ' (' + term + '): ' + ext)

# Return exit code (raises exception) 
if errfound == True:
    print("Issues found with <file_extension> property of these concepts:")
    print("\n".join(report))
    sys.exit(WARN)
else:
    print("No issues found.")
    sys.exit(NOERR)
```
