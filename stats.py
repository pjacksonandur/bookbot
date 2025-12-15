def get_book_text():
     filePath = '/Users/pjackson/Documents/Development/bootDevProjects/bookbot/books/frankenstein.txt'
     return filePath  
# def counterDef():
#     with open(get_book_text()) as f:
#         fileContents = f.read() 
#     splitText = len(fileContents.split())
#     message = f'Found {splitText} total words'
#     print(message)  
   
def characterCount():
    with open(get_book_text()) as f:
        fileContents = f.read()
    splitText = fileContents.split()
    lowerCaseWords = str(splitText).lower()
    charSplit = lowerCaseWords
    charMove = [char for char in charSplit]
    print(charMove)
    #print(lowerCaseWords)
    # splitDictLetters = {}
    # print(splitDictLetters)
    
#     for letters in splitDict():
#         splitDict[letters] = locals(splitDict)
#         return splitDict()

    
characterCount()    