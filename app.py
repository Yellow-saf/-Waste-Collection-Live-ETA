import streamlit as st
import pandas as pd
import numpy as np

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import GradientBoostingRegressor


# =========================
# PAGE SETTINGS
# =========================

st.set_page_config(
    page_title="Waste Collection Live ETA",
    page_icon="🚛",
    layout="wide"
)


# =========================
# LOAD DATA
# =========================

@st.cache_data
def load_data():
    return pd.read_csv("waste_collection_eta_dataset.csv")


df = load_data()


# =========================
# TRAIN ML MODEL
# =========================

@st.cache_resource
def train_model(data):

    features = [
        "Distance_km",
        "Traffic_Level",
        "Traffic_Delay_min",
        "Route_Condition",
        "Route_Delay_min",
        "Expected_Dwell_min",
        "Actual_Dwell_min",
        "Workload_Stops",
        "Customer_Time_Window",
        "Current_Location",
        "Dynamic_ETA"
    ]

    categorical = [
        "Traffic_Level",
        "Route_Condition",
        "Customer_Time_Window",
        "Current_Location"
    ]

    numeric = [
        "Distance_km",
        "Traffic_Delay_min",
        "Route_Delay_min",
        "Expected_Dwell_min",
        "Actual_Dwell_min",
        "Workload_Stops",
        "Dynamic_ETA"
    ]

    X = data[features]

    # Predict remaining ETA error
    y = data["Actual_ETA_min"] - data["Dynamic_ETA"]

    preprocessor = ColumnTransformer(
        transformers=[
            ("cat",
             OneHotEncoder(handle_unknown="ignore"),
             categorical),

            ("num",
             "passthrough",
             numeric)
        ]
    )

    model = Pipeline([
        ("preprocessor", preprocessor),

        ("model",
         GradientBoostingRegressor(
             n_estimators=150,
             learning_rate=0.05,
             max_depth=3,
             random_state=42
         ))
    ])

    model.fit(X, y)

    return model


model = train_model(df)


# =========================
# HYBRID ML ETA
# =========================

features = [
    "Distance_km",
    "Traffic_Level",
    "Traffic_Delay_min",
    "Route_Condition",
    "Route_Delay_min",
    "Expected_Dwell_min",
    "Actual_Dwell_min",
    "Workload_Stops",
    "Customer_Time_Window",
    "Current_Location",
    "Dynamic_ETA"
]

df["ML_Error_Correction"] = model.predict(
    df[features]
)

df["Hybrid_ML_ETA"] = (
    df["Dynamic_ETA"] +
    df["ML_Error_Correction"]
)


# =========================
# TITLE
# =========================

st.title("🚛 Waste Collection Live ETA System")

st.write(
    "Dynamic and Hybrid ML based ETA prediction "
    "for waste collection vehicles."
)


# =========================
# OVERVIEW
# =========================

st.header("📊 Project Overview")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Dataset Records", len(df))

with c2:
    st.metric(
        "Vehicles",
        df["Vehicle_ID"].nunique()
    )

with c3:
    st.metric(
        "Routes",
        df["Route_ID"].nunique()
    )

with c4:
    st.metric(
        "Features",
        len(df.columns)
    )


# =========================
# ETA PERFORMANCE
# =========================

st.header("⏱️ ETA Performance")

baseline_mae = np.mean(
    abs(
        df["Baseline_ETA"] -
        df["Actual_ETA_min"]
    )
)

dynamic_mae = np.mean(
    abs(
        df["Dynamic_ETA"] -
        df["Actual_ETA_min"]
    )
)

hybrid_mae = np.mean(
    abs(
        df["Hybrid_ML_ETA"] -
        df["Actual_ETA_min"]
    )
)

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "Baseline MAE",
        f"{baseline_mae:.2f} min"
    )

with c2:
    st.metric(
        "Dynamic ETA MAE",
        f"{dynamic_mae:.2f} min"
    )

with c3:
    st.metric(
        "Hybrid ML ETA MAE",
        f"{hybrid_mae:.2f} min"
    )


# =========================
# DATA
# =========================

st.header("📁 Dataset")

st.dataframe(
    df.head(20),
    use_container_width=True
)


# =========================
# LIVE ETA SIMULATOR
# =========================

st.header("🚦 Live ETA Simulator")

st.write(
    "Change the conditions below to simulate an ETA update."
)

c1, c2 = st.columns(2)

with c1:

    distance = st.slider(
        "Distance (km)",
        0.5,
        10.0,
        5.0,
        0.5
    )

    traffic = st.selectbox(
        "Traffic",
        ["Low", "Medium", "High"]
    )

    route = st.selectbox(
        "Route Condition",
        ["Normal", "Changed", "Blocked"]
    )

    expected_dwell = st.slider(
        "Expected Collection Time",
        3,
        8,
        5
    )


with c2:

    actual_dwell = st.slider(
        "Current Collection Time",
        2,
        20,
        7
    )

    workload = st.slider(
        "Vehicle Workload",
        10,
        60,
        40
    )

    time_window = st.selectbox(
        "Customer Time Window",
        ["Morning", "Afternoon", "Evening"]
    )

    location = st.selectbox(
        "Current Location",
        ["Zone A", "Zone B", "Zone C", "Zone D", "Zone E"]
    )


# =========================
# CONDITIONS
# =========================

traffic_delay = {
    "Low": 2,
    "Medium": 7,
    "High": 20
}[traffic]

route_delay = {
    "Normal": 0,
    "Changed": 5,
    "Blocked": 12
}[route]


base_time = np.ceil(
    (distance / 30) * 60
)

planned_eta = (
    base_time +
    expected_dwell
)

dwell_delay = max(
    actual_dwell - expected_dwell,
    0
)

dynamic_eta = (
    planned_eta +
    traffic_delay +
    dwell_delay +
    route_delay
)


# =========================
# ML PREDICTION
# =========================

simulation = pd.DataFrame([{
    "Distance_km": distance,
    "Traffic_Level": traffic,
    "Traffic_Delay_min": traffic_delay,
    "Route_Condition": route,
    "Route_Delay_min": route_delay,
    "Expected_Dwell_min": expected_dwell,
    "Actual_Dwell_min": actual_dwell,
    "Workload_Stops": workload,
    "Customer_Time_Window": time_window,
    "Current_Location": location,
    "Dynamic_ETA": dynamic_eta
}])


correction = model.predict(simulation)[0]

hybrid_eta = (
    dynamic_eta +
    correction
)


# =========================
# SHOW ETA
# =========================

st.subheader("🕒 Updated ETA")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "Planned ETA",
        f"{planned_eta:.1f} min"
    )

with c2:
    st.metric(
        "Dynamic ETA",
        f"{dynamic_eta:.1f} min"
    )

with c3:
    st.metric(
        "Hybrid ML ETA",
        f"{hybrid_eta:.1f} min"
    )


st.info(
    f"🤖 ML Correction: {correction:+.2f} minutes"
)


# =========================
# OPERATIONAL STATUS
# =========================

st.header("⚠️ Operational Status")

if workload > 50:
    st.error(
        "🚨 Vehicle workload is above safe limit."
    )
else:
    st.success(
        "✅ Vehicle workload is within safe limit."
    )


if route == "Blocked":
    st.error(
        "🚧 Route is blocked."
    )

elif route == "Changed":
    st.warning(
        "🔄 Route has changed."
    )

else:
    st.success(
        "🛣️ Route is normal."
    )


if traffic == "High":
    st.error(
        "🚦 Heavy traffic detected."
    )

elif traffic == "Medium":
    st.warning(
        "🚦 Moderate traffic detected."
    )

else:
    st.success(
        "🚦 Traffic is low."
    )


# =========================
# CUSTOMER MESSAGE
# =========================

st.header("📱 Customer Notification")

delay = hybrid_eta - planned_eta

if delay >= 15:

    st.error(
        "🚨 Major delay: Collection ETA has "
        "increased significantly."
    )

elif delay >= 5:

    st.warning(
        "⚠️ Delay update: Collection ETA has "
        "been updated."
    )

elif delay > 0:

    st.info(
        "🔄 ETA updated slightly."
    )

else:

    st.success(
        "✅ Collection is on schedule."
    )


# =========================
# FOOTER
# =========================

st.markdown("---")

st.caption(
    "Waste Collection Live ETA System | "
    "Hybrid Rule-Based + Machine Learning Prototype"
)