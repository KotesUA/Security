Part 1

Password generation consists of 4 parts: picking one of top-100, one of top-100k, generating a random string and human-like generator with a dict of 3000 most popular English words.

Percentage of output passwords (weights):

- top-100 = 10%
- top-100k = 65%
- random string = 5%
- human-like = 20%

By default, the program generates 100k passwords with given percentage of weights and saves passwords to passwords.txt

Then, these passwords are encrypted with MD5, SHA-1 Salt and BCrypt algorythms. Every generated dataset of hashed password is stored in separate file.