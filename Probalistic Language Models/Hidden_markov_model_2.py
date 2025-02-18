import nltk
from nltk.tag import hmm #hidden markov model
from nltk.corpus import conll2000 #Önceden etiketlenmiş POS verilerini içeren bir veri kümesidir.

#veri paketini indir
nltk.download("conll2000")

# CoNLL2000 veri setinin etiketlenmiş (tagged) cümlelerini yükleyelim
train_data=conll2000.tagged_sents("train.txt") 
test_data=conll2000.tagged_sents("test.txt")
#sents(): Sadece kelimeleri getirir (etiketsiz).
#tagged_sents(): Kelimeleri POS etiketleriyle birlikte getirir.


#hmm 
hmm_trainer=hmm.HiddenMarkovModelTrainer()
hmm_tagger=hmm_trainer.train(train_data)

#test
test_sent="I like going to park".split()
tags=hmm_tagger.tag(test_sent)
print(tags)

