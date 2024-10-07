import streamlit as st

# st.session_state is a dict that stores info for the length of the session
# if key "messages" not in session state
# messages is self-defined
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

# writes message to page
for msg in st.session_state.messages:
    # chat_message creates the bubble with param name
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    print(st.session_state.messages)
    