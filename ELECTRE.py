import numpy as np

poids = [3, 2, 3, 1, 1]

tableau_performances = np.array([
    [10, 20, 5, 10, 16],
    [0, 5, 5, 16, 10],
    [0, 10, 0, 16, 7],
    [20, 5, 10, 10, 13],
    [20, 10, 15, 10, 13],
    [20, 10, 20, 13, 13],
])

c = 0.8
d = 0.3

def concordance(tableau_performances = tableau_performances, poids = poids):
    m, n = tableau_performances.shape
    tab_concordances = np.zeros((m, m))

    for indexP1, p1 in enumerate(tableau_performances):
        for indexP2, p2 in enumerate(tableau_performances):
            concordance = 0
            for indexC, (c1, c2) in enumerate(zip(p1, p2)):
                critere1 = c1 > c2
                critere2 = c1 == c2
                if critere1 or critere2:
                    concordance += poids[indexC]

            tab_concordances[indexP1, indexP2] = concordance / sum(poids)

    return tab_concordances


def searchOmega(tableau_performances = tableau_performances):
    for p in tableau_performances:
        mx = max(p)
        mn = 0
        if max(p) > mx:
            mx = max(p)
        if min(p) < mn:
            mn = min(p)
    omega = mx - mn
    return omega

def dis_concordance(omega, tableau_performances = tableau_performances, poids = poids):
    m, n = tableau_performances.shape
    tab_discordances = np.zeros((m, m))

    for indexP1, p1 in enumerate(tableau_performances):
        for indexP2, p2 in enumerate(tableau_performances):
            discordance = []
            for c1, c2 in zip(p1, p2):
                if c1 < c2:
                    discordance.append(c2 - c1)

            tab_discordances[indexP1, indexP2] = max(discordance) / omega if discordance else 0

    return tab_discordances

tab_concordances = concordance()
print("tableau de concordances: \n", tab_concordances)
omega = searchOmega()
print("Omega: \n", omega)
tab_dis_cordance = dis_concordance(omega)
print("tableau de discordances: \n", tab_dis_cordance)

def couples(tab_discordances = tab_dis_cordance, tab_concordances = tab_concordances):
    couples = []
    for indexI, (ci, di) in enumerate(zip(tab_concordances, tab_discordances)):
        for indexJ, (cij, dij) in enumerate(zip(ci, di)):
            if cij >= c and dij <= d:
                if indexI != indexJ:
                    couples.append((indexI + 1, indexJ + 1))
    return couples

couples = couples()

def plotGraphe(couples = couples):
    import networkx as nx
    import matplotlib.pyplot as plt

    G = nx.Graph()
    G.add_edges_from(couples)
    nx.draw_networkx(G)
    plt.show()

plotGraphe()

