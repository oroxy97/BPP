import pdb

Lista = [[1, 2, 3], [5, 6, 705, 8, 16, 80], [9, 10, 11, 12, 100, 200, 5000, 4000]]

c = [max(i) for i in Lista]
print(c)

lista = list(range(1, 1000))


def es_primo(n):
    primo = True
    for i in range(2,n):
        if (n % i == 0):
            primo = False
    return primo


primos = list(filter(es_primo, lista))
print(primos)
