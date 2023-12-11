import streamlit as st
from streamlit_folium import folium_static
import folium

# Coordenadas do Vaticano
vaticano_coords = (41.9022, 12.4537)

# Criação do mapa Folium centrado no Vaticano
mapa = folium.Map(location=vaticano_coords, zoom_start=15)

# Adiciona marcador para a Basílica de São Pedro com um ícone personalizado
folium.Marker(
    location=(41.9021493,12.4511064),
    popup="Basílica de São Pedro",
    icon=folium.Icon(color="blue", icon="info-sign"),
).add_to(mapa)

# Adiciona marcador para os Museus do Vaticano com um ícone personalizado
folium.Marker(
    location=(41.9058542, 12.4517364),
    popup="Museus do Vaticano",
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(mapa)

# Adiciona marcador para a Capela Sistina com um ícone personalizado
folium.Marker(
    location=(41.9029508,12.4519086),
    popup="Capela Sistina",
    icon=folium.Icon(color="red", icon="info-sign"),
).add_to(mapa)

# Exibe o mapa no Streamlit
st.title("Recursos Turísticos do Vaticano")
st.write("Mapa destacando alguns pontos turísticos no Vaticano.")
folium_static(mapa)
