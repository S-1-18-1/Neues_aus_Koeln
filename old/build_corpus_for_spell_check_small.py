from lxml import etree as ET
import os

path="corpus"
output = "corpus_for_spellcheck.txt"
stories = []

parser = ET.XMLParser(remove_blank_text=True)

for root, dir, files in os.walk(path):
    for file_name in files:
        full_path = os.path.join(path, file_name)
        tree = ET.parse(full_path, parser)
        for story in tree.findall(".//text"):
            stories.append(story.text)


with open(output, "w") as f:
    i=0
    while i < len(stories):
        f.write(str(stories[i])+"\n")
        i+=1

