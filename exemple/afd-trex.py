# afd-trex.py
# Implmentação da função de transição extendida para um autômato finito
# determinístico (AFD).

tr1 = {(0, 'a'): 1,
       (0, 'b'): 2,
       (1, 'a'): 3,
       (1, 'b'): 2,
       (2, 'a'): 1,
       (2, 'b'): 3,
       (3, 'a'): 3,
       (3, 'b'): 3}


# Exemplo de implementação da função de transição extendida diretamente sobre a
# função de transição.
def tr1ex(q, w):
    if len(w) == 0:
        return q
    else:
        a = w[0]
        w1 = w[1:]
        qj = tr1[(q, a)]
        return tr1ex(qj, w1)


# Implmentação de uma classe para representar AFD's o construtor da classe
# recebe como parâmetro a função de transição (função programa) na forma de um
# dicionário.
class AFD:
    def __init__(self, states, tr, init, finals):
        self.tr = tr
        self.states = states
        self.init = init
        self.finals = finals

    def trex(self, qi, w):
        if len(w) == 0:
            return qi
        else:
            x = w[0]
            u = w[1:]
            qj = self.tr[(qi, x)]
            return self.trex(qj, u)

    def accept(self, w):
        q = self.trex(self.init, w)
        return (q in self.finals)


# Local Variables:
# ispell-local-dictionary: "brasileiro"
# End
