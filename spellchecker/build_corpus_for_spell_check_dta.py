import os

path="resources/dta_komplett_1800-1899"
output = "corpus_for_spellcheck_dta.txt"
#https://deutschestextarchiv.de/download#text

for root, dir, files in os.walk(path):
    for file_name in files:
        with open("%s/%s" %(root,file_name) , "r") as f:
            content = f.read()
        with open(output, "a") as f:
            f.write(content)

