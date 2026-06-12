a = [1,1,1,1,2,2,2,3,3,4,5,6,5,6,7,44,2,4,6,44]
num = []

for i in a:
    ja_existe = False
    for j in range(len(num)):
        if i == num[j]:
            ja_existe = True
            break
    if not ja_existe:
        num.append(i)

print(num)