numero = str(input()).split(" ")
pares = []
for i in range(len(numero)):
    if int(numero[i])%2 ==0:
        pares.append(int(numero[i])**2)
print(*pares)
#nachito putito