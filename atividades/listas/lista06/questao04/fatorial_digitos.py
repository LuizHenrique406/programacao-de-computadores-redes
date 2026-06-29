def fatorial(n):
    num = []
    for i in range(n + 1):
        num.append(i)
    num = sorted(num, reverse = True)
    num.remove(0)
    