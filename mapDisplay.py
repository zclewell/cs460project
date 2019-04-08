# Libraries
import pandas as pd
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

# Set the dimension of the figure
my_dpi = 96
plt.figure(figsize=(2600/my_dpi, 1800/my_dpi), dpi=my_dpi)

data = pd.read_csv('./loc.csv')

# Make the background map
m = Basemap(llcrnrlon=-180, llcrnrlat=-65, urcrnrlon=180, urcrnrlat=80)
m.drawmapboundary(fill_color='#A6CAE0', linewidth=0)
m.fillcontinents(color='grey', alpha=0.3)
m.drawcoastlines(linewidth=0.1, color="white")

# prepare a color for each point depending on the continent.
data['labels_enc'] = pd.factorize(data['country'])[0]

# Add a point per position
m.scatter(data['long'], data['lat'], alpha=0.4, c=data['labels_enc'], cmap="Set1")

# copyright and source data info
# plt.text(-170, -58, 'Where people talk about #Surf\n\nData collected on twitter by @R_Graph_Gallery during 300 days\nPlot realized with Python and the Basemap library',
#          ha='left', va='bottom', size=9, color='#555555')

# Save as png
plt.savefig('ipSource.png', bbox_inches='tight')
plt.show()
