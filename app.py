import streamlit as st
from neuron import Neuron

st.image("img_neurona.jpg", width=400)
st.header("Neuron Simulator")

inputs = st.slider("Choose the number of inputs/weights for the neuron", 1, 10, 1)

st.subheader("Weights")
w = []
columns_width_weights = st.columns(inputs)

for i in range(inputs):
    w.append(i)

    with columns_width_weights[i]:
        st.markdown(f"w<sub>{i}</sub>", unsafe_allow_html=True)
        w[i] = st.number_input(f"w{i}", label_visibility="collapsed", value=0.0)
    

st.text("Weights: " + str(w))

st.subheader("Inputs")
x = []
columns_width_inputs = st.columns(inputs)

for i in range(inputs):
    x.append(i)

    with columns_width_inputs[i]:
        st.markdown(f"x<sub>{i}</sub>", unsafe_allow_html=True)
        x[i] = st.number_input(f"x{i}", label_visibility="collapsed", value=0.0)

st.text("Inputs: " + str(x))

col1, col2 = st.columns(2)

with col1:
    st.subheader("Bias")
    b = st.number_input("Enter the value of the bias", value=0.0)

with col2:
    st.subheader("Select the activation function")
    
    activation_function = st.selectbox("Choose the activation function",
        ("Sigmoide", "ReLU", "Hiperbolic Tangent", "Binary Step"))
    

activation_function_map = {
    "Sigmoide": "sigmoid",
    "ReLU": "relu",
    "Hiperbolic Tangent": "tanh",
    "Binary Step": "binary_step"
}

if st.button("Calculate Output"):
    neuron = Neuron(weights=w, bias=b, activation_function=activation_function_map[activation_function])
    try:
        output = neuron.run(x)
        st.success(f"Neuron output: {output}")
    except ValueError as e:
        st.error(e)