from flair.data import Sentence
from flair.models import SequenceTagger
sentence = Sentence(" Hermann Freckmnar 0 M. Gereonswall 5.“, Gertrud, Asthoper, 67 J. Am Bollwerk 9. Franz Kohl, Kaufmannslehrling, 16 J.„Tauheng., 7. ")
tagger: SequenceTagger = SequenceTagger.load("dbmdz/flair-historic-ner-onb")
tagger.predict(sentence)

print(sentence.to_tagged_string())