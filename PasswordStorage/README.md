#Password Storage

This repository is a simple client-server application, showing:
* simple register/login form
* password storing using Fernet symmetric encryption

##Secure register and login
Secure connection is implemented using OpenSSL library cert generation for every server startup. This is selected as the most simple way to self-generate cert and establish a "secure" connection. Furthermore, this lib can be used to work with SSL authorities in production mode.

##Password storage
To ensure security of users' credentials, we are using Fernet symmetric encryption. The key of encryption is static in this implementation, but in further production development it is to be generated on client side every registration and use cryptography.fernet.MultiFernet to ensure security.

##Registration
Password is required to be 8 chars or longer, including at least 8 digits.

##Personal info
Storing password and personal data is secured by envelope protection: DEK exists in database, encrypted with static KEK. However, this can be improved by generating KEK locally on client side.