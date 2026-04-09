num = int(input("Número: ")
					
dig1 = num // 1000
num = num % 1000
dig2 = num // 100
num = num % 100
dig3 = num // 10
dig4 = num % 10

soma = dig1 + dig2 + dig3 + dig4 

print("soma: ", soma)
