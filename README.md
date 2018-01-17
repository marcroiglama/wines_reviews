# wines_reviews
The data is coming from https://www.kaggle.com/zynicide/wine-reviews and it's a massive dataset of wines reviews with information as the professional description, price, points and so on. The aim of the project is to give an overview of a worldwide wine clues, for example, the relation between price and quality(points), the countries where the wines are made or perform an analysis of the most used words to decrive wines. The future lines of this analysis could be to implement a Machine Learning algorithm to predict the clues(aroma,taste) that corresponds to an exellent wine. 

In order to develop the project the raw data is cleaned and normalized using python scripts. Finnally, the processed data is used to create a dashboard using PowerBi and DAX lenguange.

The steps to execute the project:
- download the dataset
- execute normalization.py to obtain wines.csv, location.csv and tasters.csv
- execute word_paser.py to o obtain ranking_words.csv from wines.csv
- import all the resulting csv's as the database of the wines.pbix

My own result is: 
