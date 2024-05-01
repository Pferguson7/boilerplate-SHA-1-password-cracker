import hashlib
hashed_pw = input("Please provide the hash:\n")
def crack_sha1_hash(hash, use_salts = False):
    if use_salts == False:
        with open("top-10000-passwords.txt", 'r') as f:
            for line in f:
                if hash == hashlib.sha1(line.strip().encode()).hexdigest():
                 return line.strip()
    else:
        with open("top-10000-passwords.txt", 'r') as f:
            for line in f:
                if hash == hashlib.sha1(line.strip().encode()).hexdigest():
                    with open("known-salts.txt", "r") as salts:
                        for x in salts:
                            hash = x + hash + x 
        return hash
    return "PASSWORD NOT IN DATABASE"


key = crack_sha1_hash(hashed_pw)

print(key)