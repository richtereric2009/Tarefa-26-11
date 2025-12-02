import random
palavra = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
pergunta = int(input("Quantos dígitos terá sua senha?"))
senha = ""
for i in range(pergunta):
    senha += random.choice(palavra)
print("A sua senha é:", senha)