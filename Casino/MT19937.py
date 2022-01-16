# imported from https://github.com/yinengy/Mersenne-Twister-in-Python/blob/master/MT19937.py
# coefficients for MT19937
(w, n, m, r) = (32, 624, 397, 31)
a = 0x9908B0DF
(u, d) = (11, 0xFFFFFFFF)
(s, b) = (7, 0x9D2C5680)
(t, c) = (15, 0xEFC60000)
l = 18
f = 0x6c078965

# (1 << r) - 1 // That is, the binary number of r 1's
lower_mask = 0x7FFFFFFF

# lowest w bits of (not lower_mask)
upper_mask = 0x80000000


class MT19937:
    def __init__(self, seed=None):
        # make an array to store the state of the generator
        self.MT = [0 for _ in range(n)]
        self.index = n
        if seed is not None:
            self.mt_seed(seed)

    # initialize the generator from a seed
    def mt_seed(self, seed):
        self.MT[0] = seed
        for i in range(1, n):
            temp = f * (self.MT[i - 1] ^ (self.MT[i - 1] >> (w - 2))) + i
            self.MT[i] = temp & 0xffffffff

    # Extract a tempered value based on MT[index]
    # calling twist() every n numbers
    def extract_number(self):
        if self.index >= 624:
            self.twist()

        y = self.MT[self.index]
        y ^= y >> u
        y ^= ((y << s) & b)
        y ^= ((y << t) & c)
        y ^= y >> l

        self.index += 1
        return y & 0xffffffff

    # Generate the next n values from the series x_i
    def twist(self):
        for i in range(n):
            x = ((self.MT[i] & upper_mask) +
                 (self.MT[(i + 1) % n] & lower_mask)) \
                & 0xffffffff
            self.MT[i] = self.MT[(i + m) % n] ^ (x >> 1)

            if x & 1 != 0:
                self.MT[i] ^= a

        self.index = 0


if __name__ == '__main__':
    generator = MT19937(123123123)
    for i in range(n):
        print(generator.extract_number())
