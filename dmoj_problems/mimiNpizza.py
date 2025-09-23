def main():
    import sys
    data = sys.stdin.read().split()
    B = int(data[0])
    P = int(data[1])
    veg = data[2].strip()

    # Define pizza types: (name, price, is_veg)
    # In preference order: A, B, C, D
    pizzas = [
        ('A', 5, False),
        ('B', 5, True),
        ('C', 2, False),
        ('D', 2, True),
    ]

    answer = "NO PIZZA"
    for name, price, is_veg in pizzas:
        if veg == 'Y' and not is_veg:
            continue
        cost = price * P
        if cost <= B:
            answer = name
            break

    print(answer)

if __name__ == "__main__":
    main()
