
import csv
import os
import re


dataPath ="data"
corpus = {}
containsLocales = {}
containsNeuesAusKoeln = {}


testcounter = 0

#for file in os.listdir(dataPath):
for root, dir, files in os.walk(dataPath):
    for file_name in files:
        file_path = os.path.join(root, file_name)
        richtigeRubrik = False
        story = -1
        addNext = False
        containsLocales[str(file_name)] = 0
        containsNeuesAusKoeln[str(file_name)] = 0
        with open (file_path, 'r') as f:
            
            for line in f:
                if richtigeRubrik >= 0:
                    if len(line) >= 20 and line[1] == " " :
                        story +=1
                        addNext = False
                        try: 
                            corpus[str(file_name)].update({story : line})
                        except KeyError:
                            corpus[str(file_name)]={story : line}
                        
                        if len(line.strip()) > 0 and line.strip()[-1] not in [".", "!", "?", "—"]:
                            addNext = True
                            
                    elif addNext==True:
                        addNext = False
                        try: 
                            
                            new_s = corpus[str(file_name)][story] + line
                            corpus[str(file_name)][story] = new_s
                        except KeyError:
                            continue
                        if len(line.strip()) > 0 and line.strip()[-1] not in [".", "!", "?", "—"]:
                            addNext = True
                    
    
                    richtigeRubrik -=1
                
                elif re.match("[TL]ocales", line):
                    richtigeRubrik = 30
                    
                    containsLocales[str(file_name)] +=1
                elif re.match("aus Köln .{1}$", line) or re.match("aus Köln\n", line):
                    richtigeRubrik = 30
                    #print(line)
                    containsNeuesAusKoeln[str(file_name)] +=1
                    testcounter += 1
                else:
                    continue
                
counter_test = 0       

with open("locales.csv", "w") as file:
    writer = csv.writer(file)
    for ausgabe in containsLocales:

        writer.writerow([ausgabe, containsLocales[ausgabe], containsNeuesAusKoeln[ausgabe]])
print(testcounter)
with open("rubrikcontent.txt", "w") as file:
    textToWrite = ""
    for k, v in corpus.items():
        textToWrite += k
        textToWrite += ":\n \n"

        for key, story in v.items():
            textToWrite += story
            textToWrite += "\n \n"
            counter_test +=1
            
            
    file.write(textToWrite)

print( counter_test)