lista = []
for i in range(1000):
    lista.append(i)

multiples = []
lista.pop(0)

for a in lista:
    if a%3 == 0:
        multiples.append(a)
    elif a%5 == 0:
        multiples.append(a)

print(multiples)
print(sum(multiples))