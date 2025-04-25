import streamlit as st
import numpy as np
import joblib  # or import your model loader if different

# Load your trained model
model = joblib.load("model_to_upload_on_streamlit.pkl")  # Update with your model path

# Example output feature names (replace with your actual list)
output_feature_names = [
    "Front Left Blank holder Pressure-Kg/cm",
    "Front Right Blank holder Pressure Kg/cm",
    "Rear Left Blank holder Pressure Kg/cm",
    "Rear Right Blank holder Pressure Kg/cm",
    "Inner Setting-mm",
    "Outer Setting mm"
]

# Input form
st.title("Best Possible AI Setting")

# Input from user
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

st.write("### Continuous Features")
# Continuous input features (default values can be adjusted)
mn = st.number_input("Mn%", value=0.072, format="%.3f")
p = st.number_input("p%", value=0.009, format="%.3f")
s = st.number_input("S%", value=0.003, format="%.3f")
si = st.number_input("Si%", value=0.002, format="%.3f")
al = st.number_input("Al%", value=0.0, format="%.3f")
ti = st.number_input("Ti%", value=0.0, format="%.3f")
ys = st.number_input("YS (Mpa)", value=159)
uts = st.number_input("UTS (Mpa)", value=298)
el = st.number_input("El%", value=43)
r_bar = st.number_input("R Bar", value=2.24, format="%.2f")

# Create input array in the correct order:
input_array = np.array([[remark_crack_val, remark_wrinkle_val, oiling_val,
                          bull_ring_val, fmb_rmb_val,
                          mn, p, s, si, al, ti, ys, uts, el, r_bar]])

# Prediction button
if st.button("Predict"):
    prediction = model.predict(input_array)
    st.subheader("Prediction Output")

    # Ensure prediction is a 2D array
    prediction = prediction.reshape(1, -1)

    # Display each predicted value rounded to 1 decimal place
    for i, feature in enumerate(output_feature_names):
        rounded_value = round(float(prediction[0][i]), 1)
        st.write(f"**{feature}:** {rounded_value:.1f}")
