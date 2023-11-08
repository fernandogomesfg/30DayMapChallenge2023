# Importancao do osmnx e matplotlib
import osmnx as ox
import matplotlib.pyplot as plt

distrito = "Cidade de Inhambane"

# pega as vias de acesso
vias_de_acesso = ox.graph_from_place(distrito, network_type="all")

# Mostra a rede de vias de acesso
fig,ax = ox.plot_graph(vias_de_acesso)

# Salva as vias de acesso em um arquivo Shapefile
ox.save_graph_shapefile(vias_de_acesso, filepath='vias_de_acesso_inhambane')