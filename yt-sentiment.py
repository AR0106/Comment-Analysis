import time
import nltk
import requests
from bs4 import BeautifulSoup
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from rake_nltk import Rake
from selenium import webdriver

# Input
print('Please Enter The URL of the Video You Would Like to Analyze:')
url = input()


driver = webdriver.Chrome()

driver.get(url)  # example video

time.sleep(2)  # if you have slow internet , increase the value of sleep


driver.execute_script('window.scrollTo(1, 500);')
# Here is a trick , Youtube only load comments when you scroll just down of video , if you scroll bottom or elsewhere, comments will not load , so first scroll to that down part and wait for loading comments after that scroll to bottom or whenever you want
# now wait let load the comments
time.sleep(5)

driver.execute_script('window.scrollTo(1, 3000);')


comment_div = driver.find_element_by_xpath('//*[@id="contents"]')
comments = comment_div.find_elements_by_xpath('//*[@id="content-text"]')
for comment in comments:
    print(comment.text)

    # Sentiment Analysis
    try:
        sentimentAnalyzer = SentimentIntensityAnalyzer()
    except LookupError:
        nltk.download('vader_lexicon')

    sentimentAnalyzer = SentimentIntensityAnalyzer()

    scores = sentimentAnalyzer.polarity_scores(comment.text)

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
        rake.extract_keywords_from_text(comment.text)
    except LookupError:
        nltk.download('punkt')

    rake.extract_keywords_from_text(comment.text)

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
    print('------------------------------------------------')
