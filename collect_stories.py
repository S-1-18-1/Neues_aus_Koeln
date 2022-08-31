import csv
import os
import re
import copy
import pandas as pd
from lxml import etree as ET

dataPath ="data"
template = "template.xml"

outputName = "corpora"

corpus = {}


week_day_names = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
week_day_regex = []

for regex in week_day_names:
    week_day_regex.append(re.compile(regex, re.IGNORECASE))

other_categories = ["Aus Kölns Nachbarschaft\.", "Aus dem sozialen Leben\.", "Aus dem Geschäftsverkehr\.", "Unterhaltendes\.", "Aus der Arbeiterwelt\.", "Von Nah und Fern\.", "Mitteilungen\.", "Gerichts[-=]Verhandlungen\.", "Kirchliches\.", "Gesellschafts- und Vereinsleben\.", "Standesamt\.", "Was der .* bringt\.", "Kölner Local-Anzeiger"]
# other_categories_regex = map(re.compile, other_categories)
other_categories_regex = []
for regex in other_categories:
    other_categories_regex.append(re.compile(regex, re.IGNORECASE))

two_char_words = ["In", "Im", "An", "Ab", "Am", "Da", "Du", "Er", "Ja", "Wo", "Zu", "Es", "Um", "\d(\.)*"] 
two_char_regex = []

for regex in two_char_words:
    two_char_regex.append(re.compile(regex, re.IGNORECASE))

for root, dir, files in os.walk(dataPath):
    for file_name in files:
        file_path = os.path.join(root, file_name)
        with open (file_path, 'r') as f:
            lines = []
            for line in f:
               lines.append(line)

        richtigeRubrik = 0
        story = -1
        addNext = False

        for index, current_line in enumerate(lines):
            if richtigeRubrik > 0:
                
                if any(regex.match(current_line) for regex in other_categories_regex):
                    # Beginn einer neuen (falschen) Kategorie
                    richtigeRubrik = 0
                elif len(current_line) >= 40 and len(current_line.split(" ")[0]) < 3 and not any(regex.match(current_line.split(" ")[0]) for regex in two_char_regex): 
                    # Anfang einer Story (getrennt vom einzelnen Symbol)

                    story +=1
                    addNext = False

                    try: 
                        corpus[str(file_name)].update({story : current_line})
                    except KeyError:
                        corpus[str(file_name)]={story : current_line}
                       


                    if len(current_line.strip()) > 0 and current_line.strip()[-1] not in [".", "!", "?", "—"]:
                         addNext = True   
                elif addNext==True and len(current_line) >= 40:
                    # Fortsetzung einer Story
                    new_s = corpus[str(file_name)][story] + current_line
                    corpus[str(file_name)][story] = new_s
                    addNext = False

                    if len(current_line.strip()) > 0 and current_line.strip()[-1] not in [".", "!", "?", "—"]:
                        addNext = True

                #sammeln

            # finden einer richtigen Kategorie
            elif re.match("\w*[TLk][oes][ce]a[lt]es($|\.)", current_line):
                richtigeRubrik = 30
            elif re.match("aus [RKtA][öo][li](n|\.)", current_line) and re.match("[TNLn]eues", lines[index-1]):                
                    richtigeRubrik = 30
            elif re.match("(aus [RKtA][öo][li]n)(\.)?$", current_line) and ("Anzeiger" in lines[index-1] or any(name in lines[index-1] for name in week_day_names) or "Seite" in lines[index-1] or len(lines[index-1])<=7) and len(lines[index-1])<70:
                    richtigeRubrik = 30
            elif re.match("[Aa]us [RKtA][öo][li]n-", current_line):
                    richtigeRubrik = 5
                    # Stadtteilanzeigen

parser = ET.XMLParser(remove_blank_text=True)

# root = tree.getroot()

for ausgabe, v in corpus.items():
    tree = ET.parse(template, parser)
    metadata = ausgabe.split("_")
    tree.find(".//year").text=metadata[0]
    tree.find(".//month").text=metadata[1]
    tree.find(".//day").text=metadata[2]
    tree.find(".//ID").text=metadata[3].split(".")[0]
    # print(len(v))
    # print(tree)
    story_xml = tree.find(".//story")  
    if story_xml == None:
        print("uhuh")
    count=len(v)
    print(count)
    if count != 0: 
        for i in range(0, count):
            if i > 0:
                story_xml.addnext(copy.deepcopy(story_xml))
        all_stories=tree.findall(".//story")
        print(len(all_stories))

        for key, story in v.items():
            text_to_write = story.replace(story.split(" ")[0],"").replace("\n"," ")
            all_stories[key].find(".//number").text=str(key)
            all_stories[key].find(".//text").text=text_to_write

    tree.write("corpus/%s.xml" %metadata[3].split(".")[0], pretty_print=True, encoding='utf-8')        

# for ausgabe, v in corpus.items():
#     for key, story in v.items():
#         #print(story)
#         #open("%s/%s_%s" %(outputName, str(key), ausgabe ),'wb').write(story)
#         with open("%s/%s_%s" %(outputName, str(key), ausgabe ),'w') as file:
#             file.write(story)

# for elem in list(template.iter()):
#         if recursively_empty(elem):
#             elem.getparent().remove(elem)    