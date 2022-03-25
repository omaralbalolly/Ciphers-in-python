#!/usr/bin/python3
from string import ascii_lowercase


class Vingere:
    def __init__(self):
        self.key = None
        j = [i for i in range(0, 26)]
        self.char = dict(zip(list(ascii_lowercase), j))

    def generate_key(self, text, key: list):
        i = 0
        """Repeating the key until it matches the plain text length"""
        while len(text) > len(key):
            key.append(key[i])
            i += 1
        if len(text) < len(key):
            key = key[:len(text)]
        self.key = key
        print(f"[+] Key: {''.join(self.key).upper()}")

        """Minimizing key length if its smaller than the plain text"""
        if len(text) < len(key):
            key = key[:len(text)]
        self.key = key

    def encrypt(self, plain, key):
        plain = list(plain)
        if not key:
            print("[*] User didn't provide a valid key\n[-] Generating a key...")
            key = list("deceptive")
        self.generate_key(plain, list(key))
        num_key = [i for i in self.key]
        num_plain = [i for i in plain]
        num_cipher = [self.char[i] + self.char[j] for (i, j) in zip(num_plain, num_key)]
        char_inv = {v: k for k, v in self.char.items()}
        cipher = []
        for number in num_cipher:
            if number > 25:
                """Making sure that number isn't out of alphabet range"""
                number = number % 26
            cipher.append(char_inv[number])
        print(f"[+] Generated cipher: {''.join(cipher).upper()}")

    def decrypt(self, cipher, key):
        while not key:
            key = input("[!] Enter a key: ")
        cipher = list(cipher)
        self.generate_key(cipher, list(key))
        num_key = [i for i in self.key]
        num_cipher = [i for i in cipher]
        num_plain = [self.char[i] - self.char[j] + 26 for (i, j) in zip(num_cipher, num_key)]
        char_inv = {v: k for k, v in self.char.items()}
        plain = []
        for number in num_plain:
            if number > 25:
                """Making sure that number isn't out of alphabet range"""
                number = number % 26
            plain.append(char_inv[number])
        print(f"[+] Decrypted cipher: {''.join(plain).upper()}")

    def main(self):
        self.banner()
        choice = input(
            "[@] Please choose a number from the following:\n-> 1- Encrypt\n-> 2- Decrypt\n\n[-] Choice: ")
        if choice == "1":
            plain = input("\n[*] Enter a text to encrypt: ")
            while plain == '':
                plain = input("[*] Enter a text to encrypt: ")
            plain = plain.replace(" ", "").lower()
            key = input("[*] Enter a key (Default: deceptive): ")
            if key == '':
                key = None
            else:
                key = key.replace(" ", "").lower()
            self.encrypt(plain, key)
        elif choice == "2":
            cipher = input("\n[*] Enter a cipher to decrypt: ")
            while cipher == '':
                cipher = input("[*] Enter a cipher to decrypt: ")
            cipher = cipher.replace(" ", "").lower()
            key = input("[*] Enter a key: ")
            if key == '':
                key = None
            else:
                key = key.replace(" ", "").lower()
            self.decrypt(cipher, key)
        else:
            print("\n[!] Invalid choice!\n[#] Exiting...")
            exit(1)

    def banner(self):
        print("""       
 ██      ██ ██
░██     ░██░░   █████
░██     ░██ ██ ██░░░██  █████  ███████  ██████  █████
░░██    ██ ░██░██  ░██ ██░░░██░░██░░░██░░██░░█ ██░░░██
 ░░██  ██  ░██░░██████░███████ ░██  ░██ ░██ ░ ░███████
  ░░████   ░██ ░░░░░██░██░░░░  ░██  ░██ ░██   ░██░░░░
   ░░██    ░██  █████ ░░██████ ███  ░██░███   ░░██████
    ░░     ░░  ░░░░░   ░░░░░░ ░░░   ░░ ░░░     ░░░░░░ v.0.97
-------------------------------------------------------
A Code written to demonstrate a -> Vigenère cipher <- \n\n""")


if __name__ == '__main__':
    try:
        run = Vingere()
        run.main()
    except (KeyboardInterrupt, EOFError):
        print("\n\n[#] Good Bye :(\n")
