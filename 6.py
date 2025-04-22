lista1 = []

i = 1
while i < 101:
    lista1.append(i)
    i=i+1


svar_lista1 = []
x = 0

while x < 100:
   svar_lista1.append(lista1[x] ** 2)
   x=x+1

svar1 = (sum(svar_lista1))

svar2 = sum(lista1) ** 2

print(svar2 - svar1)
