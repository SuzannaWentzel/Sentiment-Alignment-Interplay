# Thesis: Alignment, Agreement, and Sentiment in online discussions
Contains the data processing of my Master Thesis and example notebooks for further reference

## Running the project
Data should be added to a Data folder, add the path to the __datapath__ variable in preprocessing_notebook.py. Data should be in .csv and have the following columns (see also [dummy_data.csv](Data/dummy_data.csv)):
- discussion_id
- topic
- post_id
- text
- username
- parent_post_id
- parent_missing

After adding the data, the following notebooks can be used step by step to investigate the interplay between sentiment and alignment:
1. Preprocessing => [preprocessing.py](preprocessing.py)
2. Alignment analysis => [compute_lexical_word_alignment_v2_all.py](compute_lexical_word_alignment_v2_all.py)
3. Sentiment analysis => [sentiment_analysis.py](sentiment_analysis.py)
4. Interplay analysis => [interplay_analysis.py](interplay_analysis.py)

Cleaning up the code is still a work in progress, but will appear here:
1. Preprocessing => [preprocessing_notebook.py](preprocessing_notebook.py)
2. Alignment analysis => [lexical_alignment_notebook.py](lexical_alignment_notebook.py)
3. Sentiment analysis => [sentiment_notebook.py](sentiment_notebook.py)
4. Interplay analysis => [interplay_alignment_sentiment_notebook.py](interplay_alignment_sentiment_notebook.py)

The code for the time-based-overlap lives in [linguistic_alignment_analysis/time_based_overlap.py](linguistic_alignment_analysis/time-based-overlap.py)

## Dependencies
This repo needs the following packages (including their dependencies):
- matplotlib
- nltk
- numba
- numpy
- pandas
- stanza
- scipy
- transformers
