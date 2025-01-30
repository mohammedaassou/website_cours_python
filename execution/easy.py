# 1



for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# 2 

somme = 0
for i in range(1, 11):
    somme += i
print("Somme :", somme)


# 3

total = 0

for i in range(1, 20):
    if i % 3 == 0 or i % 5 == 0:
        total += i

print(total)


# 4

n = 1

while n <= 20:
    if n % 2 == 0:
        print(n)
    n += 1


# 5

n = 10

while n > 0:
    if n % 2 == 0:  
        print(n, end=" ")
    n -= 1


# 6

n = 1

while n < 30:
    if n % 5 == 0:
        print(n)
        break
    print(n)
    n += 1


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
