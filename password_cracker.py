import hashlib

hashed_pw = input("Please provide the hash:\n")
def crack_sha1_hash(hash, use_salts = False):
    with open("top-10000-passwords.txt", "r") as f:
        passwords = f.readlines()

    with open("known-salts.txt", "r") as salt_file:
        salts = salt_file.readlines() 
    
    for password in passwords:
        if hash == hashlib.sha1(password.strip().encode()).hexdigest():
            return password.strip()
  

    return "PASSWORD NOT FOUND IN DATABASE"





key = crack_sha1_hash(hashed_pw, use_salts=True)

print(key)