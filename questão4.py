Lista_de_compras = []
while True:
    item = input("Digite o item que deja adicionar á lista(ou 'parar' para encerrar):")

    if item.lower() == 'parar':
        break

    Lista_de_compras.append(item)
    print("Sua lista de compras:")
    print(item)

for item in Lista_de_compras:
    print (item)