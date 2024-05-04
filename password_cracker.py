import hashlib

hashed_pw = input("Please provide the hash or press \"q\" to quit:\n")

def crack_sha1_hash(hash, use_salts = False):
    with open("top-10000-passwords.txt", "r") as f:
        passwords = [password.strip() for password in f.readlines()]

    with open("known-salts.txt", "r") as salt_file:
        salts = [salt.strip() for salt in salt_file.readlines()]
    
    
    if use_salts:
        for password in passwords:
            for salt in salts:
                for salted_password in [salt + password, password + salt]:
                    hashed_pw = hashlib.sha1(salted_password.encode()).hexdigest()
                    if hash == hashed_pw:
                        return password
    else:
        for password in passwords:
            if hash == hashlib.sha1(password.strip().encode()).hexdigest():
                return password.strip()
  

    return "PASSWORD NOT IN DATABASE"

multiple_attempts = ''

while multiple_attempts != "q":
    use_salts = input("Would you like to check for the salted version? Press \"y\" or \"n\".\n")

    if use_salts == "y":
        key = crack_sha1_hash(hashed_pw, use_salts=True)
        print(f"Here is the password: {key}")
    elif use_salts == "n":
        key = crack_sha1_hash(hashed_pw)
        print(f"Here is the password: {key}")
    
    multiple_attempts = input("Please provide the hash or press \"q\" to quit:\n")

    if multiple_attempts == "q":
        print("See you next time!")















