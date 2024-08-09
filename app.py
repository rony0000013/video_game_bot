
# import getpass
# import os
import streamlit as st
from PIL import Image as PILImage
import io

from model import image, chat


st.set_page_config(page_title="Video Game Chat", page_icon="🎮")


st.title("🎮 Video Game chat 🕹️")
try:
    graph_image = image()
    image = PILImage.open(io.BytesIO(graph_image))
    st.image(image, caption='Graph Visualization', use_column_width="auto")
except Exception:
    # This requires some extra dependencies and is optional
    st.warning("Graph visualization requires additional dependencies.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Ask About Video Games"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        response = st.write_stream(chat(prompt))
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

