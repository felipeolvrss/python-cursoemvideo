lista = []
maior = []
menor = []

for itens in range(5):
    lista.append(int(input("Digite um valor: ")))

maiorvalor = max(lista)
menorvalor = min(lista)

for posi, m in enumerate(lista):
    if m == maiorvalor:
        maior.append(posi)
    if m == menorvalor:
        menor.append(posi)

print(f'''O menor valor da lista é {menorvalor} e está nas posições {menor}
O maior valor da lista é {maiorvalor} e está nas posições {maior}''')