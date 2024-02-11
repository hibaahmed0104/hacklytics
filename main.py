from textblob import TextBlob
from newspaper import Article
import csv

# read from url.csv to get the companies
with open('url.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=' ')
    next(csv_reader)

    # write fieldnames header to sentimentscores.csv
    with open('sentimentscores.csv', 'a', newline='') as new_file:
            fieldnames = ['company', 'score1', 'score2', 'score3', 'score4', 'score5']
            csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=' ')
            csv_writer.writeheader()
            new_file.close()

    for line in csv_reader:
        company_name = line[0]
        sentiment_list = [None] * 5
        for i in range (1, len(line)):
            url = line[i]
            url = url.strip()
            article = Article(url)

            # Try-Except-Continue will skip to the next article in the For loop if there is an exception because some websites are blocked for security reasons
            try:
                article.download()
                article.parse()
                article.nlp()
            except:
                continue
            
            # forms a summary of the full article
            text = article.summary

            blob = TextBlob(text)
            # calculates sentiment score from -1 to 1
            sentiment = blob.sentiment.polarity
            sentiment_list[i - 1] = sentiment

        # write sentiment scores to sentimentscores.csv
        with open('sentimentscores.csv', 'a', newline='') as new_file:
            csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=' ')
            csv_writer.writerow({'company': company_name, 'score1': sentiment_list[0], 'score2': sentiment_list[1], 'score3': sentiment_list[2], 'score4': sentiment_list[3], 'score5': sentiment_list[4]})
            new_file.close()