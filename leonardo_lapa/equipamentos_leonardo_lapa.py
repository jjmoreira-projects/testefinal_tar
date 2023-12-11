#a)

ficheiro = open('devices.txt', 'r')

#b)

lista = []

for i in ficheiro:
   i = i.strip()
   lista.append(i)

ficheiro.close()

for i in lista:
   print(i)

#c)

while True:
   equipamento = input('Equipamento a procurar (sair p/terminar): ')
   if equipamento == 'sair':
      break

#d)

   cont = 0

   for i in lista:
#      print(i)

      if equipamento in i:
         cont += 1
         print(i)

   if cont == 0:
       print('Equipamento não existe')
   else:
       print(f'Quantidade: {cont}')
