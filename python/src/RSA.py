import secrets


class RSAKeyGenerator:

    def generate_keys(self):
        p = Prime(1024).generate_number()
        q = Prime(1024).generate_number()
        n = p * q
        phi_n = (p - 1) * (q - 1)

        gcd = [0]
        exponent = None
        while gcd[0] != 1:
            exponent = secrets.randbits(1024)
            gcd = self.__extended_euclidean(phi_n, exponent)

        return RSAPublicKey(n, exponent), RSAPrivateKey(n, gcd[2] % phi_n)

    def __extended_euclidean(self, phi_n, e):
        large = max(phi_n, e)
        small = min(phi_n, e)

        if large % small == 0:
            return [small, 0, 1]

        output = self.__extended_euclidean(small, large % small)

        a = output[2]
        b = output[1] - ((large // small) * a)
        return [output[0], a, b]


class RSAPrivateKey:
    def __init__(self, modulus, exponent):
        self.modulus = modulus
        self.exponent = exponent


class RSAPublicKey:
    def __init__(self, modulus, exponent):
        self.modulus = modulus
        self.exponent = exponent


class Prime:
    def __init__(self, bit_len):
        self.bit_len = bit_len

    def generate_number(self):
        output = None
        is_prime = False
        while not is_prime:
            output = secrets.randbits(self.bit_len)
            if output > 2 ** (self.bit_len - 1):
                is_prime = self.__is_prime(output)
        return output

    def __is_prime(self, number):
        if number % 2 == 0:
            return False

        b = 0
        m = number - 1
        remainder = "Temp"

        while remainder == 0:
            divide, remainder = divmod(m, 2)
            if remainder == 0:
                m = divide
                b += 1

        a = 0
        while a % 2 == 0 & a < number:
            a = secrets.randbits(self.bit_len)

        z = pow(a, m, number)

        if z == 1:
            return True

        if z == number - 1:
            return False

        for _ in range(b):
            m = m * 2
            z = z * pow(a, m, number)

            if z == 1:
                return False

            if z == number - 1:
                return True

        z = z * 2
        z = z % number
        return z == number - 1
