#Paige Neff

menu = '''Menu
-------------
1. Encode
2. Decode
3. Quit'''

def encode(password):
    newpassword = ''
    for num in password:
        newpassword += str(int(num) + 3)
    return newpassword

def decode(password):
    newpassword = ''
    for num in password:
        newpassword += str(int(num) - 3)
    return newpassword

if __name__ == '__main__':
    while True:
        print(menu)
        option = int(input('Please enter an option: '))
        if option == 1:
            password = input('Please enter your password to encode: ')
            encoded = encode(password)
            print('Your password has been encoded and stored!')
        if option == 2:
            print("Encoded password:", decode(password))
