import osmnx as ox
import pandas as pd

df_bj = pd.read_csv('数据/北京数据.csv')

lon_max, lon_min = df_bj.lon.max(), df_bj.lon.min()
lat_max, lat_min = df_bj.lat.max(), df_bj.lat.min()

lon_max, lon_min = lon_max + 0.001, lon_min - 0.001
lat_max, lat_min = lat_max + 0.001, lat_min - 0.001

G = ox.graph.graph_from_bbox(lon_max, lon_min, lat_max, lat_min, network_type='drive')

ox.plot_graph(G, show=True)