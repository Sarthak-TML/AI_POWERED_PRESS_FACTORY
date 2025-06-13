import streamlit as st
import numpy as np
import joblib  # or import your model loader if different

# Load your trained model
model = joblib.load("streamlitmodel-inner-outter-input.pkl")  # Update with your model path

# Updated output feature names (excluding inner/outer setting)
output_feature_names = [
    "Front Left Blank holder Pressure-Kg/cm",
    "Front Right Blank holder Pressure Kg/cm",
    "Rear Left Blank holder Pressure Kg/cm",
    "Rear Right Blank holder Pressure Kg/cm"
]

# Title
st.title("Press-1 Best Possible Setting through AI Program")

# Categorical Inputs
remark_crack = st.selectbox("Remark (Crack)", options=["No Crack", "Crack"])
remark_wrinkle = st.selectbox("Remark (Wrinkle)", options=["No Wrinkle", "Wrinkle"])
oiling = st.selectbox("Oiling M/c.- Oil Pattern, Program No.", options=["yes,86", "yes,12"])
bull_ring = st.selectbox("Bull ring.", options=["ba", "bb"])
fmb_rmb = st.selectbox("FMB/RMB", options=["fmb", "rmb"])

# Convert categorical selections to numeric values
remark_crack_val = 0 if remark_crack == "No Crack" else 1
remark_wrinkle_val = 0 if remark_wrinkle == "No Wrinkle" else 1
oiling_val = 0 if oiling == "yes,86" else 1
bull_ring_val = 0 if bull_ring == "ba" else 1
fmb_rmb_val = 0 if fmb_rmb == "fmb" else 1

# Continuous Inputs
st.write("### Metallurgical Properties")
mn = st.number_input("Mn%", value=0.072, format="%.3f")
p = st.number_input("P%", value=0.009, format="%.3f")
s = st.number_input("S%", value=0.003, format="%.3f")
si = st.number_input("Si%", value=0.002, format="%.3f")
al = st.number_input("Al%", value=0.0, format="%.3f")
ti = st.number_input("Ti%", value=0.0, format="%.3f")
ys = st.number_input("YS (MPa)", value=159)
uts = st.number_input("UTS (MPa)", value=298)
el = st.number_input("El%", value=43)
r_bar = st.number_input("R Bar", value=2.24, format="%.2f")

# New inputs for Inner and Outer Setting
st.write("### Tool Settings")
inner_setting = st.number_input("Inner Setting (mm)", value=1664.00, format="%.2f")
outer_setting = st.number_input("Outer Setting (mm)", value=1390.00, format="%.2f")

# Create input array in the correct order
input_array = np.array([[remark_crack_val, remark_wrinkle_val, oiling_val,
                         bull_ring_val, fmb_rmb_val,
                         mn, p, s, si, al, ti, ys, uts, el, r_bar,
                         inner_setting, outer_setting]])

# Predict Button
if st.button("Predict"):
    prediction = model.predict(input_array)
    st.subheader("Prediction Output")

    prediction = prediction.reshape(1, -1)
    for i, feature in enumerate(output_feature_names):
        rounded_value = round(float(prediction[0][i]), 1)
        st.write(f"**{feature}:** {rounded_value:.1f}")

# Add this at the end of your script
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .footer:after {
        content:'Developed by Sarthak Kadam – Tata Motors AI/ML Intern';
        visibility: visible;
        display: block;
        position: relative;
        color: gray;
        text-align: center;
        padding: 10px;
    }
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

