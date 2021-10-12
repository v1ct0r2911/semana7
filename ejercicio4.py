#Crear una aplicación en Python que lea 6 números e imprima la cantidad de números pares e impares

par=0
impar=0
suma=0
for i in range(6):
    numero=int(input("ingrese numero: "))
    if numero%2==0:
        par+=1
    else:
        impar+=1
print("numeros pares es: ", par)
print("numeros impres es: ",impar)