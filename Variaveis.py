# Variaveis são usadas para salvar dados na memória do computador
# f"Claro, tenho {sua_idade} anos", usando o f com {} atribue a variavel ao texto


idade = 18
print("Olá boa noite, pode informar seu nome completo por gentileza: ")

nome_complet = input("Olá noite me chamo: ")

sua_idade = int(input(f"Sr {nome_complet}, poderia nos informar sua idade também, por favor: "))

print(f"Claro, tenho {sua_idade} anos.")

print("Agradecemos por nos informar sua idade!!!")

if sua_idade > idade:
    print("Pode entrar na festa, se divirta e tenha uma ótima noite!!!")
elif sua_idade == idade:
    print(f"Mostre seu RG por favor Sr {nome_complet}, para assim confirmamos sua identidade.")
else:
    print(f"Infelizmente Sr {nome_complet}, você não pode entrar na festa. ")
