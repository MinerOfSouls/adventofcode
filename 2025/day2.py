
f = open("day2_input.txt")
content = f.read()
ranges = content.split(",")
intr = []
for r in ranges:
    a = r.split("-")
    intr.append((int(a[0]), int(a[1])))

sum = 0
for s, e in intr:
    for j in range(s, e+1):
        string = str(j)
        if (string+string).find(string, 1) != len(string):
            sum += j
print(sum)
