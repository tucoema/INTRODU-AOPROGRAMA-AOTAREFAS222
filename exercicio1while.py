somavalor=0
contnegativo=0  
contador=0
while contador < 20:
    valor=int(input("digite um numero"))
    if valor>=0:
        somavalor+=valor
    else:
        contnegativo+=1
    contador+=1

print("positivos" ,somavalor)
print("negativo", contnegativo)
    

