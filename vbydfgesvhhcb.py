import math

def soma():
	a = float(input("Digite o primeiro número: "))
	b = float(input("Digite o segundo número: "))
	print(f"Resultado: {a + b}")

def subtracao():
	a = float(input("Digite o primeiro número: "))
	b = float(input("Digite o segundo número: "))
	print(f"Resultado: {a - b}")

def multiplicacao():
	a = float(input("Digite o primeiro número: "))
	b = float(input("Digite o segundo número: "))
	print(f"Resultado: {a * b}")

def divisao():
	a = float(input("Digite o primeiro número: "))
	b = float(input("Digite o segundo número: "))
	if b == 0:
		print("Não é possível dividir por zero!")
	else:
		print(f"Resultado: {a / b}")

def par_ou_impar():
	n = int(input("Digite um número inteiro: "))
	if n % 2 == 0:
		print("O número é PAR.")
	else:
		print("O número é ÍMPAR.")

def fatorial():
	n = int(input("Digite um número inteiro: "))
	if n < 0:
		print("Não existe fatorial de número negativo!")
	else:
		print(f"Fatorial de {n} é {math.factorial(n)}")

def primo():
	n = int(input("Digite um número inteiro: "))
	if n < 2:
		print("Não é primo.")
		return
	for i in range(2, int(n ** 0.5) + 1):
		if n % i == 0:
			print("Não é primo.")
			return
	print("É primo!")

def menu():
	while True:
		print("************MENU DE OPERAÇÕES MATEMATICAS************")
		print("-----------------------------------------------------")
		print("Escolha a sua operação matemática:")
		print("1 - Soma")
		print("2 - Subtração")
		print("3 - Multiplicação")
		print("4 - Divisão")
		print("5 - Par ou Ímpar")
		print("6 - Fatorial")
		print("7 - Primo")
		print("8 - Sair")
		opcao = input("Digite a opção desejada: ")
		if opcao == '1':
			soma()
		elif opcao == '2':
			subtracao()
		elif opcao == '3':
			multiplicacao()
		elif opcao == '4':
			divisao()
		elif opcao == '5':
			par_ou_impar()
		elif opcao == '6':
			fatorial()
		elif opcao == '7':
			primo()
		elif opcao == '8':
			print("Saindo...")
			break
		else:
			print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
	menu()
