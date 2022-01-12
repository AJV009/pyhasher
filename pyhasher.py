import uuid
import hashlib
 
def hash_secret(secret):
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + secret.encode()).hexdigest() + ':' + salt
    
def check_secret(hashed_secret, user_secret):
    secret, salt = hashed_secret.split(':')
    return secret == hashlib.sha256(salt.encode() + user_secret.encode()).hexdigest()
 
new_sec = input('Please enter a secret: ')
hashed_secret = hash_secret(new_sec)
print('The string to store in the db is: ' + hashed_secret)
old_sec = input('Now please enter the secret again to check: ')
if check_secret(hashed_secret, old_sec):
    print('You entered the right secret')
else:
    print('I am sorry but the secret does not match')