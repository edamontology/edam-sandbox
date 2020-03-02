#  Concrete identifier concept is missing mandatory relationships

**Problem:**
A concrete EDAM Identifier does not descend (via ```subClassOf``` relations) from 1) [Accession](http://edamontology.org/data_2091) or [Name](http://edamontology.org/data_2099) and 2) [Identifier (typed)](http://edamontology.org/data_0976) (or its kids) - these relationships are mandatory!

**Solution:** Inspect EDAM and add the missing relationship(s), to the highest level ancestor of the concept as appropriate.

**Further information:** Note the rule only applies to [concrete](https://edamontologydocs.readthedocs.io/en/latest/technical_details.html#concept-types) Identifier concepts, *i.e.* ones where the ```notRecommendedForAnnotation``` [attribute](https://edamontologydocs.readthedocs.io/en/latest/developers_guide.html#optional-attributes) has not been set to ```true```.  For more information see the [Developers Guide](https://edamontologydocs.readthedocs.io/en/latest/developers_guide.html#hierarchy).


**Query:** [identifierRelationMissing.sparql](https://github.com/edamontology/edamverify/blob/master/queries/identifierRelationMissing.sparql)

```sparql
PREFIX obo: <http://purl.obolibrary.org/obo/>
PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ... <todo>
```
