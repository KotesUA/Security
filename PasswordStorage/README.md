#Password Storage

This repository is a simple client-server application, showing:
* simple register/login form
* password storing using Fernet symmetric encryption

##Secure register and login
TODO using TLS

##Password storage
To ensure security of users' credentials, we are using Fernet symmetric encryption. The key of encryption is static in this implementation, but in further production development it is to be generated on client side every registration and use cryptography.fernet.MultiFernet to ensure security.

##Registration
Password is required to be 8 chars or longer, including at least 8 digits.