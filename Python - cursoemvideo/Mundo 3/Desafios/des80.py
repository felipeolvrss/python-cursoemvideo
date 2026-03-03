lista = []

for c in range(1,6):
    valor = int(input(f"Digite o {c}º valor: "))
    if c == 1:
        lista.append(valor)
        continue
    for posi, item in enumerate(lista):
        if valor <= item:
            lista.insert(posi, valor)
            break
    if valor > lista[-1]:
        lista.append(valor)
    # else:
    #     lista.append(valor)

print(lista)