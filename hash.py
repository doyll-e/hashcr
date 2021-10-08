import os,sys,platform
import hashlib 
from colorama import Fore

def clear():
    if platform.uname()[0] == "Linux" :
        os.system("clear")
    else:
        os.system("cls")
def hashcracker():
    # if platform.uname()[0] == "Linux" :
    #     os.system("clear")
    # else:
    #     os.system("cls")
    clear()
    print('''
    ████████▄   ▄██████▄  ▄██   ▄            ▄█        ▄█          ▄████████ 
    ███   ▀███ ███    ███ ███   ██▄          ███       ███         ███    ███ 
    ███    ███ ███    ███ ███▄▄▄███          ███       ███         ███    █▀  
    ███    ███ ███    ███ ▀▀▀▀▀▀███          ███       ███        ▄███▄▄▄     
    ███    ███ ███    ███ ▄██   ███          ███       ███       ▀▀███▀▀▀     
    ███    ███ ███    ███ ███   ███          ███       ███         ███    █▄  
    ███   ▄███ ███    ███ ███   ███          ███▌    ▄ ███▌    ▄   ███    ███ 
    ████████▀   ▀██████▀   ▀█████▀ _________ █████▄▄██ █████▄▄██   ██████████ 
                                             ▀         ▀                      
    ''')   
    try:
        from colorama import Fore
    except:
        os.system("pip install colorama")
    from platform import platform
    #banner design
    # def baner():
    #     plat = platform()
    #     if "Windows" in plat:
    #         os.system("cls")
    #     else:
    #         os.system("clear")

    #try to get hash type 
    try:
        
        print(Fore.MAGENTA + "Select Your Hash Type: ")
        print(Fore.GREEN + """
{1}md5
{2}sha1
{3}sha224
{4}sha256
{5}sha384
{6}sha512
+++ Other Hashes Unsuported +++
        """)
        hashtype = int(input(Fore.CYAN  + "Enter Your HashType -- (example 1 / 2 / 3) : ")) 
        while hashtype >= 7:
            print(Fore.RED + "Just Select 1-6 . !!! Try Again :)) ")
            hashtype = int(input(Fore.CYAN  + "Enter Your HashType -- (example 1 / 2 / 3) : "))    
    except:
        print(Fore.RED + "Just Select 1-6 . !!! Bye :) ")
        sys.exit()

    #get hash
    hash = input(Fore.LIGHTMAGENTA_EX+ "Enter Your Hash: ... ")


    passlist = input(Fore.LIGHTGREEN_EX + "Enter Your WordList Addres : Example D:\password.txt:...")
    try:
        file = open(passlist,"r").readlines()
    except:
        print(Fore.RED+ "i Cant find this wordlist... :{{ ")
        sys.exit()


    #cracking hash by wordlist!!!

    if hashtype == 1:
        for i in file:
            i = i.strip()
            md5 = hashlib.md5()
            md5.update(i.encode())
            End = md5.hexdigest()
            print(Fore.LIGHTCYAN_EX +  "checking {u} hash... ++ ".format(u=i))
            if End == hash:
                print(Fore.GREEN + "your hash has been cracked... :)) password is : {a}".format(a=i))
                break
    if hashtype == 2:
        for i in file:
            i = i.strip()
            sha_1 = hashlib.sha1()
            sha_1.update(i.encode())
            End = sha_1.hexdigest()
            print(Fore.LIGHTCYAN_EX +  "checking {u} hash... ++ ".format(u=i))
            if End == hash:
                print(Fore.GREEN + "your hash has been cracked... :)) password is : {a}".format(a=i))
                break
    if hashtype == 3:
        for i in file:
            i = i.strip()
            sha_224 = hashlib.sha224()
            sha_224.update(i.encode())
            End = sha_224.hexdigest()
            print(Fore.LIGHTCYAN_EX +  "checking {u} hash... ++ ".format(u=i))
            if End == hash:
                print(Fore.GREEN + "your hash has been cracked... :)) password is : {a}".format(a=i))
                break
    if hashtype == 4:
        for i in file:
            i = i.strip()
            sha_256 = hashlib.sha256()
            sha_256.update(i.encode())
            End = sha_256.hexdigest()
            print(Fore.LIGHTCYAN_EX +  "checking {u} hash... ++ ".format(u=i))
            if End == hash:
                print(Fore.GREEN + "your hash has been cracked... :)) password is : {a}".format(a=i))
                break
    if hashtype == 5:
        for i in file:
            i = i.strip()
            sha_384 = hashlib.sha384()
            sha_384.update(i.encode())
            End = sha_384.hexdigest()
            print(Fore.LIGHTCYAN_EX +  "checking {u} hash... ++ ".format(u=i))
            if End == hash:
                print(Fore.GREEN + "your hash has been cracked... :)) password is : {a}".format(a=i))
                break
    if hashtype == 6:
        for i in file:
            i = i.strip()
            sha_512 = hashlib.sha512()
            sha_512.update(i.encode())
            End = sha_512.hexdigest()
            print(Fore.LIGHTCYAN_EX +  "checking {u} hash... ++ ".format(u=i))
            if End == hash:
                print(Fore.GREEN + "your hash has been cracked... :)) password is : {a}".format(a=i))
                break
    
    print(Fore.LIGHTRED_EX + "Good loock :) see you later :} ")
    print( Fore.WHITE +  " ")

hashcracker()