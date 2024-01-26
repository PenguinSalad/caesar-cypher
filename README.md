# Caesar Cipher
Simple cli program to encrypt/decrypt a caesar cipher. Allows for brute force.

```
usage: main.py [-h] [-e | -d] [-i INPUT] [-k KEY] [-f]

Encrypts/Decrypts a Caesar cipher

options:
  -h, --help            show this help message and exit
  -e, --encrypt         Encrypts the entered message
  -d, --decrypt         Decrypts the entered message
  -i INPUT, --input INPUT
                        The message you want to encrypt/decrypt
  -k KEY, --key KEY
  -f, --force           If key is not know, you can force the decryption and all 26 possible choices will be shown
```