# Reference: 
# https://github.com/gboeing/data-visualization/tree/master/location-history

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print >> sys.stderr, "Usage: {0} <input> <output> <title>".format(sys.argv[0])
        exit(-1)

    df = pd.read_csv(sys.argv[1], names=['lat','lon','group'])
    print "There are", len(df), "rows in this dataset."

    land_color = '#f5f5f5'
    water_color = '#cdd2d4'
    coastline_color = '#f5f5f5'
    border_color = '#757575'
    state_color = '#b0bec5'
    meridian_color = '#cfd8dc'
    marker_fill_color = ['#2196f3','#f44336','#4caf50','#000000','#ffeb3b']
    marker_edge_color = 'None'
    center_fill_color = '#5d4037'
    center_edge_color = 'None'

    fig = plt.figure(figsize=(10, 5))
    ax = fig.add_subplot(111, axisbg='#ffffff', frame_on=False)
    ax.set_title(sys.argv[3], fontsize=10, color='#333333')

    m = Basemap(projection='mill', resolution='i', llcrnrlat=30, urcrnrlat=50, llcrnrlon=-125, urcrnrlon=-105)
    m.drawmapboundary(color=border_color, fill_color=water_color)
    m.drawcoastlines(color=coastline_color)
    m.drawstates(color=state_color)
    m.drawcountries(color=border_color)
    m.fillcontinents(color=land_color, lake_color=water_color)
    m.drawparallels(np.arange(-90., 90., 5.), labels=[1,0,0,0], color=meridian_color, fontsize=7)
    m.drawmeridians(np.arange(0., 360., 5.), labels=[0,0,0,1], color=meridian_color, fontsize=7)

    for i in range(5):
        dfp = df.loc[lambda df: df.group == i, :]
        x, y = m(dfp['lon'].values, dfp['lat'].values)
        m.scatter(x, y, s=.5, color=marker_fill_color[i], edgecolor=marker_edge_color, alpha=1, zorder=3)

    dfc = df.loc[lambda df: df.group == -1, :]
    xc, yc = m(dfc['lon'].values, dfc['lat'].values)
    m.scatter(xc, yc, s=60, marker='P', color=center_fill_color, edgecolor=center_edge_color, alpha=1, zorder=3)

    plt.savefig(sys.argv[2], dpi=300, bbox_inches='tight', pad_inches=0.1)
    plt.show()


