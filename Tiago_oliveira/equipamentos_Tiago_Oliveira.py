import os
import sys


with open("devices.txt", "r") as f:
    devices = f.readlines()


devices = [device.strip() for device in devices]


while True:
    print("Equipamento a procurar (sair p/terminar):")
    equipamento = input()


    if equipamento == "sair":
        break


    quantidade = len([equipamento for equipamento in devices if equipamento == equipamento.lower()])

    print(f"O equipamento {equipamento} foi encontrado {quantidade} vezes.")
