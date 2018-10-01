import threading
global key

# file = open("texto.txt", "r")
# text = file.read()
# print(text)
# file.close()

def indentText(text):    
    text[0] = '\t' + text[0]
    return text

def writeInXLine(text):
    numberLine = int(raw_input("Line: "))
    newLine = raw_input("New line: ")
    text[numberLine] = newLine
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
    print("Q: Ident\tW: Replace in X line\t S: Save")
    for i in range(len(text)):
        print ('['+str(i)+'] ' + text[i])


def manageKeys(key, text):
    # print("The keyy is: %s" %key)
    newText = None
    if(key == 'q'):
        newText = indentText(text)
    if(key == 'w'):
        newText = writeInXLine(text)
    if(key == 's'):
        newText = saveFile(text)

    return newText

def waitForKey(text):    
    thread = threading.currentThread()
    newText = None
    while getattr(thread, "running", True):
        key = raw_input("Key: ")
        if(key == 'p'):
            thread.running = False
        else:
            newText = manageKeys(key, text)
            readText(newText)


def system():
    text = readFile("texto.txt")
    threadKey = threading.Thread(target=waitForKey, args=(text,))
    threadKey.start()

def main():
    system()

if __name__ == "__main__":
    main()