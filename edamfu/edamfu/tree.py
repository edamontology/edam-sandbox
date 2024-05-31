import xml.etree.ElementTree as ET

SUBSET_ORDER = [
    "http://edamontology.org/properties",
    "http://edamontology.org/data",
    "http://edamontology.org/bio",
    "http://edamontology.org/events",
    "http://edamontology.org/obsolete",
    "http://edamontology.org/formats",
    "http://edamontology.org/identifiers",
    "http://edamontology.org/operations",
    "http://edamontology.org/topics",
]


def get_element_sort_keys(elem, parent, root):
    """
    This function returns a tuple of two values that are used to sort the element `elem` in the XML tree.
    Elements of context are the parent element `parent` and the root element `root` of the XML tree.
    The tuple of two values return sorts the elements using the order of the element type (tag) as the first key,
    and the alphabetical value a value identifying the element as the second key (usually `text()` or `rdf:resource`).
    :param elem: the element to be sorted
    :param parent: the parent element of `elem`
    :param root: the root element of the XML tree
    :return: a tuple of two values used to sort the element `elem` in the XML tree
    """
    # first reorder by element order
    # then reorder by the alphabetical value of the owl:Class/@rdf:about or the owl:Axiom/owl:annotatedSource/@rdf:resource
    first_key = -1
    secondary_key = "__"
    ## first-level elements (child nodes of RDF)
    if parent.tag == "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}RDF":
        if elem.tag == "{http://www.w3.org/2002/07/owl#}Ontology":
            first_key = 1
            # unique, no need for secondary_key
        elif elem.tag == "{http://www.w3.org/2002/07/owl#}AnnotationProperty":
            first_key = 2
            secondary_key = elem.get(
                "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about"
            )
        elif elem.tag == "{http://www.w3.org/2002/07/owl#}ObjectProperty":
            first_key = 3
            secondary_key = elem.get(
                "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about"
            )
        elif elem.tag == "{http://www.w3.org/2002/07/owl#}Class":
            first_key = 4
            secondary_key = elem.get(
                "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about"
            )
        elif elem.tag == "{http://www.w3.org/2002/07/owl#}Axiom":
            secondary_key = elem.find(
                "{http://www.w3.org/2002/07/owl#}annotatedSource"
            ).get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource")
            # if annotatedSource is an owl:Class
            if root.find(
                f".//{{http://www.w3.org/2002/07/owl#}}Class[@{{http://www.w3.org/1999/02/22-rdf-syntax-ns#}}about='{secondary_key}']"
            ):
                first_key = 4
            # elif annotatedSource is an owl:ObjectProperty
            elif root.find(
                f".//{{http://www.w3.org/2002/07/owl#}}ObjectProperty[@{{http://www.w3.org/1999/02/22-rdf-syntax-ns#}}about='{secondary_key}']"
            ):
                first_key = 3
    ## second-level elements below owl:Ontology
    elif parent.tag == "{http://www.w3.org/2002/07/owl#}Ontology":
        if elem.tag == "{http://edamontology.org/}next_id":
            first_key = 1
            # unique, no need for secondary_key
        elif elem.tag == "{http://purl.obolibrary.org/obo/}date":
            first_key = 2
            # unique, no need for secondary_key
        elif elem.tag == "{http://purl.obolibrary.org/obo/}idspace":
            first_key = 3
            secondary_key = elem.text
        elif elem.tag == "{http://purl.obolibrary.org/obo/}remark":
            first_key = 4
            secondary_key = elem.text
        elif elem.tag == "{http://purl.org/dc/elements/1.1/}contributor":
            first_key = 5
            secondary_key = elem.text
        elif elem.tag == "{http://purl.org/dc/elements/1.1/}creator":
            first_key = 6
            secondary_key = elem.text
        elif elem.tag == "{http://purl.org/dc/elements/1.1/}format":
            first_key = 7
            secondary_key = elem.text
        elif elem.tag == "{http://purl.org/dc/terms/}format":
            first_key = 8
            secondary_key = elem.get(
                "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource"
            )
        if elem.tag == "{http://edamontology.org/}has_format":
            first_key = 9
            secondary_key = elem.get(
                "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource"
            )
        elif elem.tag == "{http://purl.org/dc/elements/1.1/}title":
            first_key = 10
            secondary_key = elem.text
        elif elem.tag == "{http://purl.org/dc/elements/1.1/}description":
            first_key = 11
            secondary_key = elem.text
        elif elem.tag == "{http://usefulinc.com/ns/doap#}Version":
            first_key = 12
            secondary_key = elem.text
        elif elem.tag == "{http://purl.org/dc/terms/}license":
            first_key = 13
            secondary_key = elem.get(
                "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource"
            )
        elif elem.tag == "{http://www.geneontology.org/formats/oboInOwl#}hasSubset":
            first_key = 14
            secondary_key = SUBSET_ORDER.index(
                elem.get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource")
            )
        elif elem.tag == "{http://www.geneontology.org/formats/oboInOwl#}savedBy":
            first_key = 15
            secondary_key = elem.text
        elif elem.tag == "{http://www.w3.org/2000/01/rdf-schema#}isDefinedBy":
            first_key = 16
            secondary_key = elem.get(
                "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource"
            )
        elif elem.tag == "{http://xmlns.com/foaf/0.1/}page":
            first_key = 17
            secondary_key = elem.get(
                "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource"
            )
        elif elem.tag == "{http://xmlns.com/foaf/0.1/}logo":
            first_key = 18
            secondary_key = elem.get(
                "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource"
            )
        elif elem.tag == "{http://edamontology.org/}repository":
            first_key = 19
            secondary_key = elem.get(
                "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource"
            )
        elif elem.tag == "{http://edamontology.org/}citation":
            first_key = 20
            secondary_key = elem.get(
                "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource"
            )
    ## second-level elements below owl:AnnotationProperty
    elif parent.tag == "{http://www.w3.org/2002/07/owl#}AnnotationProperty":
        if elem.tag == "{http://edamontology.org/}created_in":
            first_key = 1
            # unique, no need for secondary_key
        elif elem.tag == "{http://purl.obolibrary.org/obo/}is_metadata_tag":
            first_key = 2
            # unique, no need for secondary_key
        elif (
            elem.tag == "{http://www.geneontology.org/formats/oboInOwl#}hasBroadSynonym"
        ):
            first_key = 3
            secondary_key = elem.text
        elif elem.tag == "{http://www.geneontology.org/formats/oboInOwl#}hasDefinition":
            first_key = 4
            # unique, no need for secondary_key
        elif (
            elem.tag == "{http://www.geneontology.org/formats/oboInOwl#}hasExactSynonym"
        ):
            first_key = 5
            secondary_key = elem.text
        elif (
            elem.tag
            == "{http://www.geneontology.org/formats/oboInOwl#}hasNarrowSynonym"
        ):
            first_key = 6
            secondary_key = elem.text
        elif (
            elem.tag
            == "{http://www.geneontology.org/formats/oboInOwl#}hasRelatedSynonym"
        ):
            first_key = 7
            secondary_key = elem.text
        elif elem.tag == "{http://www.geneontology.org/formats/oboInOwl#}inSubset":
            first_key = 8
            secondary_key = SUBSET_ORDER.index(
                elem.get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource")
            )
        elif elem.tag == "{http://www.w3.org/2000/01/rdf-schema#}comment":
            first_key = 9
            secondary_key = elem.text
        elif elem.tag == "{http://www.w3.org/2000/01/rdf-schema#}label":
            first_key = 10
            # unique, no need for secondary_key
        elif elem.tag == "{http://www.w3.org/2000/01/rdf-schema#}subPropertyOf":
            first_key = 11
            secondary_key = elem.get(
                "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource"
            )
    ## second-level elements below owl:ObjectProperty
    elif parent.tag == "{http://www.w3.org/2002/07/owl#}ObjectProperty":
        if elem.tag == "{http://www.w3.org/2002/07/owl#}inverseOf":
            first_key = 1
            secondary_key = elem.get(
                "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource"
            )
        elif elem.tag == "{http://www.w3.org/2000/01/rdf-schema#}domain":
            first_key = 2
            # unique, no need for secondary_key
        elif elem.tag == "{http://www.w3.org/2000/01/rdf-schema#}range":
            first_key = 3
            # unique, no need for secondary_key
        elif elem.tag == "{http://purl.obolibrary.org/obo/}is_anti_symmetric":
            first_key = 4
            # unique, no need for secondary_key
        elif elem.tag == "{http://purl.obolibrary.org/obo/}is_reflexive":
            first_key = 5
            # unique, no need for secondary_key
        elif elem.tag == "{http://purl.obolibrary.org/obo/}is_symmetric":
            first_key = 6
            # unique, no need for secondary_key
        elif elem.tag == "{http://purl.obolibrary.org/obo/}transitive_over":
            first_key = 7
            secondary_key = elem.text
        elif (
            elem.tag == "{http://www.geneontology.org/formats/oboInOwl#}hasBroadSynonym"
        ):
            first_key = 8
            secondary_key = elem.text
        elif elem.tag == "{http://www.geneontology.org/formats/oboInOwl#}hasDefinition":
            first_key = 9
            # unique, no need for secondary_key
        elif (
            elem.tag == "{http://www.geneontology.org/formats/oboInOwl#}hasExactSynonym"
        ):
            first_key = 10
            secondary_key = elem.text
        elif (
            elem.tag
            == "{http://www.geneontology.org/formats/oboInOwl#}hasNarrowSynonym"
        ):
            first_key = 11
            secondary_key = elem.text
        elif (
            elem.tag
            == "{http://www.geneontology.org/formats/oboInOwl#}hasRelatedSynonym"
        ):
            first_key = 12
            secondary_key = elem.text
        elif elem.tag == "{http://www.geneontology.org/formats/oboInOwl#}inSubset":
            first_key = 13
            secondary_key = elem.get(
                "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource"
            )
        elif elem.tag == "{http://www.geneontology.org/formats/oboInOwl#}isCyclic":
            first_key = 14
            # unique, no need for secondary_key
        elif elem.tag == "{http://www.w3.org/2000/01/rdf-schema#}comment":
            first_key = 15
        elif elem.tag == "{http://www.w3.org/2000/01/rdf-schema#}label":
            first_key = 16
            # unique, no need for secondary_key
        elif elem.tag == "{http://www.w3.org/2004/02/skos/core#}broadMatch":
            first_key = 17
            secondary_key = elem.get(
                "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource"
            )
        elif elem.tag == "{http://www.w3.org/2004/02/skos/core#}closeMatch":
            first_key = 18
            secondary_key = elem.get(
                "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource"
            )
        elif elem.tag == "{http://www.w3.org/2004/02/skos/core#}exactMatch":
            first_key = 19
            secondary_key = elem.get(
                "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource"
            )
        elif elem.tag == "{http://www.w3.org/2004/02/skos/core#}relatedMatch":
            first_key = 20
            secondary_key = elem.get(
                "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource"
            )
    ## second-level elements below owl:Axiom
    elif parent.tag == "{http://www.w3.org/2002/07/owl#}Axiom":
        if elem.tag == "{http://www.w3.org/2002/07/owl#}annotatedSource":
            first_key = 1
            secondary_key = (
                elem.get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource")
                or elem.text
            )
        if elem.tag == "{http://www.w3.org/2002/07/owl#}annotatedProperty":
            first_key = 2
            secondary_key = (
                elem.get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource")
                or elem.text
            )
        if elem.tag == "{http://www.w3.org/2002/07/owl#}annotatedTarget":
            first_key = 3
            secondary_key = (
                elem.get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource")
                or elem.text
            )
        elif elem.tag == "{http://www.w3.org/2000/01/rdf-schema#}comment":
            first_key = 4
            secondary_key = (
                elem.get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource")
                or elem.text
            )
    ## second-level elements below owl:Class
    elif parent.tag == "{http://www.w3.org/2002/07/owl#}Class":
        if elem.tag == "{http://www.w3.org/2000/01/rdf-schema#}subClassOf":
            first_key = 1
            secondary_key = elem.get(
                "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource"
            )
            if secondary_key is None:
                restr_elem = elem.find(".{http://www.w3.org/2002/07/owl#}Restriction")
                secondary_key = (
                    "z"
                    + restr_elem.find(
                        ".{http://www.w3.org/2002/07/owl#}onProperty"
                    ).get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource")
                    + "/"
                    + restr_elem.find(
                        "./{http://www.w3.org/2002/07/owl#}someValuesFrom"
                    ).get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource")
                )
        elif elem.tag == "{http://edamontology.org/}comment_handle":
            first_key = 2
            secondary_key = elem.get(
                "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource"
            )
        elif elem.tag == "{http://edamontology.org/}citation":
            first_key = 3
            secondary_key = elem.get(
                "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource"
            )
        elif elem.tag == "{http://edamontology.org/}created_in":
            first_key = 4
            # unique, no need for secondary_key
        elif elem.tag == "{http://edamontology.org/}deprecation_comment":
            first_key = 5
            secondary_key = elem.text
        elif elem.tag == "{http://edamontology.org/}documentation":
            first_key = 6
            secondary_key = (
                elem.get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource")
                or elem.text
            )
        elif elem.tag == "{http://www.w3.org/2002/07/owl#}disjointWith":
            first_key = 7
            secondary_key = elem.get(
                "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource"
            )
        elif elem.tag == "{http://edamontology.org/}example":
            first_key = 8
            secondary_key = (
                elem.get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource")
                or elem.text
            )
        elif elem.tag == "{http://edamontology.org/}file_extension":
            first_key = 9
            secondary_key = elem.text
        elif elem.tag == "{http://edamontology.org/}information_standard":
            first_key = 10
            secondary_key = elem.get(
                "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource"
            )
        elif elem.tag == "{http://edamontology.org/}is_deprecation_candidate":
            first_key = 11
            # unique, no need for secondary_key
        elif elem.tag == "{http://edamontology.org/}is_refactor_candidate":
            first_key = 12
            # unique, no need for secondary_key
        elif elem.tag == "{http://edamontology.org/}notRecommendedForAnnotation":
            first_key = 13
            # unique, no need for secondary_key
        elif elem.tag == "{http://edamontology.org/}media_type":
            first_key = 14
            secondary_key = (
                elem.get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource")
                or elem.text
            )
        elif elem.tag == "{http://edamontology.org/}obsolete_since":
            first_key = 15
            # unique, no need for secondary_key
        elif elem.tag == "{http://edamontology.org/}oldParent":
            first_key = 16
            secondary_key = elem.get(
                "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource"
            )
        elif elem.tag == "{http://edamontology.org/}ontology_used":
            first_key = 17
            secondary_key = (
                elem.get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource")
                or elem.text
            )
        elif elem.tag == "{http://edamontology.org/}organisation":
            first_key = 18
            secondary_key = elem.get(
                "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource"
            )
        elif elem.tag == "{http://edamontology.org/}refactor_comment":
            first_key = 19
        elif elem.tag == "{http://edamontology.org/}regex":
            first_key = 20
            # unique, no need for secondary_key
        elif elem.tag == "{http://edamontology.org/}related_term":
            first_key = 21
            secondary_key = elem.text
        elif elem.tag == "{http://edamontology.org/}repository":
            first_key = 22
            secondary_key = elem.get(
                "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource"
            )
        elif (
            elem.tag
            == "{http://www.geneontology.org/formats/oboInOwl#}hasAlternativeId"
        ):
            first_key = 23
            secondary_key = (
                elem.get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource")
                or elem.text
            )
        elif (
            elem.tag == "{http://www.geneontology.org/formats/oboInOwl#}hasBroadSynonym"
        ):
            first_key = 24
            secondary_key = (
                elem.get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource")
                or elem.text
            )
        elif elem.tag == "{http://www.geneontology.org/formats/oboInOwl#}hasDbXref":
            first_key = 25
            secondary_key = (
                elem.get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource")
                or elem.text
            )
        elif elem.tag == "{http://www.geneontology.org/formats/oboInOwl#}hasDefinition":
            first_key = 26
            # unique, no need for secondary_key
        elif (
            elem.tag == "{http://www.geneontology.org/formats/oboInOwl#}hasExactSynonym"
        ):
            first_key = 27
            secondary_key = (
                elem.get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource")
                or elem.text
            )
        elif (
            elem.tag
            == "{http://www.geneontology.org/formats/oboInOwl#}hasNarrowSynonym"
        ):
            first_key = 28
            secondary_key = (
                elem.get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource")
                or elem.text
            )
        elif (
            elem.tag
            == "{http://www.geneontology.org/formats/oboInOwl#}hasRelatedSynonym"
        ):
            first_key = 29
            secondary_key = elem.text
        elif elem.tag == "{http://www.geneontology.org/formats/oboInOwl#}inSubset":
            first_key = 30
            secondary_key = elem.get(
                "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource"
            )
        if elem.tag == "{http://www.w3.org/2000/01/rdf-schema#}comment":
            first_key = 31
            secondary_key = elem.text
        if elem.tag == "{http://www.w3.org/2000/01/rdf-schema#}label":
            first_key = 32
            # unique, no need for secondary_key
        elif elem.tag == "{http://edamontology.org/}isdebtag":
            first_key = 6.5
            # unique, no need for secondary_key
        if (
            elem.tag
            == "{http://www.geneontology.org/formats/oboInOwl#}hasHumanReadableId"
        ):
            first_key = 27.5
            secondary_key = elem.text
        if elem.tag == "{http://www.w3.org/2002/07/owl#}deprecated":
            first_key = 35
            # unique, no need for secondary_key
        elif elem.tag == "{http://www.geneontology.org/formats/oboInOwl#}consider":
            first_key = 16.5
            secondary_key = elem.get(
                "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource"
            )
        elif elem.tag == "{http://www.geneontology.org/formats/oboInOwl#}replacedBy":
            first_key = 30.5
            secondary_key = elem.get(
                "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource"
            )
        if elem.tag == "{http://www.w3.org/2000/01/rdf-schema#}seeAlso":
            first_key = 38
            secondary_key = (
                elem.get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource")
                or elem.text
            )
        elif elem.tag == "{http://www.w3.org/2004/02/skos/core#}broadMatch":
            first_key = 39
            secondary_key = elem.get(
                "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource"
            )
        elif elem.tag == "{http://www.w3.org/2004/02/skos/core#}closeMatch":
            first_key = 40
            secondary_key = elem.get(
                "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource"
            )
        elif elem.tag == "{http://www.w3.org/2004/02/skos/core#}exactMatch":
            first_key = 41
            secondary_key = elem.get(
                "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource"
            )
        elif elem.tag == "{http://www.w3.org/2004/02/skos/core#}narrowMatch":
            first_key = 42
            secondary_key = elem.get(
                "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource"
            )
        elif elem.tag == "{http://www.w3.org/2004/02/skos/core#}relatedMatch":
            first_key = 43
            secondary_key = elem.get(
                "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource"
            )
        # unionOf is the only element in the owl:Class constructs that contain it
        if elem.tag == "{http://www.w3.org/2002/07/owl#}unionOf":
            first_key = 1000
            # unique, no need for secondary_key

    ## third-level elements below owl:Class/rdfs:subClassOf
    elif parent.tag == "{http://www.w3.org/2000/01/rdf-schema#}subClassOf":
        if elem.tag == "{http://www.w3.org/2002/07/owl#}Restriction":
            first_key = 1
            secondary_key = (
                elem.find(".{http://www.w3.org/2002/07/owl#}onProperty").get(
                    "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource"
                )
                + "/"
                + elem.find("./{http://www.w3.org/2002/07/owl#}someValuesFrom").get(
                    "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource"
                )
            )
    ## third-level elements below owl:Class/owl:Restriction
    elif parent.tag == "{http://www.w3.org/2002/07/owl#}Restriction":
        if elem.tag == "{http://www.w3.org/2002/07/owl#}onProperty":
            first_key = 1
            # unique, no need for secondary_key
        if elem.tag == "{http://www.w3.org/2002/07/owl#}someValuesFrom":
            first_key = 2
            # unique, no need for secondary_key
    ## third-level elements below owl:Class/owl:unionOf
    elif parent.tag == "{http://www.w3.org/2002/07/owl#}unionOf":
        if elem.tag == "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description":
            first_key = 1
            secondary_key = elem.get(
                "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about"
            )
    ## third-level elements below owl:ObjectProperty/owl:range and owl:ObjectProperty/owl:domain
    elif (
        parent.tag == "{http://www.w3.org/2000/01/rdf-schema#}domain"
        or parent.tag == "{http://www.w3.org/2000/01/rdf-schema#}range"
    ):
        if elem.tag == "{http://www.w3.org/2002/07/owl#}Class":
            first_key = 1
    if first_key == -1 and secondary_key == "__":
        print(f"TODO: parent={parent.tag}, elem={elem.tag}")
    if secondary_key is None:
        print(f"ERROR: no secondary sort key found for {parent.tag}/{elem.tag}")
    return (first_key, secondary_key)


def reorder_elements(element, parent, root):
    """
    Recursively reorder elements in element `element`
    :param elem: the element to be sorted
    :param parent: the parent element of `elem`
    :param root: the root element of the XML tree
    :return: a new element, just reordered
    """
    new_child_elements = [reorder_elements(child, element, root) for child in element]
    sorted_elements = sorted(
        new_child_elements, key=lambda elem: get_element_sort_keys(elem, element, root)
    )
    new_element = ET.Element(element.tag, attrib=element.attrib)
    new_element.extend(sorted_elements)
    if element.text:
        new_element.text = element.text
    return new_element


def reorder_root(xml_file_path):
    """
    Reorder all elements in the XML file with path `xml_file_path`
    :param xml_file_path: path to the XML file to process
    """
    ET.register_namespace("", "http://edamontology.org/")
    ET.register_namespace("dc", "http://purl.org/dc/elements/1.1/")
    ET.register_namespace("dcterms", "http://purl.org/dc/terms/")
    ET.register_namespace("owl", "http://www.w3.org/2002/07/owl#")
    ET.register_namespace("rdf", "http://www.w3.org/1999/02/22-rdf-syntax-ns#")
    ET.register_namespace("skos", "http://www.w3.org/2004/02/skos/core#")
    ET.register_namespace("xml", "http://www.w3.org/XML/1998/namespace")
    ET.register_namespace("xsd", "http://www.w3.org/2001/XMLSchema#")
    ET.register_namespace("doap", "http://usefulinc.com/ns/doap#")
    ET.register_namespace("foaf", "http://xmlns.com/foaf/0.1/")
    ET.register_namespace("rdfs", "http://www.w3.org/2000/01/rdf-schema#")
    ET.register_namespace("oboInOwl", "http://www.geneontology.org/formats/oboInOwl#")
    ET.register_namespace("oboLegacy", "http://purl.obolibrary.org/obo/")
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    # Reorder the root element and its children recursively
    new_root = reorder_elements(root, root, root)

    # Create a new tree with the sorted root
    sorted_tree = ET.ElementTree(new_root)
    ET.indent(sorted_tree, space="    ", level=0)
    # Save the sorted XML to a new file or overwrite the existing one
    sorted_tree.write(xml_file_path, encoding="utf-8", xml_declaration=True)
    # sorted_tree.write('sorted_' + xml_file_path, encoding='utf-8', xml_declaration=True)

    print(f"XML elements reordered and saved to '{xml_file_path}'.")


def add_comments(xml_file_path):
    """
    Add comments according to the EDAM ontology convention to the file located at `xml_file_path`
    :param xml_file_path: path to the XML file to process
    """
    tree = ET.parse(xml_file_path)
    root = tree.getroot()
    for class_element in root.findall("{http://www.w3.org/2002/07/owl#}*"):
        if class_element.tag != "{http://www.w3.org/2002/07/owl#}Ontology":
            class_uri = class_element.get(
                "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about"
            )
            if class_uri is not None:
                root.insert(
                    list(root).index(class_element), ET.Comment(f" {class_uri} ")
                )
    with open(xml_file_path, "wb") as f:
        tree.write(f, encoding="utf-8", xml_declaration=True)
    print(f"Comments added to '{xml_file_path}'.")
