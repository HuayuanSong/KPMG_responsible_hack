import streamlit as st
from streamlit import session_state as session
import pickle
import sister
#from streamlit_extras.app_logo import add_logo
from transformers import pipeline
import operator


# Configure Streamlit page
st.set_page_config(page_title="Insights Dashboard📊", page_icon="📊")

import numpy as np
from transformers import Auclientkenizer, AutoModelWithLMHead

tokenizer = Auclientkenizer.from_pretrained("mrm8488/t5-small-finetuned-emotion")

model = AutoModelWithLMHead.from_pretrained("mrm8488/t5-small-finetuned-emotion")

def get_emotion(text):
    input_ids = tokenizer.encode(text + '</s>', return_tensors='pt')

    output = model.generate(input_ids=input_ids,
               max_length=2)
    dec = [tokenizer.decode(ids) for ids in output]
    label = dec[0]
    return label


#add_logo("logo.png", height=300)
st.title("Insights Dashboard📊")
st.markdown("Get insights about customer satisfaction using emotion and sentiment models.")
inputs = st.radio(
    "Please choose source of messages:",
    ("Insert message", "Load all new messages from WhatsApp"),
)
example_mes = [
        "Happy mashuja day to all managers who are doing their best to ensure the safety of the childrens in there daycares,this is your day,we know it's not easy bt we celebrate you guys",
        "How do I use the client app?",
        "Your business is important as it ensures that children have a safe space and are taken care of, mothers go to work and you earn a decent income from your business.",
        "I know someone who wants to become a manager for client",
        "what is some nutritious food I can feed my child",
    ]

if inputs == "Load all new messages from WhatsApp":
    fetch = st.button(
        "📥 Get insights from new WhatsApp messages",
        help="Messages from WhatsApp group chat will be loaded",
    )
    a = ""
    if fetch:
        with st.expander("View messages", expanded=False): 
            for i, ele in enumerate(example_mes):
                st.markdown(f"**User {i+1}:**")
                st.markdown(ele)
                st.markdown("_______________")

        with st.spinner("Processing..."):
            for i, ele in enumerate(example_mes):
                a += ele
                a += " "
            st.markdown(f"**Overall emotion: {get_emotion(a)[5:]}**")

if inputs == "Insert message":
    topic = st.text_area(
        "Insert your message below and the emotion will be classified",
        value="Help, my child is hungry!",
    )
    submitted = st.button(
        "✔️ Submit",
        help="Submit message for emotion classification",
    )

    if submitted:
        with st.spinner("Processing..."):
            st.markdown(f"**Overall emotion: {get_emotion(topic)[5:]}**")
     
st.markdown("**Parent satisfaction over time**")
with st.expander("The parent satisfaction is calculated as the sentiment scores over incoming WhatsApp messages on a given day.", expanded=True):  
    st.image("daplot.png")
        