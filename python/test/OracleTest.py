import unittest

from python.src.Oracle import Oracle, EncryptionType
from python.src.RSA import RSAKeyGenerator, RSAPublicKey, RSAPrivateKey


class OracleTest(unittest.TestCase):
    def setUp(self):
        self.oracle = Oracle()

        self.test_public_key, self.test_private_key = RSAKeyGenerator().generate_keys()

    def test_generate_keys(self):
        self.assertEqual(17, self.oracle.decrypt(self.oracle.encrypt(17, self.test_private_key),
                                                 self.test_public_key))
        self.assertEqual(17, self.oracle.decrypt(self.oracle.encrypt(17, self.test_public_key),
                                                 self.test_private_key))

        self.assertEqual(201, self.oracle.decrypt(self.oracle.encrypt(201, self.test_private_key),
                                                  self.test_public_key))
        self.assertEqual(201, self.oracle.decrypt(self.oracle.encrypt(201, self.test_public_key),
                                                  self.test_private_key))

    def test_alt_start(self):
        test_alt_public_key = RSAPublicKey(143, 7)
        test_alt_private_key = RSAPrivateKey(143, 103)

        self.assertEqual(105, self.oracle.decrypt(self.oracle.encrypt(105, test_alt_public_key),
                                                  test_alt_private_key))

    def test_too_large_encrypt(self):
        test_alt_public_key = RSAPublicKey(143, 7)
        test_alt_private_key = RSAPrivateKey(143, 103)

        with self.assertRaises(ValueError):
            self.oracle.encrypt(200, test_alt_public_key)

        with self.assertRaises(ValueError):
            self.oracle.encrypt(200, test_alt_private_key)

        with self.assertRaises(ValueError):
            self.oracle.decrypt(200, test_alt_public_key)

        with self.assertRaises(ValueError):
            self.oracle.decrypt(200, test_alt_private_key)

        with self.assertRaises(ValueError):
            self.oracle.encrypt(143, test_alt_public_key)

        with self.assertRaises(ValueError):
            self.oracle.encrypt(143, test_alt_private_key)

        with self.assertRaises(ValueError):
            self.oracle.decrypt(143, test_alt_public_key)

        with self.assertRaises(ValueError):
            self.oracle.decrypt(143, test_alt_private_key)


if __name__ == '__main__':
    unittest.main()
