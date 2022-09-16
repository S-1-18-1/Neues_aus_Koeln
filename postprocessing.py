import re
from cleantext import clean
from spellchecker import SpellChecker
from lxml import etree as ET
import os

path="corpus"
parser = ET.XMLParser(remove_blank_text=True)


spell = SpellChecker(language="DE", distance=1,case_sensitive=True)
spell.word_frequency.load_dictionary("dictionary.json")

spell_short = SpellChecker(language="DE",case_sensitive=True)
spell_short.word_frequency.load_dictionary("dictionary.json")


def remove_whitespace(sequence):
    sequence = sequence.group()
    return sequence.replace(" ", "")


def check_spelling(word):
    word = word.group()
    if word in spell:
        return word
    else:
        if len(word)<=5:
            corr=spell_short.correction(word)
        else:
            corr = spell.correction(word)
        if corr == None:
            corr = word
        if word[0].isupper():
            corr = corr.title()
        else:
            corr = corr.casefold()
        return corr
   
def clean_up(story):
    story = clean(story,fix_unicode=True,  normalize_whitespace=True,lower=False, lang="de")
    story = re.sub(r'(?<=<space>).*?(?=<space>)', remove_whitespace, story)
    story = story.replace("<space>", " ")
    story = story.replace("=", "-")
    story = re.sub(r'[a-zA-Z]+', check_spelling, story)
    return story


for root, dir, files in os.walk(path):
    for file_name in files:
        print("Cleaning up '%s'..." %file_name)
        full_path = os.path.join(path, file_name)
        tree = ET.parse(full_path, parser)
        for story in tree.findall(".//text"):
            story.text=clean_up(story.text)
        tree.write("%s" % full_path, pretty_print=True, encoding='utf-8')        

print("Done!")