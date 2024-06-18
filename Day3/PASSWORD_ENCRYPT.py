from cryptography.fernet import Fernet
'''
def generate_pass():
    key = Fernet.generate_key()
    with open('key.txt','wb') as f:
        f.write(key)
generate_pass()
'''

def load_key():
    with open('key.txt','rb') as f:
        key = f.read()
    return key
key = load_key()
fer = Fernet(key)


choice = input("Do you want to view your passwords or add a new password (view/add) or press q to quit  ").lower()

if(choice=='q'):
    quit()
def view():
    with open('password.txt','r') as f:
        for line in f.readlines():
            name,passw = line.split("|")
            print("Name : " + name)
            print("Password : " + fer.decrypt(passw.encode()).decode())
def add():
    name = input("Enter the username :  ")
    passw = input("Enter the password :  ")
    passwe = fer.encrypt(passw.encode()).decode() + "\n"
    with open('password.txt','a') as f:
        f.write(f'{name}|{passwe}')
if(choice=='view'):
    view()
if(choice=='add'):
    add()

