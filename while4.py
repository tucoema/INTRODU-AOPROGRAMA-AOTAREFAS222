num_jogadores = int(input("Digite o número de jogadores do time: "))

contador = 1
soma_alturas = 0.0

while contador <= num_jogadores:
	altura = float(input(f"Digite a altura do jogador {contador}: "))
	soma_alturas += altura
	contador += 1

if num_jogadores > 0:
	media = soma_alturas / num_jogadores
	print(f"A altura média do time é: {media:.2f} metros")
else:
	print("Número de jogadores inválido.")