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
file_path = r"1.0-pre-boarding.txt"
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
df.to_csv(r"1.1-sentiment-pre-boarding.csv", index=False)

# Count sentiments
sentiment_counts = df['sentiment'].value_counts()

# Ensure all categories are present
categories = ['positive', 'neutral', 'negative']
counts = [sentiment_counts.get(category, 0) for category in categories]

# Plot the results
fig, ax = plt.subplots()

# Add bars
bars = ax.bar(categories, counts, color=['green', 'blue', 'red'])

# Add text labels above the bars
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2.0, height, str(height), ha='center', va='bottom', fontweight='bold')

# Set fixed y-axis limit to 100
ax.set_ylim(0, 100)

# Add title and labels
plt.title('Pre-boarding', fontweight='bold')
plt.xlabel('Emotions', fontweight='bold')
plt.ylabel('Number of Words', fontweight='bold')
plt.xticks(rotation=0)

plt.show()
