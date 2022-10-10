
import re

RESOURCES = "./notes/resources.bib"

with open(RESOURCES) as f:
    for line in f:
        title = re.search('.*?\{(.*)}.*', line)
        print(title)