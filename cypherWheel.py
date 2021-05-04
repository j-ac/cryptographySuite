#!/bin/python3
import string
import random
import argparse

def main():
    parser = argparse.ArgumentParser()
    action = parser.add_mutually_exclusive_group(required=True) #make encrypting and decrypting mutually exclusive operations.
    action.add_argument("--encrypt", "-e", help="encrypts the message string", action="store_true")
    action.add_argument("--decrypt", "-d", help="decrypts the message string", action="store_true")

    parser.add_argument("--characterset", default="ascii", choices=["ascii", "japanese", "greek"], required=False)

    parser.add_argument("WHEELS", nargs=4, type=int, metavar='N', help="integer position for the wheels in the cypher. Numbers divisible by 26 will not encrypt well")
    parser.add_argument("MESSAGE", help="the message you want to encrypt or decrypt.")
    args = parser.parse_args()
    
    if(args.decrypt):
        decrypt(args.MESSAGE, args.WHEELS, args.characterset)
    else:
        encrypt(args.MESSAGE, args.WHEELS, args.characterset)

    
def encrypt(message, offsets, characterSetName):
    if characterSetName == "ascii":
        characterSet = symbolArrayAscii
    elif characterSetName == "japanese":
        characterSet = symbolArrayJp
    elif characterSetName == "greek":
        characterSet = symbolArrayGr
    else:
        print("Problem in decrypt function, invalid character set encountered: " + characterSet)
        quit()

    for i in range(len(offsets)):
        offsets[i] = offsets[i] % ALPHABET_SIZE  

    message = message.replace(" ", "")
    message = message.upper()
    #TODO: verify string is alphabetical.

    encryptedMessage = ""
    encryptedMessageInCharacterSet = ""
    for character in message:
        characterAsInt = (ord(character) - 65) #interptet the character as a number
        wheelNumber = random.randint(0, 3)
        #encryptedMessage += str(wheels[wheelNumber][(characterAsInt + (offsets[wheelNumber])) % 26]) + " " #prints a numerical representation (insecure)
        encryptedMessageInCharacterSet += characterSet[ALPHABET_SIZE * wheelNumber + (characterAsInt + (offsets[wheelNumber])) % 26] + " "

    print(encryptedMessageInCharacterSet)
        
def decrypt(message, offsets, characterSetName):
    if characterSetName == "ascii":
        characterSet = symbolArrayAscii
    elif characterSetName == "japanese":
        characterSet = symbolArrayJp
    elif characterSetName == "greek":
        characterSet = symbolArrayGr
    else:
        print("Problem in decrypt function, invalid character set encountered: " + characterSet)
        quit()

    for i in range(len(offsets)):
        offsets[i] = offsets[i] % ALPHABET_SIZE

    decryptedMessage = ""
    #split the message up at the spaces an interpret each integer, matching it to the wheel.
    for symbol in message.split():
        symbolIndex = characterSet.index(symbol)
        wheel = int(symbolIndex / ALPHABET_SIZE)
        totalOffset = (symbolIndex % ALPHABET_SIZE)
        correctedOffset = totalOffset - offsets[wheel]
        decypheredSymbol = correctedOffset % ALPHABET_SIZE
        decryptedMessage += chr(decypheredSymbol + 65)

    print(decryptedMessage) 

symbolArray = []
symbolArrayAscii = ['s', '∩', '∞', 'Q', 'V', 'y', '└', '@', 'x', '≤', 'j', 'â', 'v', '1', '&', 'G', 'N', 'ê', '≡', '⌠', '^', 'e', 'o', '4', 'é', 'a', 'J', '_', 'd', 'å', 'D', 'Φ', 'l', '¬', '\\', '/', 'C', '0', 'Z', 'b', 'ä', 'r', ']', 'f', '(', 'i', 'Y', '7', 'm', '2', 'W', '⌡', 'B', 'h', 'H', 'g', '+', '≥', 'P', 'w', 'ü', '[', 'u', 'X', '-', '~', 'S', '$', '±', '3', 'U', 'q', '5', 'R', 'à', 'E', '9', 'c', 'I', '%', '*', 'M', 'µ', 'τ', '8', 's', 'L', 'z', 'Ç', 'k', '#', 'T', 'O', 'p', 'ç', ')', '!', '6', 't', 'K', 'n', 'A', 'F', 'Ω']
#note: some greek characters are missing, simply need to find a different character to replace each broken one.
symbolArrayGr = ['Λ', 'Δ', 'ꭕ', '︎', 'Φ', 'ὰ', '♌', '♑', '♊', 'σ', 'Υ', 'ζ', '►', '︎', 'δ', 'ὺ', '♍', 'χ', 'Σ', 'φ', 'ά', 'ε', '♋', 'ꭃ', '︎', '︎', 'Η', 'Π', '︎', '︎', 'Α', 'Χ', 'γ', 'α', '♈', 'Ρ', 'ῶ', 'Γ', 'θ', '︎', '︎', 'Ψ', 'ξ', 'ἐ', 'ο', 'ψ', 'Ξ', 'Ζ', 'β', 'Ν', 'ꬻ', 'ὸ', '♎', 'Ι', 'ꭖ', 'ꭂ', 'ν', 'ω', 'Ὧ', '♊', 'κ', 'ꭍ', 'ꭀ', 'ὁ', 'ρ', '︎', 'λ', 'μ', 'η', '♏', 'ῼ', '︎', '♓', 'Ο', 'Ᾰ', 'Ὃ', 'ꭄ', 'ꭔ', 'Ε', 'Μ', 'ὴ', '⑅', 'Β', 'Κ', 'ꭁ', '︎', 'ᾳ', '⫷', '︎', 'ꬷ', '⫸', 'ὲ', '♐', 'Ω', '♒', 'Ἔ', 'τ', 'έ', 'υ', 'ι', 'ῐ', 'π', 'Τ', 'Θ']
symbolArrayJp = ['ヤ', 'む', 'よ', 'ユ', 'ナ', 'ヲ', 'カ', 'ぬ', 'た', 'ス', 'ぎ', '五', 'マ', 'で', 'く', '円', 'ど', 'レ', 'み', 'ろ', 'モ', 'ま', 'ノ', 'が', 'う', 'れ', 'り', 'ミ', 'ソ', 'ぞ', 'あ', 'ぴ', 'タ', 'ム', 'し', 'を', 'チ', 'ゆ', 'め', 'え', 'ク', 'ハ', 'ウ', 'ず', 'さ', 'つ', 'け', 'す', '天', 'サ', 'も', 'メ', 'へ', 'ち', 'て', 'こ', 'な', 'ワ', 'ツ', 'コ', 'ラ', 'や', 'い', 'シ', '心', '山', 'ホ', '女', 'ほ', 'び', 'ヌ', 'オ', 'る', 'わ', 'ト', 'ぷ', 'そ', 'ぐ', 'テ', 'に', 'お', 'ネ', 'セ', 'せ', 'じ', 'ケ', 'ね', 'フ', 'ふ', 'は', 'か', 'リ', 'き', 'の', 'ら', 'と', '小', 'ひ', '田', 'キ', 'ヒ', 'ぺ', 'だ', 'ル']

ALPHABET_SIZE = 26
wheels = [
    [i for i in range(0, ALPHABET_SIZE)],
    [i for i in range(ALPHABET_SIZE, ALPHABET_SIZE * 2)],
    [i for i in range((ALPHABET_SIZE * 2), (ALPHABET_SIZE * 3))],
    [i for i in range((ALPHABET_SIZE * 3), (ALPHABET_SIZE * 4))]
]

if __name__ == "__main__":
    main()