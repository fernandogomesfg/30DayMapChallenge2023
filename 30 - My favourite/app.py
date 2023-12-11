import osmnx as ox

distrito = "Maputo"

# pega as vias de acesso
vias_de_acesso = ox.graph_from_place(distrito)

# Mostra a rede de vias de acesso
fig,ax = ox.plot_graph(vias_de_acesso)
