import streamlit as st

st.title(" 📏 Length & 🌡️ Temperature Converter")
st.markdown("### Instantly convert Length and Temperature")
st.write("Welcome to the world of Conversion! Select a category, enter the value, and get the converted result in real time.")

# Define conversion factors (GLOBAL VARIABLES)
length_units = {
    "Meter": 1,
    "Kilometer": 0.001,
    "Centimeter": 100,
    "Millimeter": 1000,
    "Mile": 0.000621371,
    "Yard": 1.09361,
    "Foot": 3.28084,
    "Inch": 39.3701
}

temperature_conversions = {
    "Celsius to Fahrenheit": lambda c: (c * 9/5) + 32,
    "Celsius to Kelvin": lambda c: c + 273.15,
    "Fahrenheit to Celsius": lambda f: (f - 32) * 5/9,
    "Fahrenheit to Kelvin": lambda f: (f - 32) * 5/9 + 273.15,
    "Kelvin to Celsius": lambda k: k - 273.15,
    "Kelvin to Fahrenheit": lambda k: (k - 273.15) * 9/5 + 32
}

# Conversion Function
def convert_units(category, value, from_unit, to_unit):
    if category == "Length":
        return value * (length_units[to_unit] / length_units[from_unit])

    elif category == "Temperature":
        conversion_key = f"{from_unit} to {to_unit}"
        if conversion_key in temperature_conversions:
            return temperature_conversions[conversion_key](value)

    return None  # If conversion is invalid

# User selects conversion category
category = st.selectbox("Choose a category:", ["📏 Length", "🌡️ Temperature"])

# Input Section
if category == "📏 Length":
    from_unit = st.selectbox("Convert from:", list(length_units.keys()))
    to_unit = st.selectbox("Convert to:", list(length_units.keys()))
elif category == "🌡️ Temperature":
    from_unit = st.selectbox("Convert from:", ["Celsius", "Fahrenheit", "Kelvin"])
    to_unit = st.selectbox("Convert to:", ["Celsius", "Fahrenheit", "Kelvin"])

value = st.number_input("Enter value:", min_value=0.0, format="%.2f")

# Convert Button
if st.button("Convert"):
    result = convert_units(category, value, from_unit, to_unit)
    if result is not None:
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
    else:
        st.error("Invalid conversion selected!")

st.write("🚀 Made with ❤️ using Streamlit")
