from textwrap import dedent

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
        {"Band": "Gamma", "Classifier": "SVM", "Training Accuracy": 0.8491, "Test Accuracy": 0.8195},
        {"Band": "Gamma", "Classifier": "Random Forest", "Training Accuracy": 0.8856, "Test Accuracy": 0.7955},
        {"Band": "Gamma", "Classifier": "1D CNN", "Training Accuracy": 0.8371, "Test Accuracy": 0.8088},

        {"Band": "Beta", "Classifier": "SVM", "Training Accuracy": 0.8578, "Test Accuracy": 0.8168},
        {"Band": "Beta", "Classifier": "Random Forest", "Training Accuracy": 0.8876, "Test Accuracy": 0.7794},
        {"Band": "Beta", "Classifier": "1D CNN", "Training Accuracy": 0.8667, "Test Accuracy": 0.7901},

        {"Band": "Alpha", "Classifier": "SVM", "Training Accuracy": 0.8503, "Test Accuracy": 0.8249},
        {"Band": "Alpha", "Classifier": "Random Forest", "Training Accuracy": 0.8779, "Test Accuracy": 0.7901},
        {"Band": "Alpha", "Classifier": "1D CNN", "Training Accuracy": 0.8549, "Test Accuracy": 0.7995},

        {"Band": "Theta", "Classifier": "SVM", "Training Accuracy": 0.8466, "Test Accuracy": 0.8316},
        {"Band": "Theta", "Classifier": "Random Forest", "Training Accuracy": 0.8868, "Test Accuracy": 0.8088},
        {"Band": "Theta", "Classifier": "1D CNN", "Training Accuracy": 0.8319, "Test Accuracy": 0.8128},

        {"Band": "Delta", "Classifier": "SVM", "Training Accuracy": 0.8388, "Test Accuracy": 0.8249},
        {"Band": "Delta", "Classifier": "Random Forest", "Training Accuracy": 0.8414, "Test Accuracy": 0.7914},
        {"Band": "Delta", "Classifier": "1D CNN", "Training Accuracy": 0.8563, "Test Accuracy": 0.8075},

        {"Band": "All Bands", "Classifier": "SVM", "Training Accuracy": 0.8736, "Test Accuracy": 0.8316},
        {"Band": "All Bands", "Classifier": "Random Forest", "Training Accuracy": 0.9057, "Test Accuracy": 0.8168},
        {"Band": "All Bands", "Classifier": "1D CNN", "Training Accuracy": 0.8727, "Test Accuracy": 0.8035},
    ]
)


FEATURES_DATA = pd.DataFrame(
    [
        {"Feature": "Band Power", "Code": "BP", "Features": 20, "Domain": "Frequency"},
        {"Feature": "Relative Power", "Code": "RP", "Features": 20, "Domain": "Frequency"},
        {"Feature": "Entropy", "Code": "EN", "Features": 4, "Domain": "Time Frequency"},
        {"Feature": "Hjorth Parameters", "Code": "HJ", "Features": 12, "Domain": "Time"},
        {"Feature": "Spectral Flux", "Code": "SF", "Features": 4, "Domain": "Frequency"},
        {"Feature": "Spectral Ratio", "Code": "SR", "Features": 4, "Domain": "Frequency"},
        {"Feature": "Discrete Wavelet Transform", "Code": "DWT", "Features": 72, "Domain": "Time Frequency"},
        {"Feature": "Wavelet Packet", "Code": "WP", "Features": 64, "Domain": "Time Frequency"},
        {"Feature": "Zero Crossing Rate", "Code": "ZCR", "Features": 4, "Domain": "Time"},
        {"Feature": "Root Mean Square", "Code": "RMS", "Features": 4, "Domain": "Time"},
    ]
)


st.markdown(
    dedent(
        """
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap');

            :root {
                --forest: #1F6B35;
                --forest-dark: #155126;
                --forest-light: #EAF5ED;
                --ink: #20252B;
                --muted: #69736C;
                --border: #DBE7DE;
                --panel: #FFFFFF;
            }

            * {
                font-family: "Manrope", sans-serif;
            }

            .stApp {
                background:
                    radial-gradient(circle at 100% 0%, #EDF8EF 0%, transparent 26%),
                    #FFFFFF;
            }

            header[data-testid="stHeader"] {
                background: transparent;
            }

            #MainMenu, footer {
                visibility: hidden;
            }

            .block-container {
                max-width: 1180px;
                padding-top: 2.2rem;
                padding-bottom: 3.5rem;
            }

            .hero {
                text-align: center;
                padding: 3.2rem 1rem 2rem;
            }

            .eyebrow {
                display: inline-block;
                color: var(--forest);
                background: var(--forest-light);
                padding: 8px 16px;
                border-radius: 99px;
                font-size: 0.72rem;
                font-weight: 800;
                letter-spacing: 0.16em;
                text-transform: uppercase;
            }

            .hero h1 {
                color: var(--ink);
                margin: 1rem 0 0.75rem;
                font-size: clamp(2rem, 4.2vw, 3.45rem);
                line-height: 1.12;
                letter-spacing: -0.07em;
            }

            .hero h1 span {
                color: var(--forest);
            }

            .hero p {
                max-width: 760px;
                margin: 0 auto;
                color: var(--muted);
                font-size: 1rem;
                line-height: 1.8;
            }

            .line {
                width: 86px;
                height: 4px;
                border-radius: 99px;
                margin: 1.7rem auto 0;
                background: linear-gradient(90deg, var(--forest), #9AD5A8);
            }

            .section-title {
                text-align: center;
                margin: 1.6rem 0 2rem;
            }

            .section-title h2 {
                color: var(--ink);
                font-size: 1.22rem;
                margin: 0;
            }

            .section-title p {
                color: var(--muted);
                font-size: 0.9rem;
                margin: 0.5rem 0 0;
            }

            .card-grid {
                display: grid;
                grid-template-columns: repeat(2, minmax(0, 1fr));
                gap: 24px;
            }

            .report-card {
                min-height: 280px;
                display: flex;
                flex-direction: column;
                justify-content: space-between;
                padding: 30px;
                background: rgba(255, 255, 255, 0.96);
                border: 1px solid var(--border);
                border-radius: 20px;
                box-shadow: 0 10px 28px rgba(31, 70, 42, 0.07);
                transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;
            }

            .report-card:hover {
                transform: translateY(-7px);
                border-color: var(--forest);
                box-shadow: 0 18px 38px rgba(31, 107, 53, 0.16);
            }

            .report-card.coming {
                background: #FBFDFB;
                border-style: dashed;
            }

            .report-card.coming:hover {
                transform: none;
                border-color: var(--border);
                box-shadow: 0 10px 28px rgba(31, 70, 42, 0.07);
            }

            .card-label {
                color: var(--forest);
                font-size: 0.72rem;
                font-weight: 800;
                letter-spacing: 0.12em;
                text-transform: uppercase;
            }

            .report-card h3 {
                color: var(--ink);
                font-size: 1.85rem;
                margin: 0.65rem 0 0.65rem;
                letter-spacing: -0.055em;
            }

            .report-card p {
                color: var(--muted);
                margin: 0;
                line-height: 1.7;
                font-size: 0.91rem;
            }

            .tag {
                display: inline-block;
                margin-top: 1rem;
                padding: 7px 10px;
                border-radius: 8px;
                color: var(--forest);
                background: var(--forest-light);
                font-size: 0.76rem;
                font-weight: 700;
            }

            .card-button {
                display: inline-block;
                width: fit-content;
                margin-top: 1.5rem;
                padding: 12px 17px;
                color: #FFFFFF !important;
                background: var(--forest);
                border-radius: 12px;
                font-size: 0.82rem;
                font-weight: 700;
                text-decoration: none !important;
                transition: background 0.2s ease, transform 0.2s ease;
            }

            .card-button:hover {
                color: #FFFFFF !important;
                background: var(--forest-dark);
                transform: translateY(-2px);
            }

            .page-head {
                margin-bottom: 1rem;
            }

            .page-head h1 {
                color: var(--ink);
                font-size: 2.35rem;
                letter-spacing: -0.06em;
                margin: 0.9rem 0 0.5rem;
            }

            .page-head p {
                color: var(--muted);
                max-width: 820px;
                line-height: 1.8;
            }

            .info-card {
                padding: 22px;
                border: 1px solid var(--border);
                border-radius: 16px;
                background: #FFFFFF;
                box-shadow: 0 8px 22px rgba(31, 70, 42, 0.04);
                margin-bottom: 1rem;
            }

            .info-card h3 {
                color: var(--forest);
                margin: 0 0 0.6rem;
                font-size: 1rem;
            }

            .info-card p {
                color: var(--muted);
                line-height: 1.7;
                margin: 0;
                font-size: 0.9rem;
            }

            .empty-report {
                text-align: center;
                padding: 4rem 1rem;
                border: 1px dashed var(--border);
                border-radius: 20px;
                background: #FBFDFB;
            }

            .empty-report h2 {
                color: var(--ink);
                margin-bottom: 0.7rem;
            }

            .empty-report p {
                color: var(--muted);
                max-width: 620px;
                line-height: 1.8;
                margin: auto;
            }

            .footer {
                text-align: center;
                color: #89928B;
                font-size: 0.76rem;
                margin-top: 3.5rem;
            }

            div[data-testid="stMetric"] {
                border: 1px solid var(--border);
                border-radius: 16px;
                background: #FFFFFF;
                padding: 18px;
                box-shadow: 0 8px 22px rgba(31, 70, 42, 0.05);
            }

            div[data-testid="stMetricLabel"] {
                color: var(--muted);
            }

            div[data-testid="stMetricValue"] {
                color: var(--forest);
            }

            button[kind="secondary"] {
                border-radius: 10px;
                border-color: var(--border);
                color: var(--forest);
                font-weight: 700;
            }

            button[kind="secondary"]:hover {
                border-color: var(--forest);
                color: var(--forest-dark);
            }

            button[data-baseweb="tab"] {
                font-weight: 700;
            }

            button[data-baseweb="tab"][aria-selected="true"] {
                color: var(--forest);
            }

            @media (max-width: 760px) {
                .block-container {
                    padding: 1.25rem 1rem 2.5rem;
                }

                .hero {
                    padding: 2.3rem 0.2rem 1.4rem;
                }

                .card-grid {
                    grid-template-columns: 1fr;
                    gap: 16px;
                }

                .report-card {
                    min-height: 245px;
                    padding: 24px;
                }
            }
        </style>
        """
    ).strip(),
    unsafe_allow_html=True,
)


def go_home():
    st.query_params.clear()
    st.rerun()


def render_landing_page():
    landing_html = dedent(
        """
        <div class="hero">
            <div class="eyebrow">Report</div>

            <h1>
                Cannabis EEG Classification<br>
                <span>Research Portal</span>
            </h1>

            <p>
                Artificial Intelligence for cannabis classification using
                Auxiliary Classifier Generative Adversarial Network.
            </p>

            <div class="line"></div>
        </div>

        <div class="section-title">
            <h2>Choose one of the available reports</h2>

            <p>
                Select an experimental scale to explore EEG processing,
                model development, and classification results.
            </p>
        </div>

        <div class="card-grid">

            <div class="report-card">
                <div>
                    <div class="card-label">Experimental Report 01</div>

                    <h3>Subject 02</h3>

                    <p>
                        Single-subject cannabis EEG classification with
                        preprocessing, feature extraction, ACGAN augmentation,
                        and model evaluation.
                    </p>

                    <div class="tag">2,488 EEG Epochs</div>
                </div>

                <a class="card-button" href="?report=subject_02" target="_self">
                    Explore Report &rarr;
                </a>
            </div>

            <div class="report-card">
                <div>
                    <div class="card-label">Experimental Report 02</div>

                    <h3>Subject 10</h3>

                    <p>
                        Multi-subject cannabis EEG analysis prepared for a
                        comparative study across 10 users, focusing on the
                        BCM and ACM conditions.
                    </p>

                    <div class="tag">BCM vs ACM</div>
                </div>

                <a class="card-button" href="?report=subject_10" target="_self">
                    Explore Report &rarr;
                </a>
            </div>

            <div class="report-card">
                <div>
                    <div class="card-label">Experimental Report 03</div>

                    <h3>Subject 30</h3>

                    <p>
                        Large-scale cannabis EEG analysis prepared for a
                        comparative study across 30 users, with expanded
                        preprocessing, ACGAN augmentation, and model evaluation.
                    </p>

                    <div class="tag">BCM vs ACM</div>
                </div>

                <a class="card-button" href="?report=subject_30" target="_self">
                    Explore Report &rarr;
                </a>
            </div>

            <div class="report-card coming">
                <div>
                    <div class="card-label">Experimental Report 04</div>

                    <h3>Future Subject</h3>

                    <p>
                        Reserved for future cannabis EEG experiments,
                        additional participants, and extended classification studies.
                    </p>

                    <div class="tag">Coming Soon</div>
                </div>
            </div>

        </div>

        <div class="footer">
            Cannabis EEG Classification Research Portal
        </div>
        """
    ).strip()

    st.markdown(landing_html, unsafe_allow_html=True)


def render_subject_02():
    st.markdown(
        dedent(
            """
            <div class="page-head">
                <div class="eyebrow">Experimental Report 01</div>

                <h1>Subject 02</h1>

                <p>
                    Single-subject cannabis EEG classification dashboard.
                    The report compares Before and After conditions using
                    feature-based classification and ACGAN-based data augmentation.
                </p>
            </div>
            """
        ).strip(),
        unsafe_allow_html=True,
    )

    if st.button("Back to all reports", key="back_subject_02"):
        go_home()

    st.write("")

    metric_1, metric_2, metric_3, metric_4 = st.columns(4)
    metric_1.metric("EEG Epochs", "2,488")
    metric_2.metric("EEG Channels", "4")
    metric_3.metric("Feature Methods", "10")
    metric_4.metric("Total Features", "152")

    (
        overview_tab,
        dataset_tab,
        preprocessing_tab,
        feature_tab,
        models_tab,
        acgan_tab,
        results_tab,
    ) = st.tabs(
        [
            "Overview",
            "Dataset",
            "Preprocessing",
            "Feature Extraction",
            "Models",
            "ACGAN",
            "Results",
        ]
    )

    with overview_tab:
        left_column, right_column = st.columns([1.25, 1])

        with left_column:
            st.markdown(
                dedent(
                    """
                    <div class="info-card">
                        <h3>Research objective</h3>

                        <p>
                            Classify cannabis EEG conditions before and after
                            treatment using machine-learning and deep-learning models.
                            This dashboard presents the complete analytical workflow.
                        </p>
                    </div>

                    <div class="info-card">
                        <h3>Classification labels</h3>

                        <p>
                            Label 0 represents BCF, BCM, BF, and BM.
                            Label 1 represents ACF, ACM, AF, and AM.
                        </p>
                    </div>
                    """
                ).strip(),
                unsafe_allow_html=True,
            )

        with right_column:
            st.markdown(
                dedent(
                    """
                    <div class="info-card">
                        <h3>Research workflow</h3>

                        <p>
                            Raw EEG data → preprocessing → epoch segmentation →
                            feature extraction → baseline modelling →
                            ACGAN augmentation → final evaluation.
                        </p>
                    </div>

                    <div class="info-card">
                        <h3>Frequency bands</h3>

                        <p>
                            Gamma, Beta, Alpha, Theta, Delta, and All Bands.
                        </p>
                    </div>
                    """
                ).strip(),
                unsafe_allow_html=True,
            )

    with dataset_tab:
        st.subheader("Dataset summary")

        dataset_metric_1, dataset_metric_2, dataset_metric_3 = st.columns(3)
        dataset_metric_1.metric("Before Condition", "1,244 epochs")
        dataset_metric_2.metric("After Condition", "1,244 epochs")
        dataset_metric_3.metric("Epoch Shape", "(512, 4)")

        conditions = pd.DataFrame(
            {
                "Condition": ["BCF", "BCM", "BF", "BM", "ACF", "ACM", "AF", "AM"],
                "Label": [0, 0, 0, 0, 1, 1, 1, 1],
                "Epochs": [311, 311, 311, 311, 311, 311, 311, 311],
                "State": [
                    "Before",
                    "Before",
                    "Before",
                    "Before",
                    "After",
                    "After",
                    "After",
                    "After",
                ],
            }
        )

        st.dataframe(conditions, use_container_width=True, hide_index=True)

        st.subheader("EEG channels")

        channel_1, channel_2, channel_3, channel_4 = st.columns(4)
        channel_1.metric("Channel", "RAW_TP9")
        channel_2.metric("Channel", "RAW_AF7")
        channel_3.metric("Channel", "RAW_AF8")
        channel_4.metric("Channel", "RAW_TP10")

        st.caption(
            "File CSV asli dapat ditambahkan nanti untuk menampilkan preview "
            "sinyal EEG, visualisasi waveforms, dan pemeriksaan kualitas data."
        )

    with preprocessing_tab:
        st.subheader("Preprocessing pipeline")

        preprocessing_steps = [
            (
                "1. Signal parsing",
                "Memilih empat kanal EEG utama dari setiap file input.",
            ),
            (
                "2. Missing-value handling",
                "Menginterpolasi short NaN gaps pada setiap kanal EEG.",
            ),
            (
                "3. Band-pass filtering",
                "Menerapkan filtering pada rentang frekuensi 0.5 sampai 50 Hz.",
            ),
            (
                "4. Artifact handling",
                "Menerapkan clipping berdasarkan batas mean ± 3 standard deviation.",
            ),
            (
                "5. Epoch segmentation",
                "Membagi sinyal menjadi epoch dengan panjang 512 time points.",
            ),
        ]

        for title, description in preprocessing_steps:
            st.markdown(
                dedent(
                    f"""
                    <div class="info-card">
                        <h3>{title}</h3>
                        <p>{description}</p>
                    </div>
                    """
                ).strip(),
                unsafe_allow_html=True,
            )

    with feature_tab:
        st.subheader("Feature extraction methods")

        st.dataframe(
            FEATURES_DATA,
            use_container_width=True,
            hide_index=True,
        )

        st.markdown(
            dedent(
                """
                <div class="info-card">
                    <h3>Feature groups</h3>

                    <p>
                        Time-domain features include Hjorth Parameters,
                        Zero Crossing Rate, and Root Mean Square.
                        Frequency-domain features include Band Power,
                        Relative Power, Spectral Flux, and Spectral Ratio.
                        Time-frequency features include Entropy,
                        Discrete Wavelet Transform, and Wavelet Packet.
                    </p>
                </div>
                """
            ).strip(),
            unsafe_allow_html=True,
        )

    with models_tab:
        st.subheader("Baseline classifiers")

        model_1, model_2, model_3 = st.columns(3)

        with model_1:
            st.markdown(
                dedent(
                    """
                    <div class="info-card">
                        <h3>SVM</h3>

                        <p>
                            Support Vector Machine used for supervised
                            classification between Label 0 and Label 1.
                        </p>
                    </div>
                    """
                ).strip(),
                unsafe_allow_html=True,
            )

        with model_2:
            st.markdown(
                dedent(
                    """
                    <div class="info-card">
                        <h3>Random Forest</h3>

                        <p>
                            Ensemble tree classifier for identifying
                            nonlinear relationships in EEG features.
                        </p>
                    </div>
                    """
                ).strip(),
                unsafe_allow_html=True,
            )

        with model_3:
            st.markdown(
                dedent(
                    """
                    <div class="info-card">
                        <h3>1D CNN</h3>

                        <p>
                            Deep-learning classifier using one-dimensional
                            convolution over feature sequences.
                        </p>
                    </div>
                    """
                ).strip(),
                unsafe_allow_html=True,
            )

        st.subheader("Dataset split")

        split_data = pd.DataFrame(
            {
                "Dataset": ["Training", "Validation", "Test"],
                "Samples": [1740, 374, 374],
                "Percentage": ["69.94%", "15.03%", "15.03%"],
            }
        )

        st.dataframe(split_data, use_container_width=True, hide_index=True)

    with acgan_tab:
        st.subheader("ACGAN-based data augmentation")

        acgan_metric_1, acgan_metric_2, acgan_metric_3 = st.columns(3)
        acgan_metric_1.metric("Real Training Data", "1,740")
        acgan_metric_2.metric("Synthetic Training Data", "1,740")
        acgan_metric_3.metric("Mixed Training Data", "3,480")

        st.markdown(
            dedent(
                """
                <div class="info-card">
                    <h3>Augmentation strategy</h3>

                    <p>
                        ACGAN generates synthetic data for each feature set.
                        Real and synthetic samples are combined for model training
                        and evaluation. Frequency-band feature sets contain
                        24 features, while the All Bands feature set contains
                        56 features.
                    </p>
                </div>
                """
            ).strip(),
            unsafe_allow_html=True,
        )

        acgan_data = pd.DataFrame(
            {
                "Dataset": ["Training", "Validation", "Test"],
                "Real Samples": [1740, 374, 374],
                "Synthetic Samples": [1740, 374, 374],
                "Mixed Samples": [3480, 748, 748],
            }
        )

        st.dataframe(acgan_data, use_container_width=True, hide_index=True)

    with results_tab:
        st.subheader("Classification performance")

        selected_band = st.selectbox(
            "Select frequency band",
            options=["All Bands", "Gamma", "Beta", "Alpha", "Theta", "Delta"],
        )

        selected_results = RESULTS_DATA[
            RESULTS_DATA["Band"] == selected_band
        ].copy()

        chart_data = selected_results.melt(
            id_vars="Classifier",
            value_vars=["Training Accuracy", "Test Accuracy"],
            var_name="Evaluation Set",
            value_name="Accuracy",
        )

        chart = px.bar(
            chart_data,
            x="Classifier",
            y="Accuracy",
            color="Evaluation Set",
            barmode="group",
            text_auto=".2%",
            color_discrete_map={
                "Training Accuracy": "#1F6B35",
                "Test Accuracy": "#8FCF9C",
            },
        )

        chart.update_layout(
            height=420,
            margin=dict(l=10, r=10, t=30, b=10),
            plot_bgcolor="#FFFFFF",
            paper_bgcolor="#FFFFFF",
            legend_title_text="",
            xaxis_title="",
            yaxis_title="Accuracy",
            yaxis=dict(range=[0, 1], tickformat=".0%"),
        )

        st.plotly_chart(chart, use_container_width=True)

        display_results = selected_results.copy()
        display_results["Training Accuracy"] = display_results["Training Accuracy"].map(
            lambda value: f"{value:.2%}"
        )
        display_results["Test Accuracy"] = display_results["Test Accuracy"].map(
            lambda value: f"{value:.2%}"
        )

        st.dataframe(
            display_results,
            use_container_width=True,
            hide_index=True,
        )

        best_result = selected_results.loc[
            selected_results["Test Accuracy"].idxmax()
        ]

        st.success(
            f"Best test result for {selected_band}: "
            f"{best_result['Classifier']} with "
            f"{best_result['Test Accuracy']:.2%} accuracy."
        )

        st.markdown(
            dedent(
                """
                <div class="info-card">
                    <h3>Confusion matrix</h3>

                    <p>
                        Tambahkan file confusion matrix dalam format PNG, CSV,
                        atau NumPy array saat output gambar dan data model
                        tersedia.
                    </p>
                </div>
                """
            ).strip(),
            unsafe_allow_html=True,
        )


def render_empty_report(subject_name, report_number, user_count):
    st.markdown(
        dedent(
            f"""
            <div class="page-head">
                <div class="eyebrow">Experimental Report {report_number}</div>

                <h1>{subject_name}</h1>

                <p>
                    Multi-subject cannabis EEG analysis prepared for a comparative
                    study across {user_count} users, focusing on BCM versus ACM
                    conditions. Dataset information and model results will be
                    added when the processing workflow is completed.
                </p>
            </div>
            """
        ).strip(),
        unsafe_allow_html=True,
    )

    if st.button("Back to all reports", key=f"back_{subject_name}"):
        go_home()

    st.markdown(
        dedent(
            f"""
            <div class="empty-report">
                <h2>{subject_name} report is being prepared</h2>

                <p>
                    This report will later include Overview, Dataset,
                    Preprocessing, Feature Extraction, Models, ACGAN,
                    and Results sections for the BCM versus ACM analysis
                    across {user_count} users.
                </p>
            </div>
            """
        ).strip(),
        unsafe_allow_html=True,
    )


current_report = st.query_params.get("report", "home")

if current_report == "subject_02":
    render_subject_02()

elif current_report == "subject_10":
    render_empty_report(
        subject_name="Subject 10",
        report_number="02",
        user_count="10",
    )

elif current_report == "subject_30":
    render_empty_report(
        subject_name="Subject 30",
        report_number="03",
        user_count="30",
    )

else:
    render_landing_page()
