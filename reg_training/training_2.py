import string
import re
string.punctuation
import nltk
stopwords = nltk.corpus.stopwords.words('english')
def clean_text(text):
    text = "".join([word.lower() for word in text if word not in string.punctuation])
    tokens = re.split('\W+', text)
    text = [word for word in tokens if word not in stopwords]
    return text


data['body_text_nostop'] = data['body_text'].apply(lambda x: clean_text(x.lower()))