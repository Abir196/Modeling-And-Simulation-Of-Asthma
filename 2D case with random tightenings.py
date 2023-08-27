# pour le point d'indice k


# A[3 * k][ k ]  désigne le le coefficient multiplie par ux dans la première équation


# A[3 * k + 1][ k +N*M ]  désigne le coefficient multiplie par uy dans la deuxième équation


# A[3 * k + 2][ k + 2*N*M ]désigne le coefficient multiplie par P dans la 3eme équation


# .........et ainsi de suite


import math

import numpy as np

import matplotlib.pyplot as plt

import random

# la pression à l'entrée

Pe = 101324.4465

# la pression à la sortie

Ps = 101324.4465 - 0.013

# la longeur du tube

L = 0.024576

# la largeur du tube

l = 0.008192

# le nombre de discrétisation horizontale

N = 60

# le nombre de discrétisation verticale

M = 20

# alpha est le coefficient responsable à equilibrer entre le dérivé centrale et le dérivé decentré

# remarque: 0<alpha <=1

alpha = 0.6

# n represente le coefficient de viscosité

n = 0.00002

# invdx est l'inverse de dx

invdx = N / L

# invdy est l'inverse de dy

invdy = M / l

# le nombre de point dans la discrétisation

nb = int(N * M)

print("N = ", N, " M = ", M)

# Lb et Lh representent les parois bas et haut du tube on les remplit par un indice entre 0 et nb-1

# xb et yb sont les coordonnées de Lb

limh = (2 * M // 3) * (N) - 1 + 2 * N

limb = (M // 3) * (N) - 1

Lb = [0, 1, 2, 3]

Lh = [nb - N, nb - N + 1, nb - N + 2, nb - N + 3]

xb = [0, 1, 2, 3]

yb = [0, 0, 0, 0]

xh = [0, 1, 2, 3]

yh = [M - 1, M - 1, M - 1, M - 1]

i = 4

modulo = 0

while modulo <= N - 1 - 2:

    if modulo >= N - 7:

        if (Lb[-1] - ((Lb[-1]) % N)) / N > 0:

            Lb.append(Lb[i - 1] - N)

            Lb.append(Lb[i] - N)

            xb.append((Lb[i - 1] - N) % N)

            xb.append((Lb[i] - N) % N)

            yb.append((Lb[i - 1] - N - (Lb[i - 1] - N) % N) / N)

            yb.append((Lb[i] - N - (Lb[i] - N) % N) / N)



        else:

            Lb.append(Lb[i - 1] + 1)

            Lb.append(Lb[i] + 1)

            xb.append((Lb[i - 1] + 1) % N)

            xb.append((Lb[i] + 1) % N)

            yb.append((Lb[i - 1] + 1 - (Lb[i - 1] + 1) % N) / N)

            yb.append((Lb[i] + 1 - (Lb[i] + 1) % N) / N)

        i = i - 2




    else:

        b = random.sample([N, -N, 1], 1)

        if Lb[i - 1] + b[0] < 0:

            Lb.append(Lb[i - 1] + 1)

            Lb.append(Lb[i] + 1)

            Lb.append(Lb[i] + 2)

            Lb.append(Lb[i] + 3)

            xb.append((Lb[i - 1] + 1) % N)

            xb.append((Lb[i] + 1) % N)

            xb.append((Lb[i] + 2) % N)

            xb.append((Lb[i] + 3) % N)

            yb.append((Lb[i - 1] + 1 - (Lb[i - 1] + 1) % N) / N)

            yb.append((Lb[i] + 1 - (Lb[i] + 1) % N) / N)

            yb.append((Lb[i] + 2 - (Lb[i] + 2) % N) / N)

            yb.append((Lb[i] + 3 - (Lb[i] + 3) % N) / N)




        elif Lb[i - 1] + b[0] > limb:

            Lb.append(Lb[i - 1] + 1)

            Lb.append(Lb[i] + 1)

            Lb.append(Lb[i] + 2)

            Lb.append(Lb[i] + 3)

            xb.append((Lb[i - 1] + 1) % N)

            xb.append((Lb[i] + 1) % N)

            xb.append((Lb[i] + 2) % N)

            xb.append((Lb[i] + 3) % N)

            yb.append((Lb[i - 1] + 1 - (Lb[i - 1] + 1) % N) / N)

            yb.append((Lb[i] + 1 - (Lb[i] + 1) % N) / N)

            yb.append((Lb[i] + 2 - (Lb[i] + 2) % N) / N)

            yb.append((Lb[i] + 3 - (Lb[i] + 3) % N) / N)




        else:

            if ((Lb[i - 1] + b[0]) in Lb):

                Lb.append(Lb[i - 1] + 1)

                Lb.append(Lb[i] + 1)

                Lb.append(Lb[i] + 2)

                Lb.append(Lb[i] + 3)

                xb.append((Lb[i - 1] + 1) % N)

                xb.append((Lb[i] + 1) % N)

                xb.append((Lb[i] + 2) % N)

                xb.append((Lb[i] + 3) % N)

                yb.append((Lb[i - 1] + 1 - (Lb[i - 1] + 1) % N) / N)

                yb.append((Lb[i] + 1 - (Lb[i] + 1) % N) / N)

                yb.append((Lb[i] + 2 - (Lb[i] + 2) % N) / N)

                yb.append((Lb[i] + 3 - (Lb[i] + 3) % N) / N)



            else:

                Lb.append(Lb[i - 1] + b[0])

                Lb.append(Lb[i] + b[0])

                Lb.append(Lb[i + 1] + b[0])

                Lb.append(Lb[i + 2] + b[0])

                xb.append((Lb[i - 1] + b[0]) % N)

                xb.append((Lb[i] + b[0]) % N)

                xb.append((Lb[i + 1] + b[0]) % N)

                xb.append((Lb[i + 2] + b[0]) % N)

                yb.append((Lb[i - 1] + b[0] - (Lb[i - 1] + b[0]) % N) / N)

                yb.append((Lb[i] + b[0] - (Lb[i] + b[0]) % N) / N)

                yb.append((Lb[i + 1] + b[0] - (Lb[i] + b[0]) % N) / N)

                yb.append((Lb[i + 2] + b[0] - (Lb[i] + b[0]) % N) / N)

                # i = i - 2

    i = i + 4

    modulo = Lb[i - 1] % N

i = 4

modulo = 0

while modulo <= N - 1 - 2:

    if modulo >= N - 7:

        if (Lh[-1] - ((Lh[-1]) % N)) / N < M - 1:

            Lh.append(Lh[i - 1] + N)

            Lh.append(Lh[i] + N)

            xh.append((Lh[i - 1] + N) % N)

            xh.append((Lh[i] + N) % N)

            yh.append((Lh[i - 1] + N - (Lh[i - 1] + N) % N) / N)

            yh.append((Lh[i] + N - (Lh[i] + N) % N) / N)




        else:

            Lh.append(Lh[i - 1] + 1)

            Lh.append(Lh[i] + 1)

            xh.append((Lh[i - 1] + 1) % N)

            xh.append((Lh[i] + 1) % N)

            yh.append((Lh[i - 1] + 1 - (Lh[i - 1] + 1) % N) / N)

            yh.append((Lh[i] + 1 - (Lh[i] + 1) % N) / N)

        i = i - 2




    else:

        b = random.sample([-N, N, 1], 1)

        if Lh[i - 1] + b[0] > nb:

            Lh.append(Lh[i - 1] + 1)

            Lh.append(Lh[i] + 1)

            Lh.append(Lh[i] + 2)

            Lh.append(Lh[i] + 3)

            xh.append((Lh[i - 1] + 1) % N)

            xh.append((Lh[i] + 1) % N)

            xh.append((Lh[i] + 2) % N)

            xh.append((Lh[i] + 3) % N)

            yh.append((Lh[i - 1] + 1 - (Lh[i - 1] + 1) % N) / N)

            yh.append((Lh[i] + 1 - (Lh[i] + 1) % N) / N)

            yh.append((Lh[i] + 2 - (Lh[i] + 2) % N) / N)

            yh.append((Lh[i] + 3 - (Lh[i] + 3) % N) / N)




        elif Lh[i - 1] + b[0] < limh:

            Lh.append(Lh[i - 1] + 1)

            Lh.append(Lh[i] + 1)

            Lh.append(Lh[i] + 2)

            Lh.append(Lh[i] + 3)

            xh.append((Lh[i - 1] + 1) % N)

            xh.append((Lh[i] + 1) % N)

            xh.append((Lh[i] + 2) % N)

            xh.append((Lh[i] + 3) % N)

            yh.append((Lh[i - 1] + 1 - (Lh[i - 1] + 1) % N) / N)

            yh.append((Lh[i] + 1 - (Lh[i] + 1) % N) / N)

            yh.append((Lh[i] + 2 - (Lh[i] + 2) % N) / N)

            yh.append((Lh[i] + 3 - (Lh[i] + 3) % N) / N)



        else:

            if ((Lh[i - 1] + b[0]) in Lh):

                Lh.append(Lh[i - 1] + 1)

                Lh.append(Lh[i] + 1)

                Lh.append(Lh[i] + 2)

                Lh.append(Lh[i] + 3)

                xh.append((Lh[i - 1] + 1) % N)

                xh.append((Lh[i] + 1) % N)

                xh.append((Lh[i] + 2) % N)

                xh.append((Lh[i] + 3) % N)

                yh.append((Lh[i - 1] + 1 - (Lh[i - 1] + 1) % N) / N)

                yh.append((Lh[i] + 1 - (Lh[i] + 1) % N) / N)

                yh.append((Lh[i] + 2 - (Lh[i] + 2) % N) / N)

                yh.append((Lh[i] + 3 - (Lh[i] + 3) % N) / N)



            else:

                Lh.append(Lh[i - 1] + b[0])

                Lh.append(Lh[i] + b[0])

                xh.append((Lh[i - 1] + b[0]) % N)

                xh.append((Lh[i] + b[0]) % N)

                yh.append((Lh[i - 1] + b[0] - (Lh[i - 1] + b[0]) % N) / N)

                yh.append((Lh[i] + b[0] - (Lh[i] + b[0]) % N) / N)

                i = i - 2

    i = i + 4

    modulo = Lh[i - 1] % N

# A * X = B

A = np.zeros((3 * nb, 3 * nb))

B = np.zeros(3 * nb)

# PN est la liste des points de l'asthme

PN = []

for i in range(0, N):

    j = i

    while j not in Lb:
        PN.append(j)

        j = j + N

for i in range(nb - N, nb):

    j = i

    while j not in Lh:
        PN.append(j)

        j = j - N


# la fonction f(k) précise ou appartient le point k dans le cas ou l'asthme n'existe pas

def f(k):
    if (k > 0 and k < N - 1):  # parois basse

        return "bas"



    elif (k > (M - 1) * (N) and k < ((N) * (M)) - 1):  # parois haute

        return "haut"



    elif (k % (N) == 0 and k > 0 and k < (N) * (M - 1)):  # parois de l'entree

        return "entree"



    elif (k % (N) == N - 1 and k > N and k < N * M - 1):  # parois de la sortie

        return "sortie"



    elif (k == 0 or k == N * (M - 1) or k == N - 1 or k == (N) * (M) - 1):  # coins du tube

        return "critique"



    else:

        return "Milieu"  # milieu du tube


# la fonction pc(k) remplit les équations des points des parois superieure et inferieure

def pc(k):
    if k in Lb:

        # la premiere équation Ux=0

        A[3 * k][k] = 1

        B[3 * k] = 0

        # la deuxieme équation Uy=0

        A[3 * k + 1][k + nb] = 1

        B[3 * k + 1] = 0

        # la troisieme équation dépend de la position du point

        if k + 1 in Lb and k - 1 in Lb:

            #     .+.

            #     . .

            #   .+. .+.

            # Uy(k+N)-Uy(k)=0

            A[3 * k + 2][k + nb] = 1

            A[3 * k + 2][k + N + nb] = -1



        elif k + 1 in Lb and k + N in Lb:

            #     ...

            #     . .

            #   ... +..

            # (P(k+1)+P(k)-2*P(k))/(dx**2)+(P(k+N)+P(k)-2*P(k))/(dy**2)=0

            A[3 * k + 2][k + 2 * nb] = -2 * n * ((invdx ** 2) + (invdy ** 2)) + n * invdx ** 2 + n * invdy ** 2

            A[3 * k + 2][k + 1 + 2 * nb] = n * invdx ** 2

            A[3 * k + 2][k + N + 2 * nb] = n * invdy ** 2



        elif k + N in Lb and k - 1 in Lb:

            #     ...

            #     . .

            #   ..+ ...

            # (P(k-1)+P(k)-2*P(k))/(dx**2)+(P(k+N)+P(k)-2*P(k))/(dy**2)=0

            A[3 * k + 2][k + 2 * nb] = -2 * n * ((invdx ** 2) + (invdy ** 2)) + n * invdx ** 2 + n * invdy ** 2

            A[3 * k + 2][k - 1 + 2 * nb] = n * invdx ** 2

            A[3 * k + 2][k + N + 2 * nb] = n * invdy ** 2



        elif (k + N in Lb and k - N in Lb) and (f(k + 1) == "Milieu" or f(k + 1) == "sortie") and k - 1 in PN:

            #     ...

            #     . +

            #   ... ...

            # Ux(k+1)-Ux(k)=0

            A[3 * k + 2][k] = 1

            A[3 * k + 2][k + 1] = -1



        elif (k + N in Lb and k - N in Lb) and (f(k - 1) == "Milieu" or f(k - 1) == "entree") and k - 1 not in PN:

            #     ...

            #     + .

            #   ... ...

            # Ux(k-1)-Ux(k)=0

            A[3 * k + 2][k] = 1

            A[3 * k + 2][k - 1] = -1



        elif k - 1 in Lb and k - N in Lb:

            #     ..+

            #     . .

            #   ... ...

            # (Ux(k-1)-Ux(k+1))/dx+(Uy(k-N)-Uy(k+N))/dy=0

            A[3 * k + 2][k + 1] = -invdx

            A[3 * k + 2][k - 1] = invdx

            A[3 * k + 2][k + N + nb] = invdy

            A[3 * k + 2][k - N + nb] = -invdy



        elif k + 1 in Lb and k - N in Lb:

            #     +..

            #     . .

            #   ... ...

            # (Ux(k-1)-Ux(k+1))/dx+(Uy(k-N)-Uy(k+N))/dy=0

            A[3 * k + 2][k + 1] = -invdx

            A[3 * k + 2][k - 1] = invdx

            A[3 * k + 2][k + N + nb] = invdy

            A[3 * k + 2][k - N + nb] = -invdy



        else:

            #         ...

            #         . .

            #   +.  ... ...

            # P(k)=Pe

            if k == 0:

                A[3 * k + 2][k + 2 * nb] = 1

                B[3 * k + 2] = Pe



            #         ...

            #         . .

            #   ..  ... ...  .+

            # P(k)=Ps

            elif k == N - 1:

                A[3 * k + 2][k + 2 * nb] = 1

                B[3 * k + 2] = Ps

        return "true"




    elif k in Lh:

        # la premiere équation Ux=0

        A[3 * k][k] = 1

        B[3 * k] = 0

        # la deuxieme équation Uy=0

        A[3 * k + 1][k + nb] = 1

        B[3 * k + 1] = 0

        # la troisieme équation dépend de la position du point

        if k + 1 in Lh and k - 1 in Lh:

            #       .+. .+.

            #         . .

            #         .+.

            # Uy(k-N)-Uy(k)=0

            A[3 * k + 2][k + nb] = 1

            A[3 * k + 2][k - N + nb] = -1



        elif k + 1 in Lh and k + N in Lh:

            #       ... ...

            #         . .

            #         +..

            # (Ux(k-1)-Ux(k+1))/dx+(Uy(k-N)-Uy(k+N))/dy=0

            A[3 * k + 2][k + 1] = -invdx

            A[3 * k + 2][k - 1] = invdx

            A[3 * k + 2][k + N + nb] = invdy

            A[3 * k + 2][k - N + nb] = -invdy



        elif k + N in Lh and k - 1 in Lh:

            #       ... ...

            #         . .

            #         ..+

            # (Ux(k-1)-Ux(k+1))/dx+(Uy(k-N)-Uy(k+N))/dy=0

            A[3 * k + 2][k + 1] = -invdx

            A[3 * k + 2][k - 1] = invdx

            A[3 * k + 2][k + N + nb] = invdy

            A[3 * k + 2][k - N + nb] = -invdy



        elif (k + N in Lh and k - N in Lh) and (f(k - 1) == "Milieu" or f(k - 1) == "entree") and k - 1 not in PN:

            #       ... ...

            #         + .

            #         ...

            # Ux(k-1)-Ux(k)=0

            A[3 * k + 2][k] = 1

            A[3 * k + 2][k - 1] = -1



        elif (k + N in Lh and k - N in Lh) and (f(k + 1) == "Milieu" or f(k + 1) == "sortie") and k - 1 in PN:

            #       ... ...

            #         . +

            #         ...

            # Ux(k+1)-Ux(k)=0

            A[3 * k + 2][k] = 1

            A[3 * k + 2][k + 1] = -1



        elif k - 1 in Lh and k - N in Lh:

            #       ..+ ...

            #         . .

            #         ...

            # (P(k-1)+P(k)-2*P(k))/(dx**2)+(P(k-N)+P(k)-2*P(k))/(dy**2)=0

            A[3 * k + 2][k + 2 * nb] = -2 * n * ((invdx ** 2) + (invdy ** 2)) + n * invdx ** 2 + n * invdy ** 2

            A[3 * k + 2][k - 1 + 2 * nb] = n * invdx ** 2

            A[3 * k + 2][k - N + 2 * nb] = n * invdy ** 2



        elif k + 1 in Lh and k - N in Lh:

            #       ... +..

            #         . .

            #         ...

            # (P(k+1)+P(k)-2*P(k))/(dx**2)+(P(k-N)+P(k)-2*P(k))/(dy**2)=0

            A[3 * k + 2][k + 2 * nb] = -2 * n * ((invdx ** 2) + (invdy ** 2)) + n * invdx ** 2 + n * invdy ** 2

            A[3 * k + 2][k + 1 + 2 * nb] = n * invdx ** 2

            A[3 * k + 2][k - N + 2 * nb] = n * invdy ** 2



        else:

            #    +. ... ... ..

            #         . .

            #         ...

            # P(k)=Pe

            if k == nb - 1:

                A[3 * k + 2][k + 2 * nb] = 1

                B[3 * k + 2] = Ps



            #    .. ... ... .+

            #         . .

            #         ...

            # P(k)=Ps

            elif k == nb - N:

                A[3 * k + 2][k + 2 * nb] = 1

                B[3 * k + 2] = Pe



            else:

                print("error")

        return "true"



    else:

        return "false"


# la boucle principale dans là quel pour chaque point de la discrétisation, on remplit les trois équations


for k in range(nb):

    # pos est l'emplacement du point dans le tube

    pos = f(k)

    # si (pc(k) == "true" ) alors le point est dans les parois et on remplit les trois équations dans la fonction pc

    if pc(k) == "true":

        next



    # si k appatient à les points de l'asthme on met la vitesse nulle et la pression égale la pression à la sortie

    # remarque les point de l'asthme n'ont pas d'effet sur le système

    elif k in PN:

        # UX=0

        A[3 * k][k] = 1

        B[3 * k] = 0

        # UY

        A[3 * k + 1][k + nb] = 1

        B[3 * k + 1] = 0

        # P(k)= Ps

        A[3 * k + 2][k + 2 * nb] = 1

        B[3 * k + 2] = Ps

    # si k appartient au milieu du tube

    elif pos == "Milieu":

        # 1er équation Stokes suivant X

        A[3 * k][k] = -2 * n * ((invdx ** 2) + (invdy ** 2))

        A[3 * k][k - 1] = n * invdx ** 2

        A[3 * k][k + 1] = n * invdx ** 2

        A[3 * k][k + N] = n * invdy ** 2

        A[3 * k][k - N] = n * invdy ** 2

        A[3 * k][k + 1 + 2 * nb] = -(invdx / 2) * alpha

        A[3 * k][k - 1 + 2 * nb] = (invdx / 2) * (2 - alpha)

        A[3 * k][k + 2 * nb] = - (invdx) * (1 - alpha)

        # 2eme équation Stokes suivant Y

        A[3 * k + 1][k + nb] = -2 * n * ((invdx ** 2) + (invdy ** 2))

        A[3 * k + 1][k - 1 + nb] = n * invdx ** 2

        A[3 * k + 1][k + 1 + nb] = n * invdx ** 2

        A[3 * k + 1][k + N + nb] = n * invdy ** 2

        A[3 * k + 1][k - N + nb] = n * invdy ** 2

        A[3 * k + 1][k + N + 2 * nb] = (invdy / 2) * alpha

        A[3 * k + 1][k - N + 2 * nb] = (invdy / 2) * (alpha - 2)

        A[3 * k + 1][k + 2 * nb] = -(invdy) * (alpha - 1)

        # 3eme équation conservation de masse

        A[3 * k + 2][k + 1] = - invdx / 2

        A[3 * k + 2][k - 1] = invdx / 2

        A[3 * k + 2][k + N + nb] = invdy / 2

        A[3 * k + 2][k - N + nb] = - invdy / 2



    elif f(k) == "entree":

        # 1er équation Stokes suivant X

        A[3 * k][k] = -2 * n * ((invdx ** 2) + (invdy ** 2)) + n * invdx ** 2

        A[3 * k][k + 1] = n * invdx ** 2

        A[3 * k][k + N] = n * invdy ** 2

        A[3 * k][k - N] = n * invdy ** 2

        A[3 * k][k + 2 * nb] = invdx

        A[3 * k][k + 1 + 2 * nb] = -invdx

        # 2eme équation Stokes suivant Y

        A[3 * k + 1][k + nb] = -2 * n * ((invdx ** 2) + (invdy ** 2)) + n * invdx ** 2

        A[3 * k + 1][k + 1 + nb] = n * invdx ** 2

        A[3 * k + 1][k + N + nb] = n * invdy ** 2

        A[3 * k + 1][k - N + nb] = n * invdy ** 2

        A[3 * k + 1][k + N + 2 * nb] = -invdy / 2

        A[3 * k + 1][k - N + 2 * nb] = invdy / 2

        # 3eme équation P(k)=Pe

        A[3 * k + 2][k + 2 * nb] = 1

        B[3 * k + 2] = Pe



    elif pos == "sortie":

        # 1er équation Stokes suivant X

        A[3 * k][k + 2 * nb] = -invdx

        A[3 * k][k - 1 + 2 * nb] = invdx

        A[3 * k][k] = -2 * n * ((invdx ** 2) + (invdy ** 2)) + n * invdx ** 2

        A[3 * k][k - 1] = n * invdx ** 2

        A[3 * k][k + N] = n * invdy ** 2

        A[3 * k][k - N] = n * invdy ** 2

        # 2eme équation Stokes suivant Y

        A[3 * k + 1][k + N + 2 * nb] = -invdy / 2

        A[3 * k + 1][k - N + 2 * nb] = invdy / 2

        A[3 * k + 1][k + nb] = -2 * n * ((invdx ** 2) + (invdy ** 2)) + n * invdx ** 2

        A[3 * k + 1][k - 1 + nb] = n * invdx ** 2

        A[3 * k + 1][k + N + nb] = n * invdy ** 2

        A[3 * k + 1][k - N + nb] = n * invdy ** 2

        # 3eme équation P(k)=Ps

        A[3 * k + 2][k + 2 * nb] = 1

        B[3 * k + 2] = Ps

# la resolution de A*X0=B

X0 = np.dot(np.linalg.inv(A), B)

# Conserver 4 chiffres après la virgule

X = np.around(X0, decimals=4)

# extraire Ux de X

Ux = X[:nb]

# extraire Uy de X

Uy = X[nb:2 * nb]

# extraire P de X

P = X[2 * nb:]

# calcule de la vitesse U(ux,uy)

Ul = []

for i in range(nb):
    Ul.append(math.sqrt(Ux[i] ** 2 + Uy[i] ** 2))

U = np.array(Ul)

# calcule de débit


debit = []

vit = []

max = 0

min = 10000000000000

for j in range(N):

    for i in range(0, M):
        c = j + i * N

        vit.append(Ul[c])

    s = (np.array(vit) * 1 / invdy).sum()

    debit.append(s)

    if max < s:
        max = s

    if min > s:
        min = s

    print("le débit", j, s)

    vit.clear()

print("la variation de débit est de " + str(100 * (max - min) / max) + "%")

# la partie affichage


x = np.linspace(0, N - 1, N)

y = np.linspace(0, M - 1, M)

X, Y = np.meshgrid(x, y)

# UY

Z = Uy.reshape(M, N)

fig, ax = plt.subplots()

pc = ax.pcolormesh(X, Y, Z, shading='auto')

fig.colorbar(pc)

plt.scatter(xb, yb, s=130, c='red', marker='.')

plt.scatter(xh, yh, s=50, c='red', marker='.', linewidth=3)

plt.title('Vitesse Uy')

# UX

Z = Ux.reshape(M, N)

fig, ax = plt.subplots()

pc = ax.pcolormesh(X, Y, Z, shading='auto')

fig.colorbar(pc)

plt.scatter(xb, yb, s=130, c='red', marker='.')

plt.scatter(xh, yh, s=50, c='red', marker='.', linewidth=3)

plt.title('Vitesse Ux')

# U


Z = U.reshape(M, N)

fig, ax = plt.subplots()

pc = ax.pcolormesh(X, Y, Z, shading='auto')

fig.colorbar(pc)

plt.scatter(xb, yb, s=130, c='red', marker='.')

plt.scatter(xh, yh, s=50, c='red', marker='.', linewidth=3)

plt.title('Vitesse')

# la pression


Z = P.reshape(M, N)

fig, ax = plt.subplots()

pc = ax.pcolormesh(X, Y, Z, shading='auto')

fig.colorbar(pc)

plt.scatter(xb, yb, s=130, c='red', marker='.')

plt.scatter(xh, yh, s=50, c='red', marker='.', linewidth=3)

plt.title('Pression')

plt.show()



