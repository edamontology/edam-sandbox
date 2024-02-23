from lxml import etree
import re
from copy import copy

def get_element_sort_key(elem, order_mapping):
    first_key = order_mapping.get(elem.tag, {}).get("element_order", 0)
    if elem.tag == "{http://www.w3.org/2002/07/owl#}Class":
        secondary_key = elem.get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about")
    elif elem.tag == "{http://www.w3.org/2002/07/owl#}Axiom":
        annotated_source = elem.find("{http://www.w3.org/2002/07/owl#}annotatedSource")
        secondary_key = annotated_source.get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource") if annotated_source is not None else "zzz"
    else:
        secondary_key = "zzz"
    return (first_key, secondary_key)


## A
##  C
##   C1
##   C2
##  B
##   B1
##   B2
def reorder_elements(element, order_mapping):
    ## element=A
    sorted_elements = sorted(element, key=lambda elem: get_element_sort_key(elem, order_mapping))
    ## element=A, sorted_elements=[B,C]
    new_element = etree.Element(element.tag, attrib=element.attrib)
    if element.text:
        new_element.text = etree.CDATA(element.text)
    for child in sorted_elements:
        child = reorder_elements(child, order_mapping)
    new_element.extend(sorted_elements)
    print(new_element.tag, len(new_element.getchildren()))
    ontology = new_element.iter("{http://www.w3.org/2002/07/owl#}Ontology")
    return new_element

def add_comments(xml_file_path):
    tree = etree.parse(xml_file_path)
    root = tree.getroot()
    for class_element in root.findall("{http://www.w3.org/2002/07/owl#}*"):
        class_uri = class_element.get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about")
        root.insert(list(root).index(class_element), etree.Comment(f" {class_uri} "))
    with open(xml_file_path, "wb") as f:
        tree.write(f, encoding="utf-8", xml_declaration=True)
    print(f"Comments added to '{xml_file_path}'.")


def reorder_root(xml_file_path, order_mapping, namespaces):
    # etree.register_namespace(None, "http://edamontology.org/")
    # etree.register_namespace("dc", "http://purl.org/dc/elements/1.1/")
    # etree.register_namespace("dcterms", "http://purl.org/dc/terms/")
    # etree.register_namespace("owl", "http://www.w3.org/2002/07/owl#")
    # etree.register_namespace("rdf", "http://www.w3.org/1999/02/22-rdf-syntax-ns#")
    # etree.register_namespace("skos", "http://www.w3.org/2004/02/skos/core#")
    # etree.register_namespace("xml", "http://www.w3.org/XML/1998/namespace")
    # etree.register_namespace("xsd", "http://www.w3.org/2001/XMLSchema#")
    # etree.register_namespace("doap", "http://usefulinc.com/ns/doap#")
    # etree.register_namespace("foaf", "http://xmlns.com/foaf/0.1/")
    # etree.register_namespace("rdfs", "http://www.w3.org/2000/01/rdf-schema#")
    # etree.register_namespace("oboInOwl", "http://www.geneontology.org/formats/oboInOwl#")
    # etree.register_namespace("oboLegacy", "http://purl.obolibrary.org/obo/")

    tree = etree.parse(xml_file_path, parser=etree.XMLParser(resolve_entities=False, remove_comments=True))
    root = tree.getroot()
    etree.strip_elements(root, etree.Comment, with_tail=True)
    new_root = reorder_elements(root, order_mapping)
    ontology = new_root.iter("{http://www.w3.org/2002/07/owl#}Ontology")
    for el in ontology:
        print("##", el)

    #escape_special_characters(new_root)
    
    sorted_path = "/home/hmenager/edamfu/tests/EDAM_dev.sorted-lxml.owl"
    
    with open(sorted_path, "wb") as f:
        f.write(etree.tostring(new_root, xml_declaration=True))
    
    print(f"XML elements reordered and saved to '{sorted_path}'.")
    return sorted_path

def prettify_xml(file_path):
    with open(file_path, 'r') as file:
        file_content = file.read()
    modified_content = file_content.replace('" />', '"/>')
    modified_content = modified_content.replace('--><', '-->\n\n    <')
    modified_content = modified_content.replace('>\n    \n\n\n    \n\n    <!--', '>\n    \n\n\n    <!--')
    with open(file_path, 'w') as file:
        file.write(modified_content)
    print(f"XML prettified in '{file_path}'.")

# Example usage:
xml_file_path = "/home/hmenager/edamfu/tests/EDAM_dev.owl"  # Replace with the path to your XML file

order_mapping = {
    "{http://www.w3.org/2002/07/owl#}Ontology": {
        "element_order": 1,
        "attribute_order": {etree.QName("http://example.com/ns1", "attribute1"): 1},
    },
    "{http://www.w3.org/2002/07/owl#}AnnotationProperty": {
        "element_order": 2,
        "attribute_order": {etree.QName("http://example.com/ns1", "attribute1"): 1},
    },
    "{http://www.w3.org/2002/07/owl#}ObjectProperty": {
        "element_order": 3,
        "attribute_order": {etree.QName("http://example.com/ns1", "attribute1"): 1},
    },
    "{http://www.w3.org/2002/07/owl#}Axiom": {
        "element_order": 4,
        "attribute_order": {etree.QName("http://example.com/ns1", "attribute1"): 1},
    },
    "{http://www.w3.org/2002/07/owl#}Class": {
        "element_order": 4,
        "attribute_order": {etree.QName("http://example.com/ns1", "attribute1"): 1},
    },
}

namespaces = {"prefix1": "http://example.com/ns1", "prefix2": "http://example.com/ns2"}

sorted_path = reorder_root(xml_file_path, order_mapping, namespaces)
#add_comments(sorted_path)
#prettify_xml(sorted_path)