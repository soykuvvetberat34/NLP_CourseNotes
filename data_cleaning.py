from bs4 import BeautifulSoup
from textblob import TextBlob
import string
import re

#tüm boşlukları kaldırma / remove to spaces
text="Hello ,     World!    2025"
cleaned_text=" ".join(text.split())
print(cleaned_text)

#tüm harfleri küçültme / minimize the letters
cleaned_text2=cleaned_text.lower()
print(cleaned_text2)

#noktalama işaretlerini kaldırma /remove the punctuation
cleaned_text3=text.translate(str.maketrans("","",string.punctuation))
print(cleaned_text3)
cleaned_text4=" ".join(cleaned_text3.split())
print(cleaned_text4)

#özel karakterleri kaldırma - regular expression / remove the special characters
text2="Hello && World$ 2025/%"
cleaned_text5=re.sub(r"[^A-Za-z0-9]"," ",text2)
cleaned_text6=" ".join(cleaned_text5.split())
print(cleaned_text6)


#yazım yanlışlarını düzeltme textblob / fix the sentences
text3="Helıo Wirlt! 2025"
cleaned_text7=str(TextBlob(text3).correct())
print(cleaned_text7)

#url ve html etiketlerini kaldırma / remove the url and html tags
text4="<div>Hello<div> World! 2025"
cleaned_text8=BeautifulSoup(text4,"html.parser").get_text()
print(cleaned_text8)
