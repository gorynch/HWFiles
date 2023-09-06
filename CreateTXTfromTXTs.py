import os

filePath = "files/"
outputFile = "outText.txt"
def fileList(files):
    return [el for el in os.listdir(path=files) if el.endswith(
    'txt') and el != outputFile]


def fileRead(fileName):
    with open(fileName, 'r', encoding='utf-8') as myFile:
        fileData = myFile.read()
    return fileData
def dictFromFiles(listFiles):
    myDictLen = {}
    myDictData = {}
    for el in listFiles:
        filePath = os.path.join('files', el)
        with open(filePath, 'r', encoding='utf-8') as fileSource:
            fileData = fileSource.read().splitlines()
            myDictLen[str(el)] = len(fileData)
            myDictData[str(el)] = '\n'.join(fileData)
#            myDict[str(el+"DATA")] = '\n'.join(fileData) didn't find how to
    #            sort dictionary like { "fileLEN" : "StringCount", "fileDATA"
    #            : "strings from file" } by value stringCount, so have to
    #            using 2 dictionaries
    return myDictLen, myDictData
def sortANDwrite2newFile(filePath, file2write):
    dictData = dictFromFiles(fileList(filePath))[1]
    sortedDict = dict(sorted(dictFromFiles(fileList(filePath))[0].items(),
                             key=lambda item: item[1]))
    with open(filePath + file2write, 'w', encoding='utf-8') as file:
        for el in sortedDict:
            newLine = "\n"
            text2file = (f"Имя файла: {el}{newLine}Количество строк: "
                         f"{sortedDict[el]}{newLine}{dictData[el]}")
            file.write(text2file)

if __name__ == '__main__':
    print("let's start!")
    print()
    sortANDwrite2newFile(filePath, outputFile)
    print(f"Done. Check {outputFile}")