import sys
def main():
    alphabet = {
        'A': ("o.", "..", ".."),
        'B': ("o.", "o.", ".."),
        'C': ("oo", "..", ".."),
        'D': ("oo", ".o", ".."),
        'E': ("o.", ".o", ".."),
        'F': ("oo", "o.", ".."),
        'G': ("oo", "oo", ".."),
        'H': ("o.", "oo", ".."),
        'I': (".o", "o.", ".."),
        'J': (".o", "oo", ".."),
        'K': ("o.", "..", "o."),
        'L': ("o.", "o.", "o."),
        'M': ("oo", "..", "o."),
        'N': ("oo", ".o", "o."),
        'O': ("o.", ".o", "o."),
        'P': ("oo", "o.", "o."),
        'Q': ("oo", "oo", "o."),
        'R': ("o.", "oo", "o."),
        'S': (".o", "o.", "o."),
        'T': (".o", "oo", "o."),
        'U': ("o.", "..", "oo"),
        'V': ("o.", "o.", "oo"),
        'W': (".o", "oo", ".o"),
        'X': ("oo", "..", "oo"),
        'Y': ("oo", ".o", "oo"),
        'Z': ("o.", ".o", "oo"),
        ' ': ("..", "..", ".."),
    }
    
    input = sys.stdin.readline().rstrip("\n") #remove new line
    
    row1=[]
    row2=[]
    row3=[]
    
    for char in input:
        top, mid, bot = alphabet[char]
        row1.append(top)
        row2.append(mid)
        row3.append(bot)
        
    print("".join(row1))
    print("".join(row2))
    print("".join(row3))
    
if __name__=="__main__":
    main()
    
    
    