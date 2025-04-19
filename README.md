# CSE6242
Default site: <https://shiyao-monster.github.io/CSE6242/index.html>


DESCRIPTION
-----------
Text based emotion analysis:
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

Video based emotion analysis:
The video based analysis is based on fine-tuning the EmoStim dataset on the NVILA model

INSTALLATION
------------
Text based emotion analysis:
Clone this repo:
   git clone https://shiyao-monster.github.io/CSE6242.git


Video based emotion analysis:
1. For VILA install, follow the install instructions from https://github.com/peterchenyipu/VILA/. Or in CODE/VILA.
2. For dataset install, follow the install instructions at https://github.com/peterchenyipu/EmoStimDS. Or in CODE/EmoStimDS.

EXECUTION
-----
Text based emotion analysis:
From the project root (CODE/CSE6242-main):

Interactive Notebooks
   Launch and step through:
     Movie_Script_Sentiments_Line.ipynb  
     Movie_Review_Scirpts_Classification_Sentiments.ipynb  
     Movie_Script_Sentiments_Evaluation.ipynb  
   jupyter notebook

Video based emotion analysis:
Follow the instructions at https://github.com/peterchenyipu/VILA/blob/main/CSE6242_README.md. Or in CODE/VILA/CSE6242_README.md.

Visualization:
Our website is deployed on https://shiyao-monster.github.io/CSE6242/index.html. The source files are located in CODE/CSE6242-main
