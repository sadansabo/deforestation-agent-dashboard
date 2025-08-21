import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="🌍 Deforestation Agent Dashboard", layout="wide")

st.title("🌍 Deforestation Agent Dashboard")

# Sidebar navigation
st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", ["Overview", "Agent Reports", "Deforestation Map", "About"])

# ---------------------- Overview ----------------------
if page == "Overview":
    st.subheader("Overview of Deforestation Monitoring")
    st.write("""
        This dashboard shows deforestation alerts and agent reports.  
        Data is updated regularly via the connected repository.
    """)
    col1, col2, col3 = st.columns(3)
    col1.metric("Active Monitoring Regions", 12)
    col2.metric("Agents Reporting", 5)
    col3.metric("Total Alerts (Last 30 Days)", 27)

# ---------------------- Agent Reports ----------------------
elif page == "Agent Reports":
    st.subheader("Agent Reports")
    st.write("📊 Recent reports submitted by agents:")
    sample_data = {
        "Agent": ["A1", "A2", "A3", "A4"],
        "Region": ["North", "Central", "South", "West"],
        "Deforestation Alerts": [3, 5, 2, 6]
    }
    st.table(sample_data)

# ---------------------- Interactive Map ----------------------
elif page == "Deforestation Map":
    st.subheader("🗺️ Interactive Deforestation Map")

    # Initialize Folium map
    m = folium.Map(location=[9.0820, 8.6753], zoom_start=6, tiles="CartoDB positron")

    # Example regions with alerts
    alerts = [
        {"name": "North Region", "lat": 11.5, "lon": 8.0, "alerts": 3},
        {"name": "Central Region", "lat": 9.5, "lon": 7.5, "alerts": 5},
        {"name": "South Region", "lat": 6.5, "lon": 5.0, "alerts": 2},
    ]

    for alert in alerts:
        folium.Marker(
            location=[alert["lat"], alert["lon"]],
            popup=f"{alert['name']} - {alert['alerts']} alerts",
            icon=folium.Icon(color="red" if alert["alerts"] > 3 else "green"),
        ).add_to(m)

    # Display folium map in Streamlit
    st_map = st_folium(m, width=700, height=500)

# ---------------------- About ----------------------
elif page == "About":
    st.subheader("About This Dashboard")
    st.write("""
        ✅ Built with **Streamlit + Folium** on Hugging Face Spaces.  
        ✅ Shows live deforestation alerts and agent activity.  
        ✅ Optimized for monitoring and reporting environmental activities.
    """)
