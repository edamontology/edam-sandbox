import shutil
import tempfile

from edamfu.tree import reorder_root, add_comments

from edamfu.utils import (
    escape_irrelevant_xml_entities_in_text,
    unescape_irrelevant_xml_entities_in_text,
    prettify_xml,
)


def reformat(input_file_path, output_file_path):
    temp_edam_file = tempfile.NamedTemporaryFile(delete=False)
    temp_edam_file.close()
    shutil.copy2(input_file_path, temp_edam_file.name)
    escape_irrelevant_xml_entities_in_text(temp_edam_file.name)
    reorder_root(temp_edam_file.name)
    add_comments(temp_edam_file.name)
    unescape_irrelevant_xml_entities_in_text(temp_edam_file.name)
    prettify_xml(temp_edam_file.name)
    shutil.copy2(temp_edam_file.name, output_file_path)
    return output_file_path
