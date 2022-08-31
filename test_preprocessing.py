from german_transliterate.core import GermanTransliterate

text = 'Um 13:15h kaufte Hr. Meier (Mitarbeiter der Firma ABC) 1.000 Luftballons für 250€.'
print('ORIGINAL:', text, '\n')

ops = {'acronym_phoneme', 'accent_peculiarity', 'amount_money', 'date', 'timestamp',
        'weekday', 'month', 'time_of_day', 'ordinal', 'special', 'math_symbol', 'spoken_symbol'}

# use these setting for PHONEMIC ENCODINGS as input (e.g. with TTS)
print('TRANSLITERATION with phonemic encodings:',
      GermanTransliterate(replace={';': ',', ':': ' '}, sep_abbreviation=' -- ').transliterate(text), '\n')

# use none or your own for other purposes than phonemic encoding and do not use 'spoken_symbol' or 'acronym_phoneme'
print('TRANSLITERATION (default):',
      GermanTransliterate(transliterate_ops=list(ops-{'spoken_symbol', 'acronym_phoneme'})).transliterate(text), '\n')