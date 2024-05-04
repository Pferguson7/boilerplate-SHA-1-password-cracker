# SHA-1 Password Cracker

This a project is inspired by: https://www.freecodecamp.org/learn/information-security/information-security-projects/sha-1-password-cracker

What is a password hash ? In the context of authentication and security, a password hash is a cryptographic representation of a user's password. Instead of storing the actual password in plaintext, which poses a significant security risk if the database is compromised, the password is transformed into a fixed-length string of characters using a mathematical algorithm called a hash function. To enhance security further, it's common practice to use a cryptographic salt along with the password before hashing. A salt is a random value unique to each password and is concatenated with the password before hashing. This mitigates attacks like rainbow table attacks, where precomputed tables of hashes are used to quickly reverse passwords.

# Project Objectives
In this project, I embarked on a personal exploration of password security by developing a custom rainbow table attack targeting over 10,000 commonly used passwords. This endeavor allowed me to gain insights into the vulnerabilities associated with weak passwords and the importance of robust password security practices.

# Motivation
My motivation for undertaking this project stemmed from a desire to deepen my understanding of cryptographic concepts and security practices. By simulating a rainbow table attack, I aimed to explore the effectiveness of various password hashing techniques and highlight the significance of choosing strong, unique passwords.

# Methodology
Data Collection: I sourced a dataset provided by https://www.freecodecamp.org/ consisting of over 10,000 commonly used passwords from various public datasets and breaches.
- Hash Computation: Checking SHA1 hashes of each password using the hashlib Python library. 
- Password Verification: When testing passwords, I compared the hash value of each password against the entries in my rainbow table. If a match was found, it indicated the presence of a weak or commonly used password.
- Checking for salt: If user specified, this function also prepends, and appends common salt values to each password before converting the password to it's hash value. After conversion the comparison is made!

# Key Learnings
Password Security Awareness: Through this project, I gained a deeper appreciation for the importance of strong, unique passwords in safeguarding sensitive information.
Hashing Techniques: I explored various cryptographic hashing algorithms and their implications for password security, including the benefits of incorporating salts to mitigate rainbow table attacks.

# Script installation
Package installation instructions:



