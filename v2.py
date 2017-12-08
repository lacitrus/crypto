def alphabet_position(letter):
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if letter in alphabet:
        for i in range(len(alphabet)):
            if letter == alphabet[i]:
                return i
    else:
        for i in range(len(alphabet2)):
            if letter == alphabet2[i]:
                return i

def rotate_character(char, rot):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    if char in alphabet:
        index = (alphabet_position(char) + rot ) % 26
        return alphabet[index]
    elif char in alphabet2:
        index2 = (alphabet_position(char) + rot ) % 26
        return alphabet2[index2]
    else:
        return char

def  encrypt(text, code):
    number = []
    for letter in code:
        number.append(alphabet_position(letter)) # Conver the code/key to numbers that are basically the rotation number being used by the rotat_character() function
    
    text_length = len(text)
    newtext = ""
    code_length = len(code)
    
    for i in range(text_length):
        if text[i] not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            newtext += text[i]
            
        else:
            index =  number[(i % code_length)] 
            newtext += rotate_character(text[i], index)
           
    return newtext

def main():
    message = input("Type a message:")
    key = input("Encryption key:")
    print(encrypt(message, key))

if __name__ == "__main__":
    main()  