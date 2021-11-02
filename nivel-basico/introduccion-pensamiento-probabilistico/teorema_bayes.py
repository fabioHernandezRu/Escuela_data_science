"""
P(A | B) = P(B | A )P(A) / P(B)
ejemplo
probabilidad de que alguien sea ingeniero y sea timido es igual
a la probabilidad de que alguien sea ingeniero y sea timido sobre
la probabilidad de que alguien sea timido
---------------------------------------------

P(H|E) = P(H Y E)/P(E)
P(H | E ) = P(H)P(E|H)/P(H)P(E|H)+ P(~H)P(E|~H)

P(H) = prior
P(H | E) =posterior

H = hipótesis
E = Evento
P(H) = Prior = hipótesis antes de la evidencia
P(H|E) = Posterior = Ya teniendo evidencia como actualizamos cierta creencia.
P(E|H) = Likelihood = Certeza de que esta situación es correcta.

Ecosograma
"""

def calc_bayes(prior_A,prob_b_dado_A, prob_B):
    return (prior_A*prob_b_dado_A) / prob_B


if __name__ == '__main__':
    prob_cancer = 1 /100000
    prob_sintoma_dado_cancer = 1
    prob_sintoma_dado_no_cancer = 10 / 99999
    prob_no_cancer = 1 - prob_cancer
    
    prob_sintoma = (10 + 1)/ 100000

    prob_cancer_dado_sintoma =calc_bayes (prob_cancer, prob_sintoma_dado_cancer, prob_sintoma)
    print(prob_cancer_dado_sintoma)