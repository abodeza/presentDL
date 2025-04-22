import streamlit as st

# Set the page config and keep the sidebar (collapsed by default)
st.set_page_config(page_title="About Us", page_icon="ℹ️", layout="wide")

# -------- CSS --------
st.markdown(
    """
    <style>
    /* Hide Streamlit header bar and footer */
    header {visibility: hidden;}
    footer {visibility: hidden;}

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #708ba1 !important;
    }

    [data-testid="stSidebar"] * {
        color: white !important;
    }

    .stApp {
        background: #f7f9fc;
        color: #1f2d3d;
        padding-top: 3rem;
    }

    h1, h2, h3 {
        text-align: center;
    }

    .team-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 30px;
        margin-top: 30px;
    }

    .team-card {
        background: white;
        border-radius: 12px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        padding: 25px 20px;
        width: 200px;
        height: 220px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
    }

    .team-icon {
        font-size: 50px;
        margin-bottom: 15px;
        color: #1e88e5;
    }

    .team-card h4 {
        margin: 5px 0;
        font-size: 18px;
        color: #324556;
    }

    .team-card p {
        margin: 0;
        font-size: 14px;
        color: #666;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -------- Content --------
st.markdown("<h2 id='About' style='color: #191a1f;'>About Us</h2>", unsafe_allow_html=True)
st.markdown(
    """
    <p style='text-align:center; font-size: 1.1rem; color: #191a1f;'>
    <strong><span style="color: #db7c53; font-size: 1.3rem;">CarInfo</span></strong> is a project developed by Tuwaiq Academy students that helps individuals and car dealers estimate realistic used car 
    prices across the market. We rely on real data and machine learning techniques to 
    deliver accurate and transparent estimates.
    </p>
    """, unsafe_allow_html=True
)

st.markdown("<h3 id='Mission' style='color: #191a1f;'>Our Mission</h3>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center; color: #191a1f;'>Building the most trusted, data-driven source for used car prices in the region.</p>",
    unsafe_allow_html=True
)

# -------- Team Section with Icons --------
st.markdown("<h3 id='Team' style='color: #191a1f;'>Our Team</h3>", unsafe_allow_html=True)

st.markdown(
    """
    <div class="team-container">
        <div class="team-card">
            <div class="team-icon">👩‍💻</div>
            <h4>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Dania Emad</h4>
            <p></p>
        </div>
        <div class="team-card">
            <div class="team-icon">👩‍💻</div>
            <h4>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Renad Alajmi</h4>
            <p></p>
        </div>
        <div class="team-card">
            <div class="team-icon">👨‍💻</div>
            <h4>Abdullah Alzahrani</h4>
            <p></p>
        </div>
        <div class="team-card">
            <div class="team-icon">👨‍💻</div>
            <h4>Abdulaziz Alhayzan</h4>
            <p></p>
        </div>
        <div class="team-card">
            <div class="team-icon">👨‍💻</div>
            <h4>Mohanad &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Abuassonon</h4>
            <p></p>
        </div>
    </div>
    """, unsafe_allow_html=True
)
