arr = [2, 7, 11, 15, 3]
k = 9

seen = set()
found = False

for e in arr:
    if k - e in seen:
        found = True
        break
    seen.add(e)

print("YES" if found else "NO")
