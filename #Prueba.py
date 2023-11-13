#Prueba
import numpy as np
import matplotlib.pyplot as plt
import random
minutoss =list( range(1,1440))

temp= []
#random.uniform(0.9, 1.1)*
for minutos in minutoss:
       
    TE = 13*np.sin((np.pi*minutos/1440))+19
      
    UV = 0
    temp.append(TE)

# Crear el gráfico
plt.plot(minutoss, temp, label='Radiación Solar')
plt.title('Radiación Solar a lo largo del día')
plt.xlabel('Minutos del día')
plt.ylabel('Radiación')
plt.legend()
plt.show()