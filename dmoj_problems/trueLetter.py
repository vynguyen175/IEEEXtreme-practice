import sys
def isTrue(word):
    freq={}
    for c in word:
        freq[c]= freq.get(c,0)+1    
    for c in word:
        if freq[c]==1:
            return c

def main():
    for i in range(5):
        word= sys.stdin.readline().strip()
        print(isTrue(word))

if __name__=="__main__":
    main()
