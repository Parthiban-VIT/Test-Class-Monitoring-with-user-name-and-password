import streamlit as st


def login_page():

    st.markdown(
        """
        <div style="text-align:center;">
            <h2>Department of Mathematics</h2>
            <h3>School of Advanced Sciences</h3>
            <h3>Vellore Institute of Technology, Chennai</h3>
            <hr>
            <h2 style="color:#1f77b4;">Class Monitoring System</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("### Login")

    emp_id = st.text_input("Employee ID")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login", use_container_width=True):

        st.success("Login button is working!")
