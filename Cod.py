text = open ("C:/Users/eleio/Desktop/Corpus.txt")
data = text.read()
print(data)

from nltk.stem import SnowballStemmer
import nltk
from nltk.corpus import stopwords
import re
def tokenize(text):
        tokens = nltk.WhitespaceTokenizer().tokenize(text)
        tokens = list(set(re.sub("[^a-zA-Z\']", "", token) for token in tokens))
        tokens = [word for word in tokens if word not in stopwords.words('romanian')]
        tokens = list(set(re.sub("[^a-zA-Z]", "", token) for token in tokens))
        stems = []
        stemmer = SnowballStemmer("romanian")
        for token in tokens:
            token = stemmer.stem(token)
            if token != "":
                stems.append(token)
        return stems 

token=tokenize(data)
print token


data_tag=nltk.pos_tag (token)

import nltk
def findtags(tag_prefix, tagged_text):
    cfd = nltk.ConditionalFreqDist((tag, word) for (word, tag) in tagged_text
                                  if tag.startswith(tag_prefix))
    return dict((tag, cfd[tag].most_common(1074)) for tag in cfd.conditions())

tagdict = findtags('NN', data_tag)
for tag in sorted(tagdict): print(tag, tagdict[tag])

tag_fd = nltk.FreqDist(tag for (word, tag) in data_tag)
common=tag_fd.most_common()

#######################################

tok1=teprolinresult["tokenized"]
tok2=teprolinresult000["tokenized"]
tok3=teprolinresult001["tokenized"]
tok4=teprolinresult002["tokenized"]
tok5=teprolinresult003["tokenized"]
tok6=teprolinresult004["tokenized"]
tok7=teprolinresult005["tokenized"]
tok8=teprolinresult006["tokenized"]
tok9=teprolinresult007["tokenized"]



token=tok1+tok2+tok3+tok4+tok5+tok6+tok7+tok8+tok9
print(token)

