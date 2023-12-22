
# here we define the main variables of the script, using the Alphabet list as our base to encrypt or decrtypt messages
encrypted_message = []
decrypted_message = []
Alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

Clogo = """      
  ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,
 a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8 
 8b         ,adPPPPP88 8PP'''''''  `"Y8ba,  ,adPPPPP88 88         
 "8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
  `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88               
"""

# we first need user input in order to perform Caesar cipher on any given message
print(Clogo)
mode = input("<< Enter 'encrypt' to encrypt your message or enter 'decrypt' to decrypt it >> \n")
shift = int(input("<< Enter the shift number for the cipher >> \n"))
message = input("<< Enter the message to cipher >> \n")

# this is the main function that applies the Caesar cipher to the user input
def Caesar_c(message, shift, mode):
    if mode == "encrypt":
        for character in message:
            try:
                current_position = Alphabet.index(character)
                new_position = current_position + shift
                # here we check if the position of the character to cipher goes over the maxium number of indexes (26)
                # this way we go back to the beginning of the Alphabet and assign a new character this way
                if new_position > 26:
                   new_position -= 26
                # finally we create the new encrypted message by first using appen () and then creating a string with join ()
                encrypted_message.append(Alphabet[new_position])
                encrypted_message_joined = ''.join(encrypted_message)
            #this is to handle white spaces
            except:
                encrypted_message.append(character)
        print("The encrypted message is: ", encrypted_message_joined)

    elif mode == "decrypt":
        for character in message:
            try:
                # for decrypting we essentially do the opposite of what we did above for encrypting
                current_position = Alphabet.index(character)
                new_position = current_position - shift
                if new_position < 0:
                   new_position += 26
                decrypted_message.append(Alphabet[new_position])
                decrypted_message_joined = ''.join(decrypted_message)
            except:
                 decrypted_message.append(character)
        print("The decoded message is: ", decrypted_message_joined)

    else:
        print("<< Wrong syntax, please enter either 'encrypt' or  'decrypt' >>")
        exit

#we call the function to perform the cipher
Caesar_c(message, shift, mode)
