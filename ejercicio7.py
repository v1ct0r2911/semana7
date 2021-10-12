#Elabore una aplicación en Python que lea n números e imprima la suma de los números pares e impares

sumapares=0
sumaimpares=0
limite=int(input("ingrese limite: "))
for i in range(limite):
    number=int(input("ingrese numero: "))
    if number%2==0:
       sumapares+=number 
    else:
        sumaimpares+=number
print("la suma de los pares es:" ,sumapares)
print("suma de impares", sumaimpares)