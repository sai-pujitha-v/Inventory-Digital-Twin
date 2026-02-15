# Inventory Digital Twin 📦

A digital twin software that replicates warehouse stock levels in a 3D interface for real-time logistical visibility and optimization.

## Description
A digital twin software that replicates warehouse stock levels in a 3D interface for real-time logistical visibility and spatial optimization using SQL-driven data mapping.

## Key Features
- **Spatial Mapping:** Visualizes stock placement within a virtual 3D warehouse grid.
- **Stock Predictive Analysis:** Simulates future inventory levels based on current supply chain velocity.
- **Automated Reordering:** Logic-driven triggers that flag low-stock items in the virtual twin.

## Tech Stack
- **Language:** Python
- **Libraries:** Streamlit, SQLAlchemy, Plotly (3D), Pandas
- **Database:** SQLite/PostgreSQL for persistent state management.

## Engineering Logic
- **Backend:** The system uses SQLAlchemy ORM to map physical coordinates (Shelf, Row, Bin) to a relational database, creating a "Digital Shadow" of every item.
- **Software Engine:** A Streamlit dashboard utilizes Plotly 3D scatter plots to render a navigable map of the warehouse, highlighting high-traffic zones and bottlenecks.
