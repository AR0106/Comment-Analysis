import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

try:
    sentimentAnalyzer = SentimentIntensityAnalyzer()
except LookupError:
    nltk.download('vader_lexicon')


sentimentAnalyzer = SentimentIntensityAnalyzer()

print('Please Enter The Sentence You Would Like to Analyze:')
sentence = input()


scores = sentimentAnalyzer.polarity_scores(sentence)

if scores['neg'] > scores['pos'] and scores['neg'] > scores['neu']:
    print('Negative')
elif scores['neg'] < scores['pos'] and scores['pos'] > scores['neu']:
    print('Positive')
else:
    print('Neutral')
