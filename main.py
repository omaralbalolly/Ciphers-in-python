from string import ascii_uppercase


class HillCipher:
    def __init__(self, message, key_word):
        j = []
        for i in range(0, 26):
            j.append(i)
        self.char = dict(zip(list(ascii_uppercase), j))
        self.message = list(message.upper())
        self.key_word = key_word
        key = [[0] * 3, [0] * 3, [0] * 3]
        counter = 0
        for i in range(3):
            for j in range(3):
                key[i][j] = self.char[self.key_word[counter]]
                counter += 1
        self.key = key
        self.message_matrix = [self.char[l] for l in self.message]
        self.message_lists = [self.message_matrix[i:i + 3] for i in range(0, len(self.message_matrix), 3)]

    def encrypt(self):
        # print(f'Alphabet {self.char}')
        # print(f'Message {self.message_lists}')
        # print(f'Key {self.key}')
        # key_columns = [[l[i] for l in self.key] for i in range(len(self.key))]
        result = []
        for pair in self.message_lists:
            for column in self.key:
                result.append((pair[0] * column[0] + pair[1] * column[1] + pair[2] * column[2]) % 26)
        word = ''
        char_inv = {v: k for k, v in self.char.items()}
        for number in result:
            word += char_inv[number]
        return word
    def decrypt(self):
        pass


if __name__ == '__main__':
    key = 'GYBNQKURP'
    message = 'ACTDEFGHI'
    p = HillCipher(message, key)
    print(p.encrypt())
