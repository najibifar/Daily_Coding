import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.show()

wrold = gpd.read_file('ne_110m_admin_0_countries.shp')

wrold.plot(edgecolor = 'pink')
plt.title("world map with country borders")
plt.show()
