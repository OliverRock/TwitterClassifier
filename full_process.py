
# load_corpus takes a training set of data- tweets which are labeled as either positive or negative
# and returns a list of cleaned data
def load_corpus():
    print ("loading corpus")
    corpus = []
    # cvs file to learn from
    input_file = open ('training_full.csv')
    count = 0
    for line in input_file :
        (ident, emot, tweet) = line.split(",")
        clean_tweet = tweet.lower().rstrip().lstrip().strip(',.!;#*&@)(')
        corpus = corpus + [[ident, emot, clean_tweet]]
        # to restrict the number of tweets to train on
        if count > 50000:
            break
        #if count % 1000 == 0:
            # print(count)
        count += 1
    return corpus



# creates a dictionary of all words and the number of times they appear in positive or negative tweets
# as a proportion of the frequency of all words
def create_dictionary(corpus):
    print ("creating dictionary")
    total_pos = 0
    total_neg = 0
    total_both = 0
    
    word_freq = {}
    for item in corpus:
        for word in item[2].split() :
            word_freq[word] =[0,0,0]
            
    for item in corpus:
        for word in item[2].split() :
            [pos, neg, both] = word_freq[word]
            if item[1] == '1':
                pos = pos + 1
                total_pos = total_pos + 1
            elif item [1] == '0':
                neg = neg + 1
                total_neg = total_neg + 1
            both = both + 1
            total_both = total_both + 1
            word_freq[word] = [pos, neg, both]
            word_freq['totals!'] = [total_pos,total_neg,total_both]
    return word_freq



# classify a tweet as either possitive (1) or negative (0)
def classify_tweet(tweet, word_dictionary):
    clean_tweet = tweet.lower().rstrip().lstrip().strip(',.!;#*&@)(').split()
    total_pos = 1
    total_neg = 1
    for word in clean_tweet:
        if word in word_dictionary:
            [pos, neg, total] = word_dictionary[word]
            total_pos = total_pos * pos
            total_neg = total_neg * neg

    [p_pos, p_neg, total_both] = word_dictionary['totals!']
    total_pos = total_pos * (p_pos/total_both)
    total_neg = total_neg * (p_neg/total_both)

    if total_pos > total_neg:
        return 1
    else:
        return 0




# to evaluate the word dictionary. It uses the test file and returns a percentage of the number of tweets it classifies correctly
def evaluate (word_dictionary):
    print ("evaluating classifier")
    count = 0
    correct = 0
    input_file = open ('test.csv')
    for line in input_file :
        (ident, emot, tweet) = line.split(",")
        guess = classify_tweet(tweet, word_dictionary)
        if guess == int(emot) : correct = correct + 1
        count = count + 1
    score = round(correct / count * 100)
    print ("classifer is " + str(score) + "% correct")


# Function takes cvs file of a users tweets and prints the number of positive, the number of negative and
# the total number of tweets
def classifyPerson(csvFile, word_dictionary):
    input_file = open(csvFile)
    pos = 0
    neg = 0
    total = 0
    for line in input_file:
        if(classify_tweet(line,word_dictionary) == 0):
            neg +=1
        else:
            pos += 1
        total +=1
    print('pos: ' + str(pos) + ', neg: ' + str(neg) + ', total: ' + str(total))



# create the corpus from the training set
corpus = load_corpus()

# create a dictionary of each words
word_dictionary = create_dictionary (corpus)

# print(classify_tweet('i am happy', word_dictionary))

# evaluate the accuracy of the program
evaluate(word_dictionary)

# classify a users tweets
classifyPerson("realDonaldTrump_tweets.csv", word_dictionary)