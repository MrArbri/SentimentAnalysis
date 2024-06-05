import string
from collections import Counter
import matplotlib.pyplot as plt
import nltk

# Download NLTK resources if not already downloaded
nltk.download('punkt')

# Read the text file and convert it to lowercase
text = open('read.txt', encoding='utf-8').read()
lower_case = text.lower()

# Tokenize the text into sentences
sentences = nltk.sent_tokenize(lower_case)

# Define your list of stop words
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you",  
              "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", 
              "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", 
              "their", "theirs", "themselves", "what", "which", "who", "whom", "this", 
              "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", 
              "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", 
              "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", 
              "of", "at", "by", "for", "with", "about", "against", "between", "into", 
              "through", "during", "before", "after", "above", "below", "to", "from", 
              "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", 
              "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", 
              "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", 
              "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", 
              "will", "just", "don", "should", "now"]

# Define a list of emotional words
emotional_words = ["happy", "sad", "angry", "joyful", "excited", "fearful", "surprised", "relaxed", "nervous", "grateful"]

# Define a list to store emotional words surrounding "trust"
emotion_words = []

# Iterate through the sentences to find emotional words surrounding "trust"
for sentence in sentences:
    if 'trust' in sentence:
        # Tokenize the sentence into words
        words = nltk.word_tokenize(sentence)

        # Check if the words are emotional and not in the stop words list
        for word in words:
            if word not in stop_words and word in emotional_words:
                emotion_words.append(word)

# Display the list of emotional words
print(emotion_words)

# Count the occurrences of each emotional word
emotion_word_counts = Counter(emotion_words)

# Plot the bar chart
plt.bar(emotion_word_counts.keys(), emotion_word_counts.values())
plt.xlabel('Emotional Words')
plt.ylabel('Frequency')
plt.title('Emotional Words Surrounding "Trust"')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
