import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(
    page_title="Braunkohleförderung",
    page_icon="chart_with_upwards_trend",
    )

data = {
  "Jahr": ["1970", "1980", "1990", "2000", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2020", "2021", "2022"],
  "Volksrepublik China": ["15.4", "24.3", "45.5", "47.7", "97.4", "115", "115.5", "125.3", "136.3", "145", "147", "145", "140", "140", "145", "150", "260", "299", "325"],
  "Indonesien": ["0", "0", "0", "13.8", "28", "38", "38.2", "40", "51.3", "60", "65", "60", "60", "60", "60", "60", "118.1", "128.6", "140"],
  "Deutschland": ["369", "387.9", "356.5", "167.7", "180.4", "175.3", "169.9", "169.4", "176.5", "185.4", "183", "178.2", "178.1", "171.5", "171.3", "166.3", "107.4", "126.3", "130.8"],
  "Russland": ["116.2", "141.5", "138.5", "87.8", "71.3", "82", "68.2", "76", "77.6", "77.9", "73", "70", "73.2", "73.7", "75", "80", "73.3", "75", "89"],
  "Türkei": ["4", "14.5", "44.4", "60.9", "70", "81.5", "75.6", "70", "71", "70", "57.5", "62.6", "56.1", "70.2", "71.5", "85", "71.6", "80.1", "80.9"],
  "Polen": ["32.8", "36.9", "67.6", "59.5", "57.5", "59.6", "57.1", "56.5", "62.8", "64.3", "65.8", "63.9", "63.1", "60.2", "61.2", "58.6", "46", "52.4", "54.6"],
  "Indien": ["3.5", "5", "14.1", "24.2", "32.8", "32.2", "34.1", "37.7", "42.3", "46.5", "44.3", "47.2", "43.8", "45.3", "46.7", "45.3", "37.9", "47.5", "44.8"],
  "Vereinigte Staaten": ["5.4", "42.8", "79.9", "77.6", "71.2", "68.6", "65.8", "71", "73.6", "71.6", "70.1", "72.1", "64.3", "64.7", "61.2", "58.6", "44.8", "43", "43.1"],
  "Australien": ["24.2", "32.9", "46", "67.3", "72.3", "72.4", "68.3", "68.8", "66.7", "69.1", "59.9", "58", "61", "59.7", "56.1", "45.1", "40.4", "42.3", "39.1"],
  "Bulgarien": ["28.8", "29.9", "31.5", "26.3", "25.4", "26.2", "27.3", "27.1", "34.5", "31", "26.5", "31.3", "35.9", "31.2", "34.4", "30.3", "22.3", "28.3", "35.5"],
  "Serbien": ["13.5", "22.7", "36.9", "33.9", "29.8", "30.4", "38.3", "37.8", "41.1", "38.2", "40.3", "29.7", "37.7", "38.4", "39.8", "37.5", "39.7", "36.4", "35.1"],
  "Tschechien": ["77", "90.1", "76", "50.3", "54.5", "46.8", "45.6", "43.9", "46.8", "43.7", "40.6", "38.3", "38.3", "38.6", "39.3", "39.2", "29.4", "29.3", "33.4"],
  "Rumänien": ["14.2", "26.5", "33.7", "29", "35.5", "32.1", "28.4", "27.7", "32.9", "34.1", "24.7", "23.6", "25.5", "23", "25.7", "23.6", "15", "17.7", "18.2"],
  "Laos": ["", "", "", "", "", "", "", "", "", "", "0.4", "0", "4.5", "13.1", "13.4", "15.9", "14.4", "13.6", "15.4"],
  "Griechenland": ["7.9", "23.2", "51.9", "63.9", "64.4", "65.7", "61.8", "53.6", "58.4", "62.4", "54", "50.4", "45.6", "32.3", "37.7", "36.1", "13.9", "12.1", "13.7"],
  "Thailand": ["0.4", "1.5", "12.4", "17.8", "18.2", "18.3", "17.6", "18.3", "21.3", "18.1", "18.1", "18", "15.2", "17", "16.3", "14.9", "13.3", "14.2", "13.6"],
  "Bosnien und Herzegowina": ["", "", "", "", "", "", "", "", "7.1", "7", "11.8", "11.7", "12.2", "13.6", "13.8", "14", "13.6", "12.8", "13.3"],
  "Mongolei": ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "9.8", "9", "9.5"],
  "Kosovo": ["3.1", "5.2", "8.5", "3", "6.7", "7", "7.9", "8", "8.2", "8", "8.2", "7.2", "8.2", "8.8", "7.6", "7.2", "8.5", "8.5", "8.3"],
  "Kanada": ["3.5", "6", "9.4", "11.2", "10.5", "9.9", "10.6", "10.3", "9.7", "9.5", "9", "8.5", "8.4", "10", "9.4", "7.7", "7.4", "8.3", "6.4"],
  "Nordkorea": ["5.2", "10", "10.6", "7.2", "9", "9", "9", "7", "7.6", "7", "7", "7", "7", "7", "", "", "", "", ""],
  "Ungarn": ["23.7", "22.6", "15.8", "14", "9.8", "9.4", "9", "9", "9.5", "9.3", "9.6", "9.6", "9.3", "9.2", "8", "7.9", "", "", ""]
}

df = pd.DataFrame(data)

# Melt the DataFrame to long format for Altair
df_melted = df.melt(id_vars='Jahr', var_name='Land', value_name='Value')

# Convert 'Value' column to numeric
df_melted['Value'] = pd.to_numeric(df_melted['Value'])

# Streamlit app
st.title(':material/globe_asia: Braunkohleförderung weltweit')
st.header(':material/timeline: Verlauf der Braunkohle-Fördermenge nach Land im Zeitraum von 1970 bis 2022:')

# Auswahl der Länder
selected_countries = st.multiselect(
    'Wähle Länder aus:', 
    df_melted['Land'].unique(), 
    default=['Deutschland', 'Volksrepublik China', 'Russland']
)

# Filter die Daten basierend auf der Auswahl
filtered_df = df_melted[df_melted['Land'].isin(selected_countries)]

# Create the Altair chart
chart = alt.Chart(filtered_df).mark_line(point=True).encode(
    x='Jahr',
    y=alt.Y('Value', title='Fördermenge in Mio. t'),
    color='Land',
    tooltip=['Jahr', 'Land', 'Value']
).properties(
    title='Braunkohleförderung nach Land in Millionen Tonnen',
).interactive()


container = st.container(border=True)

container.altair_chart(chart, use_container_width=True)


st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('')
# ... second chart ...

st.header(':material/percent: Prozentualer Anteil der Länder an der Braunkohleförderung für das ausgewählte Jahr zwischen 1970 und 2022:')
df_melted2 = df.melt(id_vars='Jahr', var_name='Land', value_name='Foerderung')

# Wandle 'Foerderung' in numerische Werte um
df_melted2['Foerderung'] = pd.to_numeric(df_melted2['Foerderung'])  # Diese Zeile hinzugefügt

# Jahreszahl-Auswahl
selected_year = st.selectbox('Wähle ein Jahr aus:', df_melted2['Jahr'].unique())

# Filtere die Daten basierend auf der ausgewählten Jahreszahl
filtered_df2 = df_melted2[df_melted2['Jahr'] == selected_year]

# Berechne den prozentualen Anteil jedes Landes an der Gesamtförderung
total_foerderung = filtered_df2['Foerderung'].sum()
filtered_df2['Prozent'] = (filtered_df2['Foerderung'] / total_foerderung) * 100

# Erstelle das Altair Donut-Diagramm
chart2 = alt.Chart(filtered_df2).mark_arc(innerRadius=100).encode(
    theta=alt.Theta(field="Prozent", type="quantitative", stack=True),
    color=alt.Color(field="Land", type="nominal"),  # "Land" zu "Land" geändert
    tooltip=['Land', 'Foerderung', alt.Tooltip('Prozent', format=".1f")]  # Auch hier im Tooltip
).properties(
    title=f'Braunkohleförderung im Jahr {selected_year}'
)

# Zeige das Diagramm in Streamlit an

container = st.container(border=True)

container.altair_chart(chart2, use_container_width=True)


st.markdown('')#
st.markdown('')

with st.expander("Quellen"):
    st.link_button('Enerdata',"https://energiestatistik.enerdata.net/kohle-braunkohle/kohle-produktion-data.html")
    st.link_button('Wikipedia',"https://de.wikipedia.org/wiki/Kohle/Tabellen_und_Grafiken")
    st.link_button("Statistisches Bundesamt","https://www.destatis.de/Europa/DE/Thema/Umwelt-Energie/Braunkohle.html")