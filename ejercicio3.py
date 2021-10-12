#Crear una aplicación en Python que solicite n numeros e imprima la suma y el promedio.

suma=0
limite=int(input("ingrese numero: "))
for i in range(limite):
    print(i)
    suma+=i
promedio=suma/limite
print("la suma es", suma)
print("el promedio es", promedio)  
