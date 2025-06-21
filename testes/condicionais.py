MAIOR_IDADE = 18

idade = int(input("Informe sua idade: "))

'''
if idade >= MAIOR_IDADE:
    print ("Maior de idade, pode tirar CNH.")

if idade < MAIOR_IDADE:
    print ("Ainda não pode tirar CNH.")
'''

status = "Maior de idade, pode tirar CNH." if idade >= MAIOR_IDADE else "Ainda não pode tirar CNH."
print(f"{status}")