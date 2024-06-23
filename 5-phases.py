import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
import pandas as pd
import matplotlib.pyplot as plt

# Download VADER lexicon if not already downloaded
nltk.download('vader_lexicon')

# Function to analyze sentiments of a given file
def analyze_sentiments(file_path):
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

    # Save to CSV file
    df.to_csv(r"5.1-sentiment-across-phases.csv", index=False)

    # Count sentiments
    sentiment_counts = df['sentiment'].value_counts()

    # Ensure all categories are present
    categories = ['positive', 'neutral', 'negative']
    counts = {category: sentiment_counts.get(category, 0) for category in categories}

    return counts

# File paths
file_paths = {
    'Pre-boarding': r"1.0-pre-boarding.txt",
    'First day': r"2.0-first-day.txt",
    'Onboarding': r"3.0-on-boarding.txt"
}

# Analyze each file
sentiment_data = {phase: analyze_sentiments(file_path) for phase, file_path in file_paths.items()}

# Create DataFrame for plotting
plot_data = pd.DataFrame(sentiment_data).T

# Plot the results
fig, ax = plt.subplots(figsize=(10, 6))

# Colors for each sentiment
colors = {
    'positive': 'green',
    'neutral': 'blue',
    'negative': 'red'
}

# Plot each sentiment
for sentiment in ['positive', 'neutral', 'negative']:
    ax.plot(plot_data.index, plot_data[sentiment], marker='o', label=sentiment.capitalize(), color=colors[sentiment])

    # Add text annotations for each point with a bit of space
    for phase in plot_data.index:
        if sentiment == 'positive':
            xytext_offset = (0, -15)  # Below the point
        elif sentiment == 'negative' and phase == 'First day':
            xytext_offset = (0, -13)  # Below the point for negative sentiment on the first day
        elif sentiment == 'neutral' and phase == 'Onboarding':
            xytext_offset = (0, -15)  # Below the point for neutral sentiment on the onboarding
        else:
            xytext_offset = (0, 5)  # Above the point for all other cases

        ax.annotate(
            str(plot_data.at[phase, sentiment]),
            (phase, plot_data.at[phase, sentiment]),
            textcoords="offset points",
            xytext=xytext_offset,
            ha='center',
            color=colors[sentiment],
            fontweight='bold'
        )

# Add title and labels
plt.title('Sentiment Analysis Across Phases', fontweight='bold')
plt.xlabel('Phases', fontweight='bold')
plt.ylabel('Number of Words', fontweight='bold')
plt.legend(title='Sentiment')

# Display the plot
plt.show()
