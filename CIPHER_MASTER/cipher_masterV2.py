class CipherMaster:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


    def process_text(self, text, shift, is_encrypt):
        result = ''
        text = text.lower()

        if not is_encrypt:
            shift = -shift


        for char in text:
          if char in self.alphabet:
              original_index = self.alphabet.find(char)
              new_index = (original_index + shift) % len(self.alphabet)
              result += self.alphabet[new_index]
          else:
              result += char
        return result

# Пример использования
cipher_master = CipherMaster()

# Шифрование текста
ciphered_text = cipher_master.process_text(
    text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2,
    is_encrypt=True
)
print("Зашифрованный текст:", ciphered_text)

# Дешифровка текста
deciphered_text = cipher_master.process_text(
    text='олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=3,
    is_encrypt=False
)
print("Расшифрованный текст:", deciphered_text)