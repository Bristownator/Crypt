import unittest

from python.src.RSA import RSA, RSAKeyGenerator, RSAKey, Prime


class RSATest(unittest.TestCase):
    def setUp(self):
        self.test_rsa = RSA()
        self.test_rsa.generate_keys()

        self.test_public_key = self.test_rsa.public_key
        self.test_private_key = self.test_rsa.private_key

    def test_generate_keys(self):
        self.assertEqual(17, self.test_rsa.decrypt(self.test_rsa.encrypt(17)))
        self.assertEqual(201, self.test_rsa.decrypt(self.test_rsa.encrypt(201)))

    def test_alt_start(self):
        test_alt_rsa = RSA(RSAKey(143, 7), RSAKey(143, 103))
        self.assertEqual(105, test_alt_rsa.decrypt(test_alt_rsa.encrypt(105)))


class RSAKeyGeneratorTest(unittest.TestCase):
    def setUp(self):
        self.test_rsa_key_generator = RSAKeyGenerator()

    def test_generate_keys(self):
        self.test_rsa_key_generator.generate_keys()

        self.assertIsNotNone(self.test_rsa_key_generator.n)
        self.assertIsNotNone(self.test_rsa_key_generator.e)
        self.assertIsNotNone(self.test_rsa_key_generator.d)

    def test_extended_euclidean(self):
        self.assertEqual([1, 4, -55], self.test_rsa_key_generator.extended_euclidean(
            179, 13))

        self.assertEqual([1, -8695508606140362309587684798, 336816648885497786477357415267846470497],
                         self.test_rsa_key_generator.extended_euclidean(
                             34732457235124123521512431323,
                             1345346245213587135273587124876523875235))


class PrimeTest(unittest.TestCase):
    def test_small_number(self):
        for x in range(8, 128):
            test = Prime(x).get_number()
            self.assertGreater(test, 2 ** (x-1))

    def test_big_number(self):
        test = Prime(1024).get_number()
        self.assertGreater(test, 2 ** 1023)
        self.assertFalse(test % 2 == 0)
        self.assertFalse(test % 3 == 0)
        self.assertFalse(test % 5 == 0)
        self.assertFalse(test % 7 == 0)
        self.assertFalse(test % 11 == 0)
        self.assertFalse(test % 13 == 0)

    def test_is_prime(self):
        test_num = 2
        test_func = Prime(test_num.bit_length())
        self.assertFalse(test_func.is_prime(test_num))

        test_num = 1
        test_func = Prime(test_num.bit_length())
        self.assertFalse(test_func.is_prime(test_num))

        test_num = 13
        test_func = Prime(test_num.bit_length())
        self.assertTrue(test_func.is_prime(test_num))

        test_num = 67280421310725
        test_func = Prime(test_num.bit_length())
        self.assertFalse(test_func.is_prime(test_num))

        test_num = 67280421310721
        test_func = Prime(test_num.bit_length())
        self.assertTrue(test_func.is_prime(test_num))


if __name__ == '__main__':
    unittest.main()
