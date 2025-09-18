print("*********** menu de operaçoes matematicas ***********")
print("-----------------------------------------------------")
print("escolha a sua operaçao matematica:")
print("1-soma")
print("2-subtração")    
print("3-multiplicação")
print("4-divisão")
print("5-par ou impar")
print("6-fatorial")
print("7-primo")
print("8-sair")

operação=int(input("digite uma operação:"))

if operação==1:

    numero=float(input("digite um numero:"))

    numero2=float(input("digite outro numero:"))

    resultado=numero+numero2

    print("o resultado é:", resultado)

if operação==2:

    numero=float(input("digite um numero:"))

    numero2=float(input("digite um numero:"))

    resultado=numero-numero2
    
    print("a subtraçao é",resultado)

if operação == 3:

    numero=float(input("digite um numero:"))

    numero2 = float(input("digite um numero:"))

    resultado= numero*numero2

    print("a multiplicaçao é", resultado)

if operação == 4:

    numero=float(input("digite um numero:"))

    numero2 = float(input("digite um numero:"))

    rusultado= numero/numero2

    print("a divisão é", resultado)

if operação == 5:

    numero=float(input("digite um numero:"))

    numero2 = float(input("digite um numero:"))

    if numero/2==0:

        print("o numero",numero,"é par")

    else:

        print("o numero",numero,"é impar")

    if numero2/2==0:
         
         print("o numero",numero2,"é par")

    else:

        print("o numero",numero2,"é impar")

    
if operação == 6:

    numero=int(input("digite um numero:"))

    fatorial=1

    for i in range(1,numero+1):

        fatorial=fatorial*i

    print("o fatorial de",numero,"é",fatorial)


if operação == 7:

    numero=int(input("digite um numero:"))

    if numero<2:

        print("não é primo")

    else:

        for i in range(2,int(numero**0.5)+1):

            if numero%i==0:

                print("não é primo")

                break

        else:

            print("é primo")

if operação == 8:

    print("saindo...")

while operação != 8:
    print("*********** menu de operaçoes matematicas ***********")
print("-----------------------------------------------------")
print("escolha a sua operaçao matematica:")
print("1-soma")
print("2-subtração")    
print("3-multiplicação")
print("4-divisão")
print("5-par ou impar")
print("6-fatorial")
print("7-primo")
print("8-sair")


