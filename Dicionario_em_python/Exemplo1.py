# alterando um metodo dict

# verificando 

pessoa = {
    "Pessoa 1" : {
    "Nome": "Bruno Lima",
    "Idade": 22,
    "Telefone": "65 98444-4600",
    "sexo": "M"
    },
    "Pessoa 2" : {
    "Nome": "Paulo Lima",
    "Idade": 26,
    "Telefone": "65 98458-4660",
    "sexo": "M"
    }
}


for indice, pessoa in pessoa.items():
    print(f'{indice},{pessoa}')
