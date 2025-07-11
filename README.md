# telemetry-data-analysis
Analyzed IoT telemetry data from manufacturing devices. Flattened complex JSON using Python, explored trends in Excel, and visualized device health metrics using Tableau.


# IoT Telemetry Data Analysis

📊 **Project Overview**  
This project explores telemetry data from manufacturing devices in an industrial setting. The original dataset came in the form of a large, deeply nested JSON file (~160,000+ rows). I cleaned, flattened, and analyzed this data using Python and then created an interactive dashboard in Tableau to visualize key trends such as device health and temperature anomalies.

---

## 🧠 Objectives

- Flatten and clean complex telemetry data in JSON format
- Identify trends and anomalies in device performance
- Create interactive visualizations for business stakeholders
- Practice real-world data handling and dashboard storytelling

---

## 🧰 Tools Used

- **Python (pandas, json)** – to flatten and export the data
- **Excel** – for preliminary classification and data exploration
- **Tableau** – to build the final interactive dashboard

---

## 🗃️ Dataset Description

Each row in the dataset represents telemetry information from a device in a factory. Some key fields include:

- `deviceID`, `deviceType`
- `timestamp`
- `location`: country, city, area, factory, section
- `data.status`: health of the device
- `data.temperature`: temperature reading

The original dataset was in nested JSON format and was flattened using Python before visualization.

---

## ⚙️ Process Summary

1. **Loading Data:** Parsed the JSON file in Python
2. **Flattening:** Used `pandas.json_normalize()` to create a tabular structure
3. **Exploration:** Performed basic filtering and checks in Excel
4. **Visualization:** Built a Tableau dashboard to highlight patterns in device health and temperature

---

## 📊 Dashboard Insights


- The majority of *unhealthy* devices were found in the `daikibo-factory-meiyo` location
- CNC and Laser Welder devices showed more frequent health issues
- Patterns suggest the need for targeted maintenance in specific factory sections

---

## 🧪 Sample Code

```python
import pandas as pd
import json

with open("daikibo-telemetry-data.json", encoding='utf-8') as f:
    data = json.load(f)

df = pd.json_normalize(data)
df.to_csv("flattened_data.csv", index=False)
