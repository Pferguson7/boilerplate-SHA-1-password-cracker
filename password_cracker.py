import hashlib


hashed_pw = input("Please provide the hash:\n")
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
  

    return "PASSWORD NOT FOUND IN DATABASE"


user_answer = input("Would you like to check for the salt version ?\nPlease type \"yes\" or \"no\" or press \"q\" to quit! \n")

if user_answer == "yes":
    key = crack_sha1_hash(hashed_pw, use_salts=True)
    print(f"Here is the password that you were looking for: {key}")
elif user_answer == "q":
    print("Thanks for stopping by!")
else:
    key = crack_sha1_hash(hashed_pw)
    print(f"Here is the password that you were looking for: {key}")



