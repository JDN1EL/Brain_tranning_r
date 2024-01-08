import random
import time
import os
sistema_de_pontos = [0]

# Dicionário de itens por categoria
try:
    categorias = {
        "FLV": {
            "Abobrinha": 45,
            "Batata" : 47,
            "Cebola" : 10, 
        },
        "Cesta básica": {
            "Cesta Básica G": 30183,
            "Cesta Básica P": 53883
        },
        "Açougue": {
            "Peixe Cavalinha": 737,
            "Peixe Pelombeta": 373
        },
        "Outros": {
            "Saco De Feira": 383, 
            "Rapadura com Coco": 73833,
            "Rapadura sem Coco": 38933,
            "Rapadura 50 unidades": 333339,
            "Gelo": 73737,
            "Porta Cerveja": 733,
            "Marmitex com Tampa": 0030
        }
    }

    while True:
        print("Escolha a categoria:")
        for i, categoria in enumerate(sorted(categorias.keys())):
            print(f"{i+1} para '{categoria}'")

        # Pedir ao usuário para escolher uma categoria
        escolha_categoria = int(input("Escolha a categoria pelo número: "))
        categoria_selecionada = sorted(categorias.keys())[escolha_categoria - 1]

        while True:
            
            item_escolhido = random.choice(list(categorias[categoria_selecionada].keys()))
            codigo_correto = categorias[categoria_selecionada][item_escolhido]
            try:
                tentativa = int(input(f'QUAL O CÓDIGO DESSA FRUTA: {item_escolhido}: ')) 
                
                if tentativa == codigo_correto:
                    if sistema_de_pontos[0] >= 0:#condição para prevenir números negativos 
                        sistema_de_pontos[0] += 1
                        print("Resposta correta!", f"PONTUAÇÃO: {sistema_de_pontos[0]}\n" )
                    else:
                        sistema_de_pontos[0] = 1#condição para prevenir falta do pront de números negativos no terminal 
                        print("Resposta correta!", f"PONTUAÇÃO: {sistema_de_pontos[0]}\n" ) 
                           
                else:
                    sistema_de_pontos[0] -= 1
                    print(f"Resposta incorreta! O código correto : {codigo_correto}\n")
                    time.sleep(3)
                    print("2") 
                    time.sleep(1)
                    print("1")
                    os.system('clear')
            except:
                print("Caracteres inválidos limpando terminal.. ")
                time.sleep(4)
                os.system("clear")
                
   
                
        #  continuar = input("Deseja continuar? (S/N): ")
        #  if continuar.lower() != 's':
        #      break

except:
    print("erro inesperado")
    time.sleep(3)
    print("2")
    time.sleep(1)
    print("1")
    
