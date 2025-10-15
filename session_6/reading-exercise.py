"""This script should takes an unzipped ALTO created by eScriptorium and parses some data from it.py

Read the script and try to figure out what it is doing with the ALTO XML files. The main function has
already been annotated for you - use this to help you understand the rest of the code.

Once you understand the script, try modifying it to work with your own eScriptorium ALTO files and apply it to an eScriptorium export"""

# === CODE Between these markers are functions used by the script - this has been fully commented to guide you ===

# Import the XML library to parse XML and the os library to work with file paths
import xml.etree.ElementTree as ET
import os

def parse_alto_regions(alto_xml_file):
    """Parse ALTO XML file to extract text regions.

    Args:
        alto_xml_file (str): Path to the ALTO XML file.

    Returns:
        list: List of dictionaries containing text region information.
        Dictionary structure as follows:
        {
            "Label": str,        # Region label (e.g., "Text", "Image", etc.)
            "Width": int,       # Width of the region
            "Height": int,      # Height of the region
            "Area": int,        # Area of the region (Width * Height)
            "TokenCount": int   # Number of tokens in the region
    """
    # Parse the ALTO XML file - get all of the data from it in a structured fashion
    tree = ET.parse(alto_xml_file)
    root = tree.getroot()

    # Define the ALTO namespace (used so that we can find the relevant parts of the xml)
    ns_uri = root.tag[root.tag.find("{")+1 : root.tag.find("}")]
    ns = {"alto": ns_uri}

    # Fetch the region labels from OtherTag (where eScriptorium stores regions)
    region_labels = {}
    for other_tag in root.findall(".//alto:OtherTag", ns):
        region_labels[other_tag.attrib["ID"]] = other_tag.attrib["LABEL"]


    regions = []
    # Loop through each textblock element in the XML and match the IDs to the region labels (so we have region data)
    for text_block in root.findall(".//alto:TextBlock", ns):
        
        # Get the region label using TAGREFS attribute of the text_block - if no label found, set to "Unknown"
        region_label = region_labels.get(text_block.attrib.get("TAGREFS"), "Unknown")

        # Get dimensions of region if it is available
        width = text_block.attrib.get("WIDTH")
        height = text_block.attrib.get("HEIGHT")
        if width and height:
            area = int(width) * int(height)
        else:
            area = None

        # Get the token count for the region

        # Initialise an empty list to hold all text strings for the region (text_block)
        full_text = []

        # Loop through the strings and append them to the list
        for string in text_block.findall(".//alto:String", ns):
            full_text.append(string.attrib.get("CONTENT", ""))
        
        # To count words - we join the list of lines using spaces and then split it and count the length of the resulting list
        token_count = len(" ".join(full_text).split())

        # The resulting data is stored as a dictionary
        region_info = {
            "Label": region_label,
            "Width": width,
            "Height": height,
            "Area": area,
            "TokenCount": token_count
        }

        # The dictionary is appended to a final list for the page
        regions.append(region_info)

    return regions

# == End of commented code ==


alto_directory = "sample_data/muqaffa_or14533_alto"


alto_files = os.listdir(alto_directory)

total_regions = 0
region_types = []
main_regions = ["Text", "MainZone"]
marginal_region = ["MarginTextZone", "MarginTextZone:footnote", "footnote"]

main_regions_types = 0
marginal_region_types = 0

for file in alto_files:


    file_path = os.path.join(alto_directory, file)


    regions = parse_alto_regions(file_path)
    
    for region in regions:
        label = region["Label"]
        area = region["Area"]
        token_count = region["TokenCount"]

        if label not in region_types:
            region_types.append(label)
            total_regions += 1
        
        if

        if label not in regions_summary:
            regions_summary[label] = {"total_area": 0, "total_token_count": 0, "count": 0}
        
        regions_summary[label]["total_area"] += area
        regions_summary[label]["total_token_count"] += token_count
        regions_summary[label]["count"] += 1


summary_list = []
for region in regions_summary:
    data = regions_summary[region]
    summary_list.append({
        "region_name": region,
        "total_area": data["total_area"],
        "total_token_count": data["total_token_count"],
        "count": data["count"]
    })

# 3. Finally, loop through the list and print out each region's summary data
total_regions = 0
region_types = 0
for summary in summary_list:

    # Get the data we need to print
    region_name = summary["region_name"]
    total_area = summary["total_area"]
    total_token_count = summary["total_token_count"]
    count = summary["count"]

    # Print the data nicely

    print("Region Summary:", region_name)
    print("Total Area:", total_area)
    print("Total Token Count:", total_token_count)
    print("Count:", count)
    print("----\n")
    
    total_regions += summary["count"]
    region_types += 1


print(total_regions, "regions found in total across all files.")
print(region_types, "different region types found.")
