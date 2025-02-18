import nltk
from nltk.tag import hmm #hidden markov model tabanlı 
#kelime etiketleme için kullanılan bir modül

#örnek veri seti

train_data=[
    [("I","PRP"),("am","VBP"),("a","DT"),("student","NN")],#prp zamir ,NN isim ,VBP fiil , DT tamlayıcı (a,an) 
    [("You","PRP"),("are","VBP"),("a","DT"),("teacher","NN")]
]

hmm_trainer=hmm.HiddenMarkovModelTrainer()#modeli eğitmek için eğitim nesnesi
hmm_tagger=hmm_trainer.train(train_data)#eğitim verisini kullanarak modeli eğit

#test
test_sent="I am a teacher".split()
tags=hmm_tagger.tag(test_sent)

print(tags)



















