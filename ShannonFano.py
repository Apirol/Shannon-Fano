from math import log, pow

def shenon_get_codes(table, value='', codes={}):
    if len(table) != 1:
        a, b = next_vertex(table)
        shenon_get_codes(a, value + '0', codes)
        shenon_get_codes(b, value + '1', codes)
    else:
        codes[table.popitem()[0]] = value
    return codes

def next_vertex(table):
    optimal_difference = sum(table.values())
    optimal_index = 0

    for i in range(len(table)):
        current_difference = abs(sum(list(table.values())[:i]) - sum(list(table.values())[i:]))

        if current_difference < optimal_difference:
            optimal_difference = current_difference
            optimal_index = i
    return dict({item for i, item in enumerate(table.items()) if i < optimal_index}), \
           dict({item for i, item in enumerate(table.items()) if i >= optimal_index})


def getAllInfo(code_table, alphabetWithFreq):
    averageLenght = code_symbol_lenght(code_table)
    entropyH = sum(calculateEntropyH(alphabetWithFreq))
    superfluity = calculateSuperfluity(entropyH)
    check = checkCraft(code_table)
    return list([averageLenght, entropyH, superfluity, check])

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
    try:
        if (sum(checkList) <= 1):
            return "true"
    except:
        Exception("Does not satisfy Kraft's inequality")


def decode_symbol(table, code, index=0):
    if len(table) != 1:
        a, b = next_vertex(table)
        if code[index] == '0':
            return decode_symbol(a, code, index + 1)
        else:
            return decode_symbol(b, code, index + 1)
    else:
        return table.popitem()[0]

def generateSequence(code_table):
    sequence = list()

    for i in range(0, 1000):
        sequence.append()