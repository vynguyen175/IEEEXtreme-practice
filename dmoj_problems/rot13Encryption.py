import sys

def char(c):
    if 'A'<=c<='Z': #uppercase
        return chr((ord(c)- ord('A') +13) % 26 + ord('A'))
    
    if 'a'<=c<='z': #lower
        return chr((ord(c)- ord('a') +13) % 26 + ord('a'))

    return c

def rot13_line(s):
    return "".join(char(c) for c in s)


def main():
    for i in range(5):
        line = sys.stdin.readline().rstrip('\n')
    print(rot13_line(line))

if __name__=="__main__":
    main()