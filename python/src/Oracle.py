

class Oracle:

    @staticmethod
    def encrypt(plain_text, key):
        if plain_text >= key.modulus:
            raise ValueError('Plain text was larger than key\'s modulus!')
        return pow(plain_text, key.exponent, key.modulus)

    @staticmethod
    def decrypt(cipher_text, key):
        if cipher_text >= key.modulus:
            raise ValueError('Cipher text was larger than key\'s modulus!')
        return pow(cipher_text, key.exponent, key.modulus)
