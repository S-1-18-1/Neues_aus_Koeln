from flair.data import Sentence
from flair.models import SequenceTagger
sentence = Sentence(" Einem Privatbriefe aus dem Trappistenkloster Oelenberg(Elsaß) entnehmen wir folgende interessante Mittheilung. Dem Trappistenkloster Mariawald in der Eifel ist gestattet worden, sich wieder zu bevölkern. Da Mariawald bekanntlich eine Filiale des Trappistenklosters Oelenberg ist, so hat dieses am letztverflossenen Montag eine kleine Colonie, bestehend aus fieben Patres und zwei Brüdern, dorthin abgesandt. Der Abzug war ein recht feierlicher. Nach beendigtem nächtlichem Gottesdienste warfen die Patres sich vor dem Altare auf den Boden und empfingen den Reisesegen. Nachdem die h. Messen gelesen waren, kam die ganze Kloster=Gemeinde in der Kirche zusammen. Die Reisenden knieeten auf der Stufe des Presbyteriums nieder und der P. Prior von Oelenberg betete mit lauter Stimme das Itinerarium, auf welches der Chor antwortete. Als das Gebet vollendet war, gab der Abt, bekleidet mit der Stola und dem Stab in der Linken, vom Hochaltar aus den feierlichen, dreifachen Segen, worauf der Zug unter Glockengeläute ich in Bewegung setzte. Zuerst ein Priester mit dem Kreuze, dann der P. Sacristan mit dem Weihkessel, hinter diesem in zwei Reihen die ChorPatres, welche mit kräftigen Stimmen den 148. Pfalm„Laudate Dominum de coelse“ recitirten. Dann folgte die junge Gemeinde von Mariawald, den Prior Franciscus an der Spitze. Ihnen schloß sich der Abt an und zuletzt kamen in langen Reihen die Laienbrüder. So bewegte die Procession sich aus der Kirche über den Klosterhof, an der mächtigen Linde vorbei bis zum Thore, wo der Wagen zur Abfahrt schon bereit stand. Nun begann der Abschied. Die Reisenden knieeten vor den Abt hin, küßten Ring und Hand und erhielten von ihm den Friedenskuß; dann verabschiedeten sie sich von ihren Mitbrüdern, mit denen sie durch viele Jahre das Lob Gottes gesungen und die Strengheiten des Ordenslebens getragen. Der Abschied, der, ohne daß ein Wort gesprochen wurde, still vor sich ging, war ungemein rührend. Als der Augenblick des Abreisens gekommen, knieeten Alle auf den Boden der Abt besprengte die Gemeinde mit Weihwasser, gab nochmals seinen Segen, und mit betrübtem Herzen sahen wir unsere Mitbrüder nach der Station Lutterbach fahren. Zum Prior der neuen Gemeinde in Mariawald ist P. Franciscus ernannt. Er stammt aus Gelsenkirchen in Westfalen, aus acht Jahre war er Mitglied des Oelenbergs und hat sich die Hernen Aller erworden. Die Regel des h. Benedictus, welch= die Troppisten buchstäblich befolgen, hat P. Franciscus ganz in sich aufgenommen *„#eer genug, die h. Regel in allen ihren The durchzuführen. Wir aber wünschen der jungen Gemeinde deihen zur Ehre Gottes und zum Wohle der ganzen Meuschheit.")
tagger: SequenceTagger = SequenceTagger.load("dbmdz/flair-historic-ner-onb")
tagger.predict(sentence)

print(sentence.to_tagged_string())