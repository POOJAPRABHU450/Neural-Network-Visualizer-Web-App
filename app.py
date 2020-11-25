
import streamlit as st
import json
import requests
import matplotlib.pyplot as plt
import numpy as np

URI = 'http://127.0.0.1:5000'

st.title("Neural Network")
st.sidebar.markdown("Input Image")

if st.button('Get random prediction'):
    response = requests.post(URI, data={})
    response = json.loads(response.text.decode())
    preds = response.get('predictions')
    image = response.get('image')
    image = np.reshape(image,(28,28))
    
    

