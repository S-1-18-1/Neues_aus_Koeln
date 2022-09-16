from lxml import etree as ET
import os

path="build_spellchecker/101110_GermanLexicon.xml"
output = "include.txt"
words = []

parser = ET.XMLParser(remove_blank_text=True)


tree = ET.parse(path, parser)
for word in tree.findall(".//wordform"):
    words.append(word.text)


with open(output, "w") as f:
    i=0
    while i < len(words):
        f.write(str(words[i])+"\n")
        i+=1

