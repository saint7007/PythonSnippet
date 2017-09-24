import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from random import shuffle
from nltk.corpus import movie_reviews as mr
from nltk.corpus import sentiwordnet as swn
from nltk.corpus import stopwords


reviews = []
for fileid in mr.fileids():
    tag, filename = fileid.split('/')
    reviews.append([mr.raw(fileid), tag])

print(len(reviews))

shuffle(reviews)


# Removing punctuation
# Import regex
import re
# Import string
import string
regex = re.compile('[%s]' % re.escape(string.punctuation)) #see documentation here: http://docs.python.org/2/library/string.html

tokenized_reports_no_punctuation = []

for review in reviews:
    new_review = []
    for token in review:
        new_token = regex.sub(u'', token)
        if not new_token == u'':
            new_review.append(new_token)

    tokenized_reports_no_punctuation.append(new_review)

print(tokenized_reports_no_punctuation)

#Remove filler words using stop words

tokenized_reports_no_stopwords = []
for report in tokenized_reports_no_punctuation:
    new_term_vector = []
    for word in report:
        if not word in stopwords.words('english'):
            new_term_vector.append(word)
    tokenized_reports_no_stopwords.append(new_term_vector)

print(tokenized_reports_no_stopwords)



train=tokenized_reports_no_stopwords[:1500]
test=tokenized_reports_no_stopwords[1500:]


#Required for Bag of words (unigram features) creation
vocabulary = [x.lower() for tagged_sent in train for x in tagged_sent[0].split()]
vocabulary = list(set(vocabulary))
vocabulary.sort() #sorting the list
print(len(vocabulary))
#print(vocabulary)

def get_unigram_features(data,vocab):
    fet_vec_all = []
    for tup in data:
        single_feat_vec = []
        sent = tup[0].lower() #lowercasing the dataset
        for v in vocab:
            if sent.__contains__(v):
                single_feat_vec.append(1)
            else:
                single_feat_vec.append(0)
        fet_vec_all.append(single_feat_vec)
    return fet_vec_all



def get_senti_wordnet_features(data):
    fet_vec_all = []
    for tup in data:
        sent = tup[0].lower()
        words = sent.split()
        pos_score = 0
        neg_score = 0
        for w in words:
            senti_synsets = swn.senti_synsets(w.lower())
            for senti_synset in senti_synsets:
                p = senti_synset.pos_score()
                n = senti_synset.neg_score()
                pos_score+=p
                neg_score+=n
                break #take only the first synset (Most frequent sense)
        fet_vec_all.append([float(pos_score),float(neg_score)])
    return fet_vec_all



def merge_features(featureList1,featureList2):
    # For merging two features
    if featureList1==[]:
        return featureList2
    merged = []
    for i in range(len(featureList1)):
        m = featureList1[i]+featureList2[i]
        merged.append(m)
    return merged


def get_lables(data):
    labels = []
    for tup in data:
        if tup[1].lower()=="neg":
            labels.append(-1)
        else:
            labels.append(1)
    return labels

def calculate_precision(prediction, actual):
    prediction = list(prediction)
    correct_labels = [prediction[i]  for i in range(len(prediction)) if actual[i] == prediction[i]]
    precision = float(len(correct_labels))/float(len(prediction))
    return precision

def real_time_test(classifier,vocab):
    print("Enter a sentence: ")
    inp = input()
    feat_vec_uni = get_unigram_features(inp,vocab)
    feat_vec_swn =get_senti_wordnet_features(test_data)
    feat_vec = merge_features(feat_vec_uni, feat_vec_swn)

    predict = classifier.predict(feat_vec)
    if predict[0]==1:
        print("The sentiment expressed is: positive")
    else:
        print("The sentiment expressed is: negative")


training_features = get_unigram_features(train,vocabulary) # vocabulary extracted in the beginning
training_labels = get_lables(train)

test_features = get_unigram_features(test,vocabulary)
test_gold_labels = get_lables(test)


precision_lst=[]


from sklearn.naive_bayes import MultinomialNB
nb_classifier = MultinomialNB(alpha=0.1).fit(training_features,training_labels) #training process

print("Precision NB classifier")
pred = nb_classifier.predict(training_features)
precision = calculate_precision(pred,training_labels)
print("Training \t" + str(precision))
pred = nb_classifier.predict(test_features)
precision = calculate_precision(pred,test_gold_labels)
print("Test \t" + str(precision))
precision_lst.append(precision)



from sklearn.svm import SVC
clf = SVC(C=0.1, kernel='sigmoid').fit(training_features,training_labels)
print("Precision SVM classifier")
pred = clf.predict(training_features)
precision = calculate_precision(pred,training_labels)
print("Training \t" + str(precision))
pred = clf.predict(test_features)
precision = calculate_precision(pred,test_gold_labels)
print("Test \t" + str(precision))
precision_lst.append(precision)



from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier(max_depth=5, max_features='sqrt', random_state=42).fit(training_features,training_labels)
print("Precision Decision Tree classifier")
pred = clf.predict(training_features)
precision = calculate_precision(pred,training_labels)
print("Training \t" + str(precision))
pred = clf.predict(test_features)
precision = calculate_precision(pred,test_gold_labels)
print("Test \t" + str(precision))
precision_lst.append(precision)


from sklearn.linear_model import LogisticRegression
clf = LogisticRegression(random_state=42).fit(training_features,training_labels)
print("Precision Logistic Regression")
pred = clf.predict(training_features)
precision = calculate_precision(pred,training_labels)
print("Training \t" + str(precision))
pred = clf.predict(test_features)
precision = calculate_precision(pred,test_gold_labels)
print("Test \t" + str(precision))
precision_lst.append(precision)



from nltk.corpus import twitter_samples as ts
import json


mypath= '/home/sukumar/nltk_data/corpora/twitter_samples/'
pos = []
for line in open (mypath + r'positive_tweets.json', 'r'):
    pos.append(json.loads(line))

neg = []
for line in open (mypath + r'negative_tweets.json', 'r'):
    neg.append(json.loads(line))


len(pos)
df0 = []
for dic in pos:
    ll = []
    ll.append(dic['text'])
    ll.append("pos")
    df0.append(ll)

df1 = []
for dic in neg:
    ll = []
    ll.append(dic['text'])
    ll.append("neg")
    df1.append(ll)

df0.extend(df1)


df=df0
len(df)

shuffle(df)

train=df[:7000]
test=df[7000:]

#Required for Bag of words (unigram features) creation
vocabulary = [x.lower() for tagged_sent in train for x in tagged_sent[0].split()]
vocabulary = list(set(vocabulary))
vocabulary.sort() #sorting the list
print(len(vocabulary))
#print(vocabulary)

training_features = get_unigram_features(train,vocabulary) # vocabulary extracted in the beginning
training_labels = get_lables(train)

test_features = get_unigram_features(test,vocabulary)
test_gold_labels = get_lables(test)


from sklearn.naive_bayes import MultinomialNB
nb_classifier = MultinomialNB(alpha=0.1).fit(training_features,training_labels) #training process

print("Precision NB classifier ")
pred = nb_classifier.predict(training_features)
precision = calculate_precision(pred,training_labels)
print("Training \t" + str(precision))
pred = nb_classifier.predict(test_features)
precision = calculate_precision(pred,test_gold_labels)
print("Test \t" + str(precision))
precision_lst.append(precision)


from sklearn.svm import SVC
clf = SVC(C=0.1, kernel='sigmoid').fit(training_features,training_labels)
print("Precision SVM classifier")
pred = clf.predict(training_features)
precision = calculate_precision(pred,training_labels)
print("Training\t" + str(precision))
pred = clf.predict(test_features)
precision = calculate_precision(pred,test_gold_labels)
print("Test \t" + str(precision))
precision_lst.append(precision)


from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier(max_depth=5, max_features='sqrt', random_state=34).fit(training_features,training_labels)
print("Precision Decision Tree classifier")
pred = clf.predict(training_features)
precision = calculate_precision(pred,training_labels)
print("Training\t" + str(precision))
pred = clf.predict(test_features)
precision = calculate_precision(pred,test_gold_labels)
print("Test \t" + str(precision))
precision_lst.append(precision)


from sklearn.linear_model import LogisticRegression
clf = LogisticRegression(random_state=35).fit(training_features,training_labels)
print("Precision Logistic Regression ")
pred = clf.predict(training_features)
precision = calculate_precision(pred,training_labels)
print("Training \t" + str(precision))
pred = clf.predict(test_features)
precision = calculate_precision(pred,test_gold_labels)
print("Test \t" + str(precision))
precision_lst.append(precision)


print('''
(Dataset)        (Naive Bayes)          (SVM)           (Decision-tree)       (Logistic-Regression)

movie_review        {}                    {}                 {}                     {}

twitter_dataset     {}                    {}                 {}                     {}

'''.format(*precision_lst))


'''OutPut'''
#/usr/bin/python3.6 /home/sukumar/PycharmProjects/NLP/nltkTwitterMoviePosNeg.py
'''41548
Precision NB classifier
Training 	0.9906666666666667
Test 	0.8
Precision SVM classifier
Training 	0.51
Test 	0.47
Precision Decision Tree classifier
Training 	0.5726666666666667
Test 	0.516
Precision Logistic Regression
Training 	1.0
Test 	0.822
19572
Precision NB classifier
Training 	0.9998571428571429
Test 	0.9866666666666667
#Precision SVM classifier
#Training 	0.5037142857142857
#Test 	0.49133333333333334
#Precision Decision Tree classifier
#Training	0.5915714285714285
#Test	0.5816666666666667
#Precision Logistic Regression
#Training 	1.0
#Test 	1.0

#(Dataset)        (Naive Bayes)          (SVM)           (Decision-tree)       (Logistic-Regression)

#movie_review        0.8                    0.47                 0.517                     0.822

#twitter_dataset     0.9866666666666667     0.45133333333333334   0.5016666666666667              1.0



Process finished with exit code 0


------------------------------------------------


41548
Precision NB classifier
Training 	0.9906666666666667
Test 	0.8
Precision SVM classifier
Training 	0.51
Test 	0.47
Precision Decision Tree classifier
Training 	0.5726666666666667
Test 	0.516
Precision Logistic Regression
Training 	1.0
Test 	0.822
19572
Precision NB classifier
Training 	0.9998571428571429
Test 	0.9866666666666667
Precision SVM classifier
Training	0.5021428571428571
Test 	0.495
Precision Decision Tree classifier
Training	0.6834285714285714
Test 	0.6776666666666666
Precision Logistic Regression
Training 	1.0
Test 	0.999

(Dataset)        (Naive Bayes)          (SVM)           (Decision-tree)       (Logistic-Regression)

movie_review        0.8                    0.47                 0.516                     0.822

twitter_dataset     0.9866666666666667           0.495      0.6776666666666666              0.999



'''