from typing import List, Any, Optional


def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return gcd(b, a % b)


def is_prime(num: int, i: int = 2) -> bool:
    if num == 2:
        return True
    if num < 2 or num % i == 0:
        return False
    if num < i ** 2:
        return True
    return is_prime(num, i + 1)


def is_prime_2(n):
    if n > 1:
        for i in range(2, int(n / 2) + 1):
            if (n % i) == 0:
                return False
        return True
    return False


def binary_search(sorted_list: List[Any], item: Any) -> Optional[Any]:
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = low + high
        guess = sorted_list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


def find_smallest(input_list: List[Any]) -> int:
    smallest_index = 0
    for i, item in enumerate(input_list):
        if item < input_list[smallest_index]:
            smallest_index = i
    return smallest_index
