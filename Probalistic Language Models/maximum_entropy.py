from nltk.classify import MaxentClassifier
#MaxentClassifier, Maksimum Entropi Modeli tabanlı bir doğal dil işleme (NLP) sınıflandırıcısıdır.
#Bu model, özelliklerden en olası sınıfları tahmin etmek için kullanılır.

#eğitim veri seti 
train_data=[
    ({"love":True ,"amazing":True},"positive"),
    ({"hate":True ,"terrible":True},"negative"),
    ({"happy":True ,"joy":True},"positive"),
    ({"sad":True ,"depressed":True},"negative")
]

#Max ent classifier training
classifier=MaxentClassifier.train(train_data,max_iter=10)

#test
test_sentence="I love this movie"
features= {word:(word in test_sentence.lower().split()) for word in ["love","amazing","hate","terrible","happy","joy","sad","depressed"]}

label=classifier.classify(features)
print(label)















