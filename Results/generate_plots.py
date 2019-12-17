# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 15:20:02 2019

@author: Suhaib
"""

def readFile(fname):
    file = open(fname, 'r')
    txt = file.read()
    file.close()
    txtsplit = txt.split("Iteration ")
    data = {}
    for currentTxt in txtsplit[1:]:
        iterNum = int(currentTxt.split(" **********")[0])
        firstSplit = currentTxt.split("EpRewMean           |")
        if (len(firstSplit) > 1):
            firstSplit = firstSplit[1]
            secondSplit = firstSplit.split("|\n|")[0]
            if "nan" not in secondSplit:
                score = float(secondSplit)
                if (iterNum <= 50):
                    data[iterNum] = score
        else:
            print(currentTxt)
    return (data.keys(), data.values())


import matplotlib.pyplot as plt

data_NSES_FROST_EUC = readFile("NS-ES_Frost_Euclidean.txt")
data_NSES_FROST_NCD_1 = readFile("NS-ES_Frost_NCD=1.txt")
data_NSES_FROST_NCD_3 = readFile("NS-ES_Frost_NCD=3.txt")

plt.figure(figsize=(8,6))
plt.title("Similarity Metrics Comparison: NS-ES for Frostbite")
plt.plot(data_NSES_FROST_EUC[0], data_NSES_FROST_EUC[1], data_NSES_FROST_NCD_1[0], data_NSES_FROST_NCD_1[1], data_NSES_FROST_NCD_3[0], data_NSES_FROST_NCD_3[1])
plt.legend(("Euclidean Distance", "NCD; Similarity Threshold = 1", "NCD; Similarity Threshold = 3"))
plt.xlabel("Iteration Number")
plt.ylabel("Mean Episode Reward")



data_NSRES_FROST_EUC = readFile("NSR-ES_Frost_Euclidean.txt")
data_NSRES_FROST_NCD_3 = readFile("NSR-ES_Frost_NCD=3.txt")

plt.figure(figsize=(8,6))
plt.title("Similarity Metrics Comparison: NSR-ES for Frostbite")
plt.plot(data_NSRES_FROST_EUC[0], data_NSRES_FROST_EUC[1], data_NSRES_FROST_NCD_3[0], data_NSRES_FROST_NCD_3[1])
plt.legend(("Euclidean Distance", "NCD; Similarity Threshold = 3"))
plt.xlabel("Iteration Number")
plt.ylabel("Mean Episode Reward")


