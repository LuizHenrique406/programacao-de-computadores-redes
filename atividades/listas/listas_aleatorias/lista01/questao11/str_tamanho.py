import sys
sys.set_int_max_str_digits(1000000000) 
numero = (2 ** 1000000)
numero_str = str(numero)
numero_len = len(numero_str)
print(f"{numero_len}")
