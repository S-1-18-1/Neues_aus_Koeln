import re
import os
from spellchecker import SpellChecker

#word_list_path = "resources/german.oldspell.txt"

spell = SpellChecker(language=None, case_sensitive=True)

word_list = []

# with open(word_list_path, 'r') as f:
#         for line in f:
#             word_list.append(line.strip())

# del word_list[0:21]

print("Wordlist built...")

path="resources/dta_komplett_1800-1899"
output = "corpus_for_spellcheck_dta.txt"
#https://deutschestextarchiv.de/download#text

for root, dir, files in os.walk(path):
    for file_name in files:
        print(file_name)
        spell.word_frequency.load_text_file("%s/%s" %(root, file_name))



print("Textfile loaded...")

# words_to_delete = []

# for word in spell:
#     if word not in word_list:
#         print(word)
#         words_to_delete.append(word)
# print("Words_to_delete built...")
# spell.word_frequency.remove_words(words_to_delete)

print("Words removed...")

spell.export("dictionary.json", 'utf-8', False)
