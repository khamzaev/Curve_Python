class CipherMaster:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def cipher(self, original_text, shift):
        # Метод должен возвращать зашифрованный текст
        # с учетом переданного смещения shift.
        result = ''
        original_text = original_text.lower()

        for char in original_text:
            if char in self.alphabet:
                original_index = self.alphabet.find(char)
                new_index = (original_index + shift) % len(self.alphabet)
                result += self.alphabet[new_index]
            else:
                result += char
        return result


    def decipher(self, cipher_text, shift):
        # Метод должен возвращать исходный текст
        # с учётом переданного смещения shift.
        result = ''
        cipher_text = cipher_text.lower()

        for char in cipher_text:
            if char in self.alphabet:
                cipher_index = self.alphabet.find(char)
                new_index = (cipher_index - shift) % len(self.alphabet)
                result += self.alphabet[new_index]
            else:
                result += char
        return result


cipher_master = CipherMaster()

print(cipher_master.cipher(
    original_text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2
))
print(cipher_master.decipher(
    cipher_text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3
))