import streamlit as st
import pandas as pd
import joblib


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Cancer Risk Prediction",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

/* -----------------------------------------------------------
   MAIN PAGE
----------------------------------------------------------- */

.stApp {
    background-color: #0e1117;
}

.block-container {
    max-width: 1500px !important;

    padding-top: 1.2rem !important;
    padding-bottom: 0.5rem !important;
    padding-left: 2rem !important;
    padding-right: 2rem !important;

    margin-top: 0 !important;
}


/* -----------------------------------------------------------
   REMOVE EXTRA STREAMLIT TOP SPACE
----------------------------------------------------------- */

header[data-testid="stHeader"] {
    background: transparent !important;
}

[data-testid="stAppViewContainer"] {
    padding-top: 0 !important;
}


/* -----------------------------------------------------------
   TITLE
----------------------------------------------------------- */

.app-title {
    text-align: center;
    font-size: 2.15rem;
    font-weight: 750;
    line-height: 1.15;

    color: #f5f7fa;

    margin: 0 !important;
    padding: 0 !important;
}

.app-subtitle {
    text-align: center;
    font-size: 1rem;
    font-weight: 400;
    line-height: 1.25;

    color: #e5e7eb;

    margin: 0.25rem 0 0.65rem 0 !important;
    padding: 0 !important;
}


/* -----------------------------------------------------------
   SECTION TITLES
----------------------------------------------------------- */

.section-title {
    font-size: 1.35rem;
    font-weight: 700;
    color: #f5f7fa;

    margin-top: 0.35rem;
    margin-bottom: 0.35rem;
}


/* -----------------------------------------------------------
   LABELS
----------------------------------------------------------- */

label {
    font-size: 0.95rem !important;
    font-weight: 600 !important;
}


/* -----------------------------------------------------------
   INPUT BOXES
----------------------------------------------------------- */

div[data-baseweb="select"] > div {
    min-height: 42px !important;
}

div[data-testid="stNumberInput"] input {
    min-height: 42px !important;
    font-size: 0.95rem !important;
}

div[data-testid="stSelectbox"] {
    margin-bottom: 0.15rem !important;
}


/* -----------------------------------------------------------
   BUTTON
----------------------------------------------------------- */

.stButton > button {
    font-size: 1rem !important;
    font-weight: 600 !important;

    min-height: 42px !important;

    padding: 0.35rem 1.1rem !important;

    border-radius: 8px !important;

    margin-top: 0.2rem !important;
}


/* -----------------------------------------------------------
   RESULT SECTION
----------------------------------------------------------- */

.result-title {
    font-size: 1.35rem;
    font-weight: 700;
    color: #f5f7fa;

    margin-top: 0.2rem;
    margin-bottom: 0.45rem;
}


/* -----------------------------------------------------------
   RISK CARD
----------------------------------------------------------- */

.risk-card {
    border-radius: 10px;

    padding: 0.8rem 1rem;

    font-size: 1.05rem;
    font-weight: 650;

    min-height: 58px;

    display: flex;
    align-items: center;
}


/* -----------------------------------------------------------
   LOW RISK
----------------------------------------------------------- */

.low-risk {
    background-color: #123d2b;
    color: #55f29a;
    border: 1px solid #1d6545;
}


/* -----------------------------------------------------------
   MODERATE RISK
----------------------------------------------------------- */

.moderate-risk {
    background-color: #4b3c12;
    color: #ffd75e;
    border: 1px solid #80671b;
}


/* -----------------------------------------------------------
   HIGH RISK
----------------------------------------------------------- */

.high-risk {
    background-color: #4a2027;
    color: #ff6b79;
    border: 1px solid #78323d;
}


/* -----------------------------------------------------------
   CLINICAL SUPPORT CARD
----------------------------------------------------------- */

.support-card {
    background-color: #193653;

    border-radius: 10px;

    padding: 0.8rem 1rem;

    min-height: 58px;

    border: 1px solid #244d73;
}

.support-title {
    font-size: 1.05rem;
    font-weight: 700;

    color: #42a5ff;

    margin-bottom: 0.3rem;
}

.support-text {
    font-size: 0.95rem;
    line-height: 1.45;

    color: #f0f4f8;
}


/* -----------------------------------------------------------
   MODEL INFORMATION
----------------------------------------------------------- */

.model-info {
    font-size: 0.9rem;

    color: #c9ced6;

    margin-top: 0.45rem;
}


/* -----------------------------------------------------------
   DISCLAIMER
----------------------------------------------------------- */

.disclaimer {
    border-top: 1px solid #30343b;

    margin-top: 0.55rem;
    padding-top: 0.45rem;

    font-size: 0.78rem;
    line-height: 1.35;

    color: #c7cbd1;
}


/* -----------------------------------------------------------
   DIVIDERS
----------------------------------------------------------- */

hr {
    margin: 0.45rem 0 !important;
    border: none !important;
    border-top: 1px solid #30343b !important;
}


/* -----------------------------------------------------------
   MOBILE RESPONSIVENESS
----------------------------------------------------------- */

@media (max-width: 900px) {

    .block-container {
        padding-left: 1rem !important;
        padding-right: 1rem !important;
    }

    .app-title {
        font-size: 1.7rem;
    }

    .app-subtitle {
        font-size: 0.9rem;
    }

}

</style>
""", unsafe_allow_html=True)


# ============================================================
# LOAD MODEL
# ============================================================

try:
    model = joblib.load("models/cancer_risk_model.pkl")
except Exception as e:
    st.error(
        "Unable to load the trained model. "
        "Please make sure 'cancer_risk_model.pkl' is inside the 'models' folder."
    )
    st.stop()


# ============================================================
# TITLE
# ============================================================

st.markdown(
    '<div class="app-title">🩺 Cancer Risk Prediction System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="app-subtitle">'
    'Educational AI prototype for breast cancer risk assessment and clinical decision support.'
    '</div>',
    unsafe_allow_html=True
)

st.markdown("<hr>", unsafe_allow_html=True)


# ============================================================
# PATIENT INFORMATION
# ============================================================

st.markdown(
    '<div class="section-title">👤 Patient Information</div>',
    unsafe_allow_html=True
)


# First row
col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=40,
        step=1
    )

with col2:
    family_history = st.selectbox(
        "Family History",
        ["No", "Yes"]
    )

with col3:
    breast_lump = st.selectbox(
        "Breast Lump",
        ["No", "Yes"]
    )


# Second row
col4, col5, col6 = st.columns(3, gap="medium")

with col4:
    breast_pain = st.selectbox(
        "Breast Pain",
        ["No", "Yes"]
    )

with col5:
    nipple_discharge = st.selectbox(
        "Nipple Discharge",
        ["No", "Yes"]
    )

with col6:
    skin_changes = st.selectbox(
        "Skin Changes",
        ["No", "Yes"]
    )


# Third row
col7, col8, col9 = st.columns(3, gap="medium")

with col7:
    previous_breast_disease = st.selectbox(
        "Previous Breast Disease",
        ["No", "Yes"]
    )


# ============================================================
# PREDICTION BUTTON
# ============================================================

predict_button = st.button(
    "🔍 Predict Risk",
    use_container_width=False
)


# ============================================================
# PREDICTION
# ============================================================

if predict_button:

    # Convert Yes/No into 1/0
    input_data = pd.DataFrame({
        "age": [age],

        "family_history": [
            1 if family_history == "Yes" else 0
        ],

        "breast_lump": [
            1 if breast_lump == "Yes" else 0
        ],

        "breast_pain": [
            1 if breast_pain == "Yes" else 0
        ],

        "nipple_discharge": [
            1 if nipple_discharge == "Yes" else 0
        ],

        "skin_changes": [
            1 if skin_changes == "Yes" else 0
        ],

        "previous_breast_disease": [
            1 if previous_breast_disease == "Yes" else 0
        ]
    })


    # Make prediction
    prediction = model.predict(input_data)[0]


    # Convert numerical prediction into label
    risk_labels = {
        0: "Low",
        1: "Moderate",
        2: "High"
    }

    predicted_risk = risk_labels[int(prediction)]


    # ========================================================
    # CLINICAL DECISION SUPPORT
    # ========================================================

    concerning_symptom = (
        breast_lump == "Yes"
        or nipple_discharge == "Yes"
        or skin_changes == "Yes"
    )


    if predicted_risk == "High":

        support_message = (
            "The model indicates high predicted risk. "
            "Discuss this result and any symptoms with a qualified "
            "healthcare professional. A clinician can decide whether "
            "examination, imaging, or further evaluation is appropriate."
        )

    elif predicted_risk == "Moderate" and concerning_symptom:

        support_message = (
            "The model indicates moderate predicted risk and a "
            "potentially concerning symptom was reported. The model "
            "cannot determine the cause of a symptom. Discuss the "
            "symptom and risk result with a qualified healthcare professional."
        )

    elif predicted_risk == "Moderate":

        support_message = (
            "The model indicates moderate predicted risk. Consider "
            "discussing your risk factors with a qualified healthcare "
            "professional and follow appropriate screening guidance."
        )

    elif predicted_risk == "Low" and concerning_symptom:

        support_message = (
            "The model indicates low predicted risk, but a symptom was "
            "reported. A low model result does not rule out a medical "
            "condition. Discuss the symptom with a qualified healthcare "
            "professional."
        )

    else:

        support_message = (
            "The model indicates low predicted risk. Continue appropriate "
            "breast-health awareness and routine screening according to "
            "professional guidance."
        )


    # ========================================================
    # RESULT SECTION
    # ========================================================

    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown(
        '<div class="result-title">📊 Assessment Result</div>',
        unsafe_allow_html=True
    )


    result_col1, result_col2 = st.columns(
        [1, 1],
        gap="medium"
    )


    # --------------------------------------------------------
    # RISK RESULT
    # --------------------------------------------------------

    with result_col1:

        if predicted_risk == "Low":

            st.markdown(
                '<div class="risk-card low-risk">'
                '🟢 &nbsp; Predicted Risk: LOW'
                '</div>',
                unsafe_allow_html=True
            )

        elif predicted_risk == "Moderate":

            st.markdown(
                '<div class="risk-card moderate-risk">'
                '🟡 &nbsp; Predicted Risk: MODERATE'
                '</div>',
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                '<div class="risk-card high-risk">'
                '🔴 &nbsp; Predicted Risk: HIGH'
                '</div>',
                unsafe_allow_html=True
            )


        st.markdown(
            '<div class="model-info">'
            'Generated by the Random Forest model.'
            '</div>',
            unsafe_allow_html=True
        )


    # --------------------------------------------------------
    # CLINICAL DECISION SUPPORT
    # --------------------------------------------------------

    with result_col2:

        st.markdown(
            '<div class="support-card">'
            '<div class="support-title">'
            '🩺 &nbsp; Clinical Decision Support'
            '</div>'
            '<div class="support-text">'
            + support_message +
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )


# ============================================================
# MEDICAL DISCLAIMER
# ============================================================

st.markdown(
    '<div class="disclaimer">'
    '⚠️ <strong>Medical Disclaimer:</strong> '
    'This application is an educational prototype developed using '
    'synthetic data. It is not a clinically validated diagnostic tool '
    'and must not be used to diagnose, rule out, or treat cancer. '
    'Consult a qualified healthcare professional for medical advice.'
    '</div>',
    unsafe_allow_html=True
)