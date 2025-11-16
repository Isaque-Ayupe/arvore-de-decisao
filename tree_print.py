def print_tree(node, nivel=0):
    prefix = "  " * nivel

    # Nó folha
    if node.classe is not None:
        print(f"{prefix}→ Classe: {node.classe}")
        return

    # Nó interno (atributo)
    atributo = node.atributo if node.atributo is not None else "Atributo-desconhecido"
    print(f"{prefix}[Atributo: {atributo}]")

    # Filhos
    for valor, filho in node.folhas.items():
        print(f"{prefix}  └── Nome: {valor}")
        print_tree(filho, nivel + 2)