tal1=1
tal2=1
tal = []
while tal1 < 4000000:
    tal.append(tal1)
    tal_1_backup = tal1
    tal1 = tal2
    tal2 = tal_1_backup + tal2

svar = []

for i in tal:
    if i%2 == 0:
        svar.append(i)

print(sum(svar))