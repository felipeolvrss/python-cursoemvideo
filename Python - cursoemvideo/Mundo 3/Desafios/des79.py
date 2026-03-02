lista = []
while True:
    numero = int(input('Digite um número: '))
    if numero not in lista:
        lista.append(numero)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor repetido, valor descartado!')
    quer = str(input('Deseja continuar? [S/N] '))
    if quer in 'Nn':
        break
lista.sort()
print(lista)