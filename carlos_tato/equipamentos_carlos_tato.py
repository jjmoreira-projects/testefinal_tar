# Importar bibliotecas necessárias
import os
import sys

# Abrir ficheiro devices.txt
with open("devices.txt", "r") as f:
    devices = f.readlines()

# Guardar equipamentos na lista
devices = [device.strip() for device in devices]

# Imprimir mensagem e ler equipamento a procurar
while True:
    print("Equipamento a procurar (sair p/terminar):")
    equipamento = input()

    # Se equipamento for "sair", terminar
    if equipamento == "sair":
        break

    # Procurar equipamento na lista
    quantidade = len([equipamento for equipamento in devices if equipamento == equipamento.lower()])

    # Imprimir resultado
    print(f"O equipamento {equipamento} foi encontrado {quantidade} vezes.")
