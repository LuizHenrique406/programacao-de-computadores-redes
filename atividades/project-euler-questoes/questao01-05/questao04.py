

maior_palindromo = 0

for i in range(100,1000):
    for j in range(100,1000):
        num = i * j
        num_str = str(num)
        if num_str == num_str[::-1]:
            if num > maior_palindromo:
                maior_palindromo = num
print(maior_palindromo)