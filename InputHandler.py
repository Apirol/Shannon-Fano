import numpy as np

def openFileAndReadData(fileName):
    handle = open(fileName, 'r', encoding='utf-8')
    data = handle.read()
    handle.close()
    return data

def openFileAndReadNumber(filename):
    return np.loadtxt(filename, dtype=np.float)