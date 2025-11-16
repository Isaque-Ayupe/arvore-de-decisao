import math
from collections import Counter

#objeto dos nós
class Node:
    def __init__(self, atributo=None, folhas=None, classe=None):
        self.atributo = atributo
        self.folhas = folhas or {}
        self.classe = classe

#entropia inicial
def entropia(dataset):
    total = len(dataset)
    classes = [d["Risco"] for d in dataset]
    cont = Counter(classes)
    return -sum((q/total)*math.log2(q/total) for q in cont.values())

#função para atribuir informaçoes
def ganho_info(dataset, atributo):
    total = len(dataset)
    valores = {}
    for d in dataset:
        valor = d[atributo]
        valores.setdefault(valor, []).append(d)

    ent_total = entropia(dataset)
    ent_atrib = 0

    for v, subconjunto in valores.items():
        ent_atrib += (len(subconjunto)/total) * entropia(subconjunto)

    return ent_total - ent_atrib

#melhor resultado entre os atributos
def best_attribute(dataset, atributos):
    ganhos = {a: ganho_info(dataset, a) for a in atributos}
    return max(ganhos, key=ganhos.get)


#função da arvore id3
def id3(dataset, atributos):
    classes = [d["Risco"] for d in dataset]
    if len(set(classes)) == 1:
        return Node(classe=classes[0])
    if not atributos:
        maj = Counter(classes).most_common(1)[0][0]
        return Node(classe=maj)

    melhor = best_attribute(dataset, atributos)
    node = Node(atributo=melhor)

    valores = set(d[melhor] for d in dataset)
    for v in valores:
        subset = [d for d in dataset if d[melhor] == v]
        novos = [a for a in atributos if a != melhor]
        node.folhas[v] = id3(subset, novos)
    return node

#função de previsao (bizarro)
def predict(tree, exemplo):
    if tree.classe:
        return tree.classe
    valor = exemplo[tree.atributo]
    if valor not in tree.folhas:
        return "Classe desconhecida"
    return predict(tree.folhas[valor], exemplo)
