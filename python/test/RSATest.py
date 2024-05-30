import unittest

from python.src.RSA import RSAKeyGenerator, RSAPublicKey, RSAPrivateKey, Prime
from python.src.Oracle import Oracle


class RSATest(unittest.TestCase):
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


class RSAKeyGeneratorTest(unittest.TestCase):

    def test_generate_keys(self):
        test_rsa_public_key, test_rsa_private_key = RSAKeyGenerator().generate_keys()

        self.assertIsNotNone(test_rsa_public_key.modulus)
        self.assertIsNotNone(test_rsa_public_key.exponent)

        self.assertIsNotNone(test_rsa_private_key.modulus)
        self.assertIsNotNone(test_rsa_private_key.exponent)


class PrimeTest(unittest.TestCase):
    def test_small_number(self):
        for x in range(8, 128):
            test = Prime(x).generate_number()
            self.assertGreater(test, 2 ** (x-1))

    def test_big_number(self):
        test = Prime(1024).generate_number()
        self.assertGreater(test, 2 ** 1023)
        self.assertFalse(test % 2 == 0)
        self.assertFalse(test % 3 == 0)
        self.assertFalse(test % 5 == 0)
        self.assertFalse(test % 7 == 0)
        self.assertFalse(test % 11 == 0)
        self.assertFalse(test % 13 == 0)


if __name__ == '__main__':
    unittest.main()
