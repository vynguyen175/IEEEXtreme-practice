def main():
    import sys

    non_metals = {
        "Cl","Br","Xe","Kr","Si","As","Rn","Ne","He",
        "H","C","N","O","F","P","S","I"
    }

    data = sys.stdin.read().splitlines()
    N = int(data[0].strip())
    for i in range(1, N+1):
        line = data[i].strip()
        if not line:
            print("Molecular!")
            continue
        elements = line.split()
        ok = True
        for el in elements:
            if el not in non_metals:
                ok = False
                break
        if ok:
            print("Molecular!")
        else:
            print("Not molecular!")

if __name__ == "__main__":
    main()
