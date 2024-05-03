import streamlit as st


if 'count' not in st.session_state:
    st.session_state.count = 0

col1, col2, col3 = st.columns(3)

with col1:
    minus_btn = st.button("➖", type='primary')

with col3:
    plus_btn = st.button("➕", type='primary')

if minus_btn:
    st.session_state.count -= 1

if plus_btn:
    st.session_state.count += 1

with col2:
    st.header(st.session_state.count)
