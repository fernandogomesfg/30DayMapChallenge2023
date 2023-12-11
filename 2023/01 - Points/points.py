import folium
from folium.plugins import MarkerCluster
from capitais_provinciais import capitais_provinciais  

# Cria um mapa de Moçambique
mapa = folium.Map(location=[-18.665695, 35.529562], tiles="Cartodb Positron", zoom_start=5, control_scale=True)

# Adiciona o GeoJson dos limites de MOZ
folium.GeoJson("mozambique_limites.geojson").add_to(mapa)

# Adiciona marcadores para as capitais provinciais
marker_cluster = MarkerCluster().add_to(mapa)
for capital, info in capitais_provinciais.items():
    folium.Marker([info["latitude"], info["longitude"]],
                  tooltip=f"Capital de {capital}: {info['capital']}").add_to(marker_cluster)

# Adiciona o botao de fullscreen    
folium.plugins.Fullscreen(
    position="topright",
    title="Expandir",
    title_cancel="Sair",
    force_separate_button=True,
).add_to(mapa)

# Grava o mapa em um arquivo HTML
mapa.save('mapa.html')
