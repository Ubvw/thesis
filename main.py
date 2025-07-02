import streamlit as st

pages = {
    "Landing": [
        st.Page("landing_page.py", title="Landing Page", icon="🏠"),
    ],
    "Your account": [
        st.Page("dashboard.py", title="Fraud Detection Dashboard", icon="🛡️"),
    ]
}

pg = st.navigation(pages, position="hidden")
pg.run() 