import threading


def indentText(text):        
    text[0] = '\t' + text[0]
    return text

def writeInXLine(text):
    numberLine = int(raw_input("Line: "))
    newLine = raw_input("New line: ")
    text[numberLine] = newLine
    return text

def deleteXLine(text):
    numberLine = int(raw_input("Number line to delete: "))
    del text[numberLine]
    return text

def saveFile(text):
    fileName = raw_input("Filaname: ")
    file = open(fileName, 'w')
    file.writelines(text)
    file.close()
    return text

def readFile(name):
    file = open(name, "r+")
    lines = file.readlines()    
    
    readText(lines)
    file.close()
    return lines

def readText(text):
    for i in range(len(text)):
        print ('['+str(i)+'] ' + text[i])
    print("Q: Ident\tW: Replace in X line\tD: Delete line\tS: Save\t P: Exit")


def manageKeys(key, text):
    # print("The keyy is: %s" %key)
    newText = None
    if(key == 'Q'):
        newText = indentText(text)
    if(key == 'W'):
        newText = writeInXLine(text)
    if(key == 'D'):
        newText = deleteXLine(text)
    if(key == 'S'):
        newText = saveFile(text)

    return newText

def waitForKey(text):    
    thread = threading.currentThread()
    newText = None
    while getattr(thread, "running", True):
        key = raw_input("Key: ").capitalize()
        if(key == 'P'):
            thread.running = False
        else:
            newText = manageKeys(key, text)
            readText(newText)


def system():
    newFile = raw_input("Filename + extension: ")
    text = readFile(newFile)
    threadKey = threading.Thread(target=waitForKey, args=(text,))
    threadKey.start()

def main():
    system()

if __name__ == "__main__":
    main()