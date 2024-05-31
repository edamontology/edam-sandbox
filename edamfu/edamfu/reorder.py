import shutil
from edamfu.core import reformat

# Input file:
xml_file_path = (
    "/home/hmenager/edamfu/tests/EDAM_dev.owl"  # Replace with the path to your XML file
)
# Processed file
sorted_path = "/home/hmenager/edamfu/tests/EDAM_dev.processed.owl"

reformat(xml_file_path, sorted_path)
