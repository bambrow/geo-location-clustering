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

    df = pd.read_csv(sys.argv[1], names=['lat','lon'])
    print "There are", len(df), "rows in this dataset."

    land_color = '#f5f5f3'
    water_color = '#cdd2d4'
    coastline_color = '#f5f5f3'
    border_color = '#999999'
    state_color = '#cccccc'
    meridian_color = '#eaeaea'
    marker_fill_color = '#333333'
    marker_edge_color = 'None'

    fig = plt.figure(figsize=(20, 10))
    ax = fig.add_subplot(111, axisbg='#ffffff', frame_on=False)
    ax.set_title(sys.argv[3], fontsize=18, color='#333333')

    m = Basemap(projection='mill', resolution='f', llcrnrlat=30, urcrnrlat=50, llcrnrlon=-125, urcrnrlon=-105)
    m.drawmapboundary(color=border_color, fill_color=water_color)
    m.drawcoastlines(color=coastline_color)
    m.drawstates(color=state_color)
    m.drawcountries(color=border_color)
    m.fillcontinents(color=land_color, lake_color=water_color)
    m.drawparallels(np.arange(-90., 90., 5.), labels=[1,0,0,0], color=meridian_color, fontsize=10)
    m.drawmeridians(np.arange(0., 360., 5.), labels=[0,0,0,1], color=meridian_color, fontsize=10)

    x, y = m(df['lon'].values, df['lat'].values)
    m.scatter(x, y, s=.5, color=marker_fill_color, edgecolor=marker_edge_color, alpha=1, zorder=3)

    plt.savefig(sys.argv[2], dpi=300, bbox_inches='tight', pad_inches=0.1)
    plt.show()


