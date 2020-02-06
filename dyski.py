import random
import matplotlib.pyplot as plt
import copy


dyski_przed=[]
for i in range(100):
    dyski_przed.append([random.uniform(-14.5,13.5),random.uniform(-14.5,13.5)])
dyski_po = copy.deepcopy(dyski_przed)


def kolizja(d1, d2):
    odl = (d1[0] - d2[0]) ** 2 + (d1[1] - d2[1]) ** 2
    if odl < 1:
        return True
    else:
        return False


def rozsun(d, wektor):
    d[0] = d[0] + wektor[0]
    d[1] = d[1] + wektor[1]

def plot():
    fig, ax = plt.subplots()
    for dysk in dyski_po:
        circle = plt.Circle((dysk[0], dysk[1]), 0.5, color='g')
        ax.add_artist(circle)

    plt.xlim(-15, 15)
    plt.ylim(-15, 15)
    plt.show()

def porzadek(dyski):
    loop = True
    while loop == True:
        run = True
        for dysk1 in range(len(dyski)):
            for dysk2 in range(len(dyski)):

                if dysk1 == dysk2:
                    continue
                else:
                    x = kolizja(dyski[dysk1],dyski[dysk2])

                if x:

                    run = False
                    if not kolizja([dyski[dysk1][0] + 1, dyski[dysk1][1] + 1], dyski[dysk2]) and dyski[dysk1][0] < 13.5 and dyski[dysk1][1] < 13.5:
                        rozsun(dyski[dysk1], [1, 1])
                    elif not kolizja([dyski[dysk1][0] + 1, dyski[dysk1][1] - 1], dyski[dysk2]) and dyski[dysk1][0] < 13.5 and dyski[dysk1][1] > -13.5:
                        rozsun(dyski[dysk1], [1, -1])
                    elif not kolizja([dyski[dysk1][0] - 1, dyski[dysk1][1] - 1], dyski[dysk2]) and dyski[dysk1][0] > -13.5 and dyski[dysk1][1] > -13.5:
                        rozsun(dyski[dysk1], [-1, -1])
                    elif not kolizja([dyski[dysk1][0] - 1, dyski[dysk1][1] + 1], dyski[dysk2]) and dyski[dysk1][0] > -13.5 and dyski[dysk1][1] < 13.5:
                        rozsun(dyski[dysk1], [-1, 1])
                    elif not kolizja([dyski[dysk1][0] + 2, dyski[dysk1][1]], dyski[dysk2]) and dyski[dysk1][0] < 12.5:
                        rozsun(dyski[dysk1], [2, 0])
                    elif not kolizja([dyski[dysk1][0] - 2, dyski[dysk1][1]], dyski[dysk2]) and dyski[dysk1][0] > -12.5:
                        rozsun(dyski[dysk1], [-2, 0])
                    elif not kolizja([dyski[dysk1][0], dyski[dysk1][1] + 2], dyski[dysk2]) and dyski[dysk1][1] < 12.5:
                        rozsun(dyski[dysk1], [0, 2])
                    elif not kolizja([dyski[dysk1][0], dyski[dysk1][1] - 2], dyski[dysk2]) and dyski[dysk1][1] > -12.5:
                        rozsun(dyski[dysk1], [0, -2])
        plot()
        if run:
            loop = False

porzadek(dyski_po)
print('Przesunięte dyski to:')

for i in range(100):
    if dyski_po[i]!=dyski_przed[i]:
        print(dyski_przed[i],dyski_po[i])










