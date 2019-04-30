from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters

punkt_param = PunktParameters()
punkt_param.abbrev_types = set(['dr', 's', 'u.s.w', 'f', 'z.b', 'd.h'])
sentence_splitter = PunktSentenceTokenizer(punkt_param)
f1 = open('kombi.txt', 'rU')
raw = f1.read()
sätze = sentence_splitter.tokenize(raw)

string = '\n'.join(sätze)
print(string)
f = open('kombi_saetze.txt', 'w')
f.write(string)
f.close()
