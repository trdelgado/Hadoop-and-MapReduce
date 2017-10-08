#!/usr/bin/python

import sys


answer_lengths = []
questionID = ''
questionLength = 0
prevID = ''

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 3:
        # Something has gone wrong. Skip this line.
        continue

    thisID, thisType,thisLength = data_mapped

    

    if questionID and (thisID != prevID):
        #print "second if"
        sumLength = sum(answer_lengths)
        if len(answer_lengths) != 0:
            lengthAverage = float(sumLength)/len(answer_lengths)
            print questionID, "\t", questionLength, "\t", lengthAverage
        else:
            print questionID, "\t", questionLength, "\t", 0
        answer_lengths = []
        questionID = ''
        questionLength = 0

    if thisType == "question":
        #print "first if"
        questionID = thisID
        questionLength = thisLength
    elif thisType == "answer":
        answer_lengths.append(float(thisLength))
    prevID = thisID
    


if questionID:
        sumLength = sum(map(float, answer_lengths))
        if len(answer_lengths) != 0:
            lengthAverage = float(sumLength)/len(answer_lengths)
            print questionID, "\t", questionLength, "\t", lengthAverage
        else:
            print questionID, "\t", questionLength, "\t", 0

