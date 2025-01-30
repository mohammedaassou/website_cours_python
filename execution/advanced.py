# 1

liste = [1, 2, 3, 4, 5]
inverse = []

for i in range(len(liste) - 1, -1, -1):
    inverse.append(liste[i])

print(inverse)


# 2

liste = [1, 2, 3, 4, 1, 5, 1, 6, 7, 1]
element = 1
compteur = 0

for item in liste:
    if item == element:
        compteur += 1

print(compteur)
