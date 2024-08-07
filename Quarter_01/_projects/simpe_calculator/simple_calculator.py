import streamlit as st

# Setting the title
st.title("Interactive Simple Calculator")

# Sidebar for user inputs
st.sidebar.header("Calculator Inputs")

# Getting input from the user and storing it into variables
# Using text_input for num1 to illustrate string handling and conversion
num1_input = st.sidebar.text_input("Please enter the first Number : ", value="0")
# Using number_input for num2 to directly accept numeric input
num2_input = st.sidebar.number_input("Please enter the second Number : ", value=0.0)

# Select operation
operation = st.sidebar.selectbox("Enter the operation (+, -, *, /) : ", ["+", "-", "*", "/"])

# Perform calculation and display result
try:
    # Convert num1 to float for arithmetic operations
    num1 = float(num1_input)
    num2 = float(num2_input)

    # Perform the selected operation
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error! Can't be divided by 0."

    # Display the result
    st.write(f"**Result:** {result}")
except ValueError:
    st.write("Please enter valid numbers for both inputs.")

# Add a footer
st.markdown("---")
st.write("Created with Streamlit")

# Optional: Add some styling
st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        background-color: #f0f2f6;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
