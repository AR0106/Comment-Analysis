import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from rake_nltk import Rake

# Input
print('Please Enter The Sentence You Would Like to Analyze:')
sentence = input()

# Sentiment Analysis
try:
    sentimentAnalyzer = SentimentIntensityAnalyzer()
except LookupError:
    nltk.download('vader_lexicon')

sentimentAnalyzer = SentimentIntensityAnalyzer()

scores = sentimentAnalyzer.polarity_scores(sentence)

if scores['neg'] > scores['pos'] and scores['neg'] > scores['neu']:
    print('Negative')
elif scores['neg'] < scores['pos'] and scores['pos'] > scores['neu']:
    print('Positive')
else:
    print('Neutral')

# Keyword Extraction
try:
    rake = Rake()
except LookupError:
    nltk.download('stopwords')
    nltk.download('punkt')

rake = Rake()

try:
    rake.extract_keywords_from_text(sentence)
except LookupError:
    nltk.download('punkt')

rake.extract_keywords_from_text(sentence)

keywords = rake.get_ranked_phrases()

print('Keywords:')
print(keywords)

# Safety Features
flags = ['check', 'channel', 'subscribe', 'website', 'give', 'me']

flagCount = 0

for keyword in keywords:
    if keyword in flags:
        flagCount += 1

if flagCount >= 2:
    print('! Possible Spam !')
