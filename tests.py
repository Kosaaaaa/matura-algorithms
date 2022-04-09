import random
import string

from matura_algorithms import gcd, is_prime, binary_search, find_smallest
import unittest

PRIMES_SRC_FILE = 'primes.txt'


class TestMaturaAlgorithms(unittest.TestCase):
    def test_gcd(self):
        self.assertEqual(gcd(12, 6), 6)
        self.assertEqual(gcd(1, 1), 1)
        self.assertEqual(gcd(0, 0), 0)
        self.assertEqual(gcd(111, 111), 111)
        self.assertEqual(gcd(42, 56), 14)
        self.assertEqual(gcd(461952, 116298), 18)
        self.assertEqual(gcd(7966496, 314080416), 32)
        self.assertEqual(gcd(24826148, 45296490), 526)
        self.assertEqual(gcd(12, 0), 12)
        self.assertEqual(gcd(0, 9), 9)

    def test_is_prime_primes(self):
        with open(PRIMES_SRC_FILE) as file:
            primes = [int(prime) for line in file.readlines() for prime in line.split(' ')]

        for prime in primes:
            self.assertTrue(is_prime(prime))

    def test_is_prime_non_primes(self):
        non_primes = [0, 1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36,
                      38, 39, 40, 42, 44, 45, 46, 48, 49, 50, 51, 52, 54, 55, 56, 57, 58, 60, 62, 63]

        for non_prime in non_primes:
            self.assertFalse(is_prime(non_prime))

    def test_binary_search_int(self):
        start_range, end_range = (1, 100000)
        sorted_list = list(range(start_range, end_range))

        for x in range(100):
            item = random.randint(start_range, end_range)
            guess = binary_search(sorted_list, item)
            self.assertEqual(sorted_list[guess], item)

    def test_binary_search_str(self):
        sorted_chars = [char for char in string.ascii_lowercase]
        self.assertEqual(binary_search(sorted_chars, 'a'), 0)
        self.assertEqual(binary_search(sorted_chars, 'm'), 12)
        self.assertEqual(binary_search(sorted_chars, 'z'), 25)
        self.assertIsNone(binary_search(sorted_chars, 'aaaa'))
        self.assertIsNone(binary_search(sorted_chars, ''))

    def test_find_smallest_int(self):
        self.assertEqual(find_smallest([9999, 111, 101010100101010101, -99999, 11111, 1, 3, 4]), 3)
        self.assertEqual(find_smallest([-10, 1, 333, 440, 10101010]), 0)
        self.assertEqual(find_smallest([4444444, 1, 333, 440, 10101010]), 1)

    def test_find_smallest_str(self):
        input_list1 = ['t', 'f', 'e', 'q', 'c', 'n', 'j', 'a', 'w', 'm', 'x', 'd', 'i', 'l', 'u', 'z', 'b', 's', 'h',
                       'g', 'r', 'k', 'v', 'o', 'y', 'p']
        self.assertEqual(find_smallest(input_list1), 7)


if __name__ == '__main__':
    unittest.main()
