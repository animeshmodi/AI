import nltk
nltk.download('vader_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()

text = "I really enjoyed this movie. Though acting was bad and the plot was engaging."

score = sia.polarity_scores(text)

print("negative = ", score["neg"])
print("neutral = ", score["neu"])
print("positive = ", score["pos"])
print("compound = ", score["compound"])