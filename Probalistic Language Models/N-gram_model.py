from collections import Counter
import nltk
from nltk.util import ngrams
from nltk.tokenize import word_tokenize

#örnek veri seti
corpus=[
    "I love you",
    "I love apple",
    "I love programming",
    "You love me",
    "She loves apple",
    "They love you",
    "I love you and you love me"
]


tokens= [word_tokenize(sentence.lower()) for sentence in corpus]

bigrams=[]
for token_list in tokens:
    bigrams.extend(list(ngrams(token_list,2)))#extend iter olarak ekler 

bigrams_freq=Counter(bigrams)#bigram ların sıklığını döndürür

trigrams=[]
for token_list in tokens:
    trigrams.extend(list(ngrams(token_list,3)))

trigrams_freq=Counter(trigrams)

#UYGULAMA
bigram=("i","love")#devamını soracağımız metnin tokenları
prob_you=trigrams_freq[("i","love","you")]/bigrams_freq[bigram]
prob_apple=trigrams_freq[("i","love","apple")]/bigrams_freq[bigram]

print("you kelimesinin olma olasılığı:",prob_you)
print("apple kelimesinin olma olasılığı:",prob_apple)








