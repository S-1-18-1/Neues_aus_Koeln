import os
from spellchecker import SpellChecker

def build_spelling_correction(path, output):
    """build a SpellChecker object from a corpus

    :param path: directory with textfiles, corpus on which the spellchecker should be build
    :type path: str
    :param output: output path to a json file
    :type output: str
    """
    # initialize an empty SpellChecker object
    spell = SpellChecker(language=None, case_sensitive=True)

    # add the words of each text file to the word frequency list of the SpellChecker object
    for root, dir, files in os.walk(path):
        for file_name in files:
            print(file_name)
            spell.word_frequency.load_text_file("%s/%s" %(root, file_name))
    spell.export(output, 'utf-8', False)

    print("Done!")

if __name__ == '__main__':
    """
        the data is from "https://deutschestextarchiv.de/download" "DTA-Kernkorpus und Ergänzungstexte Zeitraum 1800–1899" -> "https://media.dwds.de/dta/download/dta_komplett_1800-1899_2020-09-23_text.zip"
    """
    build_spelling_correction("resources/dta_komplett_1800-1899", "resources/dictionary.json")
