
matris = [[(8), (2)], [(1,0), (1,1)]]

print(matris[0][1], matris[1][1])

print(matris[0][0], matris[1][0])


# läs in rad från fil
file = open("matris.txt", "r")
matris = []
for line in file:
    text = line.strip()
    rad = text.split(" ")
    matris.append(rad)

file.close()

#gör om str till int
for i in range(len(matris)):
    for j in range(len(matris[i])):
        matris[i][j] = int(matris[i][j])

#hitta 4 tal efter varadra som har störst produkt, lodrätt, vågrätt eller på diagonalen

max = 0
for i in range(len(matris)):
    for j in range(len(matris[i])):
        #hitta max i rad
        if j < len(matris[i]) - 3:
            produkt = matris[i][j] * matris[i][j+1] * matris[i][j+2] * matris[i][j+3]
            if produkt > max:
                max = produkt

        #hitta max i kolumn
        if i < len(matris) - 3:
            produkt = matris[i][j] * matris[i+1][j] * matris[i+2][j] * matris[i+3][j]
            if produkt > max:
                max = produkt

        #hitta max på diagonalen
        if i < len(matris) - 3 and j < len(matris[i]) - 3:
            produkt = matris[i][j] * matris[i+1][j+1] * matris[i+2][j+2] * matris[i+3][j+3]
            if produkt > max:
                max = produkt
        if i < len(matris) - 3 and j > 2:
            produkt = matris[i][j] * matris[i+1][j-1] * matris[i+2][j-2] * matris[i+3][j-3]
            if produkt > max:
                max = produkt

print(max)