# coding: utf-8

import numpy as np
import  matplotlib.pyplot as plt


x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
c,s = np.cos(x), np.sin(x)
plt.figure(1)
plt.plot(x,c,color="blue",linewidth=1.0,linestyle="-",label="Cos",alpha=0.5)
plt.plot(x,s,"r*",label="Sin",linewidth=1.0)
plt.title("Cos & Sin")

axis = plt.gca()
axis.spines["right"].set_color("none")
axis.spines["top"].set_color("none")
axis.spines["left"].set_position(("data", 0))
axis.spines["bottom"].set_position(("data", 0))
axis.xaxis.set_ticks_position("bottom")
axis.yaxis.set_ticks_position("right")


plt.show()