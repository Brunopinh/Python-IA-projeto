contatos = {
    "guilherme@gmail.com" : {"nome": "Bruno", "Telefone": "3333-2221"}
}

#contatos["chave"]

# ele a chave e retorna se existe ou não
print(contatos.get("chave"))
print(contatos.get("chave", {}))
print(contatos.get("guilherme@gmail.com", {}))