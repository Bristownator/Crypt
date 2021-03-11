import secrets


class RSA:
    def __init__(self):
        self.public_key = None
        self.private_key = None

    def generate_keys(self):
        keys = RSAKeyGenerator()
        keys.generate_keys()
        self.public_key = RSAKey(keys.n, keys.e)
        self.private_key = RSAKey(keys.n, keys.d)

    def encrypt(self, plain_text):
        return pow(plain_text, self.public_key.exponent, self.public_key.modulus)

    def decrypt(self, cipher_text):
        return pow(cipher_text, self.private_key.exponent, self.private_key.modulus)


class RSAKeyGenerator:
    def __init__(self):
        self.p = Prime(1024).get_number()
        self.q = Prime(1024).get_number()
        self.n = self.p * self.q
        self.phi_n = (self.p - 1) * (self.q - 1)
        self.e = None
        self.d = None

    def generate_keys(self):
        gcd = [0]
        exponent = None
        while gcd[0] != 1:
            exponent = secrets.randbits(1024)
            gcd = self.extended_euclidean(self.phi_n, exponent)
        self.e = exponent
        self.d = gcd[2] % self.phi_n

    def extended_euclidean(self, phi_n, e):
        large = max(phi_n, e)
        small = min(phi_n, e)

        if large % small == 0:
            return [small, 0, 1]

        output = self.extended_euclidean(small, large % small)

        a = output[2]
        b = output[1] - ((large // small) * a)
        return [output[0], a, b]


class RSAKey:
    def __init__(self, modulus, exponent):
        self.modulus = modulus
        self.exponent = exponent


class Prime:
    def __init__(self, bits):
        self.bits = bits

    def get_number(self):
        output = None
        prime = False
        while not prime:
            output = secrets.randbits(self.bits)
            if output > 2 ** (self.bits - 1):
                prime = self.prime(output)
        return output

    def prime(self, number):
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
            a = secrets.randbits(self.bits)

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
