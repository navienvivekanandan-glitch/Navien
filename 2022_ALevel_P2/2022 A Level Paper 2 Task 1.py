#2022 A Level Paper 2

#Task 1

#Task 1.1

def encrypt(character):
    if character.isdigit() == False and character.isalpha() == False and character != ' ':
        return -1
    
    else:
        
        if character == ' ':
            return '!'
        
        value = ord(character) + 10

        if character.isupper() == True:
            if value > 97:
                value = value - 26
        else:
            if value > 122:
                value = value - 26

        return chr(value)

#Task 1.2
print(encrypt('A'))
print(encrypt('a'))
print(encrypt('#'))
print(encrypt(' '))


#Task 1.3

file = open('DATATOENCRYPT.txt','r')
encrypted_string = ''
for line in file:
    line = line.strip()
    for i in range(len(line)):
        if encrypt(line[i]) != -1:
            encrypted_string = encrypted_string + encrypt(line[i])

file.close()

print(encrypted_string)
file = open('ENCRYPTEDMESSAGE','w')
file.write(encrypted_string + '\n')
file.close()


