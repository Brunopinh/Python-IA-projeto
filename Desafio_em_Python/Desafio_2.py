consumo = 0    
def recomendar_plano():
    global consumo
    if consumo <= 10:
        print("Plano Essencial")
        
    if consumo == 10 and consumo <= 20:
        print("Plano Prata Fibra")
        
    if consumo > 20:
        print("Plano premium Fibra")

    return consumo    
        

# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = float(input("Qual seu consumo: "))
# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
print(recomendar_plano())