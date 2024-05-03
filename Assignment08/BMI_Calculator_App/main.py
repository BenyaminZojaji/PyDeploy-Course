import streamlit as st
from os import path
from assets import *



def calculate_bmi(weight, height):
    return weight / ((height / 100) ** 2)


def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"


st.title('BMI Calculator')

weight = st.number_input("Enter your weight (kg):", min_value=1.0, placeholder='eg. 68', value=None, format="%.2f")
height = st.number_input("Enter your height (cm):", min_value=1.0, placeholder='eg. 178', value=None, format="%.2f")

if st.button("Calculate BMI"):
    if height > 0 and weight > 0:
        bmi_value = calculate_bmi(weight, height)
        bmi_category = get_bmi_category(bmi_value)

        st.write(f"Your BMI is: {bmi_value:.2f}")
        st.write(f"Category: {bmi_category}")
        image_path = path.join('assets', f'{(bmi_category).lower()}.jpg')
        st.image(image_path, caption=bmi_category)
    else:
        st.error("Please enter valid values for height and weight.")
        