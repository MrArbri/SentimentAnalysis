#if you haven't installed these packages then you need to install them
#pip install nltk
#pip install pandas
#pip install matplotlib

#import packages
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
import pandas as pd
import matplotlib.pyplot as plt

# Read the text file
file_path = r"3.first-day.txt"
with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Create a DataFrame
df = pd.DataFrame(lines, columns=['text'])
df['text'] = df['text'].str.strip()  # Remove any leading/trailing whitespace
df = df[df['text'] != '']  # Remove empty lines

# Calculate sentiment
analyzer = SIA()
df['compound'] = df['text'].apply(lambda x: analyzer.polarity_scores(x)['compound'])
df['negative'] = df['text'].apply(lambda x: analyzer.polarity_scores(x)['neg'])
df['neutral'] = df['text'].apply(lambda x: analyzer.polarity_scores(x)['neu'])
df['positive'] = df['text'].apply(lambda x: analyzer.polarity_scores(x)['pos'])

# Create sentiment category
df['sentiment'] = 'neutral'
df.loc[df['compound'] > 0.05, 'sentiment'] = 'positive'
df.loc[df['compound'] < -0.05, 'sentiment'] = 'negative'

# On-screen summary
print(df['sentiment'].value_counts())

# Save to CSV file
df.to_csv(r"sentiment-first-day.csv", index=False)

# Plot the results
sentiment_counts = df['sentiment'].value_counts()
ax = sentiment_counts.plot(kind='bar', color=['green', 'red', 'blue'])

# Add text labels
for i in range(len(sentiment_counts)):
    ax.text(i, sentiment_counts[i] + 1, str(sentiment_counts[i]), ha='center')

plt.title('Sentiment Analysis')
plt.xlabel('Sentiment')
plt.ylabel('Number of Texts')
plt.xticks(rotation=0)
plt.show()
