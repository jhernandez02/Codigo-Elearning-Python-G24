# tuplas_complejas.py

tuplaComp = (2, 4, "Paman Sports", (1,2), ("Futbol",4,(5,8)))
print('elem1: ', tuplaComp[0])
print('elem2: ', tuplaComp[1])
print('elem3: ', tuplaComp[2])
print('elem4: ', tuplaComp[3])
print('elem4: ', tuplaComp[4])

# Mostramos el primer y segundo valor de la tupla (1,2)
print(tuplaComp[3][0]) # output: 1
print(tuplaComp[3][1]) # output: 2

# Mostramos el primer y segundo valor de la tupla (5,8)
print(tuplaComp[4][2]) # Output => (5,8)
print(tuplaComp[4][2][0]) # Output => 5
print(tuplaComp[4][2][1]) # Output => 8