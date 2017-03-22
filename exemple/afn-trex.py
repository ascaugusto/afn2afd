# afn-trex.py
# Implementação da função de transição estendida e de uma classe para
# representar autômatos finitos não determinísticos (AFN).

from functools import reduce

# Exemplo de função de transição para AFN.
tr1 = {(0, 'a'): frozenset([0, 1]),
       (0, 'b'): frozenset([0, 2]),
       (1, 'a'): frozenset([3]),
       (1, 'b'): frozenset(),
       (2, 'a'): frozenset(),
       (2, 'b'): frozenset([3]),
       (3, 'a'): frozenset([3]),
       (3, 'b'): frozenset([3])}


# Exemplo de implementação da função de transição extendida diretamente sobre a
# função de transição.
def tr1ex(Qi, w):
    if len(w) == 0:
        return Qi
    else:
        x = w[0]
        u = w[1:]
        Qtmp = frozenset([tr1[(q, x)] for q in Qi])
        Qj = reduce(lambda s, t: s | t, Qtmp)
        return tr1ex(Qj, u)


# Classe que implementa autômatos finitos não determinísticos (AFN). O
# construtor da classe recebe como parâmetros: (a) o conjunto de estados do
# autômato, os estados são representados por inteiros; (b) a função de
# transição, que deve ser um dicionário onde as chaves são pares ordenados
# contendo o estado e o caractere da transição, e o valor associado à chave é o
# conjunto de estados da transição -- se não houver transição deve ser colocado
# o conjunto vazio; (c) o estado inicial; e (d) o conjunto de estados finais.
# Todos os conjuntos usados devem ser `frozenset`.
class AFN:
    def __init__(self, states, tr, init, finals):
        self.tr = tr
        self.states = states
        self.init = init
        self.finals = finals

    def trex(self, Qi, w):
        if len(w) == 0:
            return Qi
        else:
            x = w[0]
            u = w[1:]
            Qtmp = frozenset([self.tr[(q, x)] for q in Qi])
            Qj = reduce(lambda s, t: s | t, Qtmp)
            return self.trex(Qj, u)

    def accept(self, w):
        Q = self.trex(frozenset([self.init]), w)
        G = Q & self.finals
        return len(G) > 0


# Local Variables:
# ispell-local-dictionary: "brasileiro"
# End:
