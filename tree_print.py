def print_tree(node, nivel=0):
    prefix = "  " * nivel
    if node.classe:
        print(f"{prefix}→ {node.classe}")
        return
    print(f"{prefix}[Atributo: {node.atributo}]")
    for valor, filho in node.folhas.items():
        print(f"{prefix}  └── {valor}:")
        print_tree(filho, nivel+2)
