from helpers import alphabet_position, rotate_character

def  encrypt(text, code):
    number = []
    for letter in code:
        number.append(alphabet_position(letter)) # Conver the code/key to numbers that are basically the rotation number being used by the rotat_character() function
    
    text_length = len(text)
    newtext = ""
    code_length = len(code)
    j = 0 # Initiate the j counter for letters
    for i in range(text_length):
        
        if text[i] not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ": # For non alphabet characters, return the orinigal character
            newtext += text[i]
            
        else:
            index =  number[(j % code_length)]  # For alphabet characters, make sure to start from the beginning after going through all letters in the code
            newtext += rotate_character(text[i], index) # Use the function to change characters
            j = j + 1 # Counter goes up by 1 after each conversion of a single letter
    return newtext

def main():
    message = input("Type a message:")
    key = input("Encryption key:")
    print(encrypt(message, key))

if __name__ == "__main__":
    main()  