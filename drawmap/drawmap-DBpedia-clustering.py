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
    meridian_color = '#eceff1'
    marker_fill_color = ['#f44336','#e91e63','#9c27b0','#3f51b5','#2196f3','#00bcd4','#009688','#4caf50','#cddc39','#ffeb3b','#ffc107','#ff5722']
    marker_edge_color = 'None'
    center_fill_color = '#5d4037'
    center_edge_color = 'None'

    fig = plt.figure(figsize=(14, 7))
    ax = fig.add_subplot(111, axisbg='#ffffff', frame_on=False)
    ax.set_title(sys.argv[3], fontsize=15, color='#333333')

    m = Basemap(projection='kav7', lon_0=0, resolution='i')
    m.drawmapboundary(color=border_color, fill_color=water_color)
    m.drawcoastlines(color=coastline_color)
    m.drawcountries(color=border_color)
    m.fillcontinents(color=land_color, lake_color=water_color)
    m.drawparallels(np.arange(-90., 90., 30.), labels=[1,0,0,0], color=meridian_color, fontsize=10)
    m.drawmeridians(np.arange(0., 360., 60.), labels=[0,0,0,1], color=meridian_color, fontsize=10)

    for i in range(12):
        dfp = df.loc[lambda df: df.group == i, :]
        x, y = m(dfp['lon'].values, dfp['lat'].values)
        m.scatter(x, y, s=1, color=marker_fill_color[i], edgecolor=marker_edge_color, alpha=1, zorder=3)

    dfc = df.loc[lambda df: df.group == -1, :]
    xc, yc = m(dfc['lon'].values, dfc['lat'].values)
    m.scatter(xc, yc, s=120, marker='P', color=center_fill_color, edgecolor=center_edge_color, alpha=1, zorder=3)

    plt.savefig(sys.argv[2], dpi=300, bbox_inches='tight', pad_inches=0.1)
    plt.show()


