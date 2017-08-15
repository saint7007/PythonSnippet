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

''' Not using Jupyter
#Pasting outPut
#####################################  outPut ##########################################
#first word = computer  | second word = keyboard | wup similarity max = 0.8235294117647058 | path similarity max = 0.25 | lch similarity max = 2.2512917986064953
#first word = Jerusalem  | second word = Israel | wup similarity max = 0.7 | path similarity max = 0.14285714285714285 | lch similarity max = 1.6916760106710724
#first word = planet  | second word = galaxy | wup similarity max = 0.631578947368421 | path similarity max = 0.125 | lch similarity max = 1.55814461804655
#first word = canyon  | second word = landscape | wup similarity max = 0.35294117647058826 | path similarity max = 0.08333333333333333 | lch similarity max = 1.1526795099383855
#first word = OPEC  | second word = Country | wup similarity max = 0.625 | path similarity max = 0.14285714285714285 | lch similarity max = 1.6916760106710724
#first word = day  | second word = summer | wup similarity max = 0.7692307692307693 | path similarity max = 0.25 | lch similarity max = 2.2512917986064953
#first word = day  | second word = dawn | wup similarity max = 0.8333333333333334 | path similarity max = 0.3333333333333333 | lch similarity max = 2.538973871058276
#first word = country  | second word = citizen | wup similarity max = 0.42857142857142855 | path similarity max = 0.1111111111111111 | lch similarity max = 1.4403615823901665
#first word = planet  | second word = people | wup similarity max = 0.2 | path similarity max = 0.1111111111111111 | lch similarity max = 1.4403615823901665
#first word = environment  | second word = ecology | wup similarity max = 0.9230769230769231 | path similarity max = 0.5 | lch similarity max = 2.9444389791664407
#Word not found in Wordnet
#first word = OPEC  | second word = oil | wup similarity max = 0.23529411764705882 | path similarity max = 0.07142857142857142 | lch similarity max = 0.9985288301111273
#first word = money  | second word = bank | wup similarity max = 0.5714285714285714 | path similarity max = 0.14285714285714285 | lch similarity max = 1.6916760106710724
#first word = computer  | second word = software | wup similarity max = 0.14285714285714285 | path similarity max = 0.07692307692307693 | lch similarity max = 1.072636802264849
#first word = law  | second word = lawyer | wup similarity max = 0.16666666666666666 | path similarity max = 0.09090909090909091 | lch similarity max = 1.2396908869280152
#Word not found in Wordnet
#first word = network  | second word = hardware | wup similarity max = 0.8 | path similarity max = 0.25 | lch similarity max = 2.2512917986064953
#first word = nature  | second word = environment | wup similarity max = 0.5454545454545454 | path similarity max = 0.16666666666666666 | lch similarity max = 1.845826690498331
#first word = FBI  | second word = investigation | wup similarity max = 0.2222222222222222 | path similarity max = 0.06666666666666667 | lch similarity max = 0.9295359586241757
#first word = money  | second word = wealth | wup similarity max = 0.9230769230769231 | path similarity max = 0.5 | lch similarity max = 2.9444389791664407
#first word = psychology  | second word = Freud | wup similarity max = 0.09523809523809523 | path similarity max = 0.05 | lch similarity max = 0.6418538861723948
#first word = news  | second word = report | wup similarity max = 0.9230769230769231 | path similarity max = 0.5 | lch similarity max = 2.9444389791664407
#first word = war  | second word = troops | wup similarity max = 0.3076923076923077 | path similarity max = 0.1 | lch similarity max = 1.3350010667323402
#first word = physics  | second word = proton | wup similarity max = 0.2222222222222222 | path similarity max = 0.06666666666666667 | lch similarity max = 0.9295359586241757
#first word = bank  | second word = money | wup similarity max = 0.5714285714285714 | path similarity max = 0.14285714285714285 | lch similarity max = 1.6916760106710724
#first word = stock  | second word = market | wup similarity max = 0.5555555555555556 | path similarity max = 0.14285714285714285 | lch similarity max = 1.6916760106710724
#first word = planet  | second word = constellation | wup similarity max = 0.7692307692307693 | path similarity max = 0.25 | lch similarity max = 2.2512917986064953
#first word = credit  | second word = card | wup similarity max = 0.6153846153846154 | path similarity max = 0.16666666666666666 | lch similarity max = 1.845826690498331
#first word = hotel  | second word = reservation | wup similarity max = 0.375 | path similarity max = 0.09090909090909091 | lch similarity max = 1.2396908869280152
#first word = closet  | second word = clothes | wup similarity max = 0.5882352941176471 | path similarity max = 0.125 | lch similarity max = 1.55814461804655
#first word = soap  | second word = opera | wup similarity max = 0.23529411764705882 | path similarity max = 0.07142857142857142 | lch similarity max = 0.9985288301111273
#first word = planet  | second word = astronomer | wup similarity max = 0.631578947368421 | path similarity max = 0.16666666666666666 | lch similarity max = 1.845826690498331
#first word = planet  | second word = space | wup similarity max = 0.5333333333333333 | path similarity max = 0.14285714285714285 | lch similarity max = 1.6916760106710724
#first word = movie  | second word = theater | wup similarity max = 0.625 | path similarity max = 0.14285714285714285 | lch similarity max = 1.6916760106710724
#first word = treatment  | second word = recovery | wup similarity max = 0.7692307692307693 | path similarity max = 0.25 | lch similarity max = 2.2512917986064953
#first word = baby  | second word = mother | wup similarity max = 0.631578947368421 | path similarity max = 0.2 | lch similarity max = 2.0281482472922856
#Word not found in Wordnet
#first word = television  | second word = film | wup similarity max = 0.7777777777777778 | path similarity max = 0.2 | lch similarity max = 2.0281482472922856
#first word = psychology  | second word = mind | wup similarity max = 0.5882352941176471 | path similarity max = 0.14285714285714285 | lch similarity max = 1.6916760106710724
#first word = game  | second word = team | wup similarity max = 0.3076923076923077 | path similarity max = 0.1 | lch similarity max = 1.3350010667323402
#first word = admission  | second word = ticket | wup similarity max = 0.5714285714285714 | path similarity max = 0.14285714285714285 | lch similarity max = 1.6916760106710724
#first word = Jerusalem  | second word = Palestinian | wup similarity max = 0.2857142857142857 | path similarity max = 0.0625 | lch similarity max = 0.8649974374866046
#first word = Arafat  | second word = terror | wup similarity max = 0.631578947368421 | path similarity max = 0.16666666666666666 | lch similarity max = 1.845826690498331
#first word = boxing  | second word = round | wup similarity max = 0.7272727272727273 | path similarity max = 0.14285714285714285 | lch similarity max = 1.6916760106710724
#first word = computer  | second word = internet | wup similarity max = 0.631578947368421 | path similarity max = 0.125 | lch similarity max = 1.55814461804655
#first word = money  | second word = property | wup similarity max = 0.8333333333333334 | path similarity max = 0.3333333333333333 | lch similarity max = 2.538973871058276
#first word = tennis  | second word = racket | wup similarity max = 0.6 | path similarity max = 0.1111111111111111 | lch similarity max = 1.4403615823901665
#first word = telephone  | second word = communication | wup similarity max = 0.16666666666666666 | path similarity max = 0.09090909090909091 | lch similarity max = 1.2396908869280152
#first word = currency  | second word = market | wup similarity max = 0.3076923076923077 | path similarity max = 0.1 | lch similarity max = 1.3350010667323402
#first word = psychology  | second word = cognition | wup similarity max = 0.6153846153846154 | path similarity max = 0.16666666666666666 | lch similarity max = 1.845826690498331
#Process finished with exit code 0'''

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

'''      firstWord   secondWord_2       wup      path       lch  normalizeLch  \
0      computer       keyboard  0.823529  0.250000  2.251292      0.240887
1     Jerusalem         Israel  0.700000  0.142857  1.691676      0.181008
2        planet         galaxy  0.166667  0.090909  1.239691      0.132646
3        canyon      landscape  0.333333  0.076923  1.072637      0.114771
4          OPEC        Country  0.625000  0.142857  1.691676      0.181008
5           day         summer  0.500000  0.142857  1.691676      0.181008
6           day           dawn  0.266667  0.083333  1.152680      0.123336
7       country        citizen  0.142857  0.076923  1.072637      0.114771
8        planet         people  0.181818  0.100000  1.335001      0.142844
9   environment        ecology  0.923077  0.500000  2.944439      0.315053
10     Maradona       Football       NaN       NaN  0.000000      0.000000
11         OPEC            oil  0.222222  0.066667  0.929536      0.099460
12        money           bank  0.153846  0.083333  1.152680      0.123336
13     computer       software  0.117647  0.062500  0.864997      0.092554
14          law         lawyer  0.166667  0.090909  1.239691      0.132646
15     wheather       forecast       NaN       NaN  0.000000      0.000000
16      network       hardware  0.153846  0.083333  1.152680      0.123336
17       nature    environment  0.545455  0.166667  1.845827      0.197502
18          FBI  investigation  0.200000  0.058824  0.804373      0.086067
19        money         wealth  0.285714  0.090909  1.239691      0.132646
20   psychology          Freud  0.095238  0.050000  0.641854      0.068678
21         news         report  0.461538  0.125000  1.558145      0.166720
22          war         troops  0.285714  0.090909  1.239691      0.132646
23      physics         proton  0.095238  0.050000  0.641854      0.068678
24         bank          money  0.153846  0.083333  1.152680      0.123336
25        stock         market  0.285714  0.090909  1.239691      0.132646
26       planet  constellation  0.133333  0.071429  0.998529      0.106842
27       credit           card  0.285714  0.090909  1.239691      0.132646
28        hotel    reservation  0.375000  0.090909  1.239691      0.132646
29       closet        clothes  0.588235  0.125000  1.558145      0.166720
30         soap          opera  0.222222  0.066667  0.929536      0.099460
31       planet     astronomer  0.470588  0.100000  1.335001      0.142844
32       planet          space  0.181818  0.100000  1.335001      0.142844
33        movie        theater  0.625000  0.142857  1.691676      0.181008
34    treatment       recovery  0.444444  0.090909  1.239691      0.132646
35         baby         mother  0.500000  0.111111  1.440362      0.154118
36        money       deposite       NaN       NaN  0.000000      0.000000
37   television           film  0.555556  0.111111  1.440362      0.154118
38   psychology           mind  0.571429  0.142857  1.691676      0.181008
39         game           team  0.285714  0.090909  1.239691      0.132646
40    admission         ticket  0.235294  0.071429  0.998529      0.106842
41    Jerusalem    Palestinian  0.285714  0.062500  0.864997      0.092554
42       Arafat         terror  0.125000  0.066667  0.929536      0.099460
43       boxing          round  0.105263  0.055556  0.747214      0.079951
44     computer       internet  0.631579  0.125000  1.558145      0.166720
45        money       property  0.333333  0.111111  1.440362      0.154118
46       tennis         racket  0.444444  0.090909  1.239691      0.132646
47    telephone  communication  0.133333  0.071429  0.998529      0.106842
48     currency         market  0.285714  0.090909  1.239691      0.132646
49   psychology      cognition  0.615385  0.166667  1.845827      0.197502

maximumSimilarity
0            0.823529
1            0.700000
2            0.166667
3            0.333333
4            0.625000
5            0.500000
6            0.266667
7            0.142857
8            0.181818
9            0.923077
10           0.000000
11           0.222222
12           0.153846
13           0.117647
14           0.166667
15           0.000000
16           0.153846
17           0.545455
18           0.200000
19           0.285714
20           0.095238
21           0.461538
22           0.285714
23           0.095238
24           0.153846
25           0.285714
26           0.133333
27           0.285714
28           0.375000
29           0.588235
30           0.222222
31           0.470588
32           0.181818
33           0.625000
34           0.444444
35           0.500000
36           0.000000
37           0.555556
38           0.571429
39           0.285714
40           0.235294
41           0.285714
42           0.125000
43           0.105263
44           0.631579
45           0.333333
46           0.444444
47           0.133333
48           0.285714
49           0.615385

Process finished with exit code 0'''