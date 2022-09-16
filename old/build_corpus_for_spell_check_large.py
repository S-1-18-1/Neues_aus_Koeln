import os

path="data"
output = "corpus_for_spellcheck_full.txt"


for root, dir, files in os.walk(path):
    for file_name in files:
        with open("%s/%s" %(root,file_name) , "r") as f:
            content = f.read()
        with open(output, "a") as f:
            f.write(content)

