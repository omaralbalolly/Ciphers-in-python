from string import ascii_uppercase
from check_invertible import isInvertible


class HillCipher:
    def __init__(self, message, key_word):
        j = []
        for i in range(0, 26):
            j.append(i)
        self.char = dict(zip(list(ascii_uppercase), j))
        if len(message) % 3 != 0:
            a = len(message) % 3
            x = 'X' * (3 - a)
            message += x
        self.message = list(message.upper())
        self.key_word = key_word.upper()
        self.key = self.make_key(self.key_word)
        self.message_matrix = [self.char[l] for l in self.message]
        self.message_lists = [self.message_matrix[i:i + 3] for i in range(0, len(self.message_matrix), 3)]

    @staticmethod
    def make_key(keyword):
        keyword = keyword.upper()
        j = []
        for i in range(0, 26):
            j.append(i)
        char = dict(zip(list(ascii_uppercase), j))
        key = [[0] * 3, [0] * 3, [0] * 3]
        counter = 0
        for i in range(3):
            for j in range(3):
                key[i][j] = char[keyword[counter]]
                counter += 1
        return key

    def encrypt(self):
        result = []
        for pair in self.message_lists:
            for column in self.key:
                result.append((pair[0] * column[0] + pair[1] * column[1] + pair[2] * column[2]) % 26)
        word = ''
        char_inv = {v: k for k, v in self.char.items()}
        for number in result:
            word += char_inv[number]
        return word

    @staticmethod
    def banner():
        print("""
 ██      ██ ██  ██  ██         ██████  ██         ██       ████
░██     ░██░░  ░██ ░██        ██░░░░██░░  ██████ ░██      █░░░ █
░██     ░██ ██ ░██ ░██       ██    ░░  ██░██░░░██░██     ░    ░█ ██████
░██████████░██ ░██ ░██ █████░██       ░██░██  ░██░██████    ███ ░░██░░█
░██░░░░░░██░██ ░██ ░██░░░░░ ░██       ░██░██████ ░██░░░██  ░░░ █ ░██ ░
░██     ░██░██ ░██ ░██      ░░██    ██░██░██░░░  ░██  ░██ █   ░█ ░██
░██     ░██░██ ███ ███       ░░██████ ░██░██     ░██  ░██░ ████ ░███
░░      ░░ ░░ ░░░ ░░░         ░░░░░░  ░░ ░░      ░░   ░░  ░░░░  ░░░ v1337.0
--------------------------------------------------------------------
 A Code written to demonstrate a -> Hill-cipher <- \n\n""")


if __name__ == '__main__':
    HillCipher.banner()
    message = input('[*] Please enter the message to encrypt: ')
    while True:
        keyword = input('[*] Please enter the cipher key: ')
        if len(keyword) != 9:
            print('[!] The key length must be 9 letters')
            continue
        if not isInvertible(HillCipher.make_key(keyword)):
            print('[!] This key is not invertible')
            continue
        break
    message = message.replace(" ", "")
    keyword = keyword.replace(" ", "")
    p = HillCipher(message, keyword)
    print(f'[+] Your encrypted message is: {p.encrypt()}')

# For testing
# key = 'GYBNQKURP' is invertible
