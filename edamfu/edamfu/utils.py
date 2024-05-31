import re

IRRELEVANT_ENTITIES_DICT = {
    "&apos;": "__apos;",
    "&quot;": "__quot;",
    "&#8725;": "__8725;",
}

REVERSED_IRRELEVANT_ENTITIES_DICT = {v: k for k, v in IRRELEVANT_ENTITIES_DICT.items()}

ANNOTATION_PROPERTY_COMMENT = """
    


    <!-- 
    ///////////////////////////////////////////////////////////////////////////////////////
    //
    // Annotation properties
    //
    ///////////////////////////////////////////////////////////////////////////////////////
     -->
"""


OBJECT_PROPERTY_COMMENT = """
    


    <!-- 
    ///////////////////////////////////////////////////////////////////////////////////////
    //
    // Object Properties
    //
    ///////////////////////////////////////////////////////////////////////////////////////
     -->
"""

CLASSES_COMMENT = """
    


    <!-- 
    ///////////////////////////////////////////////////////////////////////////////////////
    //
    // Classes
    //
    ///////////////////////////////////////////////////////////////////////////////////////
     -->
"""


def escape_irrelevant_xml_entities_in_text(file_path):
    """
    Escapes "legacy" XML entities in the text of the file
    This is useful to avoid adding differences due to the automated conversion
    of these entities by the XML parser
    Note: this function must be called before the XML file is parsed, and once
    the processing is done, `unescape_irrelevant_xml_entities_in_text` must be
    call to revert the temporary changes
    :param file_path: the path to the file to process
    """
    with open(file_path, "r") as file:
        file_content = file.read()
        for entity, replacement in IRRELEVANT_ENTITIES_DICT.items():
            file_content = file_content.replace(entity, replacement)
        with open(file_path, "w") as file:
            file.write(file_content)


def unescape_irrelevant_xml_entities_in_text(file_path):
    """
    Reverse function to unescapes "legacy" XML entities in the text of the file,
    see `escape_irrelevant_xml_entities_in_text` for more details.
    :param file_path: the path to the file to process
    """
    with open(file_path, "r") as file:
        file_content = file.read()
        for entity, replacement in REVERSED_IRRELEVANT_ENTITIES_DICT.items():
            file_content = file_content.replace(entity, replacement)
        with open(file_path, "w") as file:
            file.write(file_content)


def add_after_last(s, old, new):
    pattern = re.compile(old, re.DOTALL)
    matches = pattern.findall(s)
    if matches:
        li = s.rsplit(matches[-1], 1)
        new_s = matches[-1] + new
        return new_s.join(li)


def prettify_xml(file_path):
    """
    Adjust spaces in the file to follow EDAM source "conventions"
    :param file_path: the path to the file to process
    """
    with open(file_path, "r") as file:
        file_content = file.read()
    # no trailing whitespaces at the end of an element's attributes list
    modified_content = file_content.replace('" />', '"/>')
    # normalize line breaks after an element comment
    modified_content = modified_content.replace("--><", "-->\n\n    <")
    # normalize line breaks before an element comment
    modified_content = modified_content.replace(">\n    <!--", ">\n    \n\n\n    <!--")
    modified_content = modified_content.replace(
        ">\n    \n\n\n    \n\n    <!--", ">\n    \n\n\n    <!--"
    )

    modified_content = add_after_last(
        modified_content, r"</owl:Ontology>", ANNOTATION_PROPERTY_COMMENT
    )
    modified_content = add_after_last(
        modified_content,
        r'<owl:AnnotationProperty rdf:about="[^"]*"/>',
        OBJECT_PROPERTY_COMMENT,
    )
    modified_content = add_after_last(
        modified_content, r"</owl:Axiom>", CLASSES_COMMENT
    )

    with open(file_path, "w") as file:
        file.write(modified_content)
    print(f"XML prettified in '{file_path}'.")
