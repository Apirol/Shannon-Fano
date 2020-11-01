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


def decode_text(text, alphabetWithFreq, code_table):
    encoded_str = ''.join(text)

    index = 0
    decoded_str = ''

    while index < len(encoded_str):
        current = decode_symbol(alphabetWithFreq, encoded_str, index)
        decoded_str += current
        index += len(code_table[current])

    return decoded_str


def decode_symbol(table, code, index=0):
    if len(table) != 1:
        a, b = next_vertex(table)
        if code[index] == '0':
            return decode_symbol(a, code, index + 1)
        else:
            return decode_symbol(b, code, index + 1)
    else:
        return table.popitem()[0]


def encryptText(code_table, text):
    encryptedText = list()
    size = len(text)

    for i in range(0, size):
        encryptedText.append(code_table[text[i]])

    return encryptedText
