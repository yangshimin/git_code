import uuid
import hashlib


def hash_password(password):
    salt = uuid.uuid4().hex
    hash_password = hashlib.md5(salt.encode() + password.encode())
    hash_password = hash_password.hexdigest() + ":" + salt
    return hash_password


def check_password(user_password, hashed_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.md5(salt.encode() + user_password.encode()).hexdigest()


input_password = input('Please input password:')
print('Storing password in thd db...')

old_InputPassword = input('Please input password:')
if check_password(old_InputPassword, hash_password(input_password)):
    print('The password is right!')
else:
    print('The password is WRONG!')
