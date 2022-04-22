######################################
# File encrypter using Python        #
# Made by Imira Randeniya            #
######################################

from cryptography.fernet import Fernet
import os
import argparse

files = []

my_parser = argparse.ArgumentParser()
my_parser.add_argument('--encrypt', '-e', type=str, help="file name to encrypt", required=False, default='')
my_parser.add_argument('--decrypt', '-d', type=str, help="file name to decrypt", required=False, default='')
args = my_parser.parse_args()



def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("key.key", "rb").read()

def encrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read all file data
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
        # write the encrypted file
    with open(filename, "wb") as file:
        file.write(encrypted_data)

def decrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write the original file
    with open(filename, "wb") as file:
        file.write(decrypted_data)

def main():
    print('Hello welcome to the file encrypter/decrypter.')
    print('Do you want to [1] Encrypt or [2] Decrypt ?')
    option = input('Enter option number: ')
    if int(option) == 1:

        print('Do you want to encrypt [1] Single File [2] Multiple Files')
        option = input('Enter option number: ')
        if int(option) == 1:
            file = input('Enter file path: ')
            if os.path.isfile(file):
                pass
            else:
                exit()
            
            if os.path.isfile('key.key'):
                key = load_key()
                encrypt(file, key)
                print('[+] Done')
            else:
                write_key()
                key = load_key()
                encrypt(file, key)
                print('[+] Done')
        else:
            no_of_files = int(input('Enter number of files: '))
            for x in range(1, (no_of_files + 1)):
                file_name = input(f'Enter file name({x}): ')
                files.append(file_name)
            for file in files:

                if os.path.isfile(file):
                    pass
                else:
                    print(f'[-] File {file} does not exist')
                    continue
                
                if os.path.isfile('key.key'):
                    key = load_key()
                    encrypt(file, key)
                    print('[+] Done')
                else:
                    write_key()
                    key = load_key()
                    encrypt(file, key)
                    print('[+] Done')

    elif int(option) == 2:

        print('Do you want to decrypt [1] Single File or [2] Multiple Files')
        option = int(input('Enter option number: '))
        if option == 1:
            file = input('Enter file path: ')
            if os.path.isfile(file):
                pass
            else:
                exit()

            if os.path.isfile('key.key'):
                key = load_key()
                decrypt(file, key)
                print('[+] Done')
            else:
                print('[-] Can\'t locate key file.')
        else:
            no_of_files = int(input('Enter number of files: '))
            for x in range(1, (no_of_files + 1)):
                file_name = input(f'Enter file name({x}): ')
                files.append(file_name)
            for file in files:
                if os.path.isfile(file):
                    pass
                else:
                    print(f'[-] File {file} does not exist')
                    continue
                    
                if os.path.isfile('key.key'):
                    key = load_key()
                    decrypt(file, key)
                    print('[+] Done')
                else:
                    print('[-] Can\'t locate key file.')


if args.encrypt != '':
    if os.path.isfile(args.encrypt):
        pass
    else:
        exit()
            
    if os.path.isfile('key.key'):
        key = load_key()
        encrypt(args.encrypt, key)
        print('[+] Done')
        exit()
    else:
        write_key()
        key = load_key()
        encrypt(args.encrypt, key)
        print('[+] Done')
        exit()

if args.decrypt != '':
    if os.path.isfile(args.decrypt):
        pass
    else:
        exit()

    if os.path.isfile('key.key'):
        key = load_key()
        decrypt(args.decrypt, key)
        print('[+] Done')
        exit()
    else:
        print('[-] Can\'t locate key file.')
        exit()

main()
