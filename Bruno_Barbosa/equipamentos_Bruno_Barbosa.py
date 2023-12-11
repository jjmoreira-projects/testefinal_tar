ficheiro = open("devices.txt", "r")


lista_equipamentos = []


for linha in ficheiro:
    #print(linha)
    linha = linha.strip()
    #print(linha)
    lista_equipamentos.append(linha)


while True:
    nome_equipamento = input("Equipamento a procurar (sair p/terminar): ")

    if nome_equipamento == "sair":
            break 

  
    quant = 0
    for item in lista_equipamentos:
        #if "Router" in item:
        if  nome_equipamento in item:
            quant = quant + 1 
            print(item)

    if quant == 0:
        print("Equipamento Não existe na Lista!")
    else:
        print(f"Quantidade:{quant}")
