Sentiment Analysis Using Python


This code is designed for sentiment analysis using Python. You can analyze any text you want.
In this example, we are analyzing transcribed interviews.

Prerequisites
To use this code, you must have Python installed on your computer, along with the following libraries:

  • nltk
  • pandas
  • matplotlib

Installation instructions for these libraries can be found at the top of the code.

Instructions
Follow these steps to analyze your text and achieve the same results as in the example:


Step 1: Select the Text File

  1. Open main.py.

  2. Locate the section:

  # Read the text file
  file_path = r"3.0-first-day.txt"

  3. Replace "3.0-first-day.txt" with the name of the file you want to analyze. 
  For example, if you want to analyze "Pre-boarding", change it to "1.0-pre-boarding.txt". 
  Repeat this process for onboarding or any other file you want to analyze.


Step 2: Save Results to CSV (Optional)

  1. Locate the section:

  # Save to CSV file
  df.to_csv(r"3.1-sentiment-first-day.csv", index=False)

  2. Replace "3.1-sentiment-first-day.csv" with the desired CSV file name. 
  For example, if you are analyzing pre-boarding, it should be "1.1-sentiment-pre-boarding.csv". 
  Repeat this process for onboarding or other files.

  3. If you do not want to generate a CSV file, comment out the code by adding a # in front:

  # Save to CSV file
  # df.to_csv(r"3.1-sentiment-first-day.csv", index=False)


Step 3: Update the Graph Title

  1. Locate the section at the bottom of the code:

  # Add title and labels
  plt.title('First day at work', fontweight='bold')

  2. Replace 'First day at work' with the appropriate title for your analysis. 
  For example, if you are analyzing pre-boarding, it should be 'Pre-boarding'. 
  Repeat this process for onboarding or other files.


Running the Code

After making the necessary changes, run the code to generate the CSV file and the graphic or only the graphic if you have chosen not to generate the CSV file. Once you execute the code, the graphic will be generated automatically and displayed on the screen.
