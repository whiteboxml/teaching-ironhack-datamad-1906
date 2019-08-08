import time

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(1)
ax = fig.add_subplot(111)

def plotter(ax):

    x = [0,1,2,3]
    y = [0,1,2,3]

    ax.plot(x, y,'o')

plotter(ax)
plt.show(block=False)

chiquito_greatest_hits = ["¡Pecador!", "¿Te da cuen?", "¡Fistro!", "¡Pecaor de la praderar!", "¡No puedor, no puedor!", "¡No te digo trigor por no llamarte Rodrigo!", "¡Asexsuarrr!"]

# the only way it shows the graph (during my investigations): ÑAPA DIRECTLY FROM HELL, I strongly encourage you to find a better solution
fig.canvas.draw()
fig.canvas.draw()

while True:
    try:
        print(np.random.choice(chiquito_greatest_hits))
        time.sleep(0.5)

    except KeyboardInterrupt:
        print('\nexiting...')
        plt.close('all')
        break

