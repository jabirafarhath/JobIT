from matplotlib.style import reload_library
import pandas as pd
import pickle
from form import show_form
import streamlit as st

def load_model():
        reload_model = pickle.load(open('prediction_model.pkl','rb'))
        return reload_model

def predict(input):
    reload_model = load_model()
    result = reload_model.predict(input)
    return result
    

   








