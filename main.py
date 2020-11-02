from InputHandler import openFileAndReadData, openFileAndReadNumber, makeFrequrencyAlphabet
from OutputHandler import writeDataToFile, Report
from collections import Counter
from Info import getAllInfo
from ShannonFano import shenon_get_codes, decode_text, encryptText

if __name__ == '__main__':
        alphabet = openFileAndReadData("Data/Alphabet.txt")
        frequrency = list(openFileAndReadNumber("Data/FrequencyP1.txt"))
        textToEncrypt = openFileAndReadData("Data/Text.txt")
        alphabetWithFreq = makeFrequrencyAlphabet(alphabet, frequrency)

        code_table = shenon_get_codes(alphabetWithFreq)
        encryptedText = encryptText(code_table, textToEncrypt)
        writeDataToFile(encryptedText, "Data/encryptedText.txt")
        info = getAllInfo(code_table, alphabetWithFreq, encryptedText)
        Report("Data/Report.txt", info)

        decoded_text = decode_text(encryptedText, alphabetWithFreq, code_table)
        writeDataToFile(decoded_text, "Data/decryptedText.txt")
