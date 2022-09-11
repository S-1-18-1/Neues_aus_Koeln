from cleantext import clean
# https://github.com/jfilter/clean-text
print(clean("  a c n e&lt;space&gt; d e s&lt;space&gt; G e s i c h t s&lt;space&gt; k u n n&lt;space&gt; m a n&lt;space&gt; n i e&lt;space&gt; z u v i e l&lt;space&gt; t u n,&lt;space&gt; i s t&lt;space&gt; e s&lt;space&gt; d o c h&lt;space&gt; derjenige Teil unseres Körpers, mit dem wir steis sichtbur mit der Aufenwelt in Beziehung stehen. Das Anllitz interessiert uns steis am meisten an unsenein Nebemnenehen, und ein schönes Gesicht ist immer ein guter Empfehlungsbrief. Zur Schönheit des Gesichts gehört auch eine gesumie Gesichtsfarbe. Jede schlechte Furbe ist entweder eine Krankheit der Haut oder der Widerschein einer krankhaften Störung ninerer Organe und allgemeiner Funktionen. Alle Verunreinigungen der Haut sind daher als priniäre oder sekundäre Hautleiden zu betrachten, weiche, wenn sie nicht bloß vorübergehend durch Erkältung, Magenverderbnis und dergleiciren bedingt sind und damit auch wieder verschwrinen, als Leiden zu behundeln und nicht mit Teint- oder Schönheiismitteln. Freilich ist die Empfindlichkeit der Haut nicht bei allen Menschen gleich, die einen brauchen gar keine Hilfsmittel, um eine schöne Gesichtsfarbe zu behalten, die andern dagegen sehr. Um bei den letzten die Haut in einem nornialen Zustand zu erhalten, die Bildung saurer oller ranziger Zersetzungsprodukte zu vermeiden, ist ihnen zu einpfehlen, jeden Morgen das Gesicht mit einer Lösung von Borax zu woschen. Eine Lösung von 30 Gramm Borax auf eine Weinflesche voll Wasser ist die geeignetste, die man in der teuren Kriegszeit auch als Mund- und Zahnwasser bemtzen kann. Der Borax ist des mildeste und unechädlichste Alkali, welches wir haben. Auch gegen Mitesser, Hitzpickel und Pusteln ist die Boraxlösung mit Erfolg zu verwenden. Jedenfalls ist das gewaltsame Ausdrücken mittels Uhrschlüssel oder Daumennägel zu vermeiden. Wenn uber unbedingt ausgedrückt werden soll, so gewilligt werden.. Die Renten waren sehr niedrig, die Verwaltungskosten gering und Aufwendungen für außergewöhnliche Leistungen wurden kaum gemacht. Seit vielen Jahren hat sich das geändert, die Renten sind an Zahl und Höhe um ein Viellaches gewachsen, die außerordentlichen Leistungen usv. erfordern gewaltige Summen. Der Beharrungszustand ist aber auch jetzt noch nicht eingetreten, es werden noch Jahre vergehen, ehe es dazu kommt. Die Einnahmen müssen noch für längere Jahre die Ausgaben übersteigen, wenn das jetzige Deckungsverfahren beibehalten werden soll. Wie der Krieg mit seinen großen Aufwendungen für Kranken- und Hinterbliebenenrenten die Vermögenslage der Versicherungsanstalten gestalten wird, läßt sich noch garnicht übersehen. Die Beiträge werden sicher erhöht werden müssen, um die Sicherheit der Versicherungsanstallen zu gewährleisten. Aus dem Gesagten ergibl sich, daß der Reichtum der Versicherungsanstalten nicht vorhanden ist.",
    fix_unicode=True,               # fix various unicode errors
    to_ascii=True,                  # transliterate to closest ASCII representation
    lower=False,                     # lowercase text
    no_line_breaks=False,           # fully strip line breaks as opposed to only normalizing them
    no_urls=False,                  # replace all URLs with a special token
    no_emails=False,                # replace all email addresses with a special token
    no_phone_numbers=False,         # replace all phone numbers with a special token
    no_numbers=False,               # replace all numbers with a special token
    no_digits=False,                # replace all digits with a special token
    no_currency_symbols=False,      # replace all currency symbols with a special token
    no_punct=False,                 # remove punctuations
    # replace_with_punct="",          # instead of removing punctuations you may replace them
    # replace_with_url="<URL>",
    # replace_with_email="<EMAIL>",
    # replace_with_phone_number="<PHONE>",
    # replace_with_number="<NUMBER>",
    # replace_with_digit="0",
    # replace_with_currency_symbol="<CUR>",
    lang="de"                       # set to 'de' for German special handling
))