from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    newtext = ''
    for char in text:
        newtext += rotate_character(char, rot)
    return newtext

def main():
    message = input("Type a message:")
    rotate_number = int(input("Rotate by:"))
    print(encrypt(message, rotate_number))

if __name__ == "__main__":
    main()
