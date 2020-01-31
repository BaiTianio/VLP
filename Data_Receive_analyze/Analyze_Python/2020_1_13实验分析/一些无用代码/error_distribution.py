import numpy as np
import matplotlib.pyplot as plt
from my_Draw import *

h=200
polar_angle=np.arange(45,90)*(2*np.pi)/360#theta

one_radian=np.float64(0.0174533)
horizontal_angle=np.ones(polar_angle.shape)*30*(2*np.pi)/360#beta

e=h*(1/np.tan(polar_angle)-1/np.tan(polar_angle+one_radian))


plt.style.use("seaborn-paper") 
fig=plt.figure(figsize=[10,10],dpi=300)

plt.plot(e)

font_config()
graph_adjust(xticks=['40$\degree$','50$\degree$','60$\degree$','70$\degree$','80$\degree$','90$\degree$'],
             x_scale=e.shape[0],ticks_size=17)

plt.xlabel("俯仰角($\degree$)",fontsize=17)
plt.ylabel('误差(cm)',fontsize=17)           

plt.savefig('fig1.png')
plt.close()