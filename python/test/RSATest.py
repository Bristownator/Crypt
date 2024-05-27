import unittest

from python.src.RSA import RSA, RSAKeyGenerator, RSAKey, Prime


class RSATest(unittest.TestCase):
    @staticmethod
    def test_generate_keys():
        test = RSA()
        test.generate_keys()

    def test_encrypt(self):
        test = RSA()
        test.generate_keys()
        self.assertEqual(17, test.decrypt(test.encrypt(17)))


class RSAKeyGeneratorTest(unittest.TestCase):
    def test_generate_keys(self):
        test = RSAKeyGenerator()
        test.generate_keys()
        self.assertIsNotNone(test.n)
        self.assertIsNotNone(test.e)
        self.assertIsNotNone(test.d)

    def test_extended_euclidean(self):
        test = RSAKeyGenerator()
        self.assertEqual([1, 4, -55], test.extended_euclidean(179, 13))
        self.assertEqual([1, -8695508606140362309587684798, 336816648885497786477357415267846470497],
                         test.extended_euclidean(34732457235124123521512431323,
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
        test_func = Prime(1024)
        test_num = 2
        self.assertFalse(test_func.is_prime(test_num))

        test_num = 1
        self.assertFalse(test_func.is_prime(test_num))

        test_num = 3
        self.assertTrue(test_func.is_prime(test_num))

        test_num = 67280421310725
        self.assertFalse(test_func.is_prime(test_num))

        test_num = 67280421310721
        self.assertTrue(test_func.is_prime(test_num))


if __name__ == '__main__':
    unittest.main()
