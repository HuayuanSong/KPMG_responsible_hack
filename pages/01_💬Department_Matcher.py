import streamlit as st
from streamlit import session_state as session
import pickle
import sister
#from streamlit_extras.app_logo import add_logo

# Configure Streamlit page
st.set_page_config(page_title="Department Matcher💬", page_icon="🎶")

#add_logo("logo.png", height=300)
st.title("Department Matcher💬")
st.markdown("Automatically label messages with relevant department with the power of NLP.")

inputs = st.radio(
    "Please choose source of messages:",
    ("Load all new messages from WhatsApp", "Insert message"),
)
label_list = [
    "Comms",
    "Nutrition",
    "Business",
    "Data&Tech",
    "ECD",
    "M&L",
    "Sales",
    "All departments",
    "Network Acquision",
    "Tech",
]
bert_embedding = sister.BertEmbedding(lang="en")
loaded_model = pickle.load(open("knnpickle_file_eng", "rb"))
if inputs == "Load all new messages from WhatsApp":
    example_mes = [
        "Happy mashuja day to all managers who are doing their best to ensure the safety of the childrens in there daycares,this is your day,we know it's not easy bt we celebrate you guys",
        "How do I use the client app?",
        "Your business is important as it ensures that children have a safe space and are taken care of, mothers go to work and you earn a decent income from your business.",
        "I know someone who wants to become a manager for the client",
        "what is some nutritious food I can feed my child",
    ]
    fetch = st.button(
        "📥 Categorize new messages from WhatsApp",
        help="Messages from WhatsApp group chat will be loaded",
    )
    if fetch:
        with st.spinner("Getting all new messages..."):
            with st.spinner("Processing..."):
                with st.expander("New messages from WhatsApp", expanded=True):
                    for i, ele in enumerate(example_mes):
                        label = loaded_model.predict([bert_embedding(example_mes[i])])
                        st.markdown(f"**User {i+1} - Dept: {label_list[label[0]]}**")
                        st.markdown(ele)
                        st.markdown("_______________")

        submitted = st.button(
            "✔️ Submit to departments",
            help="Submit messages to the labeled departments",
        )
        if submitted:
            st.success("Messages have been sent to the departments", icon="✅")

if inputs == "Insert message":
    topic = st.text_area(
        "Insert your message below and it will be matched with the relevant department",
        value="what is some nutritious food I can feed my child",
    )
    submitted = st.button(
        "✔️ Submit",
        help="Submit message for department match",
    )

    if submitted:
        with st.spinner("Processing..."):
            label = loaded_model.predict([bert_embedding(topic)])
            st.markdown(f"Department: **{label_list[label[0]]}**")
