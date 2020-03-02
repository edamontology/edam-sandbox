#  Identifier concept with redundant is_identifier_of relationship

**Problem:**
An *is_identifier_of* relationship from an Identifier to a Data concept is redundant, because the relationship is already stated on an ancestor of the Identifier concept.


**Solution:** Remove the offending relationship.

**Further information:** The *is_identifier_of* [relationship](https://edamontologydocs.readthedocs.io/en/latest/technical_details.html#id1) between an EDAM Identifier and Data concept must be stated once only, *i.e.* once stated on a concept, it must not be restated on children of that concept.  See [here](https://edamontologydocs.readthedocs.io/en/latest/developers_guide.html#hierarchy) for more information.


**Query:** [isIdentifierOfRedundancy.sparql](https://github.com/edamontology/edamverify/blob/master/queries/isIdentifierOfRedundancy.sparql)

```sparql
PREFIX obo: <http://purl.obolibrary.org/obo/>
PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ... <todo>
```
