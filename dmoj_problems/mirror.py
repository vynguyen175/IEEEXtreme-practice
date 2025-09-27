import sys
import math

def isprime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def main():
    numCase = int(sys.stdin.readline())   # number of test cases
    for _ in range(numCase):
        a, b = map(int, sys.stdin.readline().split())
        L, R = min(a, b), max(a, b)
        count = 0
        for x in range(L, R):   # check every number in [L, R)
            if isprime(x):
                count += 1
        print(count)

if __name__ == "__main__":
    main()
