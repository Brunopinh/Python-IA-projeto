# Desafio 1 da dio.me

def recomendar_plano(consumo):
  
    if consumo <= 10:
        print("Plano Essencial Fibra - 50Mbps")
        
    if consumo > 10 and consumo <= 20:
        print("Plano Prata Fibra - 100Mbps")
        
    if consumo > 20:
        print("Plano Premium Fibra - 300Mbps")
    
    return consumo
      
        

# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = int(input("Qual seu consumo: "))
# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
recomendar_plano(consumo)