from german_transliterate.core import GermanTransliterate

text= "Kr. süße Rahmtafelbutt., Postc.ca.100, S. k.90, fr. Kalbsk., 10674.# vers.postfr. per Nachn. Weberstadt, Ortelsburg.(Ein neues Pult, wenig gebraucht, bill. C zu verkaufen. Breitestr. 130, 2. Et.dreßbuch 189* zu verkaufen."
print('ORIGINAL:', text, '\n')

ops = {'acronym_phoneme', 'accent_peculiarity', 'amount_money', 'date', 'timestamp',
        'weekday', 'month', 'time_of_day', 'ordinal', 'special', 'math_symbol', 'spoken_symbol'}

# # use these setting for PHONEMIC ENCODINGS as input (e.g. with TTS)
# print('TRANSLITERATION with phonemic encodings:',
#       GermanTransliterate(replace={';': ',', ':': ' '}, sep_abbreviation=' -- ').transliterate(text), '\n')

# use none or your own for other purposes than phonemic encoding and do not use 'spoken_symbol' or 'acronym_phoneme'
print('TRANSLITERATION (default):',
      GermanTransliterate(transliterate_ops=list(ops-{'spoken_symbol', 'acronym_phoneme'})).transliterate(text), '\n')