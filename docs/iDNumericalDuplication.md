# Duplicat use of numerical component of EDAM concept ID

**Problem:** The numerical component of an EDAM concept ID is duplicated in some other concept ID.

**Solution:** Inspect the concepts with the duplication and refactor the one or the other IDs accordingly.

**Further information:** The numerical component of EDAM concepts IDs must be unique across the four EDAM namespaces. See [here](https://edamontologydocs.readthedocs.io/en/latest/technical_details.html#identifiers-persistent-urls) for more information.


**Query:** [iDNumericalDuplication.sparql](https://github.com/edamontology/edamverify/blob/master/queries/iDNumericalDuplication.sparql)

```sparql
PREFIX obo: <http://purl.obolibrary.org/obo/>
PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ... <todo>
```
