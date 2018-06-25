# TwitterClassifier
Python program to create a CSV file of a twitter users twitter and a program which learns to classify tweets as either positive or negative.

The file createCSV.py uses twitters API to download a users most recent tweets. Requires tweepy package from https://github.com/tweepy/tweepy and Twitter API credentials from https://apps.twitter.com/

The file full_process.py contains the functions to learn patterns in a labelled data set, classyify individual tweets, evaluate the program against a test data set, and evaluate a twitter user's tweets.

The classification program is very simple but effective. It takes a data set of tweets which are laballed as either positive or negative. It then creates a dictionary of all words used in those tweets and gives each word a score based on the probability of whether it is in a positive or negative tweet. For this it uses a naive bayes classifier. Then to evalute a tweet, the program looks up all the words in this dictionary and returns 0 if it likly to be negative and 1 if it is positive. 


The file training_full.csv contains 1 000 000 tweets which are labeled as either positive or negative.
test.csv contains a test data set to evaluate the effectiveness of my program. To learn from this entire data set can take a long time and so you can limit how many are used in full_process.py e.g. 70 000

The file test.csv contains a data set to test the accuracy of the program.

For an example run I downloaded 3218 tweets from Barack Obama. I trained the program on 70 000 tweets from the training set. With this, the prrgram had an accuracy of 91% guessing whether a tweet was positive or negative in the test data. Om Barack Obamas tweets the program calculated 2066 to be positive, 1152 to be negative.
