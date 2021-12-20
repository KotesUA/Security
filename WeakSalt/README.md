##Weak Salt
#Theory
Let's assume Alice and Bob found a way how to make university labs fast and easily. They need secure communication, so they generate a key and transfer it in a secure way. Now, they decide to encrypt their messages with Salsa20 algorithm with no nonce, which basically means:

encrypted_message = message ^ key.

This seems good, however when using the same key for every message, this can be easily broken. Let's use some math:

encrypted_message1 ^ encrypted_message2 = (message1 ^ key) ^ (message2 ^ key)

(message1 ^ key) ^ (message2 ^ key) = message1 ^ message2

Sounds complicated, so let's encrypt some images to show this type of attack:

![Image explanation](https://github.com/KotesUA/Security/tree/master/WeakSalt/Explanation.jpg?raw=true)
