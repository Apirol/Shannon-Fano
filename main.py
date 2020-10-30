from InputHandler import openFileAndReadData, openFileAndReadNumber
from OutputHandler import writeDataToFile, Report
from collections import Counter
import numpy as np
from ShannonFano import shenon_get_codes, getAllInfo, decode_symbol

if __name__ == '__main__':
        alphabet = openFileAndReadData("Data/Alphabet.txt")
        frequrency = list(openFileAndReadNumber("Data/Frequency0.txt"))

        alphabetWithFreq = dict()
        for i in range(len(frequrency)):
                alphabetWithFreq.update({alphabet[i]: frequrency[i]})
        countForEachSymbol = Counter(alphabet)


        code_table = shenon_get_codes(alphabetWithFreq)
        writeDataToFile(code_table, "Data/encryptText.txt")
        info = getAllInfo(code_table, alphabetWithFreq)
        Report("Data/Report.txt", info)

        print(alphabetWithFreq)
        for symbol, key in sorted(code_table.items(), key=lambda item: len(item[1])):
            print(symbol, key, sep=': ')

        encoded = [code_table[letter] for letter in alphabet]
        encoded_bits = ''.join(encoded)
        encoded_str = [chr(int(encoded_bits[i:i + 8], 2)) for i in range(0, len(encoded_bits), 8)]

        print('исходная строка ({} bits): '.format(len(alphabet) * 8), alphabet)
        print('сжатая строка ({} bits): '.format(len(encoded_str) * 8), ''.join(encoded_str))
        print('данные: {}'.format(encoded_bits))

        index = 0
        decoded_str = ''

        while index < len(encoded_bits):
            current = decode_symbol(alphabetWithFreq, encoded_bits, index)  # расшифровать очередной символ
            decoded_str += current  # добавить его в результат
            index += len(code_table[current])  # перейти на следующий

        print('расшифрованная строка: ', decoded_str)


