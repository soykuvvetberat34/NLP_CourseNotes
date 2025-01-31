#bag of words metin temsili (text represention) yöntemidir.Temizlenmiş verideki kelimelerle bir veri seti oluşturur ve cümleleri veri seti üzerinden içerisinde bulunan kelime sayıları ile ifade eder
import pandas as pd# dataframeleri oluştırmak ve veri okumak için
from sklearn.feature_extraction.text import CountVectorizer# metin temsili için metinleri sayısal olarak ifade etmek için
import re#veri temizleme için
from collections import Counter
from nltk.corpus import stopwords# type: ignore #stopwordsları belirleyip metinden kaldırmak için 
import nltk# type: ignore #natural language toolkit
import numpy as np
nltk.download("stopwords")
nltk.download("punkt")
eng_sw = set(stopwords.words("english"))

df = pd.read_csv("C:\\Users\\berat\\pythonCourses\\python\\Turkcell NLP\\notes\\Metin Temsili\\IMDB Dataset.csv")
df2 = df.head(100)
texts = df2["review"]
labels = df2["sentiment"]

def text_clean(text):
    # Küçük harfe çevirme
    text = text.lower()

    # Noktalama kaldırma
    text = re.sub(r"[^a-zA-Z0-9]", " ", text)
    text = " ".join(text.split())#split kelimelerle bir liste oluşturur join ise bu listedeki elemanları boşluk ile birleştirip cümle haline getirir

    # Stopwords kaldırma ve5 kısa kelimeleri filtreleme
    cleaned_text = [w for w in text.split() if w.lower() not in eng_sw and len(w) > 2]
    #w text içindeki kelimeleri listelenmiş formatta bulur ve bu elemanları tek tek gezer eğer kelimenin küçük hali stopwrod değilse ve 2 den büyükse cleaned text listesinin içine atar
    cleaned_text = " ".join(cleaned_text)
    #cleaned text içine atılmış kelimeleri boşluk ile birleştirip string yaptık
    return cleaned_text# stringi döndürdük


cleaned_texts = [text_clean(text) for text in texts]#cleaned text listesine dataframeden aldıgımız textleri tek tek text_clean fonk içine atıp işlemleri gerçekleştirip atıyoruz
################################################################################

# Vektör temsili
vectorizer = CountVectorizer()
countered = vectorizer.fit_transform(cleaned_texts)
feature_names = vectorizer.get_feature_names_out()
vector=countered.toarray()
# Kelime frekanslarını hesapla
word_frequencies = vector.sum(axis=0)  # Her kelimenin tüm metinlerdeki toplam frekansı
df3=pd.DataFrame(vector,columns=feature_names)



feature_sums=[]
feature_names_=df3.columns
for w in feature_names_:
    feature_sums.append(df3[f"{w}"].sum(axis=0))

arr_sums=np.array(feature_sums)

df4=pd.DataFrame({"feature":feature_names,"sums":arr_sums})
df4=df4.sort_values(by="sums",ascending=False)
most_common_5=df4.head(5)
   























