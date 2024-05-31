from enum import Enum


class EncryptionType(Enum):
    DIFFIE_HELLMAN = 1
    RSA = 2
    ELLIPTIC_CURVE = 3
    KYBER = 4

    DES = 5
    AES = 6


class Oracle:
    def __init__(self, encryption_type=EncryptionType.RSA):
        self.encryption_type = encryption_type

    def encrypt(self, plain_text, key):
        if self.encryption_type is EncryptionType.RSA:
            if plain_text >= key.modulus:
                raise ValueError('Plain text was larger than key\'s modulus!')
            return pow(plain_text, key.exponent, key.modulus)

    def decrypt(self, cipher_text, key):
        if self.encryption_type is EncryptionType.RSA:
            if cipher_text >= key.modulus:
                raise ValueError('Cipher text was larger than key\'s modulus!')
            return pow(cipher_text, key.exponent, key.modulus)
