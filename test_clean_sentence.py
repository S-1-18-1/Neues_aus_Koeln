# import spacy
# from spacy.lang.de import German

# from spacy.lang.en import English

# nlp = German()
# nlp.add_pipe("sentencizer")
# doc = nlp("J. Zorn, Filzengraben 30. Restauration Althausen, Mühlenbach.  Hamacher, Schildergasse 41.")
# print( len(list(doc.sents)))

# from spellchecker import SpellChecker
# deutsch = SpellChecker(language='de')


# # find those words that may be misspelled
# misspelled = deutsch.unknown(['hallo', 'lustig', 'doofe', 'cool'])
# for word in misspelled:
#     # Get the one `most likely` answer
#     print(deutsch.correction(word))

#     # Get a list of `likely` options
#     print(deutsch.candidates(word))

import language_tool_python
tool = language_tool_python.LanguageTool('de-DE')


 
text = "Am Krolinger=Ring geht eine Häusergruppe der HH. Leybold &amp;mp; Comp. hierselbst der Vollendung entgegen, welche zeigt, dß uch n unserer breiten Ringstrße bei geschickter Anordnung sich Wohnhäuser von geringerer Frontlänge, für eine Fmilie bestimmt, noch gnz gut zur Geltung bringen lssen. Dieselben sind in einfcher, ber gediegener Weise uch Plänen des hiesigen Regierungs=Bumeisters Krings usgeführt. Die Fronten bestehen us echtem Mteril in einfcher, ber geschmckvoller Formengebung. Die Grundriß=Anordnung zeigt einen wesentlichen Vortheil vor der fst überll hierorts üblichen Ausbildung des Dreifensterhuses, indem bei möglichst geringem Rumverlust Anbu und Hupthus uf gleicher Höhe liegen. Dieser Versuch, unserm hergebrchten Fmilien= huse, im Gegenstz zu den sich immer breiter mchenden Miethscsernen, wieder zu seinem Rechte zu verhelfen, verdient lle Anerkennung; die Mnchfltigkeit und Schönheit unserer neuen Strßenzüge knn durch eine größere Anzhl derrtiger Häuser nur gewinnen. "

 
 
# get the matches
matches = tool.check(text)
 
#print(matches)


print(tool.correct(text))

# import nltk 
# from nltk import grammartestsuites

