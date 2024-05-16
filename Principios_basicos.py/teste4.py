texto = str(input("Digite  seu nome: "))
vogais = "AEIOU"

for letra in texto:
    if letra.upper() in vogais:
        print(letra, end="")


print()    




