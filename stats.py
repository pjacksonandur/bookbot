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
    
    # Convert all text to lowercase
    lowerCaseText = fileContents.lower()
    
    # Create a dictionary to store character counts
    char_count = {}
    
    # Count each character
    for char in lowerCaseText:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Print the dictionary with character counts
    print("Character counts:")
    for counter, count in char_count.items():
        print(f"'{counter}': {count}")
    
    # Alternatively, print the entire dictionary
    print("\nComplete dictionary:")
    

characterCount()
