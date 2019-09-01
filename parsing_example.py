from lxml import html, etree
import requests

# Parsing involves taking the raw data that we get from the website and parse it into a structured way

# Get an example page, of the Audio category from Indiegogo.com
page = requests.get("https://www.indiegogo.com/explore/audio?project_type=campaign&project_timing=all&sort=trending")
print (page.content)

tree = html.fromstring(page.content)
print (tree)

all_nodes = tree.xpath("//*")

# Select only the hyperlink nodes
hyperlink_nodes = tree.xpath("//*/a")

# Iterate through the node links
for node in hyperlink_nodes:
    print (node.values())

