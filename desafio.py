menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITES_SAQUES = 3

while True:

	opcao = input(menu)

	if opcao == "d":
		valor_deposito = float(input("Digite o valor do depósito: "))
		if valor_deposito > 0:
			saldo += valor_deposito
			extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
			print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso!")

		else:
			print("O valor informado é inválido, tente novamente.")

	elif opcao == "s":
		if numero_saques >= LIMITES_SAQUES:
			print("Limites de saques diários atingido, tente novamente amanhã.")
		else:
			valor_saque = float(input("Digite o valor do saque: "))
			if valor_saque > saldo:
				print("Saldo insuficiente.")

			elif valor_saque > limite:
				print("O valor máximo para saque é R$ 500,00.")

			elif valor_saque > 0:
				saldo -= valor_saque
				extrato += f"Saque: R$ {valor_saque:.2f}\n"
				numero_saques += 1
				print(f"Saque de R$ {valor_saque:,.2f} realizado com sucesso!")

			else:
				print("O valor informado é inválido, tente novamente.")

	elif opcao == "e":
		print("\n**********EXTRATO**********\n")
		if extrato == "":
			print("Não foram realizadas movimentações.")
		else:
			print(extrato)
			print(f"Saldo: {saldo:,.2f}")

		print("\n***************************\n")


	elif opcao == "q":
		break

	else:
		print("Operação inválida, por favor selecione novamente a operação desejada.")
		