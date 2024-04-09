def MaxVaMin(a,b,c):
    if a > b:
        if a > c or a == c:
            max = a
            min = b
        elif c > a:
            max = c
            min = b
    if b > a:
        if b > c or b == c:
            max = b
            min = a
        elif c > b:
            max = c
            min = a
    if a > c:
        if a > b or a == b:
            max = a
            min = c
        elif a < b:
            max = b
            min = c
    return max, min

print("Nhap 3 so duong ngau nhien: ")
a = []
for i in range(3):
    program = True
    while(program):
        value = float(input("Nhap so thu %d: "%(i+1)))
        if value < 0:
            print("Vui long nhap so duong")
        else:
            program = False
    a.append(value)
value = []
value.append(MaxVaMin(a[0],a[1],a[2])[0])
value.append(MaxVaMin(a[0],a[1],a[2])[1])
print("So lon nhat la:", MaxVaMin(a[0],a[1],a[2])[0])
print("So be nhat la:", MaxVaMin(a[0],a[1],a[2])[1])
with open("test.txt",'w') as f:
    for i in range(0, len(value)):  
        f.write(str(value[i]) )
