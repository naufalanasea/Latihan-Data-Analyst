import streamlit as st

# Import visualisasi data
from bike_sharing import (
    trend_chart,
    bar_chart,
    pie_chart,
    line_chart,
    map_chart,
)

# Buat app streamlit
st.set_page_config(layout="wide")

# Tambahkan visualisasi data ke app streamlit
st.title("Analisis Penggunaan Sepeda Berbagi di Kota Jakarta")

st.subheader("Tren Penggunaan Sepeda Berbagi")
st.plotly_chart(trend_chart)

st.subheader("Penggunaan Sepeda Berbagi Berdasarkan Cuaca")
st.bar_chart(bar_chart)

st.subheader("Penggunaan Sepeda Berbagi Berdasarkan Hari Libur")
st.pie_chart(pie_chart)

st.subheader("Penggunaan Sepeda Berbagi Berdasarkan Waktu")
st.line_chart(line_chart)

st.subheader("Penggunaan Sepeda Berbagi Berdasarkan Lokasi")
st.map(map_chart)