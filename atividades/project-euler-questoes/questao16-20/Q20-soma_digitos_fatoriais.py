print("Esse programa soma os digitos do fatorial de um número")
def soma_dig_fat(n):
    soma = 1
    soma_str = 0
    nums = []
    for i in range(n + 1):
        nums.append(i)
    nums = sorted(nums, reverse = True)
    nums.remove(0)
    for i in nums:
        soma *= i
    for i in str(soma):
        soma_str += int(i)
    return soma_str
print(soma_dig_fat(10))