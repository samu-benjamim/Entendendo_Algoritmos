def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1
    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None
minha_lista = [1, 2, 3, 4]
num = int(input("Digite o numero para verificar se está no banco de dados: "))
print (pesquisa_binaria(minha_lista, num))
