# Concept ID namespace does not match specified subset

**Problem:** The namespace of a concept URI (ID) does not match the specified EDAM branch subset.

**Solution:** Change either the ID namespace or the subset, as appropriate for the concept definition, so that they match.

**Further information:** The URI [namespace](https://edamontologydocs.readthedocs.io/en/latest/technical_details.html#identifiers-persistent-urls) of an EDAM concept ID, *e.g.* ```http://edamontology.org/topic_```, must match the EDAM [branch subset](https://edamontologydocs.readthedocs.io/en/latest/developers_guide.html#mandatory-attributes) to which the concept has been assigned by setting the ```oboInOwl:inSubset``` to one of ```topic```, ```operation```, ```data``` or ```format```.  


**Query:** [namespaceSubsetMismatch.sparql](https://github.com/edamontology/edamverify/blob/master/queries/namespaceSubsetMismatch.sparql)

```sparql
PREFIX obo: <http://purl.obolibrary.org/obo/>
PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ... <todo>
```
