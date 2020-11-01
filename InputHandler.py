import numpy as np


def openFileAndReadData(fileName):
    handle = open(fileName, 'r', encoding='utf-8')
    data = handle.read()
    handle.close()
    return data


def openFileAndReadNumber(filename):
    return np.loadtxt(filename, dtype=np.float)


def makeFrequrencyAlphabet(alphabet, frequrency):
    alphabetWithFreq = dict()

    for i in range(len(frequrency)):
        alphabetWithFreq.update({alphabet[i]: frequrency[i]})

    return alphabetWithFreq
