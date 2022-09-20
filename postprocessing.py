import re
from cleantext import clean
from spellchecker import SpellChecker
from lxml import etree as ET
import os

parser = ET.XMLParser(remove_blank_text=True)


#build spellchecker with SpellChecker Library 
#spellchecker for long words
spell = SpellChecker(language="DE", distance=1,case_sensitive=True)
spell.word_frequency.load_dictionary("resources/dictionary.json")

#spellchecker for short words
spell_short = SpellChecker(language="DE",case_sensitive=True)
spell_short.word_frequency.load_dictionary("resources/dictionary.json")




def remove_whitespace(sequence):
    """removes whitespace of a sequence, used as a callback function

    :param sequence: sequence of which the whitespaces should be removed
    :type sequence: class 're.Match'
    :return: sequence without whitespace
    """

    sequence = sequence.group()
    return sequence.replace(" ", "")


def check_spelling(word):
    """
    checks spelling of a word, used as a callback function

    :param word: word that needs to be checked
    :type word: class 're.Match'
    :return: original or corrected word
    """
    
    word = word.group()
    # if the word exists in the dictionary, it is probably correct and gets returned
    if word in spell:
        return word
    else:
        # use of the spell object for shorter words
        if len(word)<=5:
            corr=spell_short.correction(word)
        # use of the spell object for longer words
        else:
            corr = spell.correction(word)
        #checks if the correction didn't return a correction
        if corr == None:
            corr = word
        # adjust the case to the original word
        if word[0].isupper():
            corr = corr.title()
        else:
            corr = corr.casefold()
        return corr
   
def clean_up(story):
    """
    cleans up a string

    :param story: the string that should be cleaned up
    :type story: str
    :return: cleaned up string
    """
    # use the cleantext library to fix unicode errors and to remove multiple whitespaces
    story = clean(story,fix_unicode=True,  normalize_whitespace=True,lower=False, lang="de")
    # remove the whitespaces between '<space>' elements and remove the tags, used to highlight parts of the text, e.g. <space> h i g h l i g h t <space>
    story = re.sub(r'(?<=<space>).*?(?=<space>)', remove_whitespace, story)
    story = story.replace("<space>", " ")
    # some dashes are written as "=", to normalize them replace them with "-"
    story = story.replace("=", "-")
    # checks spelling of each word and replaces it with the correction
    story = re.sub(r'[a-zA-Z]+', check_spelling, story)
    return story

def pp_corpus(path):
    """
    iterates through the files of an directory and applies the postprocessing steps to them

    :param path: path to the directory
    :type path: str
    """
    for root, dir, files in os.walk(path):
        i = 1
        for file_name in files:
            full_path = os.path.join(path, file_name)
            tree = ET.parse(full_path, parser)
            # applies the postprocessing steps to all stories found in the xml file
            for story in tree.findall(".//text"):
                story.text=clean_up(story.text)
            # overwrite the old xml
            tree.write("%s" % full_path, pretty_print=True, encoding='utf-8')  
            # log
            print("Cleaned up '%s' (%s/%s)" %(file_name, i, len(files)))
            i+=1      
    print("Done!")

if __name__ == '__main__':
    """ 
        The script needs a directory of xml-files according to the template file in "resources/template.xml"
        WARNING: Overwrites the original files with a corrected version
    """
    pp_corpus("test")
