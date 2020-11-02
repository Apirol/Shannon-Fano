def Report(filename, info):
    format = list(["Средняя длина слова: ", "Энтропия: ", "Избыточность: ",
                   "Неравенство Крафта: ", "Длина текста", "Кодовые слова: "])
    size = len(format)

    handle = open(filename, 'w', encoding='utf-8')


    for i in range(0, size):
        handle.write(format[i] + str(info[i]) + "\n")

def writeDataToFile(text, fileName):
    handle = open(fileName, 'w', encoding='utf-8')
    handle.write(''.join(text) + "\n")
    handle.close()
