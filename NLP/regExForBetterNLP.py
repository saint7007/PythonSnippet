import re
def date(anyRandomText):
    date = []
    reg1 = re.compile(
        r'[0-2][0-9][-./]0?[1-9][-./]\d{4}|3[0-1][-./]0?(?:1|3|4|5|6|7|8|9)[-./]\d{4}|[0-2][0-9][-./]1[0-2][-./]\d{4}|3[0-1][-./]1[0-2][-./]\d{4}')
    reg2 = re.compile(
        r'[0-2][0-9]\s(?:January|February|March|April|May|June|July|August|September|October|November|December)\s\d{4}|[^\d]\s(?:January|February|March|April|May|June|July|August|September|October|November|December)\s\d{4}|3[0-1]\s(?:January|March|May|July|August|October|December)\s\d{4}|30\s(?:April|June|September|November)\s\d{4}')
    reg3 = re.compile(
        r'\d{4}[-./]0?[1-9][-./][0-2][0-9]|\d{4}[-./]0?[1-9][-./]3[0-1]|\d{4}[-./]1[0-2][-./][0-2][0-9]|\d{4}[-./]1[0-2][-./]3[0-1]')

    list1 = reg1.findall(anyRandomText)
    list2 = reg2.findall(anyRandomText)
    list3 = reg3.findall(anyRandomText)
    date.append(list1)
    date.append(list2)
    date.append(list3)
    return date


input = "Correct date patterns: 15 November 1989  October 2016 ,  28 February 2011, 16/11/2016 , 16.11.2016 , 16-11-2016 , 2016-11-16 , Incorrect date patterns: 02-29-2011 , 2-12-2011 , 01@11@2011, 30-02-2011, 30 February 2012"

date=date(input)

print("correct dates - ",date)

########################################Output###########################################

#/usr/bin/python3.6 /home/sukumar/PycharmProjects/NLP/regExForBetterNLP.py
#correct dates -  [['16/11/2016', '16.11.2016', '16-11-2016'], ['15 November 1989', '  October 2016', '28 February 2011'], ['2016-11-16']]
#Process finished with exit code 0