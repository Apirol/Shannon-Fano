def Report(filename, info):
    format = list(["Энтропия", "Избыточность", "Средняя длина слова", "Неравенство Крафта"])
    size = len(format)

    handle = open(filename, 'w', encoding='utf-8')
    for i in range(0, size):
        handle.write("".join(format[i]) + " " + ' '.join(map(str, info[i])) + "\n")

def writeDataToFile(text, fileName):
    handle = open(fileName, 'w', encoding='utf-8')
    handle.write(''.join(text) + "\n")
    handle.close()
