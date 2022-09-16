from spellchecker import SpellChecker
from lxml import etree as ET
import re


spell = SpellChecker(language="DE", distance=1,case_sensitive=True)
spell_short = SpellChecker(language="DE",case_sensitive=True)
spell_DE = SpellChecker(language="DE", distance=1, case_sensitive=True)
test=1


from random import randint
from lxml import etree as ET
import os

path="corpus"
output = "randomstories_corrected_2.txt"
stories = []


#spellDE = SpellChecker(language=DE)

spell.word_frequency.load_dictionary("dictionary.json")
spell_short.word_frequency.load_dictionary("dictionary.json")

def check_spell(word):
    global test 

    word = word.group()
    if word in spell:
        test +=1
        #print(word+ " returned")
        return word
    else:
        if len(word)<=5:
            corr=spell_short.correction(word)
            if word != corr and corr != None:
                print("histsh: %s-%s"%(word, corr))

        else:
            corr = spell.correction(word)
            
            if word != corr and corr != None:
                
                print("hist: %s-%s"%(word, corr))
                #print("mod: %s-%s"%(word, spell_DE.correction(word)))


        # if corr == None:
        #     corr = spell_DE.correction(word)
        #     if word != corr and corr != None:
        #         print("mod: %s-%s"%(word, corr))

        if corr == None:
            corr = word       
            #print("same: %s"%(corr))
        if word[0].isupper():
            
            corr = corr.title()
            print(corr)

        else:
            corr = corr.casefold()
            print(corr)

        
        return corr
    
# def check_spellDE(word):
#     word = word.group()
#     if word in spellDE:
#         return word
#     else:
#         corr = spellDE.correction(word)
#         if corr != None:
#             print("mod: %s-%s"%(word, corr))

#             return corr
#         else: 
#             return word


#https://lzone.de/examples/Python%20re.sub
# sentence = "In vorverflossener Ncht überfiel ein Bäcker uf dem Holzmrkt einen Schmied, wrf ihn uf die Erde und nhm ihm die Uhr und ds Portemonnie b. Mit Hülfe eines hinzukommenden Metzgers wurde der Dieb festgehlten und einem Wächter übergeben. "

# for word in sentence.split(" "):
#     print(word)
#     print(check_spell(word))

# tree = ET.parse("example.xml")
# for story in tree.findall(".//text"):
#     # corrected_story = ""

#     corrected_story= re.sub(r'[a-zA-Z]+', check_spell, story.text)

parser = ET.XMLParser(remove_blank_text=True)

for root, dir, files in os.walk(path):
    for file_name in files:
        full_path = os.path.join(path, file_name)
        tree = ET.parse(full_path, parser)
        for story in tree.findall(".//text"):
            stories.append([story.text, file_name])


with open(output, "w") as f:
    i=0
    while i < 100:
        get_story = randint(0,len(stories))
        print("Processing story %s" %str(get_story))
        f.write(str(stories[get_story])+"\n")
        f.write(re.sub(r'[a-zA-Z]+', check_spell, str(stories[get_story][0]))+"\n")
        i+=1
    
print(test)
