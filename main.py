from textblob import TextBlob
# from newspaper import Article
# import nltk
# nltk.download('punkt')

# url = 'https://www.npr.org/2024/02/09/1230086474/stocks-sp-record-5000-wall-street-new-high-economy'
# article = Article(url)

# article.download()
# article.parse()
# article.nlp()

# text = article.summary
# print(text)

with open('mytext.txt', 'r') as f:
    text = f.read()

blob = TextBlob(text)
sentiment = blob.sentiment.polarity # -1 to 1
print(sentiment)