# pour le point d'indice k


# A[3 * k][ k ]  désigne le le coefficient multiplie par ux dans la première équation


# A[3 * k + 1][ k +N*M ]  désigne le coefficient multiplie par uy dans la deuxième équation


# A[3 * k + 2][ k + 2*N*M ]désigne le coefficient multiplie par P dans la 3eme équation


# .........et ainsi de suite


import math

import numpy as np

import matplotlib.pyplot as plt

import matplotlib.ticker as mtick

# Q est la liste des débit moyenne pour chaque epsilon

Q = []

for i in range(0, 10, 2):

    # la pression à l'entrée

    Pe = 101324.4465

    # la pression à la sortie

    Ps = 101324.4465 - 0.013

    # la longeur du tube

    L = 0.024576

    # la largeur du tube

    l = 0.008192

    # l'objectif est d'avoir un un resserrement qui ne dépend pas de la discrétisation

    # pour cela on divise le tube sur 3 parties avec Lh2 represente epsilon 2 et lh2 represente epsilon 1

    # Lhi = Lhi * L /(Lh1+Lh2+Lh3)

    # remarque Lh1+Lh2+Lh3 = Lb1+Lb2+Lb3 car on doit conserver la même longueur du tube dans le bas et le haut

    Lh1 = 10 + int(i / 2)

    Lh2 = 10 - i

    Lh3 = 10 + int(i / 2)

    # ky est le coefficient pour multiplier le nombre de pas de la discrétisation suivant Y

    # remarque: 0<ky

    ky = 2

    lh2 = ky

    # de même pour le bas

    Lb1 = 10

    Lb2 = 10

    Lb3 = 10

    lb2 = 0

    # k est le coefficient pour multiplier le nombre de pas de la discrétisation suivant X

    # remarque: 0<k

    k = 6

    dx = math.gcd(Lh1, Lh2, Lh3, Lb1, Lb2, Lb3) / k

    if ky == 0:
        ky = 1

    dy = math.gcd(lh2, lb2) / ky

    if dy == 0:
        dy = 1 / ky

    # le nombre de discrétisation horizontale

    N = int((Lh1 + Lh2 + Lh3) / dx)

    # haut est le nombre de discritisation suivant Y

    haut = 10

    # le nombre de discrétisation verticale

    M = int(haut / dy)

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

    deb = 4  # x où calculer le débit

    # Lb et Lh representent les parois bas et haut du tube on les remplit par un indice entre 0 et nb-1

    # xb et yb sont les coordonnées de Lb

    Lb = []

    xb = []

    yb = []

    Lh = []

    xh = []

    yh = []

    # Dans la suit on remplit Lh,xh,yh,Lb,xb et yb

    for i in range(int(Lh1 / dx) + 1):
        Lh.append(N * (M - 1) + i)

        xh.append((N * (M - 1) + i) % N)

        yh.append((N * (M - 1) + i) // N)

    for i in range(int(Lh2 / dx) + 1):
        Lh.append(Lh1 / dx + N * (M - 1) + i - (lh2 / dy) * N)

        xh.append((Lh1 / dx + N * (M - 1) + i - (lh2 / dy) * N) % N)

        yh.append((Lh1 / dx + N * (M - 1) + i - (lh2 / dy) * N) // N)

    for i in range(int(Lh3 / dx)):
        Lh.append((Lh1 + Lh2) / dx + N * (M - 1) + i)

        xh.append(((Lh1 + Lh2) / dx + N * (M - 1) + i) % N)

        yh.append(((Lh1 + Lh2) / dx + N * (M - 1) + i) // N)

    for i in range(int(lh2 / dy) - 1):
        Lh.append(Lh1 / dx + N * (M - 1) - i * N - N)

        xh.append((Lh1 / dx + N * (M - 1) - i * N - N) % N)

        yh.append((Lh1 / dx + N * (M - 1) - i * N - N) // N)

        Lh.append((Lh1 + Lh2) / dx + N * (M - 1) - i * N - N)

        xh.append(((Lh1 + Lh2) / dx + N * (M - 1) - i * N - N) % N)

        yh.append(((Lh1 + Lh2) / dx + N * (M - 1) - i * N - N) // N)

    for i in range(int(Lb1 / dx) + 1):
        Lb.append(i)

        xb.append((i) % N)

        yb.append((i) // N)

    for i in range(int(Lb2 / dx) + 1):
        Lb.append(Lb1 / dx + i + (lb2 / dy) * N)

        xb.append((Lb1 / dx + i + (lb2 / dy) * N) % N)

        yb.append((Lb1 / dx + i + (lb2 / dy) * N) // N)

    for i in range(int(Lb3 / dx)):
        Lb.append((Lb1 + Lb2) / dx + i)

        xb.append(((Lb1 + Lb2) / dx + i) % N)

        yb.append(((Lb1 + Lb2) / dx + i) // N)

    for i in range(int(lb2 / dy) - 1):
        Lb.append(Lb1 / dx + i * N + N)

        xb.append((Lb1 / dx + i * N + N) % N)

        yb.append((Lb1 / dx + i * N + N) // N)

        Lb.append((Lb1 + Lb2) / dx + i * N + N)

        xb.append(((Lb1 + Lb2) / dx + i * N + N) % N)

        yb.append(((Lb1 + Lb2) / dx + i * N + N) // N)

    # A * X = B

    A = np.zeros((3 * nb, 3 * nb))

    B = np.zeros(3 * nb)

    # PN est la liste des points de l'asthme

    PN = []

    # dans la suite on replit PN

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

    # compute débit pour x donnée

    vit_x = []

    for i in range(0, M):
        c = deb + i * N

        vit_x.append(Ul[c])

    s_x = (np.array(vit_x) * 1 / invdy).sum()

    Q.append(s_x)

X = np.array(range(0, 10, 2)) * 10

Y = np.array(Q)

plt.xlabel('la valeur de epsilon 2 en pourcentage par rapport à sa valeur initiale')

plt.ylabel('la moyenne du débit')

plt.plot(X, Y, '-')

plt.gca().xaxis.set_major_formatter(mtick.PercentFormatter(xmax=100.0))

plt.show()