import unittest

from RSA import RSA, RSAKeyGenerator, RSAKey, Prime


class RSATest(unittest.TestCase):
    def test_generate_keys(self):
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
        self.assertEqual([1, -8695508606140362309587684798, 336816648885497786477357415267846470497], test.extended_euclidean(34732457235124123521512431323, 1345346245213587135273587124876523875235))


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


if __name__ == '__main__':
    unittest.main()
