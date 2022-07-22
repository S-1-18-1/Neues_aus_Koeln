import csv
import os
import re
#import pandas as pd

dataPath ="data/1903"
outputName = "1903"
corpus = {}


# def readInLine (index_of_line, line_list, this_files_stories):
#     line_content = line_list[index_of_line]
#     if re.match("[TL]ocales", line_content) or re.match("aus Köln .{1}$", line_content) or re.match("aus Köln\n", line_content):
#         i = 0
#         while i < 30:
#             new_line = line_list[index_of_line+i] 
#             if len(new_line) >= 10 and line[1] == " " :
#                 this_files_stories.append(new_line)
#                 if len(line.strip()) > 0 and line.strip()[-1] not in [".", "!", "?", "—"]:
                    

                
           

#df_lines = pd.DataFrame(lines)

#print(df_lines)

for root, dir, files in os.walk(dataPath):
    for file_name in files:
        file_path = os.path.join(root, file_name)
        with open (file_path, 'r') as f:
            lines = []
            for line in f:
               lines.append(line)
        
        richtigeRubrik = -1
        story = -1
        addNext = False

        for index, current_line in enumerate(lines):
            if richtigeRubrik >= 0:
                if "Standesamt" in current_line or "Vermischte Nachrichten" in current_line or "Gerichts=Verhandlungen" in current_line or "Kölner Local-Anzeiger Nr." in current_line or re.match("Ne[un]este Nachrichten", current_line):
                    richtigeRubrik = -1
                elif len(current_line) >= 20 and current_line[1] == " " :

                    if "Geburten" not in current_line and "Heiraten" not in current_line and "Sterbefälle":
                        story +=1
                        addNext = False
                        try: 
                            corpus[str(file_name)].update({story : current_line})
                        except KeyError:
                            corpus[str(file_name)]={story : current_line}
                                
                        if len(current_line.strip()) > 0 and current_line.strip()[-1] not in [".", "!", "?", "—"]:
                            addNext = True                
                                
                elif addNext==True and len(current_line) >= 20:
                    addNext = False
                    try: 
                        new_s = corpus[str(file_name)][story] + current_line
                        corpus[str(file_name)][story] = new_s
                    except KeyError:
                        continue
                    if len(current_line.strip()) > 0 and current_line.strip()[-1] not in [".", "!", "?", "—"]:
                        addNext = True

        
                richtigeRubrik -=1
                    
            elif re.match("[TL]ocales", current_line) or re.match("aus Köln .{1}$", current_line) or re.match("aus Köln\n", current_line):
                richtigeRubrik = 30
                        
            else:
                continue
        

with open("%s.txt" %outputName, "w") as file:
    textToWrite = ""
    for k, v in corpus.items():
        textToWrite += k
        textToWrite += ":\n \n"

        for key, story in v.items():
            textToWrite += story
            textToWrite += "\n \n"

            
    file.write(textToWrite)