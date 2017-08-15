'''Note there are two approaches'''


import nltk

#nltk.download("wordnet")
import numpy as np
import pandas as pd
from sklearn.preprocessing import normalize
from nltk.corpus import wordnet


words=[["computer","keyboard"],["Jerusalem","Israel"],["planet","galaxy"],["canyon","landscape"],["OPEC","Country"],
       ["day","summer"],["day","dawn"],["country","citizen"],["planet","people"],["environment","ecology"],["Maradona","Football"],
       ["OPEC","oil"],["money","bank"],["computer","software"],["law","lawyer"],["wheather","forecast"],["network","hardware"],
       ["nature","environment"],["FBI","investigation"],["money","wealth"],["psychology","Freud"],["news","report"],
       ["war","troops"],["physics","proton"],["bank","money"],["stock","market"],["planet","constellation"],["credit","card"],
       ["hotel","reservation"],["closet","clothes"],["soap","opera"],["planet","astronomer"],["planet","space"],
       ["movie","theater"],["treatment","recovery"],["baby","mother"],["money","deposite"],["television","film"],
       ["psychology","mind"],["game","team"],["admission","ticket"],["Jerusalem","Palestinian"],["Arafat","terror"],
       ["boxing","round"],["computer","internet"],["money","property"],["tennis","racket"],["telephone","communication"],
       ["currency","market"],["psychology","cognition"]]

from itertools import product
def maxSimilarity(word1, word2):
    wordFromList1 = wordnet.synsets(word1)[0]
    print("{} :".format(word1), wordFromList1)
    wordFromList2 = wordnet.synsets(word2)[0]
    print("{} :".format(word2), wordFromList2)
    s = wordFromList1.wup_similarity(wordFromList2)
    return (wordFromList1.name, wordFromList2.name, wordFromList1.wup_similarity(wordFromList2))
for word in words:
       try:
              wupSimilarity=[]
              pathSimilarity = []
              lchSimilarity = []
              firstWord=word[0]
              secondWord=word[1]
              syns1 = wordnet.synsets(firstWord, 'n')
              syns2 = wordnet.synsets(secondWord, 'n')

              for sense1, sense2 in product(syns1, syns2):
                  d = wordnet.wup_similarity(sense1, sense2)
                  wupSimilarity.append((d, syns1, syns2))

                  e = wordnet.path_similarity(sense1, sense2)
                  pathSimilarity.append((e, syns1, syns2))

                  f = wordnet.lch_similarity(sense1, sense2)
                  lchSimilarity.append((f, syns1, syns2))

              print("first word =",firstWord," | second word =", secondWord, "| wup similarity max =", max(wupSimilarity)[0],"| path similarity max =", max(pathSimilarity)[0],"| lch similarity max =", max(lchSimilarity)[0])

       except Exception:
              print("Exception still continuing ",Exception)
              continue


#APPROACH two

# https://stackoverflow.com/questions/17969532/how-to-normalize-similarity-measures-from-wordnet?noredirect=1&lq=1


firstWordApproach2=[]
secondWordApproach2=[]
wupSimilarityApproach2=[]
pathSimilarityApproach2 = []
lchSimilarityApproach2 = []
for word in words:
       try:
              firstWord=word[0]
              secondWord=word[1]
              syns1 = wordnet.synsets(firstWord)
              syns1=syns1[0]
              syns2 = wordnet.synsets(secondWord)
              syns2=syns2[0]
              firstWordApproach2.append(firstWord)
              secondWordApproach2.append(secondWord)
              wup = syns1.wup_similarity(syns2)
              path = syns1.path_similarity(syns2)
              lch = syns1.lch_similarity(syns2)
              wupSimilarityApproach2.append(wup)
              pathSimilarityApproach2.append(path)
              lchSimilarityApproach2.append(lch)

       except Exception:
              print("Exception still continuing ",Exception)
              firstWordApproach2.append(firstWord)
              secondWordApproach2.append(secondWord)
              wupSimilarityApproach2.append(np.NAN)
              pathSimilarityApproach2.append(np.NAN)
              lchSimilarityApproach2.append(np.NAN)

              continue
df=pd.concat([pd.DataFrame(firstWordApproach2, columns = ['firstWord']),
           pd.DataFrame(secondWordApproach2, columns = ['secondWord_2']),
           pd.DataFrame(wupSimilarityApproach2, columns=['wup']),
           pd.DataFrame(pathSimilarityApproach2, columns = ['path']),
           pd.DataFrame(lchSimilarityApproach2, columns = ['lch'])], axis = 1)

normalizeDf=df

normalizeDf['lch'] = normalizeDf['lch'].fillna(0)
normalizeDf['normalizeLch'] = pd.DataFrame(normalize(normalizeDf['lch'], axis=1).T)
normalizeDf['maximumSimilarity'] = normalizeDf[['wup','path','normalizeLch']].max(axis=1)

print(normalizeDf)