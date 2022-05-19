
chars =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
shifted_chars=["11","12","13","21","22","23","31","32","33","41","42","43","51","52","53","61","62","63","71","72","73","81","82","83","91","92","93"]
def find_in_list(query, mainlist):
    i=0
    while i<len(mainlist):
        if query==mainlist[i]:
            return i
        i+=1

def encrypt_message(plain_msg):
    encrypted_msg = ""
    for character in plain_msg:
        if character in chars:
            char_index = find_in_list(character, chars)
            new_char = shifted_chars[char_index]
            encrypted_msg = encrypted_msg + new_char
        else:
            encrypted_msg = encrypted_msg + character
    return encrypted_msg

def decrypt_message_multi(message):
    decrypted_msg = ""
    n = 2
    for x in range(len(message)):
        for character in message:
            split_strings = [character[index : index + n] for index in range(0, len(character), n)]
            for character in split_strings:
                if character in shifted_chars:
                    char_index = find_in_list(character, shifted_chars)
                    new_char = chars[char_index]
                    decrypted_msg = decrypted_msg + new_char
                else:
                    decrypted_msg = decrypted_msg + character
            decrypted_msg = decrypted_msg + " "
        return decrypted_msg	
	
flag = True
while flag==True:
    choice = input("What do you want to do? 1. Encrypt a message 2. Decrypt a message \nEnter= ")
    if choice =='e':
        plain_message = input("Enter message to encrypt??")
        print(encrypt_message(plain_message.lower()))
    elif choice =='d':
        encrypted_msg = input("Enter message to decrypt?").split(' ')
        print(decrypt_message_multi(encrypted_msg))
    else:
        play_again = input("Do you want to try agian or Do you want to exit? (Y/N)")
        if play_again == 'Y':
            continue
        elif play_again == 'N':
            break

