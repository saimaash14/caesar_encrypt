#Saima Ashrafi, sashr, CS111, this code encrypts and decrypts words for the user


#encrypts words based on user message and user key
def caesar_encrypt(message, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encrypted_message = ""
    for ch in message:
        if ch.upper() in alphabet:
            if ch.islower():
                ch = ch.upper()
                ch_index = alphabet.find(ch)
                letter = alphabet[(ch_index + key)%26] #loops around the alphabet
                letter = letter.lower()
                encrypted_message += letter
            else:
                ch_index = alphabet.find(ch)
                letter = alphabet[(ch_index + key)%26] #loops around the alphabet
                encrypted_message += letter
        else:
            encrypted_message += ch
    return encrypted_message

#cleans list of words
def clean(list_of_words):
    for i in range(len(list_of_words)):
        list_of_words[i] = list_of_words[i].strip()

#finds the percentage of words in message in list of words
def percentage_finder(message , list_of_words):
    message = message.split()
    count = 0
    for word in message:
        if word.lower() in list_of_words: 
            count += 1 #counts words in message in list of words
    percent = (count/len(message))*100
    return percent

#stores percentages and keys in a dictionary and then it finds the max percentage and returns the corresponding key and message
def caesar_cracker(message, filename):
    keys_percents = {} #dictionary to store percents and keys
    file = open(filename)
    list_of_words = file.readlines()
    clean(list_of_words)
    for i in range(1,26): #loops through every key and tests it out
        decrypted_message = caesar_encrypt(message, i)
        percentage_correct = percentage_finder(decrypted_message, list_of_words)
        keys_percents[percentage_correct] = i
    max_percentage = max(keys_percents.keys()) #finds max percentage
    encrypted_key = 26 - keys_percents[max_percentage] #subtracts the key from 26 to get the original key it was encrypted with
    decrypted_max = caesar_encrypt(message, keys_percents[max_percentage]) #assigns the word from the max percentage to variable
    return encrypted_key, decrypted_max




if __name__ == "__main__":
    print("Welcome to the Cipher App")
    print("---------------------------------------------")
    print("This app can help you with one of the following - ")
    print("(A) Encrypt a message with the Caesar Cipher")
    print("(B) Crack a message")
    choice = input("Which would you like to do ?: ")
    
    if(choice== "A"):
        print(f'Your choice is {choice}')
        print(f'You have chosen to Caesar Encrypt !')
        message = input('Enter your message to be encrypted: ')
        key = int(input("Enter the key (one digit number) to be used for the encryption: "))
        user_secret_message = caesar_encrypt(message, key) #encrypts user message based on key
        print(f'Your Secret Message is: {user_secret_message}')
    elif choice == "B":
        print(f'Your choice is {choice}')
        print(f'You have chosen to decrypt !')
        print(f'You have chosen Caesar Cracking !')
        message = input('Enter your message to be decrypted: ')
        filename = input('Enter the name of the file to be used to crack the code: ')
        encrypted_key, decrypted_max = caesar_cracker(message, filename) #returns the key and message based on max percentage and assign it to variables
        print(f'Your Secret Message is: {decrypted_max}')
        print(f'The key used to encrypt your message was {encrypted_key}')
    print("GoodBye!")