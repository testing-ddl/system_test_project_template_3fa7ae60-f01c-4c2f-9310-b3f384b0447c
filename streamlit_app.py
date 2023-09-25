import streamlit as st
from streamlit import components
import numpy as np
import pandas as pd
import requests

# helper function for blank streamlit lines
def V_SPACE(lines):
    for _ in range(lines):
        st.write('&nbsp;')


st.set_page_config(layout="wide")

####################
### INTRODUCTION ###
####################

row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns((.1, 2.3, .1, 1.3, .1))
with row0_1:
    st.title('Financial News Sentiment Analysis')
with row0_2:
    V_SPACE(1)
row3_spacer1, row3_1, row3_spacer2 = st.columns((.1, 3.2, .1))
with row3_1:
    st.subheader("Enter financial news text and click score to determine the sentiment")
    V_SPACE(1)
    
#################
### SELECTION ###
#################

with st.form("my_form"):
    fintext = st.text_input('Input text', 'there is a shortage of capital, and we need extra financing')
    scored = st.form_submit_button("Score")

results = list()

# Please change this URL to where your model API has been deployed or load the model from where it has been stored

api_url = "https://se-demo.domino.tech:443/models/6511ef8c3f90ce7a69ed7ed0/v/1/model"

api_token = "NZYHSbIhqQsWACR83T2GLS9BefdNIiOonJGUAzkay01PkKn96AdXO6ItlIwbMibg"

response = requests.post(api_url,
    auth=(
        api_token,
        api_token
    ),
    json = {
              "data": {
                "sentence": fintext
              }
            }
    )
results.append(response.json().get('result'))

### Results ###
result_text = "NA"
result_prob = -1

if results:
    result_text = results[0]['label']
    result_prob = round(results[0]['score'],4)
    
#################
### SHOW RESULTS ###
#################
 
row4_spacer1, row4_1, row4_spacer2 = st.columns((.2, 7.1, .2))
with row4_1:    
    st.subheader(f'The sentiment of this financial text is {result_text} with a probability of {result_prob}')
    V_SPACE(1)