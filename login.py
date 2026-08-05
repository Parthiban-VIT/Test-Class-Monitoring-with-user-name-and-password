import streamlit as st
import pandas as pd


def login_page():

    # -------------------------------------------------
    # Page Header
    # -------------------------------------------------
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

    # -------------------------------------------------
    # Load Users
    # -------------------------------------------------
    try:
        users_df = pd.read_excel("Users.xlsx", dtype=str)

        users_df = users_df.loc[
            :, ~users_df.columns.str.contains("^Unnamed")
        ]

        users_df.columns = users_df.columns.str.strip()

    except Exception as e:
        st.error(f"Unable to read Users.xlsx\n\n{e}")
        st.stop()

    # -------------------------------------------------
    # Login Form
    # -------------------------------------------------
    st.write("### Login")

    with st.form("login_form"):

        emp_id = st.text_input("Employee ID")

        password = st.text_input(
            "Password",
            type="password",
        )

        submit = st.form_submit_button(
            "Login",
            use_container_width=True,
        )

    # -------------------------------------------------
    # Authentication
    # -------------------------------------------------
    if submit:

        user = users_df[
            (users_df["Employee ID"].str.strip() == emp_id.strip())
            & (users_df["Password"].str.strip() == password.strip())
        ]

        if user.empty:

            st.error("Invalid Employee ID or Password.")

        else:

            user = user.iloc[0]

            st.session_state.logged_in = True
            st.session_state.emp_id = user["Employee ID"]
            st.session_state.name = user["Name"]
            st.session_state.role = user["Role"]

            st.rerun()
