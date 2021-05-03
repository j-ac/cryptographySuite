#!/bin/python3
import string
import random

def main():
    alphabet = list(string.ascii_uppercase)
    answer = input("Do you want to encrypt or decrypt? (E\D)")

    while not(answer == "E" or answer == "D"):
        answer = input("Do you want to encrypt or decrypt? (E\D)")
    if answer == "E":
        encrypt()
    if answer == "D":
        decrypt()

def encrypt():
    firstWheelOffset = int(input("Enter the offset for the first wheel, numbers divisible by 26 will not encrypt.")) % 26
    secondWheelOffset = int(input("Enter the offset for the second wheel, numbers divisible by 26 will not encrypt.")) % 26
    thirdtWheelOffset = int(input("Enter the offset for the third wheel, numbers divisible by 26 will not encrypt.")) % 26
    fourthWheelOffset = int(input("Enter the offset for the fourth wheel, numbers divisible by 26 will not encrypt.")) % 26

    offsets = [firstWheelOffset, secondWheelOffset, thirdtWheelOffset, fourthWheelOffset]    

    message = input("Enter the message you would like to encrypt.")
    #TODO: Remove spaces from the input
    message = message.upper()
    #TODO: verify string is alphabetical.

    encryptedMessage = ""
    for character in message:
        characterAsInt = (ord(character) - 65) #interptet the character as a number
        wheelNumber = random.randint(0, 3)
        #access the number on a random wheel at the appropriate offset, add to the string.

        #debug help
        print("Wheel: " + str(wheelNumber))
        print("character: " + str(character))
        print("As int: " + str(characterAsInt))
        print("As int with offset: " + str((characterAsInt + (offsets[wheelNumber])) % 26))

        encryptedMessage += str(wheels[wheelNumber][(characterAsInt + (offsets[wheelNumber])) % 26]) + " "
    print("your encrypted message is" + encryptedMessage)
        
def decrypt():
    message = input("Enter the message you would like to decrypt")
    firstWheelOffset = int(input("Enter the offset for the first wheel")) % 26
    secondWheelOffset = int(input("Enter the offset for the second wheel")) % 26
    thirdtWheelOffset = int(input("Enter the offset for the third wheel")) % 26
    fourthWheelOffset = int(input("Enter the offset for the fourth wheel")) % 26
    offsets = [firstWheelOffset, secondWheelOffset, thirdtWheelOffset, fourthWheelOffset]

    decryptedMessage = ""
    #split the message up at the spaces an interpret each integer, matching it to the wheel.
    for symbol in message.split():
        symbol = int(symbol)
        wheel = int(symbol / ALPHABET_SIZE)
        totalOffset = (symbol % ALPHABET_SIZE)
        correctedOffset = totalOffset - offsets[wheel]
        decypheredSymbol = correctedOffset % ALPHABET_SIZE
        decryptedMessage += chr(decypheredSymbol + 65)
        
    print("your decrypted message is: " + decryptedMessage) 

ALPHABET_SIZE = 26
wheels = [
    [i for i in range(0, ALPHABET_SIZE)],
    [i for i in range(ALPHABET_SIZE, ALPHABET_SIZE * 2)],
    [i for i in range((ALPHABET_SIZE * 2), (ALPHABET_SIZE * 3))],
    [i for i in range((ALPHABET_SIZE * 3), (ALPHABET_SIZE * 4))]
]

if __name__ == "__main__":
    main()