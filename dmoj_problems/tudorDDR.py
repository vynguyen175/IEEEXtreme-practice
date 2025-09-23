def main():
    user_input = input().strip().upper()
    if len(set(user_input))!=3:
        print("Neither")
        return
    first, middle, last = user_input[0], user_input[1], user_input[2]
    opposites = {
        'L':'R',
        'R':'L',
        'U':'D',
        'D':'U',
    }
    if opposites.get(first)!=last:
        print("Neither")
        return
    if first in ('L','R'):
        print ('Crossover')
    else:
        print('Candle')
    
    
if __name__=="__main__":
    main()