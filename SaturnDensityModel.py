import numpy as np
import matplotlib.pyplot as plt 

radiusRho = open(r"C:\Users\roryc\Documents\saturndensity.txt").read() 

radiusRho = radiusRho.replace("\n",",")
radiusRho = radiusRho.replace("\t",",")
radiusRho = radiusRho.split(",")

radii = np.array([])
rho = np.array([])

i = 0
while i < len(radiusRho) / 2: 
    radii = np.append(radii,float(radiusRho[i * 2]) * 58232)
    rho = np.append(rho,float(radiusRho[i * 2 + 1]))
    i += 1
    
i = 0
while i < len(radii) - 1: 
    xvalues = [radii[i],radii[i+1]]
    yvalues = [rho[i],rho[i+1]]
    plt.plot(xvalues,yvalues)
    i += 1
    
plt.title("Saturn density distribution")
plt.xlabel("Radius/km")
plt.ylabel("Density/g $cm^-3$")
    
plt.show()
