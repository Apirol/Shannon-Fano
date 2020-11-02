from math import log, pow


def getAllInfo(code_table, alphabetWithFreq, text):
    averageLenght = code_symbol_lenght(code_table)
    entropyH = sum(calculateEntropyH(alphabetWithFreq))
    superfluity = calculateSuperfluity(entropyH)
    check = checkCraft(code_table)
    text = "".join(text)
    lenghtOfText = len(text)
    return list([averageLenght, entropyH, superfluity, check, lenghtOfText, code_table])


def code_symbol_lenght(code_table):
    sumList = list()
    for key in code_table:
        sumList.append(len(code_table[key]))
    return sum(sumList) / len(sumList)


def calculateEntropyH(alphabetWithFreq):
    entropyH = list()

    for key in alphabetWithFreq:
        probability = alphabetWithFreq[key]
        entropyH.append(probability * log(1 / probability, 2))
    return entropyH


def calculateSuperfluity(entropyH):
    entropyH1 = log(4, 2)
    return 1 - (entropyH / entropyH1)


def checkCraft(code_table):
    checkList = list()
    for key in code_table:
        checkList.append(pow(2, -len(code_table[key])))

    return sum(checkList)