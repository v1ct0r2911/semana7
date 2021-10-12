#6.	Elabore una aplicación en Python que lea 5 números e imprima la cantidad de números pares, impares, positivos, negativos y neutros.

pares=0
impares=0
positivos=0
negativos=0
neutro=0
limite=int(input("ingrese limite: "))
for i in range(limite):
    if i%2==0:
        pares+=1
    else:
        impares+=1
    if i<0:
        negativos+=1
    else:
        positivos+=1
    if i==0:
        neutro+=1    
print("numeros pares ", pares) 
print("numeros impares", impares)
print("numero positivo", positivos)
print("numeros negativos", negativos) 
print("numeros neutros", neutro)      