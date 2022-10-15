
import fileinput
import re

RESOURCES = "./notes/resources.bib"
LINKS = "./notes/resources_links.txt"
RESEARCH_PAPERS = "./notes/research_papers.md"

titles, links = [], []
with open(RESOURCES) as f:
    for line in f:
        match = re.search('title={(.*?)}', line)
        if match is None:
            continue
        titles += [match.group()[7:-1]]

with open(LINKS) as f:
    links = [line for line in f]

with open(RESEARCH_PAPERS, 'r') as f:
    filedata = f.read()

filedata = filedata.split('\n')[:8]

for title, link in zip(titles, links):
    filedata += ["[{}]({})".format(title, link)]

with open(RESEARCH_PAPERS, 'w') as f:
    for line in filedata:
        print(line, file=f)