class CaesarCipher:
    def __init__(self):
        pass

    def encrypt_text(self, text: str, key: int) -> str:
        encrypted_text = []
        for letter in text:
            if letter.isalpha():
                if letter.isupper():
                    output_letter = chr((ord(letter) - ord('A') + key) % 26 + ord('A'))
                else:
                    output_letter = chr((ord(letter) - ord('a') + key) % 26 + ord('a'))
                encrypted_text.append(output_letter)
            else:
                encrypted_text.append(letter)
        return "".join(encrypted_text)

    def decrypt_text(self, text: str, key: int) -> str:
        decrypted_text = []
        for letter in text:
            if letter.isalpha():
                if letter.isupper():
                    output_letter = chr((ord(letter) - ord('A') - key) % 26 + ord('A'))
                else:
                    output_letter = chr((ord(letter) - ord('a') - key) % 26 + ord('a'))
                decrypted_text.append(output_letter)
            else:
                decrypted_text.append(letter)
        return "".join(decrypted_text)