# def sort_on(items):
#     return items["num"]

# vehicles = [
#     {"name": "car", "num": 7},
#     {"name": "plane", "num": 10},
#     {"name": "boat", "num": 2}
# ]
# vehicles.sort(reverse=False, key=sort_on)
# print(vehicles)




# def get_book_text():
#      filePath = '/Users/pjackson/Documents/Development/bootDevProjects/bookbot/books/frankenstein.txt'
#      return filePath  
# def counterDef():
#     with open(get_book_text()) as f:
#         fileContents = f.read() 
#     splitText = len(fileContents.split())
#     message = f'Found {splitText} total words'
#     print(message)  
   
# def characterCount():
#     with open(get_book_text()) as f:
#         fileContents = f.read()
    
#     # Convert all text to lowercase
#     lowerCaseText = fileContents.lower()
    
#     # Create a dictionary to store character counts
#     char_count = {}
    
#     # Count each character
#     def charCount():
#         for char in lowerCaseText:
#             if char in char_count:
#                 char_count[char] += 1
#             else:
#                 char_count[char] = 1
        
#     # Print the dictionary with character counts
        
#     #     charSort = [char_count]
#     #     charSort.sort(reverse=True, key=char_count)
#     #     print(charSort)
#     def charResult():
#         print("Character counts:")
#     #calls two elements in a for loop to print two values in the print statement
#         for chartSort, count in char_count.items():
#             charSort = [char_count]
#             chartSort = charSort.sort(reverse=True, key=charCount())
#             print(f"char'{chartSort}': num : {count}")
        
#     # for counter, count in char_count.items():
        
#     #     print(f"'{counter}': {count}")
        
    
    
    

# characterCount()

import sys

print(f"Script name: {sys.argv[0]}")
if len(sys.argv) > 1:
    print(f"First argument: {sys.argv[1]}")
    print(f"All arguments (excluding script name): {sys.argv[1:]}")
else:
    print("No arguments passed.")
