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


Instructions for phases.py

This script performs sentiment analysis on text files corresponding to different phases of employee onboarding and displays the results in a graphical format.

Files

The following text files are required:

  • 1.0-pre-boarding.txt
  • 2.0-on-boarding.txt
  • 3.0-first-day.txt

These files should contain text data corresponding to each phase of the employee onboarding process. Place these files in the same directory as the script or update the file paths in the script if they are located elsewhere.

Script Usage

  1. Download the VADER Lexicon:
  The script automatically downloads the VADER lexicon, which is used for sentiment analysis. Ensure you have an active internet connection for the download.

  2. Run the Script:
  To execute the script, navigate to the directory containing phases.py and run the following command:

  python phases.py

  3. Output:

  • The script will generate a CSV file named 5.1-sentiment-across-phases.csv containing the sentiment analysis results.
  • A plot showing the sentiment trends across the phases (Pre-boarding, First day, and Onboarding) will be displayed.
  • The plot will also be saved as an image file named sentiment_analysis_plot.png.

Script Details

The script performs the following steps:

  1. Reads the text files and cleans the data.
  2. Uses the VADER sentiment analysis tool to compute sentiment scores for each line of text.
  3. Categorizes each line as positive, neutral, or negative based on the compound sentiment score.
  4. Counts the occurrences of each sentiment category.
  5. Creates a plot showing the number of positive, neutral, and negative sentiments across the different phases.
  6. Annotates the plot with the counts, adjusting the position of the annotations for better readability.
