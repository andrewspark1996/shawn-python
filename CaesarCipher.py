#Caesar Cipher
#This makes sure that it stays in 1-52.
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
MAX_KEY_SIZE = len(SYMBOLS)
#This lets the player choose if they want to encrypt or decrypt the message.
def getMode():
    while True:
        print('Do you wish to encrypt or decrypt a message?')
        #This actually lets them choose, so it lets them type their choice.
        mode = input().lower()
        if mode in ['encrypt', 'e', 'decrypt', 'd']:
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d".')
#This is where it says 'Enter Your Message'. So it teams up with the lines of code above to complete their mission.
def getMessage():
    print('Enter your message:')
    return input()
#This lets you type in a message whether you are encrypting a message or decrypting it.
def getKey():
    key = 0
    while True:
        print('Enter the key number (1-%s)' % (MAX_KEY_SIZE))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key
#This is one of the most important parts. This is what actually does the encrypting and decrypting.
def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''
#This for loop iterates on each character in the message string above.
    for symbol in message:
        symbolIndex = SYMBOLS.find(symbol)
        if symbolIndex == -1:
            translated += symbol
        else:
            #This encrypts or decrypts each letter to get your final answer.
            symbolIndex += key
            #The fore loop above excutes here when the loop is finished it will hit return translated after all of the destinations.
            if symbolIndex >= len(SYMBOLS):
                symbolIndex -+ len(SYMBOLS)
            elif symbolIndex < 0:
                symbolIndex += len(SYMBOLS)
                
            translated += SYMBOLS[symbolIndex]
    #This simply returns the translated string that was decrypted or encrypted.
    return translated

mode = getMode()
message = getMessage()
key = getKey()
print('Your translated text is:')
print(getTranslatedMessage(mode, message, key))
