from argparse import ArgumentParser, Namespace

parser = ArgumentParser(description="Encrypts/Decrypts a Caesar cypher")
group = parser.add_mutually_exclusive_group()

group.add_argument("-e","--encrypt", help="Encrypts the entered message", action="store_true")
group.add_argument("-d","--decrypt", help="Decrypts the entered message", action="store_true")
parser.add_argument("-i", "--input", help="The message you want to encrypt/decrypt", type=str)
parser.add_argument("-k", "--key", type=int)
parser.add_argument("-f", "--force", help="If key is not know, you can force the decryption and all 26 possible choices will be shown",action="store_true")

args: Namespace = parser.parse_args()


def main():
    if args.encrypt:
        print(encrypt(args.input, args.key))
    elif args.decrypt:
        if args.force: # Print all possible combinations
            for i in range(1, 26):
                print(encrypt(args.input, 26-i))
        else:
            print(encrypt(args.input, 26 - args.key))




def encrypt(input: str, key: int) -> str:
    encrypted_message = ""

    for i in range(len(input)):
        c = input[i]

        if c.isupper():
            encrypted_message += chr((ord(c) + key - 65) % 26 + 65)
        elif c.isspace():
            encrypted_message += ' '
        else:
            encrypted_message += chr((ord(c) + key - 97) % 26 + 97)

    return encrypted_message


if __name__ == "__main__":
    main()