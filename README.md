# CSE6242
Default site: <https://shiyao-monster.github.io/CSE6242/index.html>

README.txt

DESCRIPTION
-----------
This package implements two core sentiment-analysis tools and accompanying Jupyter notebooks for end-to-end movie emotion analysis:

1. Subtitle-Based Sentiment Analysis (subtitle_analysis.py + notebooks)
   • Reads time-aligned subtitle CSVs
   • Scores each line with seven Hugging Face transformer models
   • Averages and LOWESS-smooths the ensemble trajectory
   • Detects emotional peaks/valleys
   • Saves a PNG of the sentiment arc

2. Review-Based Sentiment Analysis (review_analysis.py + notebooks)
   • Loads time-aligned subtitle CSVs
   • Segments reviews into sentences and scores with three transformer models
   • Aggregates scores into per-review and per-film distributions
   • Generates csv files including average sentiment classification of all reviews and subtitles

3. Evaluation Notebook (Movie_Script_Sentiments_Evaluation.ipynb)
   • Computes MAE vs. ground-truth on EmoStim

INSTALLATION
------------
1. Clone this repo:
   git clone https://github.com/your-org/movie-emotion-analysis.git
   cd movie-emotion-analysis

2. (Optional) Create a Python virtual environment:
   python3 -m venv venv
   source venv/bin/activate

3. Install dependencies:
   pip install --upgrade pip
   pip install -r requirements.txt

   requirements.txt contains:
     pandas
     numpy
     scipy
     statsmodels
     matplotlib
     transformers
     tqdm

EXECUTION
-----
From the project root:

1. Subtitle Analysis
   python subtitle_analysis.py \
     --input data/200_Meters_subtitle.csv \
     --output figures/200_Meters_subtitle_sentiment.png
   — Saves 200_Meters_subtitle_sentiment.png in figures/.

2. Review Analysis
   python review_analysis.py \
     --input data/all_movies_reviews_emotion_scores.csv \
     --output figures/review_sentiment_distribution.png
   — Saves distribution plots in figures/.

3. Interactive Notebooks
   Launch and step through:
     Movie_Script_Sentiments_Line.ipynb  
     Movie_Review_Scirpts_Classification_Sentiments.ipynb  
     Movie_Script_Sentiments_Evaluation.ipynb  
   jupyter notebook
