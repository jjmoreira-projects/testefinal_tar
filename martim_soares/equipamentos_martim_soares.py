with open('devices.txt', 'r') as file:

equipamentos = [equipamento.strip() for equipamento in file.readlines()]

while True:
	equipamento_procurar = input("Equipamento a procurar (sair p/ terminar): ")

	if equipamento_procurar.lower() == 'sair':
							break

	equipamentos_encontrados = [eq for eq
in equipamentos if 
equipamento_procurar.lower() in eq.lower()]

	if equipamentos_encontrados:
		print (f"Equipamentos encontrados:
{','.join(equipamentos_encontrados)}")
		print (f"Quantidade:
{len(equipamentos_encontrados)}")
	else:
		print("Equipamento Não-existe na Lista!") 
