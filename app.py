from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st


st.set_page_config(
    page_title="Cannabis EEG Research Portal",
    page_icon="C",
    layout="wide",
    initial_sidebar_state="collapsed",
)


RESULTS_DATA = pd.DataFrame(
    [
        ("Gamma", "SVM", 0.8491, 0.8195),
        ("Gamma", "Random Forest", 0.8856, 0.7955),
        ("Gamma", "1D CNN", 0.8371, 0.8088),
        ("Beta", "SVM", 0.8578, 0.8168),
        ("Beta", "Random Forest", 0.8876, 0.7794),
        ("Beta", "1D CNN", 0.8667, 0.7901),
        ("Alpha", "SVM", 0.8503, 0.8249),
        ("Alpha", "Random Forest", 0.8779, 0.7901),
        ("Alpha", "1D CNN", 0.8549, 0.7995),
        ("Theta", "SVM", 0.8466, 0.8316),
        ("Theta", "Random Forest", 0.8868, 0.8088),
        ("Theta", "1D CNN", 0.8319, 0.8128),
        ("Delta", "SVM", 0.8388, 0.8249),
        ("Delta", "Random Forest", 0.8414, 0.7914),
        ("Delta", "1D CNN", 0.8563, 0.8075),
        ("All Bands", "SVM", 0.8739, 0.8329),
        ("All Bands", "Random Forest", 0.8158, 0.8008),
        ("All Bands", "1D CNN", 0.7931, 0.7928),
    ],
    columns=["Band", "Classifier", "Training Accuracy", "Test Accuracy"],
)

FEATURES_DATA = pd.DataFrame(
    [
        ("Band Power", "BP", 20, "Frequency"),
        ("Relative Power", "RP", 20, "Frequency"),
        ("Entropy", "EN", 4, "Time Frequency"),
        ("Hjorth Parameters", "HJ", 12, "Time"),
        ("Spectral Flux", "SF", 4, "Frequency"),
        ("Spectral Ratio", "SR", 4, "Frequency"),
        ("Discrete Wavelet Transform", "DWT", 72, "Time Frequency"),
        ("Wavelet Packet", "WP", 64, "Time Frequency"),
        ("Zero Crossing Rate", "ZCR", 4, "Time"),
        ("Root Mean Square", "RMS", 4, "Time"),
    ],
    columns=["Feature", "Code", "Features", "Domain"],
)

SELECTED_FEATURES_DATA = pd.DataFrame(
    [
        ("Band Power", "BP", 20, "Frequency"),
        ("Relative Power", "RP", 20, "Frequency"),
        ("Entropy", "EN", 4, "Time-Frequency"),
        ("Hjorth Parameters", "HJ", 12, "Time"),
        ("Total", "-", 56, "-"),
    ],
    columns=["Feature", "Code", "Number of Features", "Domain"],
)

CONFUSION_MATRIX_IMAGES = {
    "Gamma": "assets/confusion_matrix/gamma_confusion_matrix.png",
    "Beta": "assets/confusion_matrix/beta_confusion_matrix.png",
    "Alpha": "assets/confusion_matrix/alpha_confusion_matrix.png",
    "Theta": "assets/confusion_matrix/theta_confusion_matrix.png",
    "Delta": "assets/confusion_matrix/delta_confusion_matrix.png",
    "All Bands": "assets/confusion_matrix/all_bands_confusion_matrix.png",
}

SUBJECT_10_SPLIT = pd.DataFrame(
    {
        "Dataset": ["Training", "Validation", "Test"],
        "Samples": [5978, 1281, 1281],
        "Percentage": ["70%", "15%", "15%"],
    }
)

SUBJECT_10_ACGAN = pd.DataFrame(
    {
        "Dataset": ["Training", "Validation", "Test"],
        "Real Samples": [5978, 1281, 1281],
        "Synthetic Samples": [5978, 1281, 1281],
        "Mixed Samples": [11956, 2562, 2562],
    }
)

SUBJECT_10_TEST_RESULTS = pd.DataFrame(
    [
        (1, "Beta", "SVM", "Real + Synthetic", 0.846995),
        (2, "Delta", "SVM", "Real + Synthetic", 0.843872),
        (3, "Gamma", "SVM", "Real + Synthetic", 0.843091),
        (4, "Alpha", "SVM", "Real + Synthetic", 0.842701),
        (5, "Alpha", "1D CNN", "Real + Synthetic", 0.841530),
    ],
    columns=["Ranking", "Band", "Model", "Data", "Accuracy"],
)

SUBJECT_10_TRAIN_RESULTS = pd.DataFrame(
    [
        (1, "Beta", "1D CNN", "Real + Synthetic", 0.894446),
        (2, "Delta", "1D CNN", "Real + Synthetic", 0.885330),
        (3, "Gamma", "1D CNN", "Real + Synthetic", 0.883155),
        (4, "Alpha", "1D CNN", "Real + Synthetic", 0.882988),
        (5, "Theta", "1D CNN", "Real + Synthetic", 0.876798),
    ],
    columns=["Ranking", "Band", "Model", "Data", "Accuracy"],
)


SUBJECT_10_BF_AF_SPLIT = pd.DataFrame(
    {
        "Dataset": ["Training", "Validation", "Test"],
        "Samples": [2520, 540, 540],
        "Percentage": ["70%", "15%", "15%"],
    }
)

SUBJECT_10_BF_AF_ACGAN = pd.DataFrame(
    {
        "Dataset": ["Training", "Validation", "Test"],
        "Real Samples": [2520, 540, 540],
        "Synthetic Samples": [2520, 540, 540],
        "Mixed Samples": [5040, 1080, 1080],
    }
)

SUBJECT_10_BF_AF_TEST_RESULTS = pd.DataFrame(
    [
        (1, "Gamma", "SVM", "Real + Synthetic", 0.824074),
        (2, "Delta", "1D CNN", "Real + Synthetic", 0.821296),
        (2, "Theta", "1D CNN", "Real + Synthetic", 0.821296),
        (4, "Delta", "SVM", "Real + Synthetic", 0.820370),
        (5, "Alpha", "SVM", "Real + Synthetic", 0.817593),
    ],
    columns=["Ranking", "Band", "Model", "Data", "Accuracy"],
)

SUBJECT_10_BF_AF_TRAIN_RESULTS = pd.DataFrame(
    [
        (1, "Theta", "1D CNN", "Real + Synthetic", 0.876786),
        (2, "Alpha", "SVM", "Real + Synthetic", 0.867262),
        (3, "Gamma", "SVM", "Real + Synthetic", 0.859325),
        (4, "Theta", "SVM", "Real + Synthetic", 0.853571),
        (5, "Delta", "SVM", "Real + Synthetic", 0.851984),
    ],
    columns=["Ranking", "Band", "Model", "Data", "Accuracy"],
)

SUBJECT_10_BCM_ACM_SPLIT = pd.DataFrame(
    {
        "Dataset": ["Training", "Validation", "Test"],
        "Samples": [5754, 1233, 1233],
        "Percentage": ["70%", "15%", "15%"],
    }
)

SUBJECT_10_BCM_ACM_ACGAN = pd.DataFrame(
    {
        "Dataset": ["Training", "Validation", "Test"],
        "Real Samples": [5754, 1233, 1233],
        "Synthetic Samples": [5754, 1233, 1233],
        "Mixed Samples": [11508, 2466, 2466],
    }
)

SUBJECT_10_BCM_ACM_TEST_RESULTS = pd.DataFrame(
    [
        (1, "Gamma", "SVM", "Real + Synthetic", 0.836172),
        (2, "Delta", "SVM", "Real + Synthetic", 0.831306),
        (3, "Beta", "SVM", "Real + Synthetic", 0.830089),
        (4, "Alpha", "SVM", "Real + Synthetic", 0.829684),
        (5, "Delta", "1D CNN", "Real + Synthetic", 0.827251),
    ],
    columns=["Ranking", "Band", "Model", "Data", "Accuracy"],
)

SUBJECT_10_BCM_ACM_TRAIN_RESULTS = pd.DataFrame(
    [
        (1, "Gamma", "1D CNN", "Real + Synthetic", 0.870786),
        (2, "Alpha", "SVM", "Real + Synthetic", 0.854884),
        (3, "Gamma", "SVM", "Real + Synthetic", 0.853928),
        (4, "Theta", "1D CNN", "Real + Synthetic", 0.848453),
        (5, "Beta", "SVM", "Real + Synthetic", 0.847758),
    ],
    columns=["Ranking", "Band", "Model", "Data", "Accuracy"],
)

CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap');

* { font-family: "Manrope", sans-serif; }

.stApp {
    background:
        radial-gradient(circle at 12% 15%, rgba(157, 215, 168, 0.45), transparent 25%),
        radial-gradient(circle at 88% 10%, rgba(215, 241, 220, 0.70), transparent 30%),
        linear-gradient(135deg, #f7fcf8 0%, #eef8f0 45%, #ffffff 100%);
}

header[data-testid="stHeader"] { background: transparent; }
#MainMenu, footer { visibility: hidden; }

.block-container {
    max-width: 1180px;
    padding-top: 2.4rem;
    padding-bottom: 3.5rem;
}

.hero-center { text-align: center; padding: 2.2rem 1rem 2.5rem; }

.report-label {
    display: inline-block;
    color: #1f6b35;
    background: #eaf5ed;
    padding: 8px 16px;
    border-radius: 999px;
    font-size: 0.72rem;
    font-weight: 800;
    letter-spacing: 0.16em;
}

h1.hero-title {
    margin: 1.1rem 0 0.9rem;
    font-size: clamp(2.2rem, 4.2vw, 3.7rem);
    line-height: 1.12;
    letter-spacing: -0.07em;
}

.title-green { color: #1f6b35; }
.title-black { color: #20252b; }

.hero-description {
    max-width: 980px;
    margin: 0 auto;
    color: #69736c;
    font-size: 1rem;
    line-height: 1.8;
    text-align: center;
}

.hero-line {
    width: 86px;
    height: 4px;
    border-radius: 99px;
    margin: 1.7rem auto 0;
    background: linear-gradient(90deg, #1f6b35, #9ad5a8);
}

.section-center { text-align: center; padding: 0.8rem 0 1rem; }
.section-center h2 { margin: 0; color: #20252b; font-size: 1.45rem; font-weight: 750; }
.section-center p { margin-top: 0.55rem; color: #69736c; font-size: 0.95rem; }

h1 { color: #20252b; font-weight: 800; letter-spacing: -0.06em; }
h2, h3 { color: #20252b; font-weight: 700; }

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(255, 255, 255, 0.58);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 255, 255, 0.75);
    border-radius: 20px;
    box-shadow: 0 10px 30px rgba(31, 107, 53, 0.10), inset 0 1px 0 rgba(255, 255, 255, 0.55);
    transition: all 0.25s ease;
}

div[data-testid="stVerticalBlockBorderWrapper"]:hover {
    transform: translateY(-6px);
    border-color: rgba(31, 107, 53, 0.45);
    box-shadow: 0 18px 38px rgba(31, 107, 53, 0.18), inset 0 1px 0 rgba(255, 255, 255, 0.70);
}

div[data-testid="stMetric"] {
    border: 1px solid #dbe7de;
    border-radius: 16px;
    padding: 18px;
    background: #ffffff;
    box-shadow: 0 8px 22px rgba(31, 70, 42, 0.05);
}

div[data-testid="stMetricValue"] { color: #1f6b35; }

div.stButton > button {
    background: #1f6b35;
    color: #ffffff;
    border: 1px solid #1f6b35;
    border-radius: 12px;
    font-weight: 700;
    min-height: 44px;
}

div.stButton > button:hover { background: #155126; border-color: #155126; color: #ffffff; }
button[data-baseweb="tab"] { font-weight: 700; }
button[data-baseweb="tab"][aria-selected="true"] { color: #1f6b35; }

@media (max-width: 760px) {
    .block-container { padding: 1.4rem 1rem 2.5rem; }
}
</style>
"""

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


def open_report(report_name):
    st.query_params["report"] = report_name
    st.rerun()


def return_to_home():
    st.query_params.clear()
    st.rerun()


def render_report_card(label, title, description, tag, button_text, report_name):
    with st.container(border=True):
        st.caption(label)
        st.subheader(title)
        st.write(description)
        st.caption(tag)
        st.write("")
        if st.button(button_text, key=f"button_{report_name}", use_container_width=True):
            open_report(report_name)


def render_landing_page():
    hero_html = (
        "<div class='hero-center'>"
        "<div class='report-label'>REPORT</div>"
        "<h1 class='hero-title'>"
        "<span class='title-green'>Cannabis EEG</span> "
        "<span class='title-black'>Classification</span><br>"
        "<span class='title-black'>Research</span> "
        "<span class='title-green'>Portal</span>"
        "</h1>"
        "<p class='hero-description'>"
        "Deep Generative Modeling for Cannabis Classification"
        ""
        "</p><div class='hero-line'></div></div>"
    )
    st.markdown(hero_html, unsafe_allow_html=True)
    st.divider()

    st.markdown(
        "<div class='section-center'><h2>Choose one of the available reports</h2>"
        "<p>Select an experimental scale to explore EEG processing, model development, "
        "and classification results.</p></div>",
        unsafe_allow_html=True,
    )
    st.write("")

    first_column, second_column = st.columns(2)
    with first_column:
        render_report_card(
            "EXPERIMENTAL REPORT 01",
            "Subject 02",
            "Single-subject cannabis EEG classification with preprocessing, feature extraction, "
            "ACGAN augmentation, and model evaluation.",
            "2,488 EEG Epochs",
            "Explore Report",
            "subject_02",
        )
    with second_column:
        render_report_card(
            "EXPERIMENTAL REPORT 02",
            "EEG Data Analysis of 10 Cannabis Subjects",
            "Multi-subject cannabis EEG analysis across 10 users, including comparative "
            "classification of BCF vs ACF, BF vs AF, and BCM vs ACM conditions.",
            "3 Comparative Conditions",
            "Explore Report",
            "subject_10",
        )

    st.write("")
    third_column, fourth_column = st.columns(2)
    with third_column:
        render_report_card(
            "EXPERIMENTAL REPORT 03",
            "Subject 30",
            "Large-scale cannabis EEG analysis reserved for 30-user experiments, with expanded "
            "preprocessing, ACGAN augmentation, and model evaluation.",
            "COMING SOON",
            "Explore Report",
            "subject_30",
        )
    with fourth_column:
        with st.container(border=True):
            st.caption("EXPERIMENTAL REPORT 04")
            st.subheader("Future Subject")
            st.write(
                "Reserved for future cannabis EEG experiments, additional participants, "
                "and extended classification studies."
            )
            st.caption("COMING SOON")

    st.write("")
    st.caption("Cannabis EEG Classification Research Portal")


def render_preprocessing_tab():
    st.subheader("Preprocessing pipeline")
    preprocessing_steps = [
        ("Signal parsing", "Selecting four primary EEG channels from each input file."),
        ("Missing-value handling", "Interpolating short NaN gaps in each EEG channel."),
        ("Band-pass filtering", "Applying a frequency filter from 0.5 to 50 Hz."),
        ("Artifact handling", "Applying clipping based on mean plus or minus 3 standard deviation."),
        ("Epoch segmentation", "Dividing the EEG signal into epochs with 512 time points."),
    ]
    for index, (title, description) in enumerate(preprocessing_steps, start=1):
        with st.container(border=True):
            st.subheader(f"{index}. {title}")
            st.write(description)


def render_feature_tab():
    st.subheader("Selected Feature Sets")
    st.caption("Selected features for the All Bands classification experiment.")
    selected_features_styled = SELECTED_FEATURES_DATA.style.apply(
        lambda row: (
            ["background-color: #EAF5ED; font-weight: 700; color: #1F6B35" for _ in row]
            if row["Feature"] == "Total"
            else ["" for _ in row]
        ),
        axis=1,
    )
    st.dataframe(
        selected_features_styled,
        use_container_width=True,
        hide_index=True,
        column_config={"Number of Features": st.column_config.NumberColumn(format="%d")},
    )

    st.write("")
    st.subheader("All Feature Extraction Methods")
    st.caption("Complete feature extraction methods available in the EEG processing workflow.")
    st.dataframe(FEATURES_DATA, use_container_width=True, hide_index=True)

    st.write("")
    with st.container(border=True):
        st.subheader("Feature groups")
        st.write("Time-domain features include Hjorth Parameters, Zero Crossing Rate, and Root Mean Square.")
        st.write("Frequency-domain features include Band Power, Relative Power, Spectral Flux, and Spectral Ratio.")
        st.write("Time-frequency features include Entropy, Discrete Wavelet Transform, and Wavelet Packet.")


def render_subject_02():
    st.caption("EXPERIMENTAL REPORT 01")
    st.title("Subject 02")
    st.write(
        "Single-subject cannabis EEG classification dashboard. This report compares "
        "Before and After conditions using feature-based classification and ACGAN-based "
        "data augmentation."
    )
    if st.button("Back to all reports", key="back_subject_02"):
        return_to_home()

    st.write("")
    metric_1, metric_2, metric_3, metric_4 = st.columns(4)
    metric_1.metric("EEG Epochs", "2,488")
    metric_2.metric("EEG Channels", "4")
    metric_3.metric("Feature Methods", "4")
    metric_4.metric("Total Features", "56")

    overview_tab, dataset_tab, preprocessing_tab, feature_tab, models_tab, acgan_tab, results_tab = st.tabs(
        ["Overview", "Dataset", "Preprocessing", "Feature Extraction", "Models", "ACGAN", "Results"]
    )

    with overview_tab:
        left_column, right_column = st.columns(2)
        with left_column:
            with st.container(border=True):
                st.subheader("Research objective")
                st.write("Classify cannabis EEG conditions before and after treatment using machine-learning and deep-learning models.")
        with right_column:
            with st.container(border=True):
                st.subheader("Classification labels")
                st.write("Label 0: BCF, BCM, BF, and BM.")
                st.write("Label 1: ACF, ACM, AF, and AM.")
        with st.container(border=True):
            st.subheader("Research workflow")
            st.write("Raw EEG data → preprocessing → epoch segmentation → feature extraction → baseline modelling → ACGAN augmentation → final evaluation.")

    with dataset_tab:
        st.subheader("Dataset summary")
        dataset_1, dataset_2, dataset_3 = st.columns(3)
        dataset_1.metric("Before Condition", "1,244 epochs")
        dataset_2.metric("After Condition", "1,244 epochs")
        dataset_3.metric("Epoch Shape", "(512, 4)")
        conditions = pd.DataFrame(
            {
                "Condition": ["BCF", "BCM", "BF", "BM", "ACF", "ACM", "AF", "AM"],
                "Label": [0, 0, 0, 0, 1, 1, 1, 1],
                "Epochs": [311, 311, 311, 311, 311, 311, 311, 311],
                "State": ["Before", "Before", "Before", "Before", "After", "After", "After", "After"],
            }
        )
        st.dataframe(conditions, use_container_width=True, hide_index=True)
        st.subheader("EEG channels")
        channel_1, channel_2, channel_3, channel_4 = st.columns(4)
        channel_1.metric("Channel", "RAW_TP9")
        channel_2.metric("Channel", "RAW_AF7")
        channel_3.metric("Channel", "RAW_AF8")
        channel_4.metric("Channel", "RAW_TP10")

    with preprocessing_tab:
        render_preprocessing_tab()
    with feature_tab:
        render_feature_tab()
    with models_tab:
        st.subheader("Baseline classifiers")
        model_1, model_2, model_3 = st.columns(3)
        with model_1:
            with st.container(border=True):
                st.subheader("SVM")
                st.write("Support Vector Machine for supervised classification between Label 0 and Label 1.")
        with model_2:
            with st.container(border=True):
                st.subheader("Random Forest")
                st.write("Ensemble tree classifier for identifying nonlinear relationships in EEG features.")
        with model_3:
            with st.container(border=True):
                st.subheader("1D CNN")
                st.write("Deep-learning classifier using one-dimensional convolution over feature sequences.")
        st.write("")
        st.subheader("Dataset split")
        st.dataframe(
            pd.DataFrame(
                {"Dataset": ["Training", "Validation", "Test"], "Samples": [1740, 374, 374], "Percentage": ["69.94%", "15.03%", "15.03%"]}
            ),
            use_container_width=True,
            hide_index=True,
        )

    with acgan_tab:
        st.subheader("ACGAN-based data augmentation")
        acgan_1, acgan_2, acgan_3 = st.columns(3)
        acgan_1.metric("Real Training Data", "1,740")
        acgan_2.metric("Synthetic Training Data", "1,740")
        acgan_3.metric("Mixed Training Data", "3,480")
        with st.container(border=True):
            st.subheader("Augmentation strategy")
            st.write("ACGAN generates synthetic data for each feature set. Real and synthetic samples are combined for model training and evaluation.")
            st.write("Frequency-band feature sets contain 24 features, while the All Bands feature set contains 56 features.")
        st.dataframe(
            pd.DataFrame(
                {"Dataset": ["Training", "Validation", "Test"], "Real Samples": [1740, 374, 374], "Synthetic Samples": [1740, 374, 374], "Mixed Samples": [3480, 748, 748]}
            ),
            use_container_width=True,
            hide_index=True,
        )

    with results_tab:
        st.subheader("Classification performance")
        selected_band = st.selectbox(
            "Select frequency band",
            options=["All Bands", "Gamma", "Beta", "Alpha", "Theta", "Delta"],
            key="subject_02_band",
        )
        selected_results = RESULTS_DATA[RESULTS_DATA["Band"] == selected_band].copy()
        chart_data = selected_results.melt(
            id_vars="Classifier",
            value_vars=["Training Accuracy", "Test Accuracy"],
            var_name="Evaluation Set",
            value_name="Accuracy",
        )
        figure = px.bar(
            chart_data,
            x="Classifier",
            y="Accuracy",
            color="Evaluation Set",
            barmode="group",
            text_auto=".2%",
            color_discrete_map={"Training Accuracy": "#1F6B35", "Test Accuracy": "#8FCF9C"},
        )
        figure.update_layout(
            height=420,
            margin=dict(l=10, r=10, t=30, b=10),
            plot_bgcolor="#FFFFFF",
            paper_bgcolor="#FFFFFF",
            legend_title_text="",
            xaxis_title="",
            yaxis_title="Accuracy",
            yaxis=dict(range=[0, 1], tickformat=".0%"),
        )
        st.plotly_chart(figure, use_container_width=True)
        display_results = selected_results.copy()
        display_results["Training Accuracy"] = display_results["Training Accuracy"].map(lambda value: f"{value:.2%}")
        display_results["Test Accuracy"] = display_results["Test Accuracy"].map(lambda value: f"{value:.2%}")
        st.dataframe(display_results, use_container_width=True, hide_index=True)
        best_result = selected_results.loc[selected_results["Test Accuracy"].idxmax()]
        st.success(f"Best test result for {selected_band}: {best_result['Classifier']} with {best_result['Test Accuracy']:.2%} accuracy.")
        with st.container(border=True):
            st.subheader("Confusion Matrix")
            image_path = Path(CONFUSION_MATRIX_IMAGES[selected_band])
            if image_path.exists():
                st.image(str(image_path), caption=f"Confusion Matrix, {selected_band}, Subject 02", use_container_width=True)
            else:
                st.warning(f"Image for {selected_band} has not been found. Check this file path: {image_path}")


def render_subject_10_completed_comparison(
    comparison_name,
    condition_0,
    condition_1,
    total_epochs,
    condition_epochs,
    split_data,
    acgan_data,
    test_results,
    train_results,
):
    """Render a completed 10-subject comparison using a shared dashboard layout."""
    metric_1, metric_2, metric_3, metric_4 = st.columns(4)
    metric_1.metric("EEG Epochs", f"{total_epochs:,}")
    metric_2.metric("EEG Channels", "4")
    metric_3.metric("Feature Methods", "4")
    metric_4.metric("Total Features", "56")

    overview_tab, dataset_tab, preprocessing_tab, feature_tab, models_tab, acgan_tab, results_tab = st.tabs(
        ["Overview", "Dataset", "Preprocessing", "Feature Extraction", "Models", "ACGAN", "Results"]
    )

    with overview_tab:
        left_column, right_column = st.columns(2)
        with left_column:
            with st.container(border=True):
                st.subheader("Research objective")
                st.write(
                    f"Compare the {comparison_name} multi-subject cannabis EEG conditions "
                    "using machine-learning and deep-learning models."
                )
        with right_column:
            with st.container(border=True):
                st.subheader("Classification labels")
                st.write(f"Label 0: {condition_0}, Before.")
                st.write(f"Label 1: {condition_1}, After.")
        with st.container(border=True):
            st.subheader("Research workflow")
            st.write(
                "Raw EEG data → preprocessing → epoch segmentation → feature extraction → "
                "baseline modelling → ACGAN augmentation → final evaluation."
            )

    with dataset_tab:
        st.subheader("Dataset summary")
        dataset_1, dataset_2, dataset_3 = st.columns(3)
        dataset_1.metric("Before Condition", f"{condition_epochs:,} epochs")
        dataset_2.metric("After Condition", f"{condition_epochs:,} epochs")
        dataset_3.metric("Epoch Shape", "(512, 4)")
        conditions = pd.DataFrame(
            {
                "Condition": [condition_0, condition_1],
                "Label": [0, 1],
                "Epochs": [condition_epochs, condition_epochs],
                "State": ["Before", "After"],
            }
        )
        st.dataframe(conditions, use_container_width=True, hide_index=True)
        st.subheader("EEG channels")
        st.caption("The study uses 4 EEG channels. Add the channel names here once they are finalised.")

    with preprocessing_tab:
        render_preprocessing_tab()
    with feature_tab:
        render_feature_tab()

    with models_tab:
        st.subheader("Classification models")
        model_1, model_2 = st.columns(2)
        with model_1:
            with st.container(border=True):
                st.subheader("SVM")
                st.write("Support Vector Machine evaluated with the combined real and synthetic dataset.")
        with model_2:
            with st.container(border=True):
                st.subheader("1D CNN")
                st.write("One-dimensional convolutional neural network evaluated with the combined real and synthetic dataset.")
        st.write("")
        st.subheader("Dataset split")
        st.dataframe(split_data, use_container_width=True, hide_index=True)

    with acgan_tab:
        st.subheader("ACGAN-based data augmentation")
        acgan_1, acgan_2, acgan_3 = st.columns(3)
        acgan_1.metric("Real Training Data", f"{total_epochs:,}")
        acgan_2.metric("Synthetic Training Data", f"{total_epochs:,}")
        acgan_3.metric("Mixed Training Data", f"{total_epochs * 2:,}")
        with st.container(border=True):
            st.subheader("Augmentation strategy")
            st.write(
                "ACGAN generates a synthetic counterpart for each real sample. The real and "
                "synthetic samples are then combined for the classification experiment."
            )
        st.dataframe(acgan_data, use_container_width=True, hide_index=True)

    with results_tab:
        st.subheader("Top 5 Accuracy on the Test Dataset")
        test_chart = px.bar(
            test_results,
            x="Band",
            y="Accuracy",
            color="Model",
            text="Accuracy",
            color_discrete_map={"SVM": "#1F6B35", "1D CNN": "#8FCF9C"},
        )
        test_chart.update_traces(texttemplate="%{text:.2%}", textposition="outside")
        test_chart.update_layout(
            height=420,
            margin=dict(l=10, r=10, t=30, b=10),
            plot_bgcolor="#FFFFFF",
            paper_bgcolor="#FFFFFF",
            legend_title_text="",
            xaxis_title="Frequency Band",
            yaxis_title="Accuracy",
            yaxis=dict(range=[0, 1], tickformat=".0%"),
        )
        st.plotly_chart(test_chart, use_container_width=True)
        test_display = test_results.copy()
        test_display["Accuracy"] = test_display["Accuracy"].map(lambda value: f"{value:.2%}")
        st.dataframe(test_display, use_container_width=True, hide_index=True)
        best_result = test_results.loc[test_results["Accuracy"].idxmax()]
        st.success(
            f"Best test result: {best_result['Band']} band, {best_result['Model']}, "
            f"{best_result['Data']}, {best_result['Accuracy']:.2%} accuracy."
        )

        st.write("")
        st.subheader("Top 5 Accuracy on the Training Dataset")
        train_display = train_results.copy()
        train_display["Accuracy"] = train_display["Accuracy"].map(lambda value: f"{value:.2%}")
        st.dataframe(train_display, use_container_width=True, hide_index=True)

def render_subject_10_bcf_acf():
    """Render the completed BCF vs ACF dashboard for the 10-subject study."""
    metric_1, metric_2, metric_3, metric_4 = st.columns(4)
    metric_1.metric("EEG Epochs", "8,540")
    metric_2.metric("EEG Channels", "4")
    metric_3.metric("Feature Methods", "4")
    metric_4.metric("Total Features", "56")

    overview_tab, dataset_tab, preprocessing_tab, feature_tab, models_tab, acgan_tab, results_tab = st.tabs(
        ["Overview", "Dataset", "Preprocessing", "Feature Extraction", "Models", "ACGAN", "Results"]
    )

    with overview_tab:
        left_column, right_column = st.columns(2)
        with left_column:
            with st.container(border=True):
                st.subheader("Research objective")
                st.write(
                    "Compare multi-subject cannabis EEG conditions before and after cannabis "
                    "consumption using machine-learning and deep-learning models."
                )
        with right_column:
            with st.container(border=True):
                st.subheader("Classification labels")
                st.write("Label 0: BCF, Before Cannabis Consumption.")
                st.write("Label 1: ACF, After Cannabis Consumption.")
        with st.container(border=True):
            st.subheader("Research workflow")
            st.write(
                "Raw EEG data → preprocessing → epoch segmentation → feature extraction → "
                "baseline modelling → ACGAN augmentation → final evaluation."
            )

    with dataset_tab:
        st.subheader("Dataset summary")
        dataset_1, dataset_2, dataset_3 = st.columns(3)
        dataset_1.metric("Before Condition", "4,270 epochs")
        dataset_2.metric("After Condition", "4,270 epochs")
        dataset_3.metric("Epoch Shape", "(512, 4)")
        conditions = pd.DataFrame(
            {
                "Condition": ["BCF", "ACF"],
                "Label": [0, 1],
                "Epochs": [4270, 4270],
                "State": ["Before", "After"],
            }
        )
        st.dataframe(conditions, use_container_width=True, hide_index=True)
        st.subheader("EEG channels")
        st.caption("The study uses 4 EEG channels. Add the channel names here once they are finalised.")

    with preprocessing_tab:
        render_preprocessing_tab()
    with feature_tab:
        render_feature_tab()

    with models_tab:
        st.subheader("Classification models")
        model_1, model_2 = st.columns(2)
        with model_1:
            with st.container(border=True):
                st.subheader("SVM")
                st.write("Support Vector Machine evaluated with the combined real and synthetic dataset.")
        with model_2:
            with st.container(border=True):
                st.subheader("1D CNN")
                st.write("One-dimensional convolutional neural network evaluated with the combined real and synthetic dataset.")
        st.write("")
        st.subheader("Dataset split")
        st.dataframe(SUBJECT_10_SPLIT, use_container_width=True, hide_index=True)

    with acgan_tab:
        st.subheader("ACGAN-based data augmentation")
        acgan_1, acgan_2, acgan_3 = st.columns(3)
        acgan_1.metric("Real Training Data", "8,540")
        acgan_2.metric("Synthetic Training Data", "8,540")
        acgan_3.metric("Mixed Training Data", "17,080")
        with st.container(border=True):
            st.subheader("Augmentation strategy")
            st.write(
                "ACGAN generates a synthetic counterpart for each real sample. The real and "
                "synthetic samples are then combined for the classification experiment."
            )
        st.dataframe(SUBJECT_10_ACGAN, use_container_width=True, hide_index=True)

    with results_tab:
        st.subheader("Top 5 Accuracy on the Test Dataset")
        test_chart = px.bar(
            SUBJECT_10_TEST_RESULTS,
            x="Band",
            y="Accuracy",
            color="Model",
            text="Accuracy",
            color_discrete_map={"SVM": "#1F6B35", "1D CNN": "#8FCF9C"},
        )
        test_chart.update_traces(texttemplate="%{text:.2%}", textposition="outside")
        test_chart.update_layout(
            height=420,
            margin=dict(l=10, r=10, t=30, b=10),
            plot_bgcolor="#FFFFFF",
            paper_bgcolor="#FFFFFF",
            legend_title_text="",
            xaxis_title="Frequency Band",
            yaxis_title="Accuracy",
            yaxis=dict(range=[0, 1], tickformat=".0%"),
        )
        st.plotly_chart(test_chart, use_container_width=True)
        test_display = SUBJECT_10_TEST_RESULTS.copy()
        test_display["Accuracy"] = test_display["Accuracy"].map(lambda value: f"{value:.2%}")
        st.dataframe(test_display, use_container_width=True, hide_index=True)
        st.success("Best test result: Beta band, SVM, Real + Synthetic, 84.70% accuracy.")

        st.write("")
        st.subheader("Top 5 Accuracy on the Training Dataset")
        train_display = SUBJECT_10_TRAIN_RESULTS.copy()
        train_display["Accuracy"] = train_display["Accuracy"].map(lambda value: f"{value:.2%}")
        st.dataframe(train_display, use_container_width=True, hide_index=True)


def render_subject_10():
    st.caption("EXPERIMENTAL REPORT 02")
    st.title("EEG Data Analysis of 10 Cannabis Subjects")
    st.write(
        "Multi-subject cannabis EEG analysis across 10 users, including comparative "
        "classification of BCF vs ACF, BF vs AF, and BCM vs ACM conditions."
    )
    if st.button("Back to all reports", key="back_subject_10"):
        return_to_home()

    st.write("")
    comparison_name = st.radio(
        "Select comparison",
        options=["BCF vs ACF", "BF vs AF", "BCM vs ACM"],
        horizontal=True,
        key="subject_10_comparison",
    )
    st.write("")

    if comparison_name == "BCF vs ACF":
        render_subject_10_bcf_acf()
    elif comparison_name == "BF vs AF":
        render_subject_10_completed_comparison(
            comparison_name="BF vs AF",
            condition_0="BF",
            condition_1="AF",
            total_epochs=3600,
            condition_epochs=1800,
            split_data=SUBJECT_10_BF_AF_SPLIT,
            acgan_data=SUBJECT_10_BF_AF_ACGAN,
            test_results=SUBJECT_10_BF_AF_TEST_RESULTS,
            train_results=SUBJECT_10_BF_AF_TRAIN_RESULTS,
        )
    else:
        render_subject_10_completed_comparison(
            comparison_name="BCM vs ACM",
            condition_0="BCM",
            condition_1="ACM",
            total_epochs=8220,
            condition_epochs=4110,
            split_data=SUBJECT_10_BCM_ACM_SPLIT,
            acgan_data=SUBJECT_10_BCM_ACM_ACGAN,
            test_results=SUBJECT_10_BCM_ACM_TEST_RESULTS,
            train_results=SUBJECT_10_BCM_ACM_TRAIN_RESULTS,
        )

def render_empty_report(subject_name, report_number, user_count):
    st.caption(f"EXPERIMENTAL REPORT {report_number}")
    st.title(subject_name)
    st.write(
        f"This multi-subject cannabis EEG report is prepared for a comparative analysis "
        f"across {user_count} users."
    )
    st.write(
        "The dashboard structure is ready. Dataset information, preprocessing outputs, "
        "feature extraction, ACGAN training, model evaluation, and classification results "
        "will be added after the data-processing workflow is completed."
    )
    if st.button("Back to all reports", key=f"back_{subject_name}"):
        return_to_home()

    overview_tab, dataset_tab, models_tab, results_tab = st.tabs(["Overview", "Dataset", "Models", "Results"])
    with overview_tab:
        with st.container(border=True):
            st.subheader("Report introduction")
            st.write(f"This section will provide the research objective and experimental workflow for the {user_count}-user study.")
    with dataset_tab:
        with st.container(border=True):
            st.subheader("Dataset status")
            st.write("Dataset files have not been added yet. The EEG data will appear here.")
    with models_tab:
        with st.container(border=True):
            st.subheader("Model status")
            st.write("Baseline model configuration and ACGAN augmentation results will be added here.")
    with results_tab:
        with st.container(border=True):
            st.subheader("Results status")
            st.write("Accuracy metrics, training curves, confusion matrices, and classification reports will be added here.")


current_report = st.query_params.get("report", "home")
if current_report == "subject_02":
    render_subject_02()
elif current_report == "subject_10":
    render_subject_10()
elif current_report == "subject_30":
    render_empty_report("Subject 30", "03", "30")
else:
    render_landing_page()
