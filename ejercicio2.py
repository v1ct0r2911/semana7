#2.	Crear una aplicación en Python que solicite 10 numeros e imprima la suma

suma=0
for i in range(10):
    numero=int(input("ingresa numero"+str(i)+": "))
    suma+=numero
print("la suma ", suma )