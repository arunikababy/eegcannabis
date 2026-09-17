from pathlib import Path
from zipfile import ZipFile

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st


APP_DIRECTORY = Path(__file__).resolve().parent

BCF_ACF_SUBJECT_LEVEL_FILES = [
    APP_DIRECTORY / "subject_level_master_BCF_ACF.csv",
    APP_DIRECTORY / "subject_level_master_BCF_ACF(1).csv",
    APP_DIRECTORY / "data" / "subject_level_master_BCF_ACF.csv",
    APP_DIRECTORY / "data" / "subject_level_master_BCF_ACF(1).csv",
    APP_DIRECTORY / "assets" / "data" / "subject_level_master_BCF_ACF.csv",
    APP_DIRECTORY / "assets" / "data" / "subject_level_master_BCF_ACF(1).csv",
]

BCF_ACF_BAND_ORDER = ["Gamma", "Beta", "Alpha", "Theta", "Delta"]
BCF_ACF_CHANNEL_ORDER = ["TP9", "AF7", "AF8", "TP10"]

BCF_ACF_DIRECTION_COLORS = {
    "Increase": "#1F6B35",
    "Decrease": "#D95F59",
    "No Change": "#9CA3AF",
}

# Multicolor palette used only by the BCF-ACF Pre-Post tab.
BCF_ACF_PREPOST_SUBJECT_COLORS = [
    "#6C3FD1",  # purple
    "#AEB8C8",  # soft grey-blue
    "#FF7A00",  # orange
    "#FF6B5E",  # coral
    "#E84545",  # warm red
    "#18B7A0",  # teal
    "#2F80ED",  # blue
    "#69D6A3",  # mint
    "#F2C94C",  # yellow
    "#F299B1",  # pink
]

BCF_ACF_PREPOST_CHANNEL_COLORS = {
    "TP9": "#6C3FD1",
    "AF7": "#FF7A00",
    "AF8": "#18B7A0",
    "TP10": "#2F80ED",
}

BCF_ACF_PREPOST_CHANNEL_FILLS = {
    "TP9": "rgba(108,63,209,0.18)",
    "AF7": "rgba(255,122,0,0.18)",
    "AF8": "rgba(24,183,160,0.18)",
    "TP10": "rgba(47,128,237,0.18)",
}

BCF_ACF_PREPOST_CONDITION_COLORS = {
    "BCF": "#27465A",
    "ACF": "#27465A",
}

BCF_ACF_PREPOST_DIRECTION_COLORS = {
    "Increase": "#237A57",
    "Decrease": "#9DD9AF",
    "No Change": "#B7C4BF",
}

BCF_ACF_BAND_HIGHLIGHTS = {
    "Gamma": (
        "The clearest pattern was observed for Gamma Band Power at AF8, which "
        "increased in 9 of 10 paired subjects. Its mean change was +66,320.41 "
        "and its median change was +61,998.58."
    ),
    "Beta": (
        "Beta Band Power at AF8 increased in 8 of 10 paired subjects, with a "
        "mean change of +61,725.43 and a median change of +59,376.82. Beta "
        "Relative Power at AF8 also increased in 7 of 10 subjects."
    ),
    "Alpha": (
        "Alpha Band Power increased in 8 of 10 subjects at both AF8 and TP10. "
        "Alpha Relative Power at AF8 also increased in 8 of 10 subjects."
    ),
    "Theta": (
        "Theta Relative Power at TP9 decreased in 9 of 10 subjects. Theta Band "
        "Power at TP9 decreased in 8 of 10 subjects, whereas it increased in "
        "8 of 10 subjects at AF8 and TP10."
    ),
    "Delta": (
        "Delta Relative Power decreased more often than it increased across all "
        "four channels. Delta Band Power increased in 8 of 10 subjects at AF8 "
        "but decreased in 7 of 10 subjects at TP9."
    ),
}


BCF_ACF_PAIRED_STATISTICS_ZIPS = [
    APP_DIRECTORY / "paired_statistics_master BCF ACF.zip",
    APP_DIRECTORY / "paired_statistics_master_BCF_ACF.zip",
    APP_DIRECTORY / "data" / "paired_statistics_master BCF ACF.zip",
    APP_DIRECTORY / "data" / "paired_statistics_master_BCF_ACF.zip",
    APP_DIRECTORY / "assets" / "data" / "paired_statistics_master BCF ACF.zip",
    APP_DIRECTORY / "assets" / "data" / "paired_statistics_master_BCF_ACF.zip",
]

BCF_ACF_PAIRED_STATISTICS_DIRECTORIES = [
    APP_DIRECTORY / "paired_statistics_master",
    APP_DIRECTORY / "data" / "paired_statistics_master",
    APP_DIRECTORY / "assets" / "data" / "paired_statistics_master",
    APP_DIRECTORY,
    APP_DIRECTORY / "data",
    APP_DIRECTORY / "assets" / "data",
]

BCF_ACF_PAIRED_REQUIRED_COLUMNS = {
    "channel",
    "feature_band",
    "feature_type",
    "feature",
    "n_subjects",
    "mean_change",
    "ci95_lower",
    "ci95_upper",
    "cohens_dz",
    "effect_size_interpretation",
    "t_statistic",
    "p_ttest",
    "wilcoxon_statistic",
    "p_wilcoxon",
    "p_fdr_ttest",
    "p_fdr_wilcoxon",
}

BCF_ACF_TEST_OPTIONS = {
    "Wilcoxon signed-rank": {
        "p_column": "p_wilcoxon",
        "q_column": "p_fdr_wilcoxon",
        "statistic_column": "wilcoxon_statistic",
    },
    "Paired t-test": {
        "p_column": "p_ttest",
        "q_column": "p_fdr_ttest",
        "statistic_column": "t_statistic",
    },
}


BCF_ACF_SYNTHETIC_QUALITY_ZIPS = [
    APP_DIRECTORY / "synthetic_quality_master BCF ACF.zip",
    APP_DIRECTORY / "synthetic_quality_master_BCF_ACF.zip",
    APP_DIRECTORY / "data" / "synthetic_quality_master BCF ACF.zip",
    APP_DIRECTORY / "data" / "synthetic_quality_master_BCF_ACF.zip",
    APP_DIRECTORY / "assets" / "data" / "synthetic_quality_master BCF ACF.zip",
    APP_DIRECTORY / "assets" / "data" / "synthetic_quality_master_BCF_ACF.zip",
]

BCF_ACF_SYNTHETIC_QUALITY_DIRECTORIES = [
    APP_DIRECTORY / "synthetic_quality_master",
    APP_DIRECTORY / "data" / "synthetic_quality_master",
    APP_DIRECTORY / "assets" / "data" / "synthetic_quality_master",
    APP_DIRECTORY,
    APP_DIRECTORY / "data",
    APP_DIRECTORY / "assets" / "data",
]

BCF_ACF_SYNTHETIC_REQUIRED_COLUMNS = {
    "Condition",
    "Label",
    "Channel",
    "Feature",
    "Real_Mean",
    "Synthetic_Mean",
    "Real_SD",
    "Synthetic_SD",
    "Real_Median",
    "Synthetic_Median",
    "Real_IQR",
    "Synthetic_IQR",
    "Real_N",
    "Synthetic_N",
}

BCF_ACF_SYNTHETIC_METRICS = {
    "Mean": {
        "real": "Real_Mean",
        "synthetic": "Synthetic_Mean",
        "difference": "Mean_Difference",
        "absolute": "Abs_Mean_Difference",
    },
    "Standard deviation": {
        "real": "Real_SD",
        "synthetic": "Synthetic_SD",
        "difference": "SD_Difference",
        "absolute": "Abs_SD_Difference",
    },
    "Median": {
        "real": "Real_Median",
        "synthetic": "Synthetic_Median",
        "difference": "Median_Difference",
        "absolute": "Abs_Median_Difference",
    },
    "IQR": {
        "real": "Real_IQR",
        "synthetic": "Synthetic_IQR",
        "difference": "IQR_Difference",
        "absolute": "Abs_IQR_Difference",
    },
}

BCF_ACF_SYNTHETIC_BAND_COLORS = {
    "Gamma": "#6C3FD1",
    "Beta": "#2F80ED",
    "Alpha": "#FF7A00",
    "Theta": "#18B7A0",
    "Delta": "#69B88B",
}


BF_AF_SYNTHETIC_QUALITY_ZIPS = [
    APP_DIRECTORY / "synthetic_quality_master BF AF.zip",
    APP_DIRECTORY / "synthetic_quality_master BF AF(1).zip",
    APP_DIRECTORY / "synthetic_quality_master_BF_AF.zip",
    APP_DIRECTORY / "data" / "synthetic_quality_master BF AF.zip",
    APP_DIRECTORY / "data" / "synthetic_quality_master BF AF(1).zip",
    APP_DIRECTORY / "data" / "synthetic_quality_master_BF_AF.zip",
    APP_DIRECTORY / "assets" / "data" / "synthetic_quality_master BF AF.zip",
    APP_DIRECTORY / "assets" / "data" / "synthetic_quality_master BF AF(1).zip",
    APP_DIRECTORY / "assets" / "data" / "synthetic_quality_master_BF_AF.zip",
]

BF_AF_SYNTHETIC_QUALITY_DIRECTORIES = [
    APP_DIRECTORY / "synthetic_quality_master",
    APP_DIRECTORY / "data" / "synthetic_quality_master",
    APP_DIRECTORY / "assets" / "data" / "synthetic_quality_master",
    APP_DIRECTORY,
    APP_DIRECTORY / "data",
    APP_DIRECTORY / "assets" / "data",
]

BF_AF_SYNTHETIC_REQUIRED_COLUMNS = set(
    BCF_ACF_SYNTHETIC_REQUIRED_COLUMNS
)

BF_AF_SYNTHETIC_METRICS = dict(BCF_ACF_SYNTHETIC_METRICS)


BCM_ACM_SYNTHETIC_QUALITY_ZIPS = [
    APP_DIRECTORY / "synthetic_quality_master BCM ACM.zip",
    APP_DIRECTORY / "synthetic_quality_master BCM ACM(1).zip",
    APP_DIRECTORY / "synthetic_quality_master_BCM_ACM.zip",
    APP_DIRECTORY / "data" / "synthetic_quality_master BCM ACM.zip",
    APP_DIRECTORY / "data" / "synthetic_quality_master BCM ACM(1).zip",
    APP_DIRECTORY / "data" / "synthetic_quality_master_BCM_ACM.zip",
    APP_DIRECTORY / "assets" / "data" / "synthetic_quality_master BCM ACM.zip",
    APP_DIRECTORY / "assets" / "data" / "synthetic_quality_master BCM ACM(1).zip",
    APP_DIRECTORY / "assets" / "data" / "synthetic_quality_master_BCM_ACM.zip",
]

BCM_ACM_SYNTHETIC_QUALITY_DIRECTORIES = [
    APP_DIRECTORY / "synthetic_quality_master",
    APP_DIRECTORY / "data" / "synthetic_quality_master",
    APP_DIRECTORY / "assets" / "data" / "synthetic_quality_master",
    APP_DIRECTORY,
    APP_DIRECTORY / "data",
    APP_DIRECTORY / "assets" / "data",
]

BCM_ACM_SYNTHETIC_REQUIRED_COLUMNS = set(
    BCF_ACF_SYNTHETIC_REQUIRED_COLUMNS
)

BCM_ACM_SYNTHETIC_METRICS = dict(BCF_ACF_SYNTHETIC_METRICS)


BM_AM_SYNTHETIC_QUALITY_ZIPS = [
    APP_DIRECTORY / "synthetic_quality_master BM AM.zip",
    APP_DIRECTORY / "synthetic_quality_master BM AM(1).zip",
    APP_DIRECTORY / "synthetic_quality_master_BM_AM.zip",
    APP_DIRECTORY / "data" / "synthetic_quality_master BM AM.zip",
    APP_DIRECTORY / "data" / "synthetic_quality_master BM AM(1).zip",
    APP_DIRECTORY / "data" / "synthetic_quality_master_BM_AM.zip",
    APP_DIRECTORY / "assets" / "data" / "synthetic_quality_master BM AM.zip",
    APP_DIRECTORY / "assets" / "data" / "synthetic_quality_master BM AM(1).zip",
    APP_DIRECTORY / "assets" / "data" / "synthetic_quality_master_BM_AM.zip",
]

BM_AM_SYNTHETIC_QUALITY_DIRECTORIES = [
    APP_DIRECTORY / "synthetic_quality_master",
    APP_DIRECTORY / "data" / "synthetic_quality_master",
    APP_DIRECTORY / "assets" / "data" / "synthetic_quality_master",
    APP_DIRECTORY,
    APP_DIRECTORY / "data",
    APP_DIRECTORY / "assets" / "data",
]

BM_AM_SYNTHETIC_REQUIRED_COLUMNS = set(
    BCF_ACF_SYNTHETIC_REQUIRED_COLUMNS
)

BM_AM_SYNTHETIC_METRICS = dict(BCF_ACF_SYNTHETIC_METRICS)


BF_AF_PAIRED_STATISTICS_ZIPS = [
    APP_DIRECTORY / "paired_statistics_master BF AF.zip",
    APP_DIRECTORY / "paired_statistics_master_BF_AF.zip",
    APP_DIRECTORY / "data" / "paired_statistics_master BF AF.zip",
    APP_DIRECTORY / "data" / "paired_statistics_master_BF_AF.zip",
    APP_DIRECTORY / "assets" / "data" / "paired_statistics_master BF AF.zip",
    APP_DIRECTORY / "assets" / "data" / "paired_statistics_master_BF_AF.zip",
]

BF_AF_PAIRED_STATISTICS_DIRECTORIES = [
    APP_DIRECTORY / "paired_statistics_master",
    APP_DIRECTORY / "data" / "paired_statistics_master",
    APP_DIRECTORY / "assets" / "data" / "paired_statistics_master",
    APP_DIRECTORY,
    APP_DIRECTORY / "data",
    APP_DIRECTORY / "assets" / "data",
]


BCM_ACM_PAIRED_STATISTICS_ZIPS = [
    APP_DIRECTORY / "paired_statistics_master BCM ACM.zip",
    APP_DIRECTORY / "paired_statistics_master_BCM_ACM.zip",
    APP_DIRECTORY / "data" / "paired_statistics_master BCM ACM.zip",
    APP_DIRECTORY / "data" / "paired_statistics_master_BCM_ACM.zip",
    APP_DIRECTORY / "assets" / "data" / "paired_statistics_master BCM ACM.zip",
    APP_DIRECTORY / "assets" / "data" / "paired_statistics_master_BCM_ACM.zip",
]

BCM_ACM_PAIRED_STATISTICS_DIRECTORIES = [
    APP_DIRECTORY / "paired_statistics_master",
    APP_DIRECTORY / "data" / "paired_statistics_master",
    APP_DIRECTORY / "assets" / "data" / "paired_statistics_master",
    APP_DIRECTORY,
    APP_DIRECTORY / "data",
    APP_DIRECTORY / "assets" / "data",
]


BM_AM_PAIRED_STATISTICS_ZIPS = [
    APP_DIRECTORY / "paired_statistics_master BM AM.zip",
    APP_DIRECTORY / "paired_statistics_master_BM_AM.zip",
    APP_DIRECTORY / "data" / "paired_statistics_master BM AM.zip",
    APP_DIRECTORY / "data" / "paired_statistics_master_BM_AM.zip",
    APP_DIRECTORY / "assets" / "data" / "paired_statistics_master BM AM.zip",
    APP_DIRECTORY / "assets" / "data" / "paired_statistics_master_BM_AM.zip",
]

BM_AM_PAIRED_STATISTICS_DIRECTORIES = [
    APP_DIRECTORY / "paired_statistics_master",
    APP_DIRECTORY / "data" / "paired_statistics_master",
    APP_DIRECTORY / "assets" / "data" / "paired_statistics_master",
    APP_DIRECTORY,
    APP_DIRECTORY / "data",
    APP_DIRECTORY / "assets" / "data",
]


BF_AF_SUBJECT_LEVEL_FILES = [
    APP_DIRECTORY / "subject_level_master_BF_AF.csv",
    APP_DIRECTORY / "subject_level_master_BF_AF(1).csv",
    APP_DIRECTORY / "subject_level_master_BF_AF(2).csv",
    APP_DIRECTORY / "subject_level_master_BF_AF(3).csv",
    APP_DIRECTORY / "data" / "subject_level_master_BF_AF.csv",
    APP_DIRECTORY / "data" / "subject_level_master_BF_AF(1).csv",
    APP_DIRECTORY / "data" / "subject_level_master_BF_AF(2).csv",
    APP_DIRECTORY / "data" / "subject_level_master_BF_AF(3).csv",
    APP_DIRECTORY / "assets" / "data" / "subject_level_master_BF_AF.csv",
    APP_DIRECTORY / "assets" / "data" / "subject_level_master_BF_AF(1).csv",
    APP_DIRECTORY / "assets" / "data" / "subject_level_master_BF_AF(2).csv",
    APP_DIRECTORY / "assets" / "data" / "subject_level_master_BF_AF(3).csv",
]

BF_AF_BAND_ORDER = ["Gamma", "Beta", "Alpha", "Theta", "Delta"]
BF_AF_CHANNEL_ORDER = ["TP9", "AF7", "AF8", "TP10"]

BF_AF_DIRECTION_COLORS = {
    "Increase": "#1F6B35",
    "Decrease": "#D95F59",
    "No Change": "#9CA3AF",
}

BF_AF_BAND_HIGHLIGHTS = {
    "Gamma": (
        "Gamma Band Power accounted for most of the upward pattern. At AF7, "
        "it increased in 8 of 10 paired subjects, with a mean change of "
        "+49,068.67 and a median change of +16,044.08."
    ),
    "Beta": (
        "At TP9, Beta Band Power increased in 7 of 10 paired subjects, while "
        "Beta Relative Power decreased in 7 of 10 subjects. Absolute and "
        "relative Beta power should therefore be interpreted separately."
    ),
    "Alpha": (
        "Alpha Band Power at AF8 and Alpha Relative Power at TP10 each "
        "increased in 7 of 10 paired subjects. The upward tendency occurred "
        "in both absolute and relative Alpha measures."
    ),
    "Theta": (
        "Theta Band Power at TP10 and Theta Relative Power at AF8 each "
        "decreased in 8 of 10 paired subjects, contributing to the clearest "
        "downward tendency among the five bands."
    ),
    "Delta": (
        "Delta Band Power at AF8 decreased in 7 of 10 paired subjects. Its "
        "positive mean change but negative median indicates that a small "
        "number of large increases influenced the mean."
    ),
}


BCM_ACM_SUBJECT_LEVEL_FILES = [
    APP_DIRECTORY / "subject_level_master_BCM_ACM.csv",
    APP_DIRECTORY / "subject_level_master_BCM_ACM(1).csv",
    APP_DIRECTORY / "subject_level_master_BCM_ACM(2).csv",
    APP_DIRECTORY / "data" / "subject_level_master_BCM_ACM.csv",
    APP_DIRECTORY / "data" / "subject_level_master_BCM_ACM(1).csv",
    APP_DIRECTORY / "data" / "subject_level_master_BCM_ACM(2).csv",
    APP_DIRECTORY / "assets" / "data" / "subject_level_master_BCM_ACM.csv",
    APP_DIRECTORY / "assets" / "data" / "subject_level_master_BCM_ACM(1).csv",
    APP_DIRECTORY / "assets" / "data" / "subject_level_master_BCM_ACM(2).csv",
]

BCM_ACM_BAND_ORDER = ["Gamma", "Beta", "Alpha", "Theta", "Delta"]
BCM_ACM_CHANNEL_ORDER = ["TP9", "AF7", "AF8", "TP10"]

BCM_ACM_DIRECTION_COLORS = {
    "Increase": "#1F6B35",
    "Decrease": "#D95F59",
    "No Change": "#9CA3AF",
}

BCM_ACM_BAND_HIGHLIGHTS = {
    "Gamma": (
        "Gamma Band Power decreased in 6 of 10 paired subjects at each "
        "channel. At TP9, the positive mean but negative median change "
        "indicates that a small number of large increases influenced the mean."
    ),
    "Beta": (
        "Beta Band Power decreased in 6 of 10 paired subjects at AF7, AF8, "
        "and TP9. No channel-feature combination exceeded 60% directional "
        "consistency."
    ),
    "Alpha": (
        "Alpha Band Power at AF8 decreased in 8 of 10 paired subjects, with "
        "a mean change of -2,287.77 and a median change of -4,028.63. Alpha "
        "Relative Power at AF7 increased in 7 of 10 subjects."
    ),
    "Theta": (
        "Theta Band Power decreased in 7 of 10 paired subjects at TP10 and "
        "TP9, but increased in 7 of 10 subjects at AF7. This indicates a "
        "channel-dependent response."
    ),
    "Delta": (
        "Delta Relative Power at TP9 decreased in 8 of 10 paired subjects. "
        "In contrast, Delta Relative Power at TP10 increased in 7 of 10 "
        "subjects."
    ),
}


BM_AM_SUBJECT_LEVEL_FILES = [
    APP_DIRECTORY / "subject_level_master_BM_AM.csv",
    APP_DIRECTORY / "subject_level_master_BM_AM(1).csv",
    APP_DIRECTORY / "subject_level_master_BM_AM(2).csv",
    APP_DIRECTORY / "data" / "subject_level_master_BM_AM.csv",
    APP_DIRECTORY / "data" / "subject_level_master_BM_AM(1).csv",
    APP_DIRECTORY / "data" / "subject_level_master_BM_AM(2).csv",
    APP_DIRECTORY / "assets" / "data" / "subject_level_master_BM_AM.csv",
    APP_DIRECTORY / "assets" / "data" / "subject_level_master_BM_AM(1).csv",
    APP_DIRECTORY / "assets" / "data" / "subject_level_master_BM_AM(2).csv",
]

BM_AM_BAND_ORDER = ["Gamma", "Beta", "Alpha", "Theta", "Delta"]
BM_AM_CHANNEL_ORDER = ["TP9", "AF7", "AF8", "TP10"]

BM_AM_DIRECTION_COLORS = {
    "Increase": "#1F6B35",
    "Decrease": "#D95F59",
    "No Change": "#9CA3AF",
}

BM_AM_BAND_HIGHLIGHTS = {
    "Gamma": (
        "Gamma Band Power decreased in 22 of 40 comparisons, whereas Gamma "
        "Relative Power increased in 23 of 40. At TP9, Gamma Band Power "
        "decreased in 7 of 10 subjects, with a mean change of -71,377.78 and "
        "a median change of -20,624.21."
    ),
    "Beta": (
        "Beta Band Power decreased in 23 of 40 comparisons, while Beta "
        "Relative Power increased slightly more often than it decreased. At "
        "TP10, Beta Band Power decreased in 8 of 10 subjects, with a mean "
        "change of -91,136.93 and a median change of -16,187.59."
    ),
    "Alpha": (
        "Alpha Band Power decreased in 25 of 40 comparisons. At TP9, it "
        "decreased in 9 of 10 subjects, with a mean change of -37,793.02 and "
        "a median change of -13,236.71. Alpha Relative Power at AF8 increased "
        "in 8 of 10 subjects."
    ),
    "Theta": (
        "Theta Band Power decreased in 23 of 40 comparisons, while Relative "
        "Power was more balanced. Theta Relative Power at AF8 decreased in "
        "7 of 10 subjects; its positive mean and negative median indicate that "
        "a small number of larger increases influenced the mean."
    ),
    "Delta": (
        "Delta Band Power decreased in 26 of 40 comparisons. At AF8, it "
        "decreased in 9 of 10 subjects, with a mean change of -19,166.91 and "
        "a median change of -5,746.71. Delta Relative Power at TP10 increased "
        "in 8 of 10 subjects."
    ),
}


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
        ("All Bands", "SVM", 0.8736, 0.8316),
        ("All Bands", "Random Forest", 0.9057, 0.8168),
        ("All Bands", "1D CNN", 0.8727, 0.8035),
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
        "Augmented Samples": [11956, 2562, 2562],
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
        "Augmented Samples": [5040, 1080, 1080],
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
        "Augmented Samples": [11508, 2466, 2466],
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

# ---------------------------------------------------------------------------
# BM vs AM
# ---------------------------------------------------------------------------
# BM vs AM values supplied in the 10-subject landing-page document.
SUBJECT_10_BM_AM_READY = True
SUBJECT_10_BM_AM_TOTAL_EPOCHS = 7440
SUBJECT_10_BM_AM_CONDITION_EPOCHS = 3720

SUBJECT_10_BM_AM_SPLIT = pd.DataFrame(
    {
        "Dataset": ["Training", "Validation", "Test"],
        "Samples": [5208, 1116, 1116],
        "Percentage": ["70%", "15%", "15%"],
    }
)

SUBJECT_10_BM_AM_ACGAN = pd.DataFrame(
    {
        "Dataset": ["Training", "Validation", "Test"],
        "Real Samples": [5208, 1116, 1116],
        "Synthetic Samples": [5208, 1116, 1116],
        "Augmented Samples": [10416, 2232, 2232],
    }
)

SUBJECT_10_BM_AM_TEST_RESULTS = pd.DataFrame(
    [
        (1, "Gamma", "SVM", "Real + Synthetic", 0.824074),
        (2, "Delta", "1D CNN", "Real + Synthetic", 0.821296),
        (2, "Theta", "1D CNN", "Real + Synthetic", 0.821296),
        (4, "Delta", "SVM", "Real + Synthetic", 0.820370),
        (5, "Alpha", "SVM", "Real + Synthetic", 0.817593),
    ],
    columns=["Ranking", "Band", "Model", "Data", "Accuracy"],
)

SUBJECT_10_BM_AM_TRAIN_RESULTS = pd.DataFrame(
    [
        (1, "Theta", "1D CNN", "Real + Synthetic", 0.876786),
        (2, "Alpha", "SVM", "Real + Synthetic", 0.867262),
        (3, "Gamma", "SVM", "Real + Synthetic", 0.859325),
        (4, "Theta", "SVM", "Real + Synthetic", 0.853571),
        (5, "Delta", "SVM", "Real + Synthetic", 0.851984),
    ],
    columns=["Ranking", "Band", "Model", "Data", "Accuracy"],
)


def build_split_table(total_epochs):
    """Derive the 70/15/15 split from the total epoch count."""
    holdout = round(total_epochs * 0.15)
    training = total_epochs - (holdout * 2)
    return pd.DataFrame(
        {
            "Dataset": ["Training", "Validation", "Test"],
            "Samples": [training, holdout, holdout],
            "Percentage": ["70%", "15%", "15%"],
        }
    )


def build_acgan_table(total_epochs):
    """Derive the ACGAN augmentation table from the total epoch count."""
    holdout = round(total_epochs * 0.15)
    training = total_epochs - (holdout * 2)
    return pd.DataFrame(
        {
            "Dataset": ["Training", "Validation", "Test"],
            "Real Samples": [training, holdout, holdout],
            "Synthetic Samples": [training, holdout, holdout],
            "Augmented Samples": [training * 2, holdout * 2, holdout * 2],
        }
    )


SUBJECT_10_CONCLUSIONS = {
    "BCF vs ACF": {
        "best_result": "Beta-band SVM achieved the highest Real + Synthetic test accuracy at 84.70%.",
        "summary": (
            "The 10-subject BCF versus ACF analysis shows that the 56-feature representation "
            "derived from four EEG channels can support two-class classification within the "
            "ACGAN-augmented dataset."
        ),
        "interpretation": (
            "Beta-band features showed the strongest discriminative performance in the current "
            "pipeline, followed closely by Delta, Gamma, and Alpha SVM configurations. This should "
            "be interpreted as performance within an augmented evaluation setting."
        ),
        "next_step": (
            "Validate the model using real-only unseen EEG data before concluding that performance "
            "generalizes robustly beyond the present dataset."
        ),
    },
    "BF vs AF": {
        "best_result": "Gamma-band SVM achieved the highest Real + Synthetic test accuracy at 82.41%.",
        "summary": (
            "The 10-subject BF versus AF analysis shows that the 56-feature representation "
            "derived from four EEG channels can support two-class classification within the "
            "ACGAN-augmented dataset."
        ),
        "interpretation": (
            "Gamma-band SVM provided the strongest observed discriminative performance. However, "
            "the Delta-band and Theta-band 1D CNN models were close behind at 82.13%, so the small "
            "margins do not establish clear model superiority."
        ),
        "next_step": (
            "Evaluate real-only unseen EEG data to determine whether the observed performance "
            "generalizes beyond the augmented dataset."
        ),
    },
    "BCM vs ACM": {
        "best_result": "Gamma-band SVM achieved the highest Real + Synthetic test accuracy at 83.62%.",
        "summary": (
            "The 10-subject BCM versus ACM analysis shows that the 56-feature representation "
            "derived from four EEG channels can support two-class classification within the "
            "ACGAN-augmented dataset."
        ),
        "interpretation": (
            "Gamma-band features showed the strongest discriminative performance in the current "
            "pipeline, followed by Delta, Beta, and Alpha SVM configurations. This should be "
            "interpreted as performance within an augmented evaluation setting."
        ),
        "next_step": (
            "Validate the model using real-only unseen EEG data before concluding that performance "
            "generalizes robustly beyond the present dataset."
        ),
    },
    "BM vs AM": {
        "best_result": "Gamma-band SVM achieved the highest Real + Synthetic test accuracy at 82.41%.",
        "summary": (
            "The 10-subject BM versus AM dataset contains 7,440 EEG segments, evenly divided "
            "between BM and AM. The classification workflow uses 56 features derived from "
            "four EEG channels and ACGAN-based data augmentation."
        ),
        "interpretation": (
            "Gamma-band SVM produced the highest listed test accuracy. Delta-band and "
            "Theta-band 1D CNN configurations followed closely at 82.13%, so the small "
            "differences among the leading results do not establish clear model superiority."
        ),
        "next_step": (
            "Validate the model using real-only unseen EEG data before concluding that performance "
            "generalizes robustly beyond the present dataset."
        ),
    },
}

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
        "Deep Generative Modeling for Cannabis Classification Using "
        "Auxiliary Classifier Generative Adversarial Network (ACGAN)"
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
            "2,488 Data Distribution",
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
    metric_1.metric("EEG Segment", "2,488")
    metric_2.metric("EEG Channels", "4")
    metric_3.metric("Feature Methods", "4")
    metric_4.metric("Total Features", "56")

    (
        overview_tab,
        dataset_tab,
        preprocessing_tab,
        feature_tab,
        models_tab,
        acgan_tab,
        results_tab,
        conclusion_tab,
    ) = st.tabs(
        [
            "Overview",
            "Dataset",
            "Preprocessing",
            "Feature Extraction",
            "Baseline Models",
            "ACGAN",
            "Results",
            "Conclusion",
        ]
    )

    with overview_tab:
        left_column, right_column = st.columns(2)
        with left_column:
            with st.container(border=True):
                st.subheader("About")
                st.write("Classify cannabis EEG conditions before and after treatment using machine-learning and deep-learning models.")
        with right_column:
            with st.container(border=True):
                st.subheader("Classification labels")
                st.write("Label 0: BCF, BCM, BF, and BM.")
                st.write("Label 1: ACF, ACM, AF, and AM.")
        with st.container(border=True):
            st.subheader("Research workflow")
            st.write("Raw EEG data → preprocessing → feature extraction → baseline modelling → ACGAN augmentation → final evaluation.")

    with dataset_tab:
        st.subheader("Dataset summary")
        dataset_1, dataset_2, dataset_3 = st.columns(3)
        dataset_1.metric("Before Condition", "1,244")
        dataset_2.metric("After Condition", "1,244")
        dataset_3.metric("Epoch Shape", "(512, 4)")
        conditions = pd.DataFrame(
            {
                "Condition": ["BCF", "BCM", "BF", "BM", "ACF", "ACM", "AF", "AM"],
                "Label": [0, 0, 0, 0, 1, 1, 1, 1],
                "Data Distribution": [311, 311, 311, 311, 311, 311, 311, 311],
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
                {"Dataset": ["Training", "Validation", "Test"], "Real Samples": [1740, 374, 374], "Synthetic Samples": [1740, 374, 374], "Augmented Samples": [3480, 748, 748]}
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



    with conclusion_tab:
        st.subheader("Conclusion")

        conclusion_left, conclusion_right = st.columns(2)
        with conclusion_left:
            with st.container(border=True):
                st.subheader("Best-performing model")
                st.write("SVM")
                st.subheader("Best configuration")
                st.write("All Bands")
                st.subheader("Best single frequency band")
                st.write("Theta")
        with conclusion_right:
            with st.container(border=True):
                st.subheader("Augmented test accuracy")
                st.metric("SVM All Bands", "83.29%")
                st.metric("SVM Theta", "83.16%")
                st.caption("Difference between All Bands and Theta: 0.13 percentage points.")

        with st.container(border=True):
            st.subheader("Interpretation")
            st.write(
                "The single-subject analysis indicates that cross-band EEG features can "
                "support two-class classification within the augmented intra-subject dataset. "
                "SVM achieved the highest accuracy across all configurations, with All Bands "
                "reaching 83.29% and Theta reaching 83.16%."
            )
            st.write(
                "Because the difference is only 0.13 percentage points, All Bands cannot be "
                "considered conclusively superior to Theta without repeated validation. Theta "
                "appears to capture most of the discriminative information for this subject."
            )
            st.write(
                "These findings provide preliminary evidence of subject-specific decoding, not "
                "generalizable performance on unseen individuals or newly acquired EEG data."
            )

        with st.container(border=True):
            st.subheader("Future research")
            st.write(
                "Evaluate a larger and more heterogeneous cohort to determine whether the "
                "observed feature patterns, SVM performance, and the benefit of ACGAN-based "
                "augmentation remain consistent across individuals."
            )

def render_accuracy_chart(results_data, chart_title):
    """Render a consistent Top 5 accuracy chart for a training or test dataset."""
    st.subheader(chart_title)
    chart = px.bar(
        results_data,
        x="Band",
        y="Accuracy",
        color="Model",
        text="Accuracy",
        color_discrete_map={"SVM": "#1F6B35", "1D CNN": "#8FCF9C"},
    )
    chart.update_traces(texttemplate="%{text:.2%}", textposition="outside")
    chart.update_layout(
        height=420,
        margin=dict(l=10, r=10, t=30, b=10),
        plot_bgcolor="#FFFFFF",
        paper_bgcolor="#FFFFFF",
        legend_title_text="",
        xaxis_title="Frequency Band",
        yaxis_title="Accuracy",
        yaxis=dict(range=[0, 1], tickformat=".0%"),
    )
    st.plotly_chart(chart, use_container_width=True)


def render_subject_10_conclusion(comparison_name):
    """Render the conclusion that matches the selected 10-subject comparison."""
    conclusion = SUBJECT_10_CONCLUSIONS[comparison_name]
    st.subheader(f"Conclusion: {comparison_name}")

    with st.container(border=True):
        st.subheader("Key finding")
        st.write(conclusion["best_result"])

    with st.container(border=True):
        st.subheader("Summary")
        st.write(conclusion["summary"])
        st.write(conclusion["interpretation"])

    with st.container(border=True):
        st.subheader("Next step")
        st.write(conclusion["next_step"])


def find_bcf_acf_subject_level_file():
    """Return the first configured BCF vs ACF subject-level CSV that exists."""
    for file_path in BCF_ACF_SUBJECT_LEVEL_FILES:
        if file_path.exists():
            return file_path
    return None


@st.cache_data
def load_bcf_acf_subject_level():
    """Load and validate the BCF vs ACF subject-level master table."""
    file_path = find_bcf_acf_subject_level_file()
    if file_path is None:
        expected_locations = "\n".join(
            f"- {path.relative_to(APP_DIRECTORY)}"
            for path in BCF_ACF_SUBJECT_LEVEL_FILES
        )
        raise FileNotFoundError(
            "subject_level_master_BCF_ACF.csv was not found. "
            "Place the file in one of these locations:\n"
            f"{expected_locations}"
        )

    dataframe = pd.read_csv(file_path)
    required_columns = {
        "Band",
        "Subject",
        "Channel",
        "Feature_Type",
        "Feature",
        "BCF",
        "ACF",
    }
    missing_columns = required_columns.difference(dataframe.columns)
    if missing_columns:
        raise ValueError(
            "The BCF vs ACF subject-level CSV is missing required columns: "
            + ", ".join(sorted(missing_columns))
        )

    dataframe = dataframe.copy()
    dataframe["Band"] = dataframe["Band"].astype(str).str.strip().str.title()
    dataframe["Channel"] = dataframe["Channel"].astype(str).str.strip().str.upper()
    dataframe["Feature"] = dataframe["Feature"].astype(str).str.strip()
    dataframe["Feature_Type"] = (
        dataframe["Feature_Type"].astype(str).str.strip().str.upper()
    )

    for column in ["BCF", "ACF"]:
        dataframe[column] = pd.to_numeric(dataframe[column], errors="coerce")

    # Use ACF minus BCF as the reproducible change definition.
    dataframe["Change"] = dataframe["ACF"] - dataframe["BCF"]
    baseline = dataframe["BCF"].abs().replace(0, pd.NA)
    dataframe["Change_Percent"] = dataframe["Change"] / baseline * 100

    dataframe["Direction"] = dataframe["Change"].apply(
        lambda value: (
            "Missing"
            if pd.isna(value)
            else "Increase"
            if value > 0
            else "Decrease"
            if value < 0
            else "No Change"
        )
    )

    return dataframe


def format_bcf_acf_change(value):
    """Format feature changes without hiding small relative-power values."""
    if pd.isna(value):
        return "N/A"
    if abs(value) >= 1000:
        return f"{value:+,.2f}"
    if abs(value) >= 1:
        return f"{value:+,.3f}"
    return f"{value:+.4f}"


def get_bcf_acf_band_summary(dataframe, band):
    """Summarise BP and RP observations for one frequency band."""
    band_data = dataframe[dataframe["Band"] == band]
    band_specific = band_data[band_data["Feature_Type"].isin(["BP", "RP"])]

    total = len(band_specific)
    increased = int((band_specific["Direction"] == "Increase").sum())
    decreased = int((band_specific["Direction"] == "Decrease").sum())
    unchanged = int((band_specific["Direction"] == "No Change").sum())

    increase_percentage = increased / total * 100 if total else 0.0
    decrease_percentage = decreased / total * 100 if total else 0.0

    if abs(increase_percentage - decrease_percentage) < 3:
        tendency = "a nearly balanced pattern"
    elif increased > decreased:
        tendency = "an upward tendency"
    else:
        tendency = "a slight downward tendency"

    summary_text = (
        f"{band} showed {tendency}. {increased} of {total} band-specific "
        f"comparisons increased ({increase_percentage:.1f}%), while {decreased} "
        f"decreased ({decrease_percentage:.1f}%). "
        f"{BCF_ACF_BAND_HIGHLIGHTS[band]}"
    )

    return {
        "text": summary_text,
        "total": total,
        "increased": increased,
        "decreased": decreased,
        "unchanged": unchanged,
        "increase_percentage": increase_percentage,
        "decrease_percentage": decrease_percentage,
    }


def get_bcf_acf_selected_interpretation(selected, band, feature, channel):
    """Create a concise interpretation for the selected paired plot."""
    total = len(selected)
    increased = int((selected["Direction"] == "Increase").sum())
    decreased = int((selected["Direction"] == "Decrease").sum())
    unchanged = int((selected["Direction"] == "No Change").sum())

    mean_change = selected["Change"].mean()
    median_change = selected["Change"].median()

    if increased > decreased and increased > unchanged:
        direction_text = (
            f"{increased} of {total} paired subjects showed an increase in "
            f"{feature} at {channel}."
        )
    elif decreased > increased and decreased > unchanged:
        direction_text = (
            f"{decreased} of {total} paired subjects showed a decrease in "
            f"{feature} at {channel}."
        )
    else:
        direction_text = (
            f"{feature} at {channel} showed a mixed direction of change across "
            "the paired subjects."
        )

    return (
        f"{direction_text} The mean change was "
        f"{format_bcf_acf_change(mean_change)}, and the median change was "
        f"{format_bcf_acf_change(median_change)}. This is a descriptive "
        f"{band}-band pattern and should not be interpreted as statistical "
        "significance."
    )


def render_bcf_acf_subject_level():
    """Render the completed BCF vs ACF subject-level analysis dashboard."""
    st.subheader("Pre-post subject-level analysis")
    st.caption(
        "This section summarises within-subject changes from BCF to ACF while "
        "preserving the identity of every paired observation."
    )

    try:
        dataframe = load_bcf_acf_subject_level()
    except (FileNotFoundError, ValueError, pd.errors.ParserError) as error:
        st.error(str(error))
        st.info(
            "Keep subject_level_master_BCF_ACF.csv beside app.py or place it "
            "inside data/ or assets/data/, then redeploy the application."
        )
        return

    st.success(
        "**Key finding.** BCF-ACF changes were heterogeneous across subjects, "
        "channels, features, and frequency bands. Alpha showed the strongest "
        "upward tendency, while Delta showed a slight downward tendency. Gamma "
        "Band Power at AF8 increased in 9 of 10 subjects, whereas Theta Relative "
        "Power at TP9 decreased in 9 of 10 subjects. Statistical significance "
        "must be evaluated separately using paired tests, effect sizes, and FDR "
        "correction."
    )

    selected_band = st.selectbox(
        "Frequency band",
        BCF_ACF_BAND_ORDER,
        index=0,
        key="bcf_acf_subject_band",
    )
    band_data = dataframe[dataframe["Band"] == selected_band].copy()
    band_summary = get_bcf_acf_band_summary(dataframe, selected_band)

    metric_1, metric_2, metric_3, metric_4 = st.columns(4)
    metric_1.metric("Paired Subjects", band_data["Subject"].nunique())
    metric_2.metric("Band-Specific Comparisons", band_summary["total"])
    metric_3.metric(
        "Increased",
        band_summary["increased"],
        f"{band_summary['increase_percentage']:.1f}%",
    )
    metric_4.metric(
        "Decreased",
        band_summary["decreased"],
        f"{band_summary['decrease_percentage']:.1f}%",
        delta_color="inverse",
    )

    st.info(f"**{selected_band} summary.** {band_summary['text']}")

    preferred_features = [
        f"{selected_band} Band Power",
        f"{selected_band} Relative Power",
        "Entropy",
        "Hjorth Activity",
        "Hjorth Mobility",
        "Hjorth Complexity",
    ]
    available_features = set(band_data["Feature"].dropna().unique())
    feature_options = [
        feature for feature in preferred_features if feature in available_features
    ]
    available_channels = set(band_data["Channel"].dropna().unique())
    channel_options = [
        channel for channel in BCF_ACF_CHANNEL_ORDER if channel in available_channels
    ]

    if not feature_options or not channel_options:
        st.error(
            "No valid feature or channel options were found for the selected band."
        )
        return

    filter_1, filter_2 = st.columns(2)
    with filter_1:
        selected_feature = st.selectbox(
            "Feature",
            feature_options,
            key="bcf_acf_subject_feature",
        )
    with filter_2:
        selected_channel = st.selectbox(
            "Channel",
            channel_options,
            key="bcf_acf_subject_channel",
        )

    selected = band_data[
        (band_data["Feature"] == selected_feature)
        & (band_data["Channel"] == selected_channel)
    ].copy()
    selected = selected.sort_values("Subject")

    if selected.empty:
        st.warning("No subject-level records match the selected filters.")
        return

    paired_data = selected.melt(
        id_vars=["Subject"],
        value_vars=["BCF", "ACF"],
        var_name="Condition",
        value_name="Value",
    )
    paired_data["Subject Label"] = "Subject " + paired_data["Subject"].astype(str)

    paired_figure = px.line(
        paired_data,
        x="Condition",
        y="Value",
        color="Subject Label",
        markers=True,
        category_orders={"Condition": ["BCF", "ACF"]},
        title=(
            "Paired Before-After Plot<br>"
            f"<sup>{selected_band} | {selected_feature} | {selected_channel}</sup>"
        ),
    )
    paired_figure.update_traces(line={"width": 2}, marker={"size": 8})
    paired_figure.update_layout(
        showlegend=False,
        height=430,
        margin=dict(l=20, r=20, t=75, b=20),
        xaxis_title="",
        yaxis_title="Feature Value",
        hovermode="closest",
    )

    direction_order = ["Increase", "Decrease", "No Change"]
    direction_counts = (
        selected["Direction"]
        .value_counts()
        .reindex(direction_order, fill_value=0)
        .rename_axis("Direction")
        .reset_index(name="Subjects")
    )
    direction_figure = px.bar(
        direction_counts,
        x="Direction",
        y="Subjects",
        color="Direction",
        text="Subjects",
        color_discrete_map=BCF_ACF_DIRECTION_COLORS,
        category_orders={"Direction": direction_order},
        title=(
            "Direction of Change<br>"
            f"<sup>{selected_band} | {selected_feature} | {selected_channel}</sup>"
        ),
    )
    direction_figure.update_traces(textposition="outside")
    direction_figure.update_layout(
        showlegend=False,
        height=430,
        margin=dict(l=20, r=20, t=75, b=20),
        xaxis_title="",
        yaxis_title="Number of Paired Subjects",
        yaxis=dict(dtick=1, range=[0, max(11, len(selected) + 1)]),
    )

    chart_1, chart_2 = st.columns(2)
    with chart_1:
        st.plotly_chart(
            paired_figure,
            use_container_width=True,
            key="bcf_acf_paired_plot",
        )
        st.caption(
            "Each line connects measurements from the same subject. Upward lines "
            "indicate ACF > BCF, while downward lines indicate ACF < BCF."
        )
    with chart_2:
        st.plotly_chart(
            direction_figure,
            use_container_width=True,
            key="bcf_acf_direction_plot",
        )
        st.caption(
            "The bars count paired subjects whose selected feature increased, "
            "decreased, or remained unchanged."
        )

    st.markdown("#### Interpretation")
    st.write(
        get_bcf_acf_selected_interpretation(
            selected,
            selected_band,
            selected_feature,
            selected_channel,
        )
    )

    with st.expander("View summaries for all frequency bands", expanded=False):
        for band in BCF_ACF_BAND_ORDER:
            summary = get_bcf_acf_band_summary(dataframe, band)
            st.markdown(f"**{band}**  \n{summary['text']}")

    with st.expander("Important data and methodological notes", expanded=False):
        st.markdown(
            """
- Each frequency-band file contains 80 band-specific observations for Band Power and Relative Power.
- Each file also contains 160 shared observations for Entropy and the three Hjorth features.
- Shared features are repeated across the five band files and should not be counted five times in an All Bands summary.
- Direction counts describe individual increases and decreases. They do not measure statistical significance or effect magnitude.
- Mean changes should only be compared within the same feature and channel because the features use different numerical scales.
            """
        )

    with st.expander("View selected subject-level data", expanded=False):
        display_columns = [
            "Subject",
            "Channel",
            "Feature",
            "BCF",
            "ACF",
            "Change",
            "Change_Percent",
            "Direction",
        ]
        st.dataframe(
            selected[display_columns],
            use_container_width=True,
            hide_index=True,
        )

        safe_feature = (
            selected_feature.lower().replace(" ", "_").replace("/", "_")
        )
        st.download_button(
            "Download selected data (CSV)",
            data=selected[display_columns].to_csv(index=False).encode("utf-8"),
            file_name=(
                f"BCF_ACF_{selected_band}_{safe_feature}_{selected_channel}.csv"
            ),
            mime="text/csv",
            key="bcf_acf_subject_download",
        )


def get_bcf_acf_pre_post_key_finding(dataframe):
    """Create the BCF vs ACF pre-post headline from band-specific rows."""
    band_specific = dataframe[
        dataframe["Feature_Type"].isin(["BP", "RP"])
    ].copy()
    total = len(band_specific)
    increased = int((band_specific["Direction"] == "Increase").sum())
    decreased = int((band_specific["Direction"] == "Decrease").sum())

    band_counts = (
        band_specific.groupby(["Band", "Direction"], observed=True)
        .size()
        .unstack(fill_value=0)
    )
    for direction in ["Increase", "Decrease", "No Change"]:
        if direction not in band_counts.columns:
            band_counts[direction] = 0
    band_totals = band_counts[
        ["Increase", "Decrease", "No Change"]
    ].sum(axis=1)
    increase_rates = band_counts["Increase"].div(band_totals).mul(100)
    decrease_rates = band_counts["Decrease"].div(band_totals).mul(100)
    upward_band = increase_rates.idxmax()
    downward_band = decrease_rates.idxmax()

    pattern_counts = (
        band_specific.groupby(
            ["Band", "Channel", "Feature"], observed=True
        )["Direction"]
        .value_counts()
        .unstack(fill_value=0)
    )
    for direction in ["Increase", "Decrease", "No Change"]:
        if direction not in pattern_counts.columns:
            pattern_counts[direction] = 0
    pattern_counts["Total"] = pattern_counts[
        ["Increase", "Decrease", "No Change"]
    ].sum(axis=1)
    pattern_counts["Consistency"] = pattern_counts[
        ["Increase", "Decrease", "No Change"]
    ].max(axis=1).div(pattern_counts["Total"]).mul(100)
    pattern_counts["Dominant"] = pattern_counts[
        ["Increase", "Decrease", "No Change"]
    ].idxmax(axis=1)

    strongest_increase = (
        pattern_counts[pattern_counts["Dominant"] == "Increase"]
        .sort_values("Consistency", ascending=False)
        .iloc[0]
    )
    strongest_decrease = (
        pattern_counts[pattern_counts["Dominant"] == "Decrease"]
        .sort_values("Consistency", ascending=False)
        .iloc[0]
    )
    increase_band, increase_channel, increase_feature = (
        strongest_increase.name
    )
    decrease_band, decrease_channel, decrease_feature = (
        strongest_decrease.name
    )

    return (
        f"Across {total} band-specific subject-channel-feature comparisons, "
        f"{increased} increased ({increased / total * 100:.1f}%) and "
        f"{decreased} decreased ({decreased / total * 100:.1f}%) from BCF to "
        f"ACF. {upward_band} showed the strongest upward tendency, whereas "
        f"{downward_band} had the largest proportion of decreases. The most "
        f"consistent local increase was {increase_feature} at "
        f"{increase_channel} in {increase_band} "
        f"({strongest_increase['Consistency']:.0f}% of subjects), while the "
        f"most consistent decrease was {decrease_feature} at "
        f"{decrease_channel} in {decrease_band} "
        f"({strongest_decrease['Consistency']:.0f}% of subjects)."
    )


def get_bcf_acf_pre_post_interpretation(feature_data, band, feature):
    """Create a concise group-level interpretation across all four channels."""
    total = len(feature_data)
    increased = int((feature_data["Direction"] == "Increase").sum())
    decreased = int((feature_data["Direction"] == "Decrease").sum())
    unchanged = int((feature_data["Direction"] == "No Change").sum())

    channel_summary = (
        feature_data.groupby("Channel", observed=True)["Change"]
        .agg(Mean_Change="mean", Median_Change="median", Subjects="size")
    )
    strongest_channel = channel_summary["Mean_Change"].abs().idxmax()
    strongest_mean = channel_summary.loc[strongest_channel, "Mean_Change"]

    direction_counts = (
        feature_data.groupby(["Channel", "Direction"], observed=True)
        .size()
        .unstack(fill_value=0)
    )
    for direction in ["Increase", "Decrease", "No Change"]:
        if direction not in direction_counts.columns:
            direction_counts[direction] = 0
    direction_counts["Total"] = direction_counts[
        ["Increase", "Decrease", "No Change"]
    ].sum(axis=1)
    direction_counts["Consistency"] = direction_counts[
        ["Increase", "Decrease", "No Change"]
    ].max(axis=1).div(direction_counts["Total"])
    direction_counts["Dominant"] = direction_counts[
        ["Increase", "Decrease", "No Change"]
    ].idxmax(axis=1)
    most_consistent_channel = direction_counts["Consistency"].idxmax()
    dominant_direction = direction_counts.loc[
        most_consistent_channel, "Dominant"
    ]
    dominant_count = int(
        direction_counts.loc[most_consistent_channel, dominant_direction]
    )
    dominant_total = int(
        direction_counts.loc[most_consistent_channel, "Total"]
    )

    overall_pattern = (
        "more increases than decreases"
        if increased > decreased
        else "more decreases than increases"
        if decreased > increased
        else "an equal number of increases and decreases"
    )
    unchanged_text = (
        f", and {unchanged} showed no change" if unchanged else ""
    )

    return (
        f"Across all four channels, {feature} in {band} showed "
        f"{overall_pattern}: {increased} of {total} comparisons increased and "
        f"{decreased} decreased{unchanged_text}. {strongest_channel} had the "
        f"largest absolute mean change ({format_bcf_acf_change(strongest_mean)}). "
        f"The most consistent direction occurred at {most_consistent_channel}, "
        f"where {dominant_count} of {dominant_total} subjects showed a "
        f"{dominant_direction.lower()}. These are group-level descriptive "
        "patterns and do not establish statistical significance."
    )


def style_bcf_acf_pre_post_figure(figure, height):
    """Apply a light transparent style shared by the Pre-Post figures."""
    figure.update_layout(
        height=height,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font={"color": "#26343B", "size": 13},
        title={"font": {"size": 18, "color": "#1F2933"}},
        margin=dict(l=55, r=35, t=78, b=50),
        hoverlabel={
            "bgcolor": "#F7FAF9",
            "font": {"color": "#1F2933"},
        },
    )
    figure.update_xaxes(
        gridcolor="rgba(88,110,105,0.12)",
        linecolor="rgba(88,110,105,0.25)",
        zeroline=False,
    )
    figure.update_yaxes(
        gridcolor="rgba(88,110,105,0.12)",
        linecolor="rgba(88,110,105,0.25)",
        zeroline=False,
    )
    return figure


def build_bcf_acf_pre_post_paired_figure(feature_data, band, feature):
    """Build four compact channel panels of subject trajectories and means."""
    subject_order = (
        feature_data[["Subject"]]
        .drop_duplicates()
        .sort_values("Subject")["Subject"]
        .tolist()
    )
    subject_color_map = {
        subject: BCF_ACF_PREPOST_SUBJECT_COLORS[
            index % len(BCF_ACF_PREPOST_SUBJECT_COLORS)
        ]
        for index, subject in enumerate(subject_order)
    }

    figure = make_subplots(
        rows=2,
        cols=2,
        subplot_titles=BCF_ACF_CHANNEL_ORDER,
        shared_yaxes=True,
        vertical_spacing=0.16,
        horizontal_spacing=0.10,
    )

    for index, channel in enumerate(BCF_ACF_CHANNEL_ORDER):
        row = index // 2 + 1
        column = index % 2 + 1
        channel_data = feature_data[
            feature_data["Channel"] == channel
        ].sort_values("Subject")

        for _, subject_row in channel_data.iterrows():
            subject_label = str(subject_row["Subject"])
            subject_color = subject_color_map[subject_row["Subject"]]
            figure.add_trace(
                go.Scatter(
                    x=["BCF", "ACF"],
                    y=[subject_row["BCF"], subject_row["ACF"]],
                    mode="lines+markers",
                    line={"color": subject_color, "width": 2},
                    marker={
                        "size": 7,
                        "color": subject_color,
                    },
                    customdata=[subject_label, subject_label],
                    hovertemplate=(
                        "Subject: %{customdata}<br>Condition: %{x}<br>"
                        "Value: %{y:.4g}<extra></extra>"
                    ),
                    showlegend=False,
                ),
                row=row,
                col=column,
            )

        condition_means = channel_data[["BCF", "ACF"]].mean()
        figure.add_trace(
            go.Scatter(
                x=["BCF", "ACF"],
                y=[condition_means["BCF"], condition_means["ACF"]],
                mode="lines+markers",
                line={"color": "#174C5B", "width": 4},
                marker={
                    "size": 11,
                    "color": [
                        BCF_ACF_PREPOST_CONDITION_COLORS["BCF"],
                        BCF_ACF_PREPOST_CONDITION_COLORS["ACF"],
                    ],
                    "line": {"color": "#F5FAF7", "width": 2},
                },
                hovertemplate=(
                    "Channel mean<br>Condition: %{x}<br>"
                    "Mean value: %{y:.4g}<extra></extra>"
                ),
                name="Channel mean",
                showlegend=index == 0,
            ),
            row=row,
            col=column,
        )

    figure.update_xaxes(title_text="")
    figure.update_yaxes(title_text="Feature value", col=1)
    figure.update_annotations(font={"size": 14, "color": "#174C5B"})
    figure.update_layout(
        title=(
            "BCF to ACF Subject Trajectories<br>"
            f"<sup>{band} · {feature}</sup>"
        ),
        showlegend=True,
        legend={
            "orientation": "h",
            "yanchor": "bottom",
            "y": 1.02,
            "xanchor": "right",
            "x": 1,
        },
        hovermode="closest",
    )
    return style_bcf_acf_pre_post_figure(figure, 620)


def build_bcf_acf_change_distribution_figure(feature_data, band, feature):
    """Build compact box plots with all subject-level change values."""
    figure = px.box(
        feature_data,
        x="Channel",
        y="Change",
        points="all",
        color="Channel",
        hover_data={"Subject": True, "Change": ":.4g"},
        category_orders={"Channel": BCF_ACF_CHANNEL_ORDER},
        color_discrete_map=BCF_ACF_PREPOST_CHANNEL_COLORS,
        title=(
            "Paired Change Distribution<br>"
            f"<sup>{band} · {feature}</sup>"
        ),
    )
    figure.update_traces(
        jitter=0.32,
        pointpos=0,
        marker={"size": 7, "opacity": 0.74},
        line={"width": 1.6},
    )
    for trace in figure.data:
        trace.update(
            fillcolor=BCF_ACF_PREPOST_CHANNEL_FILLS.get(
                trace.name, "rgba(85,166,143,0.18)"
            )
        )
    figure.add_hline(
        y=0,
        line_color="#455A64",
        line_dash="dash",
        line_width=1.4,
    )
    figure.update_layout(
        showlegend=False,
        xaxis_title="EEG Channel",
        yaxis_title="Change (ACF - BCF)",
    )
    return style_bcf_acf_pre_post_figure(figure, 420)


def build_bcf_acf_mean_change_figure(feature_data, band, feature):
    """Build a horizontal lollipop chart of channel-level mean change."""
    summary = (
        feature_data.groupby("Channel", observed=True)["Change"]
        .agg(Mean_Change="mean", Median_Change="median", Subjects="size")
        .reindex(BCF_ACF_CHANNEL_ORDER)
        .dropna(subset=["Mean_Change"])
        .reset_index()
    )
    figure = go.Figure()
    for _, summary_row in summary.iterrows():
        channel = summary_row["Channel"]
        mean_change = summary_row["Mean_Change"]
        figure.add_trace(
            go.Scatter(
                x=[0, mean_change],
                y=[channel, channel],
                mode="lines",
                line={
                    "color": BCF_ACF_PREPOST_CHANNEL_COLORS[channel],
                    "width": 5,
                },
                hoverinfo="skip",
                showlegend=False,
            )
        )

    figure.add_trace(
        go.Scatter(
            x=summary["Mean_Change"],
            y=summary["Channel"],
            mode="markers+text",
            marker={
                "size": 16,
                "color": [
                    BCF_ACF_PREPOST_CHANNEL_COLORS[channel]
                    for channel in summary["Channel"]
                ],
                "line": {"color": "#F5FAF7", "width": 2},
            },
            text=[
                format_bcf_acf_change(value)
                for value in summary["Mean_Change"]
            ],
            textposition=[
                "middle right" if value >= 0 else "middle left"
                for value in summary["Mean_Change"]
            ],
            customdata=summary[["Median_Change", "Subjects"]].values,
            hovertemplate=(
                "Channel: %{y}<br>Mean change: %{x:.4g}<br>"
                "Median change: %{customdata[0]:.4g}<br>"
                "Paired subjects: %{customdata[1]:.0f}<extra></extra>"
            ),
            name="Mean change",
            showlegend=False,
        )
    )
    figure.add_vline(x=0, line_color="#455A64", line_width=1.4)
    figure.update_layout(
        title=(
            "Mean Change by EEG Channel<br>"
            f"<sup>{band} · {feature}</sup>"
        ),
        xaxis_title="Mean change (ACF - BCF)",
        yaxis_title="EEG Channel",
    )
    figure.update_yaxes(
        categoryorder="array",
        categoryarray=list(reversed(BCF_ACF_CHANNEL_ORDER)),
    )
    return style_bcf_acf_pre_post_figure(figure, 360)


def build_bcf_acf_direction_by_channel_figure(feature_data, band, feature):
    """Build a compact horizontal direction-of-change chart by channel."""
    direction_order = ["Increase", "Decrease", "No Change"]
    available_channels = set(feature_data["Channel"].dropna().unique())
    channel_order = [
        channel
        for channel in BCF_ACF_CHANNEL_ORDER
        if channel in available_channels
    ]
    complete_index = pd.MultiIndex.from_product(
        [channel_order, direction_order], names=["Channel", "Direction"]
    )
    counts = (
        feature_data.groupby(["Channel", "Direction"], observed=True)
        .size()
        .reindex(complete_index, fill_value=0)
        .rename("Subjects")
        .reset_index()
    )
    totals = counts.groupby("Channel")["Subjects"].transform("sum")
    counts["Percentage"] = (
        counts["Subjects"].div(totals.replace(0, pd.NA)).mul(100).fillna(0)
    )
    totals_by_channel = (
        feature_data.groupby("Channel", observed=True)
        .size()
        .reindex(channel_order)
    )
    figure = go.Figure()
    for direction in direction_order:
        direction_data = (
            counts[counts["Direction"] == direction]
            .set_index("Channel")
            .reindex(channel_order)
            .reset_index()
        )
        labels = [
            f"{int(subjects)}/{int(totals_by_channel.loc[channel])}"
            if percentage >= 12 and subjects > 0
            else ""
            for channel, subjects, percentage in zip(
                direction_data["Channel"],
                direction_data["Subjects"],
                direction_data["Percentage"],
            )
        ]
        figure.add_trace(
            go.Bar(
                x=direction_data["Percentage"],
                y=direction_data["Channel"],
                orientation="h",
                name=direction,
                marker_color=BCF_ACF_PREPOST_DIRECTION_COLORS[direction],
                text=labels,
                textposition="inside",
                textfont={
                    "color": (
                        "#FFFFFF"
                        if direction == "Increase"
                        else "#26443A"
                    )
                },
                customdata=direction_data[["Subjects"]].values,
                hovertemplate=(
                    "Channel: %{y}<br>Direction: %{fullData.name}<br>"
                    "Subjects: %{customdata[0]:.0f}<br>"
                    "Percentage: %{x:.1f}%<extra></extra>"
                ),
            )
        )
    figure.update_layout(
        title=(
            "Direction of Change by EEG Channel<br>"
            f"<sup>{band} · {feature}</sup>"
        ),
        barmode="stack",
        xaxis_title="Paired subjects (%)",
        yaxis_title="EEG Channel",
        legend={
            "title_text": "",
            "orientation": "h",
            "yanchor": "bottom",
            "y": 1.02,
            "xanchor": "right",
            "x": 1,
        },
    )
    figure.update_xaxes(range=[0, 100], ticksuffix="%")
    figure.update_yaxes(
        categoryorder="array",
        categoryarray=list(reversed(channel_order)),
    )
    return style_bcf_acf_pre_post_figure(figure, 360)


def render_bcf_acf_pre_post_visualizations():
    """Render four interactive BCF vs ACF pre-post visualizations."""
    st.subheader("Pre-post visualizations")
    st.caption(
        "Explore subject trajectories, the distribution of paired changes, "
        "channel-level mean change, and direction of change from BCF to ACF."
    )

    try:
        dataframe = load_bcf_acf_subject_level()
    except (FileNotFoundError, ValueError, pd.errors.ParserError) as error:
        st.error(str(error))
        st.info(
            "Keep subject_level_master_BCF_ACF.csv beside app.py or place it "
            "inside data/ or assets/data/, then redeploy the application."
        )
        return

    st.success(
        f"**Key finding.** {get_bcf_acf_pre_post_key_finding(dataframe)} "
        "These visual patterns are descriptive; statistical evidence is "
        "reported separately in the Paired Statistics tab."
    )

    filter_1, filter_2 = st.columns(2)
    with filter_1:
        selected_band = st.selectbox(
            "Frequency band",
            BCF_ACF_BAND_ORDER,
            index=0,
            key="bcf_acf_prepost_band",
        )

    band_data = dataframe[dataframe["Band"] == selected_band].copy()
    preferred_features = [
        f"{selected_band} Band Power",
        f"{selected_band} Relative Power",
        "Entropy",
        "Hjorth Activity",
        "Hjorth Mobility",
        "Hjorth Complexity",
    ]
    available_features = set(band_data["Feature"].dropna().unique())
    feature_options = [
        feature for feature in preferred_features if feature in available_features
    ]
    if not feature_options:
        st.error("No valid features were found for the selected frequency band.")
        return

    with filter_2:
        selected_feature = st.selectbox(
            "Feature",
            feature_options,
            index=0,
            key="bcf_acf_prepost_feature",
        )

    feature_data = band_data[
        band_data["Feature"] == selected_feature
    ].copy().sort_values(["Channel", "Subject"])
    available_channels = set(feature_data["Channel"].dropna().unique())
    missing_channels = [
        channel
        for channel in BCF_ACF_CHANNEL_ORDER
        if channel not in available_channels
    ]
    if missing_channels:
        st.error(
            "The selected group-level view is incomplete. Missing channels: "
            + ", ".join(missing_channels)
        )
        return

    if feature_data.empty:
        st.warning("No paired observations match the selected band and feature.")
        return

    st.info(
        "**Group-level interpretation.** "
        + get_bcf_acf_pre_post_interpretation(
            feature_data,
            selected_band,
            selected_feature,
        )
    )

    paired_figure = build_bcf_acf_pre_post_paired_figure(
        feature_data, selected_band, selected_feature
    )
    st.plotly_chart(
        paired_figure,
        use_container_width=True,
        key="bcf_acf_prepost_paired_plot",
    )
    st.caption(
        "Four panels show TP9, AF7, AF8, and TP10 simultaneously. Each line "
        "connects the BCF and ACF values from the same subject."
    )

    distribution_figure = build_bcf_acf_change_distribution_figure(
        feature_data, selected_band, selected_feature
    )
    st.plotly_chart(
        distribution_figure,
        use_container_width=True,
        key="bcf_acf_prepost_change_distribution",
    )
    st.caption(
        "Boxes show the median and interquartile range; dots preserve all 10 "
        "subject-level ACF-minus-BCF changes at each channel."
    )

    mean_figure = build_bcf_acf_mean_change_figure(
        feature_data, selected_band, selected_feature
    )
    st.plotly_chart(
        mean_figure,
        use_container_width=True,
        key="bcf_acf_prepost_mean_change",
    )
    st.caption(
        "Each lollipop extends from zero to the mean paired change. Hover over "
        "a marker to compare the mean, median, and paired-subject count."
    )

    direction_figure = build_bcf_acf_direction_by_channel_figure(
        feature_data, selected_band, selected_feature
    )
    st.plotly_chart(
        direction_figure,
        use_container_width=True,
        key="bcf_acf_prepost_direction_by_channel",
    )


def find_bf_af_subject_level_file():
    """Return the first configured BF vs AF subject-level CSV that exists."""
    for file_path in BF_AF_SUBJECT_LEVEL_FILES:
        if file_path.exists():
            return file_path
    return None


@st.cache_data
def load_bf_af_subject_level():
    """Load and validate the BF vs AF subject-level master table."""
    file_path = find_bf_af_subject_level_file()
    if file_path is None:
        expected_locations = "\n".join(
            f"- {path.relative_to(APP_DIRECTORY)}"
            for path in BF_AF_SUBJECT_LEVEL_FILES
        )
        raise FileNotFoundError(
            "subject_level_master_BF_AF.csv was not found. "
            "Place the file in one of these locations:\n"
            f"{expected_locations}"
        )

    dataframe = pd.read_csv(file_path)
    required_columns = {
        "Band",
        "Subject",
        "Channel",
        "Feature_Type",
        "Feature",
        "BF",
        "AF",
    }
    missing_columns = required_columns.difference(dataframe.columns)
    if missing_columns:
        raise ValueError(
            "The BF vs AF subject-level CSV is missing required columns: "
            + ", ".join(sorted(missing_columns))
        )

    dataframe = dataframe.copy()
    dataframe["Band"] = dataframe["Band"].astype(str).str.strip().str.title()
    dataframe["Channel"] = dataframe["Channel"].astype(str).str.strip().str.upper()
    dataframe["Feature"] = dataframe["Feature"].astype(str).str.strip()
    dataframe["Feature_Type"] = (
        dataframe["Feature_Type"].astype(str).str.strip().str.upper()
    )

    for column in ["BF", "AF"]:
        dataframe[column] = pd.to_numeric(dataframe[column], errors="coerce")

    # Use AF minus BF as the reproducible pre-post change definition.
    dataframe["Change"] = dataframe["AF"] - dataframe["BF"]
    baseline = dataframe["BF"].abs().replace(0, pd.NA)
    dataframe["Change_Percent"] = dataframe["Change"] / baseline * 100

    dataframe["Direction"] = dataframe["Change"].apply(
        lambda value: (
            "Missing"
            if pd.isna(value)
            else "Increase"
            if value > 0
            else "Decrease"
            if value < 0
            else "No Change"
        )
    )

    return dataframe


def format_bf_af_change(value):
    """Format BF vs AF changes without hiding small relative-power values."""
    if pd.isna(value):
        return "N/A"
    if abs(value) >= 1000:
        return f"{value:+,.2f}"
    if abs(value) >= 1:
        return f"{value:+,.3f}"
    return f"{value:+.4f}"


def get_bf_af_band_summary(dataframe, band):
    """Summarise BP and RP observations for one BF vs AF frequency band."""
    band_data = dataframe[dataframe["Band"] == band]
    band_specific = band_data[band_data["Feature_Type"].isin(["BP", "RP"])]

    total = len(band_specific)
    increased = int((band_specific["Direction"] == "Increase").sum())
    decreased = int((band_specific["Direction"] == "Decrease").sum())
    unchanged = int((band_specific["Direction"] == "No Change").sum())

    increase_percentage = increased / total * 100 if total else 0.0
    decrease_percentage = decreased / total * 100 if total else 0.0

    if increase_percentage >= 55:
        tendency = "an upward tendency"
    elif decrease_percentage >= 55:
        tendency = "a downward tendency"
    elif increased > decreased:
        tendency = "a slight upward tendency"
    elif decreased > increased:
        tendency = "a slight downward tendency"
    else:
        tendency = "a balanced pattern"

    summary_text = (
        f"{band} showed {tendency}. {increased} of {total} band-specific "
        f"comparisons increased ({increase_percentage:.1f}%), while {decreased} "
        f"decreased ({decrease_percentage:.1f}%). "
        f"{BF_AF_BAND_HIGHLIGHTS[band]}"
    )

    return {
        "text": summary_text,
        "total": total,
        "increased": increased,
        "decreased": decreased,
        "unchanged": unchanged,
        "increase_percentage": increase_percentage,
        "decrease_percentage": decrease_percentage,
    }


def get_bf_af_selected_interpretation(selected, band, feature, channel):
    """Create a concise interpretation for the selected BF vs AF paired plot."""
    total = len(selected)
    increased = int((selected["Direction"] == "Increase").sum())
    decreased = int((selected["Direction"] == "Decrease").sum())
    unchanged = int((selected["Direction"] == "No Change").sum())

    mean_change = selected["Change"].mean()
    median_change = selected["Change"].median()

    if increased > decreased and increased > unchanged:
        direction_text = (
            f"{increased} of {total} paired subjects showed an increase in "
            f"{feature} at {channel}."
        )
    elif decreased > increased and decreased > unchanged:
        direction_text = (
            f"{decreased} of {total} paired subjects showed a decrease in "
            f"{feature} at {channel}."
        )
    else:
        direction_text = (
            f"{feature} at {channel} showed a mixed direction of change across "
            "the paired subjects."
        )

    distribution_note = ""
    if mean_change * median_change < 0:
        distribution_note = (
            " The mean and median have opposite signs, indicating that a small "
            "number of larger changes influenced the mean."
        )

    return (
        f"{direction_text} The mean change was "
        f"{format_bf_af_change(mean_change)}, and the median change was "
        f"{format_bf_af_change(median_change)}.{distribution_note} This is a "
        f"descriptive {band}-band pattern and should not be interpreted as "
        "statistical significance."
    )


def render_bf_af_subject_level():
    """Render the completed BF vs AF subject-level analysis dashboard."""
    st.subheader("Pre-post subject-level analysis")
    st.caption(
        "This section summarises within-subject changes from BF to AF while "
        "preserving the identity of every paired observation."
    )

    try:
        dataframe = load_bf_af_subject_level()
    except (FileNotFoundError, ValueError, pd.errors.ParserError) as error:
        st.error(str(error))
        st.info(
            "Keep subject_level_master_BF_AF.csv beside app.py or place it "
            "inside data/ or assets/data/, then redeploy the application."
        )
        return

    st.success(
        "**Key finding.** BF-AF changes were heterogeneous across subjects, "
        "channels, features, and frequency bands. Gamma and Alpha showed the "
        "strongest upward tendencies, while Theta showed the clearest downward "
        "tendency. Gamma Band Power at AF7 increased in 8 of 10 subjects, "
        "whereas Theta Relative Power at AF8 and Theta Band Power at TP10 "
        "decreased in 8 of 10 subjects. These are descriptive patterns. "
        "Statistical significance must be evaluated separately using paired "
        "tests, effect sizes, and FDR correction."
    )

    selected_band = st.selectbox(
        "Frequency band",
        BF_AF_BAND_ORDER,
        index=0,
        key="bf_af_subject_band",
    )
    band_data = dataframe[dataframe["Band"] == selected_band].copy()
    band_summary = get_bf_af_band_summary(dataframe, selected_band)

    metric_1, metric_2, metric_3, metric_4 = st.columns(4)
    metric_1.metric("Paired Subjects", band_data["Subject"].nunique())
    metric_2.metric("Band-Specific Comparisons", band_summary["total"])
    metric_3.metric(
        "Increased",
        band_summary["increased"],
        f"{band_summary['increase_percentage']:.1f}%",
    )
    metric_4.metric(
        "Decreased",
        band_summary["decreased"],
        f"{band_summary['decrease_percentage']:.1f}%",
        delta_color="inverse",
    )

    st.info(f"**{selected_band} summary.** {band_summary['text']}")

    preferred_features = [
        f"{selected_band} Band Power",
        f"{selected_band} Relative Power",
        "Entropy",
        "Hjorth Activity",
        "Hjorth Mobility",
        "Hjorth Complexity",
    ]
    available_features = set(band_data["Feature"].dropna().unique())
    feature_options = [
        feature for feature in preferred_features if feature in available_features
    ]
    available_channels = set(band_data["Channel"].dropna().unique())
    channel_options = [
        channel for channel in BF_AF_CHANNEL_ORDER if channel in available_channels
    ]

    if not feature_options or not channel_options:
        st.error(
            "No valid feature or channel options were found for the selected band."
        )
        return

    filter_1, filter_2 = st.columns(2)
    with filter_1:
        selected_feature = st.selectbox(
            "Feature",
            feature_options,
            key="bf_af_subject_feature",
        )
    with filter_2:
        default_channel = (
            channel_options.index("AF7") if "AF7" in channel_options else 0
        )
        selected_channel = st.selectbox(
            "Channel",
            channel_options,
            index=default_channel,
            key="bf_af_subject_channel",
        )

    selected = band_data[
        (band_data["Feature"] == selected_feature)
        & (band_data["Channel"] == selected_channel)
    ].copy()
    selected = selected.sort_values("Subject")

    if selected.empty:
        st.warning("No subject-level records match the selected filters.")
        return

    paired_data = selected.melt(
        id_vars=["Subject"],
        value_vars=["BF", "AF"],
        var_name="Condition",
        value_name="Value",
    )
    paired_data["Subject Label"] = "Subject " + paired_data["Subject"].astype(str)

    paired_figure = px.line(
        paired_data,
        x="Condition",
        y="Value",
        color="Subject Label",
        markers=True,
        category_orders={"Condition": ["BF", "AF"]},
        title=(
            "Paired Before-After Plot<br>"
            f"<sup>{selected_band} | {selected_feature} | {selected_channel}</sup>"
        ),
    )
    paired_figure.update_traces(line={"width": 2}, marker={"size": 8})
    paired_figure.update_layout(
        showlegend=False,
        height=430,
        margin=dict(l=20, r=20, t=75, b=20),
        xaxis_title="",
        yaxis_title="Feature Value",
        hovermode="closest",
    )

    direction_order = ["Increase", "Decrease", "No Change"]
    direction_counts = (
        selected["Direction"]
        .value_counts()
        .reindex(direction_order, fill_value=0)
        .rename_axis("Direction")
        .reset_index(name="Subjects")
    )
    direction_figure = px.bar(
        direction_counts,
        x="Direction",
        y="Subjects",
        color="Direction",
        text="Subjects",
        color_discrete_map=BF_AF_DIRECTION_COLORS,
        category_orders={"Direction": direction_order},
        title=(
            "Direction of Change<br>"
            f"<sup>{selected_band} | {selected_feature} | {selected_channel}</sup>"
        ),
    )
    direction_figure.update_traces(textposition="outside")
    direction_figure.update_layout(
        showlegend=False,
        height=430,
        margin=dict(l=20, r=20, t=75, b=20),
        xaxis_title="",
        yaxis_title="Number of Paired Subjects",
        yaxis=dict(dtick=1, range=[0, max(11, len(selected) + 1)]),
    )

    chart_1, chart_2 = st.columns(2)
    with chart_1:
        st.plotly_chart(
            paired_figure,
            use_container_width=True,
            key="bf_af_paired_plot",
        )
        st.caption(
            "Each line connects measurements from the same subject. Upward lines "
            "indicate AF > BF, while downward lines indicate AF < BF."
        )
    with chart_2:
        st.plotly_chart(
            direction_figure,
            use_container_width=True,
            key="bf_af_direction_plot",
        )
        st.caption(
            "The bars count paired subjects whose selected feature increased, "
            "decreased, or remained unchanged."
        )

    st.markdown("#### Interpretation")
    st.write(
        get_bf_af_selected_interpretation(
            selected,
            selected_band,
            selected_feature,
            selected_channel,
        )
    )

    with st.expander("View summaries for all frequency bands", expanded=False):
        for band in BF_AF_BAND_ORDER:
            summary = get_bf_af_band_summary(dataframe, band)
            st.markdown(f"**{band}**  \n{summary['text']}")

    with st.expander("Important data and methodological notes", expanded=False):
        st.markdown(
            """
- Each frequency-band file contains 80 band-specific observations for Band Power and Relative Power.
- Each file also contains 160 shared observations for Entropy and the three Hjorth features.
- Shared features are repeated across the five band files and should not be counted five times in an All Bands summary.
- Across the five bands, the comparison contains 400 band-specific observations and 560 unique observations after repeated shared features are removed.
- Change is calculated as AF minus BF.
- Direction counts describe individual increases and decreases. They do not measure statistical significance or effect magnitude.
- Mean changes should only be compared within the same feature and channel because the features use different numerical scales.
            """
        )

    with st.expander("View selected subject-level data", expanded=False):
        display_columns = [
            "Subject",
            "Channel",
            "Feature",
            "BF",
            "AF",
            "Change",
            "Change_Percent",
            "Direction",
        ]
        st.dataframe(
            selected[display_columns],
            use_container_width=True,
            hide_index=True,
        )

        safe_feature = (
            selected_feature.lower().replace(" ", "_").replace("/", "_")
        )
        st.download_button(
            "Download selected data (CSV)",
            data=selected[display_columns].to_csv(index=False).encode("utf-8"),
            file_name=(
                f"BF_AF_{selected_band}_{safe_feature}_{selected_channel}.csv"
            ),
            mime="text/csv",
            key="bf_af_subject_download",
        )


def get_bf_af_pre_post_key_finding(dataframe):
    """Create the BF vs AF pre-post headline from band-specific rows."""
    return (
        get_bcf_acf_pre_post_key_finding(dataframe)
        .replace("BCF", "BF")
        .replace("ACF", "AF")
    )


def get_bf_af_pre_post_interpretation(feature_data, band, feature):
    """Create a concise BF vs AF interpretation across all four channels."""
    total = len(feature_data)
    increased = int((feature_data["Direction"] == "Increase").sum())
    decreased = int((feature_data["Direction"] == "Decrease").sum())
    unchanged = int((feature_data["Direction"] == "No Change").sum())

    channel_summary = (
        feature_data.groupby("Channel", observed=True)["Change"]
        .agg(Mean_Change="mean", Median_Change="median", Subjects="size")
    )
    strongest_channel = channel_summary["Mean_Change"].abs().idxmax()
    strongest_mean = channel_summary.loc[strongest_channel, "Mean_Change"]

    direction_counts = (
        feature_data.groupby(["Channel", "Direction"], observed=True)
        .size()
        .unstack(fill_value=0)
    )
    for direction in ["Increase", "Decrease", "No Change"]:
        if direction not in direction_counts.columns:
            direction_counts[direction] = 0
    direction_counts["Total"] = direction_counts[
        ["Increase", "Decrease", "No Change"]
    ].sum(axis=1)
    direction_counts["Consistency"] = direction_counts[
        ["Increase", "Decrease", "No Change"]
    ].max(axis=1).div(direction_counts["Total"])
    direction_counts["Dominant"] = direction_counts[
        ["Increase", "Decrease", "No Change"]
    ].idxmax(axis=1)
    most_consistent_channel = direction_counts["Consistency"].idxmax()
    dominant_direction = direction_counts.loc[
        most_consistent_channel, "Dominant"
    ]
    dominant_count = int(
        direction_counts.loc[most_consistent_channel, dominant_direction]
    )
    dominant_total = int(
        direction_counts.loc[most_consistent_channel, "Total"]
    )

    overall_pattern = (
        "more increases than decreases"
        if increased > decreased
        else "more decreases than increases"
        if decreased > increased
        else "an equal number of increases and decreases"
    )
    unchanged_text = (
        f", and {unchanged} showed no change" if unchanged else ""
    )

    return (
        f"Across all four channels, {feature} in {band} showed "
        f"{overall_pattern}: {increased} of {total} comparisons increased and "
        f"{decreased} decreased{unchanged_text}. {strongest_channel} had the "
        f"largest absolute mean change ({format_bf_af_change(strongest_mean)}). "
        f"The most consistent direction occurred at {most_consistent_channel}, "
        f"where {dominant_count} of {dominant_total} subjects showed a "
        f"{dominant_direction.lower()}. These are group-level descriptive "
        "patterns and do not establish statistical significance."
    )


def _replace_bcf_acf_figure_labels(figure):
    """Convert labels in a reusable BCF-ACF figure to BF-AF labels."""
    title_text = figure.layout.title.text or ""
    figure.update_layout(
        title_text=title_text.replace("BCF", "BF").replace("ACF", "AF")
    )
    return figure


def build_bf_af_pre_post_paired_figure(feature_data, band, feature):
    """Build four channel panels of BF to AF subject trajectories."""
    reusable_data = feature_data.rename(columns={"BF": "BCF", "AF": "ACF"})
    figure = build_bcf_acf_pre_post_paired_figure(
        reusable_data, band, feature
    )
    for trace in figure.data:
        if tuple(trace.x) == ("BCF", "ACF"):
            trace.x = ("BF", "AF")
    return _replace_bcf_acf_figure_labels(figure)


def build_bf_af_change_distribution_figure(feature_data, band, feature):
    """Build channel-level box plots of AF-minus-BF paired changes."""
    figure = build_bcf_acf_change_distribution_figure(
        feature_data, band, feature
    )
    figure.update_yaxes(title_text="Change (AF - BF)")
    return _replace_bcf_acf_figure_labels(figure)


def build_bf_af_mean_change_figure(feature_data, band, feature):
    """Build a horizontal lollipop chart of AF-minus-BF mean change."""
    figure = build_bcf_acf_mean_change_figure(feature_data, band, feature)
    figure.update_xaxes(title_text="Mean change (AF - BF)")
    return _replace_bcf_acf_figure_labels(figure)


def build_bf_af_direction_by_channel_figure(feature_data, band, feature):
    """Build a horizontal direction-of-change chart for BF vs AF."""
    figure = build_bcf_acf_direction_by_channel_figure(
        feature_data, band, feature
    )
    return _replace_bcf_acf_figure_labels(figure)


def render_bf_af_pre_post_visualizations():
    """Render four interactive BF vs AF pre-post visualizations."""
    st.subheader("Pre-post visualizations")
    st.caption(
        "Explore subject trajectories, the distribution of paired changes, "
        "channel-level mean change, and direction of change from BF to AF."
    )

    try:
        dataframe = load_bf_af_subject_level()
    except (FileNotFoundError, ValueError, pd.errors.ParserError) as error:
        st.error(str(error))
        st.info(
            "Keep subject_level_master_BF_AF.csv beside app.py or place it "
            "inside data/ or assets/data/, then redeploy the application."
        )
        return

    st.success(
        f"**Key finding.** {get_bf_af_pre_post_key_finding(dataframe)} "
        "These visual patterns are descriptive; statistical evidence is "
        "reported separately in the Paired Statistics tab."
    )

    filter_1, filter_2 = st.columns(2)
    with filter_1:
        selected_band = st.selectbox(
            "Frequency band",
            BF_AF_BAND_ORDER,
            index=0,
            key="bf_af_prepost_band",
        )

    band_data = dataframe[dataframe["Band"] == selected_band].copy()
    preferred_features = [
        f"{selected_band} Band Power",
        f"{selected_band} Relative Power",
        "Entropy",
        "Hjorth Activity",
        "Hjorth Mobility",
        "Hjorth Complexity",
    ]
    available_features = set(band_data["Feature"].dropna().unique())
    feature_options = [
        feature for feature in preferred_features if feature in available_features
    ]
    if not feature_options:
        st.error("No valid features were found for the selected frequency band.")
        return

    with filter_2:
        selected_feature = st.selectbox(
            "Feature",
            feature_options,
            index=0,
            key="bf_af_prepost_feature",
        )

    feature_data = band_data[
        band_data["Feature"] == selected_feature
    ].copy().sort_values(["Channel", "Subject"])
    available_channels = set(feature_data["Channel"].dropna().unique())
    missing_channels = [
        channel
        for channel in BF_AF_CHANNEL_ORDER
        if channel not in available_channels
    ]
    if missing_channels:
        st.error(
            "The selected group-level view is incomplete. Missing channels: "
            + ", ".join(missing_channels)
        )
        return

    if feature_data.empty:
        st.warning("No paired observations match the selected band and feature.")
        return

    st.info(
        "**Group-level interpretation.** "
        + get_bf_af_pre_post_interpretation(
            feature_data,
            selected_band,
            selected_feature,
        )
    )

    paired_figure = build_bf_af_pre_post_paired_figure(
        feature_data, selected_band, selected_feature
    )
    st.plotly_chart(
        paired_figure,
        use_container_width=True,
        key="bf_af_prepost_paired_plot",
    )
    st.caption(
        "Four panels show TP9, AF7, AF8, and TP10 simultaneously. Each line "
        "connects the BF and AF values from the same subject."
    )

    distribution_figure = build_bf_af_change_distribution_figure(
        feature_data, selected_band, selected_feature
    )
    st.plotly_chart(
        distribution_figure,
        use_container_width=True,
        key="bf_af_prepost_change_distribution",
    )
    st.caption(
        "Boxes show the median and interquartile range; dots preserve all 10 "
        "subject-level AF-minus-BF changes at each channel."
    )

    mean_figure = build_bf_af_mean_change_figure(
        feature_data, selected_band, selected_feature
    )
    st.plotly_chart(
        mean_figure,
        use_container_width=True,
        key="bf_af_prepost_mean_change",
    )
    st.caption(
        "Each lollipop extends from zero to the mean paired change. Hover over "
        "a marker to compare the mean, median, and paired-subject count."
    )

    direction_figure = build_bf_af_direction_by_channel_figure(
        feature_data, selected_band, selected_feature
    )
    st.plotly_chart(
        direction_figure,
        use_container_width=True,
        key="bf_af_prepost_direction_by_channel",
    )


def find_bcm_acm_subject_level_file():
    """Return the first configured BCM vs ACM subject-level CSV that exists."""
    for file_path in BCM_ACM_SUBJECT_LEVEL_FILES:
        if file_path.exists():
            return file_path
    return None


@st.cache_data
def load_bcm_acm_subject_level():
    """Load and validate the BCM vs ACM subject-level master table."""
    file_path = find_bcm_acm_subject_level_file()
    if file_path is None:
        expected_locations = "\n".join(
            f"- {path.relative_to(APP_DIRECTORY)}"
            for path in BCM_ACM_SUBJECT_LEVEL_FILES
        )
        raise FileNotFoundError(
            "subject_level_master_BCM_ACM.csv was not found. "
            "Place the file in one of these locations:\n"
            f"{expected_locations}"
        )

    dataframe = pd.read_csv(file_path)
    required_columns = {
        "Band",
        "Subject",
        "Channel",
        "Feature_Type",
        "Feature",
        "BCM",
        "ACM",
    }
    missing_columns = required_columns.difference(dataframe.columns)
    if missing_columns:
        raise ValueError(
            "The BCM vs ACM subject-level CSV is missing required columns: "
            + ", ".join(sorted(missing_columns))
        )

    dataframe = dataframe.copy()
    dataframe["Band"] = dataframe["Band"].astype(str).str.strip().str.title()
    dataframe["Channel"] = dataframe["Channel"].astype(str).str.strip().str.upper()
    dataframe["Feature"] = dataframe["Feature"].astype(str).str.strip()
    dataframe["Feature_Type"] = (
        dataframe["Feature_Type"].astype(str).str.strip().str.upper()
    )

    for column in ["BCM", "ACM"]:
        dataframe[column] = pd.to_numeric(dataframe[column], errors="coerce")

    # Use ACM minus BCM as the reproducible pre-post change definition.
    dataframe["Change"] = dataframe["ACM"] - dataframe["BCM"]
    baseline = dataframe["BCM"].abs().replace(0, pd.NA)
    dataframe["Change_Percent"] = dataframe["Change"] / baseline * 100

    dataframe["Direction"] = dataframe["Change"].apply(
        lambda value: (
            "Missing"
            if pd.isna(value)
            else "Increase"
            if value > 0
            else "Decrease"
            if value < 0
            else "No Change"
        )
    )

    return dataframe


def format_bcm_acm_change(value):
    """Format BCM vs ACM changes without hiding small relative-power values."""
    if pd.isna(value):
        return "N/A"
    if abs(value) >= 1000:
        return f"{value:+,.2f}"
    if abs(value) >= 1:
        return f"{value:+,.3f}"
    return f"{value:+.4f}"


def get_bcm_acm_band_summary(dataframe, band):
    """Summarise BP and RP observations for one BCM vs ACM frequency band."""
    band_data = dataframe[dataframe["Band"] == band]
    band_specific = band_data[band_data["Feature_Type"].isin(["BP", "RP"])]

    total = len(band_specific)
    increased = int((band_specific["Direction"] == "Increase").sum())
    decreased = int((band_specific["Direction"] == "Decrease").sum())
    unchanged = int((band_specific["Direction"] == "No Change").sum())

    increase_percentage = increased / total * 100 if total else 0.0
    decrease_percentage = decreased / total * 100 if total else 0.0

    if increase_percentage >= 55:
        tendency = "an upward tendency"
    elif decrease_percentage >= 55:
        tendency = "a modest downward tendency"
    elif increased > decreased:
        tendency = "a slight upward tendency"
    elif decreased > increased:
        tendency = "a slight downward tendency"
    else:
        tendency = "a balanced pattern"

    summary_text = (
        f"{band} showed {tendency}. {decreased} of {total} band-specific "
        f"comparisons decreased ({decrease_percentage:.1f}%), while {increased} "
        f"increased ({increase_percentage:.1f}%). "
        f"{BCM_ACM_BAND_HIGHLIGHTS[band]}"
    )

    return {
        "text": summary_text,
        "total": total,
        "increased": increased,
        "decreased": decreased,
        "unchanged": unchanged,
        "increase_percentage": increase_percentage,
        "decrease_percentage": decrease_percentage,
    }


def get_bcm_acm_selected_interpretation(selected, band, feature, channel):
    """Create a concise interpretation for the selected BCM vs ACM plot."""
    total = len(selected)
    increased = int((selected["Direction"] == "Increase").sum())
    decreased = int((selected["Direction"] == "Decrease").sum())
    unchanged = int((selected["Direction"] == "No Change").sum())

    mean_change = selected["Change"].mean()
    median_change = selected["Change"].median()

    if increased > decreased and increased > unchanged:
        direction_text = (
            f"{increased} of {total} paired subjects showed an increase in "
            f"{feature} at {channel}."
        )
    elif decreased > increased and decreased > unchanged:
        direction_text = (
            f"{decreased} of {total} paired subjects showed a decrease in "
            f"{feature} at {channel}."
        )
    else:
        direction_text = (
            f"{feature} at {channel} showed a mixed direction of change across "
            "the paired subjects."
        )

    distribution_note = ""
    if mean_change * median_change < 0:
        distribution_note = (
            " The mean and median have opposite signs, indicating that a small "
            "number of larger changes influenced the mean."
        )

    return (
        f"{direction_text} The mean change was "
        f"{format_bcm_acm_change(mean_change)}, and the median change was "
        f"{format_bcm_acm_change(median_change)}.{distribution_note} This is a "
        f"descriptive {band}-band pattern and should not be interpreted as "
        "statistical significance."
    )


def render_bcm_acm_subject_level():
    """Render the completed BCM vs ACM subject-level analysis dashboard."""
    st.subheader("Pre-post subject-level analysis")
    st.caption(
        "This section summarises within-subject changes from BCM to ACM while "
        "preserving the identity of every paired observation."
    )

    try:
        dataframe = load_bcm_acm_subject_level()
    except (FileNotFoundError, ValueError, pd.errors.ParserError) as error:
        st.error(str(error))
        st.info(
            "Keep subject_level_master_BCM_ACM.csv beside app.py or place it "
            "inside data/ or assets/data/, then redeploy the application."
        )
        return

    st.success(
        "**Key finding.** Across 400 band-specific subject-channel-feature "
        "comparisons, 175 increased (43.8%) and 225 decreased (56.3%) from "
        "BCM to ACM. All five bands showed the same split of 35 increases and "
        "45 decreases. Alpha Band Power at AF8 and Delta Relative Power at "
        "TP9 each decreased in 8 of 10 subjects. Several opposing local "
        "patterns were also present, showing that the response depended on "
        "the channel and feature. Statistical significance must be evaluated "
        "separately using paired tests, effect sizes, and FDR correction."
    )

    selected_band = st.selectbox(
        "Frequency band",
        BCM_ACM_BAND_ORDER,
        index=0,
        key="bcm_acm_subject_band",
    )
    band_data = dataframe[dataframe["Band"] == selected_band].copy()
    band_summary = get_bcm_acm_band_summary(dataframe, selected_band)

    metric_1, metric_2, metric_3, metric_4 = st.columns(4)
    metric_1.metric("Paired Subjects", band_data["Subject"].nunique())
    metric_2.metric("Band-Specific Comparisons", band_summary["total"])
    metric_3.metric(
        "Increased",
        band_summary["increased"],
        f"{band_summary['increase_percentage']:.1f}%",
    )
    metric_4.metric(
        "Decreased",
        band_summary["decreased"],
        f"{band_summary['decrease_percentage']:.1f}%",
        delta_color="inverse",
    )

    st.info(f"**{selected_band} summary.** {band_summary['text']}")

    preferred_features = [
        f"{selected_band} Band Power",
        f"{selected_band} Relative Power",
        "Entropy",
        "Hjorth Activity",
        "Hjorth Mobility",
        "Hjorth Complexity",
    ]
    available_features = set(band_data["Feature"].dropna().unique())
    feature_options = [
        feature for feature in preferred_features if feature in available_features
    ]
    available_channels = set(band_data["Channel"].dropna().unique())
    channel_options = [
        channel for channel in BCM_ACM_CHANNEL_ORDER if channel in available_channels
    ]

    if not feature_options or not channel_options:
        st.error(
            "No valid feature or channel options were found for the selected band."
        )
        return

    filter_1, filter_2 = st.columns(2)
    with filter_1:
        selected_feature = st.selectbox(
            "Feature",
            feature_options,
            key="bcm_acm_subject_feature",
        )
    with filter_2:
        selected_channel = st.selectbox(
            "Channel",
            channel_options,
            key="bcm_acm_subject_channel",
        )

    selected = band_data[
        (band_data["Feature"] == selected_feature)
        & (band_data["Channel"] == selected_channel)
    ].copy()
    selected = selected.sort_values("Subject")

    if selected.empty:
        st.warning("No subject-level records match the selected filters.")
        return

    paired_data = selected.melt(
        id_vars=["Subject"],
        value_vars=["BCM", "ACM"],
        var_name="Condition",
        value_name="Value",
    )
    paired_data["Subject Label"] = "Subject " + paired_data["Subject"].astype(str)

    paired_figure = px.line(
        paired_data,
        x="Condition",
        y="Value",
        color="Subject Label",
        markers=True,
        category_orders={"Condition": ["BCM", "ACM"]},
        title=(
            "Paired Before-After Plot<br>"
            f"<sup>{selected_band} | {selected_feature} | {selected_channel}</sup>"
        ),
    )
    paired_figure.update_traces(line={"width": 2}, marker={"size": 8})
    paired_figure.update_layout(
        showlegend=False,
        height=430,
        margin=dict(l=20, r=20, t=75, b=20),
        xaxis_title="",
        yaxis_title="Feature Value",
        hovermode="closest",
    )

    direction_order = ["Increase", "Decrease", "No Change"]
    direction_counts = (
        selected["Direction"]
        .value_counts()
        .reindex(direction_order, fill_value=0)
        .rename_axis("Direction")
        .reset_index(name="Subjects")
    )
    direction_figure = px.bar(
        direction_counts,
        x="Direction",
        y="Subjects",
        color="Direction",
        text="Subjects",
        color_discrete_map=BCM_ACM_DIRECTION_COLORS,
        category_orders={"Direction": direction_order},
        title=(
            "Direction of Change<br>"
            f"<sup>{selected_band} | {selected_feature} | {selected_channel}</sup>"
        ),
    )
    direction_figure.update_traces(textposition="outside")
    direction_figure.update_layout(
        showlegend=False,
        height=430,
        margin=dict(l=20, r=20, t=75, b=20),
        xaxis_title="",
        yaxis_title="Number of Paired Subjects",
        yaxis=dict(dtick=1, range=[0, max(11, len(selected) + 1)]),
    )

    chart_1, chart_2 = st.columns(2)
    with chart_1:
        st.plotly_chart(
            paired_figure,
            use_container_width=True,
            key="bcm_acm_paired_plot",
        )
        st.caption(
            "Each line connects measurements from the same subject. Upward lines "
            "indicate ACM > BCM, while downward lines indicate ACM < BCM."
        )
    with chart_2:
        st.plotly_chart(
            direction_figure,
            use_container_width=True,
            key="bcm_acm_direction_plot",
        )
        st.caption(
            "The bars count paired subjects whose selected feature increased, "
            "decreased, or remained unchanged."
        )

    st.markdown("#### Interpretation")
    st.write(
        get_bcm_acm_selected_interpretation(
            selected,
            selected_band,
            selected_feature,
            selected_channel,
        )
    )

    with st.expander("View summaries for all frequency bands", expanded=False):
        for band in BCM_ACM_BAND_ORDER:
            summary = get_bcm_acm_band_summary(dataframe, band)
            st.markdown(f"**{band}**  \n{summary['text']}")

    with st.expander("Important data and methodological notes", expanded=False):
        st.markdown(
            """
- Each frequency-band file contains 80 band-specific observations for Band Power and Relative Power.
- Each file also contains 160 shared observations for Entropy and the three Hjorth features.
- Shared features are repeated across the five band files and should not be counted five times in an All Bands summary.
- The 1,200 source rows represent 400 band-specific observations and 800 repeated shared-feature rows. After repeated shared features are removed, the dataset contains 560 unique observations.
- Change is calculated as ACM minus BCM.
- Direction counts describe individual increases and decreases. They do not measure statistical significance or effect magnitude.
- Mean changes should only be compared within the same feature and channel because the features use different numerical scales.
            """
        )

    with st.expander("View selected subject-level data", expanded=False):
        display_columns = [
            "Subject",
            "Channel",
            "Feature",
            "BCM",
            "ACM",
            "Change",
            "Change_Percent",
            "Direction",
        ]
        st.dataframe(
            selected[display_columns],
            use_container_width=True,
            hide_index=True,
        )

        safe_feature = (
            selected_feature.lower().replace(" ", "_").replace("/", "_")
        )
        st.download_button(
            "Download selected data (CSV)",
            data=selected[display_columns].to_csv(index=False).encode("utf-8"),
            file_name=(
                f"BCM_ACM_{selected_band}_{safe_feature}_{selected_channel}.csv"
            ),
            mime="text/csv",
            key="bcm_acm_subject_download",
        )


def get_bcm_acm_pre_post_key_finding(dataframe):
    """Create an accurate BCM vs ACM headline from band-specific rows."""
    band_specific = dataframe[
        dataframe["Feature_Type"].isin(["BP", "RP"])
    ].copy()
    total = len(band_specific)
    increased = int((band_specific["Direction"] == "Increase").sum())
    decreased = int((band_specific["Direction"] == "Decrease").sum())

    band_counts = (
        band_specific.groupby(["Band", "Direction"], observed=True)
        .size()
        .unstack(fill_value=0)
    )
    for direction in ["Increase", "Decrease", "No Change"]:
        if direction not in band_counts.columns:
            band_counts[direction] = 0
    band_totals = band_counts[
        ["Increase", "Decrease", "No Change"]
    ].sum(axis=1)
    increase_rates = band_counts["Increase"].div(band_totals).mul(100)
    decrease_rates = band_counts["Decrease"].div(band_totals).mul(100)

    if increase_rates.nunique() == 1 and decrease_rates.nunique() == 1:
        band_tendency = (
            "All five frequency bands showed the same overall distribution "
            f"of {int(band_counts['Increase'].iloc[0])} increases and "
            f"{int(band_counts['Decrease'].iloc[0])} decreases."
        )
    else:
        band_tendency = (
            f"{increase_rates.idxmax()} showed the strongest upward tendency, "
            f"whereas {decrease_rates.idxmax()} had the largest proportion "
            "of decreases."
        )

    pattern_counts = (
        band_specific.groupby(
            ["Band", "Channel", "Feature"], observed=True
        )["Direction"]
        .value_counts()
        .unstack(fill_value=0)
    )
    for direction in ["Increase", "Decrease", "No Change"]:
        if direction not in pattern_counts.columns:
            pattern_counts[direction] = 0
    pattern_counts["Total"] = pattern_counts[
        ["Increase", "Decrease", "No Change"]
    ].sum(axis=1)
    pattern_counts["Consistency"] = pattern_counts[
        ["Increase", "Decrease", "No Change"]
    ].max(axis=1).div(pattern_counts["Total"]).mul(100)
    pattern_counts["Dominant"] = pattern_counts[
        ["Increase", "Decrease", "No Change"]
    ].idxmax(axis=1)

    strongest_increase = (
        pattern_counts[pattern_counts["Dominant"] == "Increase"]
        .sort_values("Consistency", ascending=False)
        .iloc[0]
    )
    strongest_decrease = (
        pattern_counts[pattern_counts["Dominant"] == "Decrease"]
        .sort_values("Consistency", ascending=False)
        .iloc[0]
    )
    increase_band, increase_channel, increase_feature = strongest_increase.name
    decrease_band, decrease_channel, decrease_feature = strongest_decrease.name

    return (
        f"Across {total} band-specific subject-channel-feature comparisons, "
        f"{increased} increased ({increased / total * 100:.1f}%) and "
        f"{decreased} decreased "
        f"({decreased / total * 100 + 1e-9:.1f}%) from BCM to "
        f"ACM. {band_tendency} The most consistent local increase was "
        f"{increase_feature} at {increase_channel} in {increase_band} "
        f"({strongest_increase['Consistency']:.0f}% of subjects), while the "
        f"most consistent decrease was {decrease_feature} at "
        f"{decrease_channel} in {decrease_band} "
        f"({strongest_decrease['Consistency']:.0f}% of subjects)."
    )


def get_bcm_acm_pre_post_interpretation(feature_data, band, feature):
    """Create a concise BCM vs ACM interpretation across all channels."""
    total = len(feature_data)
    increased = int((feature_data["Direction"] == "Increase").sum())
    decreased = int((feature_data["Direction"] == "Decrease").sum())
    unchanged = int((feature_data["Direction"] == "No Change").sum())

    channel_summary = (
        feature_data.groupby("Channel", observed=True)["Change"]
        .agg(Mean_Change="mean", Median_Change="median", Subjects="size")
    )
    strongest_channel = channel_summary["Mean_Change"].abs().idxmax()
    strongest_mean = channel_summary.loc[strongest_channel, "Mean_Change"]

    direction_counts = (
        feature_data.groupby(["Channel", "Direction"], observed=True)
        .size()
        .unstack(fill_value=0)
    )
    for direction in ["Increase", "Decrease", "No Change"]:
        if direction not in direction_counts.columns:
            direction_counts[direction] = 0
    direction_counts["Total"] = direction_counts[
        ["Increase", "Decrease", "No Change"]
    ].sum(axis=1)
    direction_counts["Consistency"] = direction_counts[
        ["Increase", "Decrease", "No Change"]
    ].max(axis=1).div(direction_counts["Total"])
    direction_counts["Dominant"] = direction_counts[
        ["Increase", "Decrease", "No Change"]
    ].idxmax(axis=1)
    most_consistent_channel = direction_counts["Consistency"].idxmax()
    dominant_direction = direction_counts.loc[
        most_consistent_channel, "Dominant"
    ]
    dominant_count = int(
        direction_counts.loc[most_consistent_channel, dominant_direction]
    )
    dominant_total = int(
        direction_counts.loc[most_consistent_channel, "Total"]
    )

    overall_pattern = (
        "more increases than decreases"
        if increased > decreased
        else "more decreases than increases"
        if decreased > increased
        else "an equal number of increases and decreases"
    )
    unchanged_text = (
        f", and {unchanged} showed no change" if unchanged else ""
    )

    return (
        f"Across all four channels, {feature} in {band} showed "
        f"{overall_pattern}: {increased} of {total} comparisons increased and "
        f"{decreased} decreased{unchanged_text}. {strongest_channel} had the "
        f"largest absolute mean change "
        f"({format_bcm_acm_change(strongest_mean)}). The most consistent "
        f"direction occurred at {most_consistent_channel}, where "
        f"{dominant_count} of {dominant_total} subjects showed a "
        f"{dominant_direction.lower()}. These are group-level descriptive "
        "patterns and do not establish statistical significance."
    )


def _replace_bcf_acf_with_bcm_acm_figure_labels(figure):
    """Convert labels in a reusable BCF-ACF figure to BCM-ACM labels."""
    title_text = figure.layout.title.text or ""
    figure.update_layout(
        title_text=title_text.replace("BCF", "BCM").replace("ACF", "ACM")
    )
    return figure


def build_bcm_acm_pre_post_paired_figure(feature_data, band, feature):
    """Build four channel panels of BCM to ACM subject trajectories."""
    reusable_data = feature_data.rename(
        columns={"BCM": "BCF", "ACM": "ACF"}
    )
    figure = build_bcf_acf_pre_post_paired_figure(
        reusable_data, band, feature
    )
    for trace in figure.data:
        if tuple(trace.x) == ("BCF", "ACF"):
            trace.x = ("BCM", "ACM")
    return _replace_bcf_acf_with_bcm_acm_figure_labels(figure)


def build_bcm_acm_change_distribution_figure(feature_data, band, feature):
    """Build channel box plots of ACM-minus-BCM paired changes."""
    figure = build_bcf_acf_change_distribution_figure(
        feature_data, band, feature
    )
    figure.update_yaxes(title_text="Change (ACM - BCM)")
    return _replace_bcf_acf_with_bcm_acm_figure_labels(figure)


def build_bcm_acm_mean_change_figure(feature_data, band, feature):
    """Build a horizontal lollipop chart of ACM-minus-BCM mean change."""
    figure = build_bcf_acf_mean_change_figure(feature_data, band, feature)
    figure.update_xaxes(title_text="Mean change (ACM - BCM)")
    return _replace_bcf_acf_with_bcm_acm_figure_labels(figure)


def build_bcm_acm_direction_by_channel_figure(feature_data, band, feature):
    """Build a horizontal direction-of-change chart for BCM vs ACM."""
    figure = build_bcf_acf_direction_by_channel_figure(
        feature_data, band, feature
    )
    return _replace_bcf_acf_with_bcm_acm_figure_labels(figure)


def render_bcm_acm_pre_post_visualizations():
    """Render four interactive BCM vs ACM pre-post visualizations."""
    st.subheader("Pre-post visualizations")
    st.caption(
        "Explore subject trajectories, the distribution of paired changes, "
        "channel-level mean change, and direction of change from BCM to ACM."
    )

    try:
        dataframe = load_bcm_acm_subject_level()
    except (FileNotFoundError, ValueError, pd.errors.ParserError) as error:
        st.error(str(error))
        st.info(
            "Keep subject_level_master_BCM_ACM.csv beside app.py or place it "
            "inside data/ or assets/data/, then redeploy the application."
        )
        return

    st.success(
        f"**Key finding.** {get_bcm_acm_pre_post_key_finding(dataframe)} "
        "These visual patterns are descriptive; statistical evidence is "
        "reported separately in the Paired Statistics tab."
    )

    filter_1, filter_2 = st.columns(2)
    with filter_1:
        selected_band = st.selectbox(
            "Frequency band",
            BCM_ACM_BAND_ORDER,
            index=0,
            key="bcm_acm_prepost_band",
        )

    band_data = dataframe[dataframe["Band"] == selected_band].copy()
    preferred_features = [
        f"{selected_band} Band Power",
        f"{selected_band} Relative Power",
        "Entropy",
        "Hjorth Activity",
        "Hjorth Mobility",
        "Hjorth Complexity",
    ]
    available_features = set(band_data["Feature"].dropna().unique())
    feature_options = [
        feature for feature in preferred_features if feature in available_features
    ]
    if not feature_options:
        st.error("No valid features were found for the selected frequency band.")
        return

    with filter_2:
        selected_feature = st.selectbox(
            "Feature",
            feature_options,
            index=0,
            key="bcm_acm_prepost_feature",
        )

    feature_data = band_data[
        band_data["Feature"] == selected_feature
    ].copy().sort_values(["Channel", "Subject"])
    available_channels = set(feature_data["Channel"].dropna().unique())
    missing_channels = [
        channel
        for channel in BCM_ACM_CHANNEL_ORDER
        if channel not in available_channels
    ]
    if missing_channels:
        st.error(
            "The selected group-level view is incomplete. Missing channels: "
            + ", ".join(missing_channels)
        )
        return

    if feature_data.empty:
        st.warning("No paired observations match the selected band and feature.")
        return

    st.info(
        "**Group-level interpretation.** "
        + get_bcm_acm_pre_post_interpretation(
            feature_data,
            selected_band,
            selected_feature,
        )
    )

    paired_figure = build_bcm_acm_pre_post_paired_figure(
        feature_data, selected_band, selected_feature
    )
    st.plotly_chart(
        paired_figure,
        use_container_width=True,
        key="bcm_acm_prepost_paired_plot",
    )
    st.caption(
        "Four panels show TP9, AF7, AF8, and TP10 simultaneously. Each line "
        "connects the BCM and ACM values from the same subject."
    )

    distribution_figure = build_bcm_acm_change_distribution_figure(
        feature_data, selected_band, selected_feature
    )
    st.plotly_chart(
        distribution_figure,
        use_container_width=True,
        key="bcm_acm_prepost_change_distribution",
    )
    st.caption(
        "Boxes show the median and interquartile range; dots preserve all 10 "
        "subject-level ACM-minus-BCM changes at each channel."
    )

    mean_figure = build_bcm_acm_mean_change_figure(
        feature_data, selected_band, selected_feature
    )
    st.plotly_chart(
        mean_figure,
        use_container_width=True,
        key="bcm_acm_prepost_mean_change",
    )
    st.caption(
        "Each lollipop extends from zero to the mean paired change. Hover over "
        "a marker to compare the mean, median, and paired-subject count."
    )

    direction_figure = build_bcm_acm_direction_by_channel_figure(
        feature_data, selected_band, selected_feature
    )
    st.plotly_chart(
        direction_figure,
        use_container_width=True,
        key="bcm_acm_prepost_direction_by_channel",
    )


def find_bm_am_subject_level_file():
    """Return the first configured BM vs AM subject-level CSV that exists."""
    for file_path in BM_AM_SUBJECT_LEVEL_FILES:
        if file_path.exists():
            return file_path
    return None


@st.cache_data
def load_bm_am_subject_level():
    """Load and validate the BM vs AM subject-level master table."""
    file_path = find_bm_am_subject_level_file()
    if file_path is None:
        expected_locations = "\n".join(
            f"- {path.relative_to(APP_DIRECTORY)}"
            for path in BM_AM_SUBJECT_LEVEL_FILES
        )
        raise FileNotFoundError(
            "subject_level_master_BM_AM.csv was not found. "
            "Place the file in one of these locations:\n"
            f"{expected_locations}"
        )

    dataframe = pd.read_csv(file_path)
    required_columns = {
        "Band",
        "Subject",
        "Channel",
        "Feature_Type",
        "Feature",
        "BM",
        "AM",
    }
    missing_columns = required_columns.difference(dataframe.columns)
    if missing_columns:
        raise ValueError(
            "The BM vs AM subject-level CSV is missing required columns: "
            + ", ".join(sorted(missing_columns))
        )

    dataframe = dataframe.copy()
    dataframe["Band"] = dataframe["Band"].astype(str).str.strip().str.title()
    dataframe["Channel"] = dataframe["Channel"].astype(str).str.strip().str.upper()
    dataframe["Feature"] = dataframe["Feature"].astype(str).str.strip()
    dataframe["Feature_Type"] = (
        dataframe["Feature_Type"].astype(str).str.strip().str.upper()
    )

    for column in ["BM", "AM"]:
        dataframe[column] = pd.to_numeric(dataframe[column], errors="coerce")

    if dataframe[["BM", "AM"]].isna().any().any():
        raise ValueError(
            "The BM vs AM subject-level CSV contains missing or non-numeric "
            "values in the BM or AM columns."
        )

    # Recalculate all derived fields so the dashboard consistently uses AM - BM.
    dataframe["Change"] = dataframe["AM"] - dataframe["BM"]
    baseline = dataframe["BM"].abs().replace(0, pd.NA)
    dataframe["Change_Percent"] = dataframe["Change"] / baseline * 100
    dataframe["Direction"] = dataframe["Change"].apply(
        lambda value: (
            "Missing"
            if pd.isna(value)
            else "Increase"
            if value > 0
            else "Decrease"
            if value < 0
            else "No Change"
        )
    )

    return dataframe


def format_bm_am_change(value):
    """Format BM vs AM changes without hiding small relative-power values."""
    if pd.isna(value):
        return "N/A"
    if abs(value) >= 1000:
        return f"{value:+,.2f}"
    if abs(value) >= 1:
        return f"{value:+,.3f}"
    return f"{value:+.4f}"


def get_bm_am_band_summary(dataframe, band):
    """Summarise BP and RP observations for one BM vs AM frequency band."""
    band_data = dataframe[dataframe["Band"] == band]
    band_specific = band_data[band_data["Feature_Type"].isin(["BP", "RP"])]

    total = len(band_specific)
    increased = int((band_specific["Direction"] == "Increase").sum())
    decreased = int((band_specific["Direction"] == "Decrease").sum())
    unchanged = int((band_specific["Direction"] == "No Change").sum())

    increase_percentage = increased / total * 100 if total else 0.0
    decrease_percentage = decreased / total * 100 if total else 0.0

    if increase_percentage >= 55:
        tendency = "an upward tendency"
    elif decrease_percentage >= 57:
        tendency = "the clearest downward tendency"
    elif decrease_percentage >= 55:
        tendency = "a modest downward tendency"
    elif increased > decreased:
        tendency = "a slight upward tendency"
    elif decreased > increased:
        tendency = "a slight downward tendency"
    else:
        tendency = "a balanced pattern"

    summary_text = (
        f"{band} showed {tendency}, with {increased} of {total} band-specific "
        f"comparisons increasing ({increase_percentage:.1f}%) and {decreased} "
        f"decreasing ({decrease_percentage:.1f}%). "
        f"{BM_AM_BAND_HIGHLIGHTS[band]}"
    )

    return {
        "text": summary_text,
        "total": total,
        "increased": increased,
        "decreased": decreased,
        "unchanged": unchanged,
        "increase_percentage": increase_percentage,
        "decrease_percentage": decrease_percentage,
    }


def get_bm_am_selected_interpretation(selected, band, feature, channel):
    """Create a concise interpretation for the selected BM vs AM plot."""
    total = len(selected)
    increased = int((selected["Direction"] == "Increase").sum())
    decreased = int((selected["Direction"] == "Decrease").sum())
    unchanged = int((selected["Direction"] == "No Change").sum())

    mean_change = selected["Change"].mean()
    median_change = selected["Change"].median()

    if increased > decreased and increased > unchanged:
        direction_text = (
            f"{increased} of {total} paired subjects showed an increase in "
            f"{feature} at {channel} from BM to AM."
        )
    elif decreased > increased and decreased > unchanged:
        direction_text = (
            f"{decreased} of {total} paired subjects showed a decrease in "
            f"{feature} at {channel} from BM to AM."
        )
    else:
        direction_text = (
            f"{feature} at {channel} showed a mixed direction of change across "
            "the paired subjects."
        )

    distribution_note = ""
    if mean_change * median_change < 0:
        distribution_note = (
            " The mean and median have opposite signs, indicating that a small "
            "number of larger changes influenced the mean."
        )

    return (
        f"{direction_text} The mean change was "
        f"{format_bm_am_change(mean_change)}, and the median change was "
        f"{format_bm_am_change(median_change)}.{distribution_note} This is a "
        f"descriptive {band}-band pattern and should not be interpreted as "
        "statistical significance."
    )


def render_bm_am_subject_level():
    """Render the completed BM vs AM subject-level analysis dashboard."""
    st.subheader("Pre-post subject-level analysis")
    st.caption(
        "This section summarises within-subject changes from BM to AM while "
        "preserving the identity of every paired observation."
    )

    try:
        dataframe = load_bm_am_subject_level()
    except (FileNotFoundError, ValueError, pd.errors.ParserError) as error:
        st.error(str(error))
        st.info(
            "Keep subject_level_master_BM_AM.csv beside app.py or place it "
            "inside data/ or assets/data/, then redeploy the application."
        )
        return

    st.success(
        "**Key finding.** Across 400 band-specific subject-channel-feature "
        "comparisons, 184 increased (46.0%) and 216 decreased (54.0%) from "
        "BM to AM. Gamma was nearly balanced with a slight upward tendency, "
        "while Delta showed the largest proportion of decreases. Alpha Band "
        "Power at TP9 and Delta Band Power at AF8 each decreased in 9 of 10 "
        "subjects. These are descriptive patterns and require separate "
        "statistical evaluation using paired tests, effect sizes, and FDR "
        "correction."
    )

    selected_band = st.selectbox(
        "Frequency band",
        BM_AM_BAND_ORDER,
        index=0,
        key="bm_am_subject_band",
    )
    band_data = dataframe[dataframe["Band"] == selected_band].copy()
    band_summary = get_bm_am_band_summary(dataframe, selected_band)

    metric_1, metric_2, metric_3, metric_4 = st.columns(4)
    metric_1.metric("Paired Subjects", band_data["Subject"].nunique())
    metric_2.metric("Band-Specific Comparisons", band_summary["total"])
    metric_3.metric(
        "Increased",
        band_summary["increased"],
        f"{band_summary['increase_percentage']:.1f}%",
    )
    metric_4.metric(
        "Decreased",
        band_summary["decreased"],
        f"{band_summary['decrease_percentage']:.1f}%",
        delta_color="inverse",
    )

    st.info(f"**{selected_band} summary.** {band_summary['text']}")

    preferred_features = [
        f"{selected_band} Band Power",
        f"{selected_band} Relative Power",
        "Entropy",
        "Hjorth Activity",
        "Hjorth Mobility",
        "Hjorth Complexity",
    ]
    available_features = set(band_data["Feature"].dropna().unique())
    feature_options = [
        feature for feature in preferred_features if feature in available_features
    ]
    available_channels = set(band_data["Channel"].dropna().unique())
    channel_options = [
        channel for channel in BM_AM_CHANNEL_ORDER if channel in available_channels
    ]

    if not feature_options or not channel_options:
        st.error(
            "No valid feature or channel options were found for the selected band."
        )
        return

    filter_1, filter_2 = st.columns(2)
    with filter_1:
        selected_feature = st.selectbox(
            "Feature",
            feature_options,
            key="bm_am_subject_feature",
        )
    with filter_2:
        selected_channel = st.selectbox(
            "Channel",
            channel_options,
            key="bm_am_subject_channel",
        )

    selected = band_data[
        (band_data["Feature"] == selected_feature)
        & (band_data["Channel"] == selected_channel)
    ].copy()
    selected = selected.sort_values("Subject")

    if selected.empty:
        st.warning("No subject-level records match the selected filters.")
        return

    paired_data = selected.melt(
        id_vars=["Subject"],
        value_vars=["BM", "AM"],
        var_name="Condition",
        value_name="Value",
    )
    paired_data["Subject Label"] = "Subject " + paired_data["Subject"].astype(str)

    paired_figure = px.line(
        paired_data,
        x="Condition",
        y="Value",
        color="Subject Label",
        markers=True,
        category_orders={"Condition": ["BM", "AM"]},
        title=(
            "Paired Before-After Plot<br>"
            f"<sup>{selected_band} | {selected_feature} | {selected_channel}</sup>"
        ),
    )
    paired_figure.update_traces(line={"width": 2}, marker={"size": 8})
    paired_figure.update_layout(
        showlegend=False,
        height=430,
        margin=dict(l=20, r=20, t=75, b=20),
        xaxis_title="",
        yaxis_title="Feature Value",
        hovermode="closest",
    )

    direction_order = ["Increase", "Decrease", "No Change"]
    direction_counts = (
        selected["Direction"]
        .value_counts()
        .reindex(direction_order, fill_value=0)
        .rename_axis("Direction")
        .reset_index(name="Subjects")
    )
    direction_figure = px.bar(
        direction_counts,
        x="Direction",
        y="Subjects",
        color="Direction",
        text="Subjects",
        color_discrete_map=BM_AM_DIRECTION_COLORS,
        category_orders={"Direction": direction_order},
        title=(
            "Direction of Change<br>"
            f"<sup>{selected_band} | {selected_feature} | {selected_channel}</sup>"
        ),
    )
    direction_figure.update_traces(textposition="outside")
    direction_figure.update_layout(
        showlegend=False,
        height=430,
        margin=dict(l=20, r=20, t=75, b=20),
        xaxis_title="",
        yaxis_title="Number of Paired Subjects",
        yaxis=dict(dtick=1, range=[0, max(11, len(selected) + 1)]),
    )

    chart_1, chart_2 = st.columns(2)
    with chart_1:
        st.plotly_chart(
            paired_figure,
            use_container_width=True,
            key="bm_am_paired_plot",
        )
        st.caption(
            "Each line connects measurements from the same subject. Upward "
            "lines indicate AM > BM, while downward lines indicate AM < BM."
        )
    with chart_2:
        st.plotly_chart(
            direction_figure,
            use_container_width=True,
            key="bm_am_direction_plot",
        )
        st.caption(
            "The bars count paired subjects whose selected feature increased, "
            "decreased, or remained unchanged."
        )

    st.markdown("#### Interpretation")
    st.write(
        get_bm_am_selected_interpretation(
            selected,
            selected_band,
            selected_feature,
            selected_channel,
        )
    )

    with st.expander("View summaries for all frequency bands", expanded=False):
        for band in BM_AM_BAND_ORDER:
            summary = get_bm_am_band_summary(dataframe, band)
            st.markdown(f"**{band}**  \n{summary['text']}")

    with st.expander("Important data and methodological notes", expanded=False):
        st.markdown(
            """
- Each frequency-band file contains 80 band-specific observations for Band Power and Relative Power.
- Each file also contains 160 shared observations for Entropy and the three Hjorth features.
- Shared features are repeated across the five band files and should not be counted five times in an All Bands summary.
- The 1,200 source rows represent 400 band-specific observations and 800 repeated shared-feature rows. After repeated shared features are removed, the dataset contains 560 unique observations.
- A `Band_Mismatches` value of 160 reflects the shared Entropy and Hjorth features; it is not a data error.
- Change is calculated as AM minus BM.
- Direction counts describe individual increases and decreases. They do not measure statistical significance or effect magnitude.
- Opposite signs between the mean and median suggest that unusually large observations influenced the average.
- Raw changes should only be compared within the same feature and channel because EEG features use different numerical scales.
            """
        )

    with st.expander("View selected subject-level data", expanded=False):
        display_columns = [
            "Subject",
            "Channel",
            "Feature",
            "BM",
            "AM",
            "Change",
            "Change_Percent",
            "Direction",
        ]
        st.dataframe(
            selected[display_columns],
            use_container_width=True,
            hide_index=True,
        )

        safe_feature = (
            selected_feature.lower().replace(" ", "_").replace("/", "_")
        )
        st.download_button(
            "Download selected data (CSV)",
            data=selected[display_columns].to_csv(index=False).encode("utf-8"),
            file_name=f"BM_AM_{selected_band}_{safe_feature}_{selected_channel}.csv",
            mime="text/csv",
            key="bm_am_subject_download",
        )


def get_bm_am_pre_post_key_finding(dataframe):
    """Create the BM vs AM pre-post headline from band-specific rows."""
    return (
        get_bcf_acf_pre_post_key_finding(dataframe)
        .replace("BCF", "BM")
        .replace("ACF", "AM")
    )


def get_bm_am_pre_post_interpretation(feature_data, band, feature):
    """Create a concise BM vs AM interpretation across all four channels."""
    total = len(feature_data)
    increased = int((feature_data["Direction"] == "Increase").sum())
    decreased = int((feature_data["Direction"] == "Decrease").sum())
    unchanged = int((feature_data["Direction"] == "No Change").sum())

    channel_summary = (
        feature_data.groupby("Channel", observed=True)["Change"]
        .agg(Mean_Change="mean", Median_Change="median", Subjects="size")
    )
    strongest_channel = channel_summary["Mean_Change"].abs().idxmax()
    strongest_mean = channel_summary.loc[strongest_channel, "Mean_Change"]

    direction_counts = (
        feature_data.groupby(["Channel", "Direction"], observed=True)
        .size()
        .unstack(fill_value=0)
    )
    for direction in ["Increase", "Decrease", "No Change"]:
        if direction not in direction_counts.columns:
            direction_counts[direction] = 0
    direction_counts["Total"] = direction_counts[
        ["Increase", "Decrease", "No Change"]
    ].sum(axis=1)
    direction_counts["Consistency"] = direction_counts[
        ["Increase", "Decrease", "No Change"]
    ].max(axis=1).div(direction_counts["Total"])
    direction_counts["Dominant"] = direction_counts[
        ["Increase", "Decrease", "No Change"]
    ].idxmax(axis=1)
    most_consistent_channel = direction_counts["Consistency"].idxmax()
    dominant_direction = direction_counts.loc[
        most_consistent_channel, "Dominant"
    ]
    dominant_count = int(
        direction_counts.loc[most_consistent_channel, dominant_direction]
    )
    dominant_total = int(
        direction_counts.loc[most_consistent_channel, "Total"]
    )

    overall_pattern = (
        "more increases than decreases"
        if increased > decreased
        else "more decreases than increases"
        if decreased > increased
        else "an equal number of increases and decreases"
    )
    unchanged_text = (
        f", and {unchanged} showed no change" if unchanged else ""
    )

    return (
        f"Across all four channels, {feature} in {band} showed "
        f"{overall_pattern}: {increased} of {total} comparisons increased and "
        f"{decreased} decreased{unchanged_text}. {strongest_channel} had the "
        f"largest absolute mean change ({format_bm_am_change(strongest_mean)}). "
        f"The most consistent direction occurred at {most_consistent_channel}, "
        f"where {dominant_count} of {dominant_total} subjects showed a "
        f"{dominant_direction.lower()}. These are group-level descriptive "
        "patterns and do not establish statistical significance."
    )


def _replace_bcf_acf_with_bm_am_figure_labels(figure):
    """Convert labels in a reusable BCF-ACF figure to BM-AM labels."""
    title_text = figure.layout.title.text or ""
    figure.update_layout(
        title_text=title_text.replace("BCF", "BM").replace("ACF", "AM")
    )
    return figure


def build_bm_am_pre_post_paired_figure(feature_data, band, feature):
    """Build four channel panels of BM to AM subject trajectories."""
    reusable_data = feature_data.rename(columns={"BM": "BCF", "AM": "ACF"})
    figure = build_bcf_acf_pre_post_paired_figure(
        reusable_data, band, feature
    )
    for trace in figure.data:
        if tuple(trace.x) == ("BCF", "ACF"):
            trace.x = ("BM", "AM")
    return _replace_bcf_acf_with_bm_am_figure_labels(figure)


def build_bm_am_change_distribution_figure(feature_data, band, feature):
    """Build channel-level box plots of AM-minus-BM paired changes."""
    figure = build_bcf_acf_change_distribution_figure(
        feature_data, band, feature
    )
    figure.update_yaxes(title_text="Change (AM - BM)")
    return _replace_bcf_acf_with_bm_am_figure_labels(figure)


def build_bm_am_mean_change_figure(feature_data, band, feature):
    """Build a horizontal lollipop chart of AM-minus-BM mean change."""
    figure = build_bcf_acf_mean_change_figure(feature_data, band, feature)
    figure.update_xaxes(title_text="Mean change (AM - BM)")
    return _replace_bcf_acf_with_bm_am_figure_labels(figure)


def build_bm_am_direction_by_channel_figure(feature_data, band, feature):
    """Build a horizontal direction-of-change chart for BM vs AM."""
    figure = build_bcf_acf_direction_by_channel_figure(
        feature_data, band, feature
    )
    return _replace_bcf_acf_with_bm_am_figure_labels(figure)


def render_bm_am_pre_post_visualizations():
    """Render four interactive BM vs AM pre-post visualizations."""
    st.subheader("Pre-post visualizations")
    st.caption(
        "Explore subject trajectories, the distribution of paired changes, "
        "channel-level mean change, and direction of change from BM to AM."
    )

    try:
        dataframe = load_bm_am_subject_level()
    except (FileNotFoundError, ValueError, pd.errors.ParserError) as error:
        st.error(str(error))
        st.info(
            "Keep subject_level_master_BM_AM.csv beside app.py or place it "
            "inside data/ or assets/data/, then redeploy the application."
        )
        return

    st.success(
        f"**Key finding.** {get_bm_am_pre_post_key_finding(dataframe)} "
        "These visual patterns are descriptive; statistical evidence is "
        "reported separately in the Paired Statistics tab."
    )

    filter_1, filter_2 = st.columns(2)
    with filter_1:
        selected_band = st.selectbox(
            "Frequency band",
            BM_AM_BAND_ORDER,
            index=0,
            key="bm_am_prepost_band",
        )

    band_data = dataframe[dataframe["Band"] == selected_band].copy()
    preferred_features = [
        f"{selected_band} Band Power",
        f"{selected_band} Relative Power",
        "Entropy",
        "Hjorth Activity",
        "Hjorth Mobility",
        "Hjorth Complexity",
    ]
    available_features = set(band_data["Feature"].dropna().unique())
    feature_options = [
        feature for feature in preferred_features if feature in available_features
    ]
    if not feature_options:
        st.error("No valid features were found for the selected frequency band.")
        return

    with filter_2:
        selected_feature = st.selectbox(
            "Feature",
            feature_options,
            index=0,
            key="bm_am_prepost_feature",
        )

    feature_data = band_data[
        band_data["Feature"] == selected_feature
    ].copy().sort_values(["Channel", "Subject"])
    available_channels = set(feature_data["Channel"].dropna().unique())
    missing_channels = [
        channel
        for channel in BM_AM_CHANNEL_ORDER
        if channel not in available_channels
    ]
    if missing_channels:
        st.error(
            "The selected group-level view is incomplete. Missing channels: "
            + ", ".join(missing_channels)
        )
        return

    if feature_data.empty:
        st.warning("No paired observations match the selected band and feature.")
        return

    st.info(
        "**Group-level interpretation.** "
        + get_bm_am_pre_post_interpretation(
            feature_data,
            selected_band,
            selected_feature,
        )
    )

    paired_figure = build_bm_am_pre_post_paired_figure(
        feature_data, selected_band, selected_feature
    )
    st.plotly_chart(
        paired_figure,
        use_container_width=True,
        key="bm_am_prepost_paired_plot",
    )
    st.caption(
        "Four panels show TP9, AF7, AF8, and TP10 simultaneously. Each line "
        "connects the BM and AM values from the same subject."
    )

    distribution_figure = build_bm_am_change_distribution_figure(
        feature_data, selected_band, selected_feature
    )
    st.plotly_chart(
        distribution_figure,
        use_container_width=True,
        key="bm_am_prepost_change_distribution",
    )
    st.caption(
        "Boxes show the median and interquartile range; dots preserve all 10 "
        "subject-level AM-minus-BM changes at each channel."
    )

    mean_figure = build_bm_am_mean_change_figure(
        feature_data, selected_band, selected_feature
    )
    st.plotly_chart(
        mean_figure,
        use_container_width=True,
        key="bm_am_prepost_mean_change",
    )
    st.caption(
        "Each lollipop extends from zero to the mean paired change. Hover over "
        "a marker to compare the mean, median, and paired-subject count."
    )

    direction_figure = build_bm_am_direction_by_channel_figure(
        feature_data, selected_band, selected_feature
    )
    st.plotly_chart(
        direction_figure,
        use_container_width=True,
        key="bm_am_prepost_direction_by_channel",
    )


def get_bcf_acf_synthetic_quality_band_from_name(file_name):
    """Extract the frequency band from a synthetic-quality filename."""
    normalized_name = Path(file_name).stem.lower()
    for band in BCF_ACF_BAND_ORDER:
        if band.lower() in normalized_name:
            return band
    return None


def find_bcf_acf_synthetic_quality_source():
    """Find the BCF-ACF synthetic-quality ZIP or extracted CSV files."""
    for zip_path in BCF_ACF_SYNTHETIC_QUALITY_ZIPS:
        if zip_path.exists():
            return "zip", zip_path

    csv_files = []
    for directory in BCF_ACF_SYNTHETIC_QUALITY_DIRECTORIES:
        if not directory.exists():
            continue
        csv_files.extend(
            directory.rglob(
                "SyntheticQuality_*_FeatureComparison_BCF_vs_ACF.csv"
            )
        )

    unique_files = sorted({path.resolve() for path in csv_files})
    if unique_files:
        return "csv", unique_files
    return None, None


@st.cache_data
def load_bcf_acf_synthetic_quality():
    """Load and validate the five BCF-ACF synthetic-quality tables."""
    source_type, source = find_bcf_acf_synthetic_quality_source()
    if source is None:
        raise FileNotFoundError(
            "BCF vs ACF synthetic-quality data were not found. Keep "
            "'synthetic_quality_master BCF ACF.zip' beside app.py, or "
            "extract its five SyntheticQuality CSV files into "
            "synthetic_quality_master/, data/, or assets/data/."
        )

    frames = []
    if source_type == "zip":
        with ZipFile(source) as archive:
            csv_sources = [
                name
                for name in archive.namelist()
                if name.lower().endswith(".csv")
                and "syntheticquality" in name.lower()
                and "featurecomparison" in name.lower()
                and "bcf" in name.lower()
                and "acf" in name.lower()
            ]
            for csv_name in csv_sources:
                band = get_bcf_acf_synthetic_quality_band_from_name(csv_name)
                if band is None:
                    continue
                with archive.open(csv_name) as csv_file:
                    dataframe = pd.read_csv(csv_file)
                dataframe["Band"] = band
                dataframe["Source_File"] = Path(csv_name).name
                frames.append(dataframe)
    else:
        for csv_path in source:
            band = get_bcf_acf_synthetic_quality_band_from_name(csv_path.name)
            if band is None:
                continue
            dataframe = pd.read_csv(csv_path)
            dataframe["Band"] = band
            dataframe["Source_File"] = csv_path.name
            frames.append(dataframe)

    if not frames:
        raise FileNotFoundError(
            "No BCF vs ACF SyntheticQuality FeatureComparison CSV files "
            "were found in the configured source."
        )

    dataframe = pd.concat(frames, ignore_index=True, sort=False)
    missing_columns = BCF_ACF_SYNTHETIC_REQUIRED_COLUMNS.difference(
        dataframe.columns
    )
    if missing_columns:
        raise ValueError(
            "The BCF vs ACF synthetic-quality data are missing required "
            "columns: " + ", ".join(sorted(missing_columns))
        )

    dataframe = dataframe.copy()
    dataframe["Band"] = dataframe["Band"].astype(str).str.strip().str.title()
    dataframe["Condition"] = (
        dataframe["Condition"].astype(str).str.strip().str.upper()
    )
    dataframe["Channel"] = (
        dataframe["Channel"].astype(str).str.strip().str.upper()
    )
    dataframe["Feature"] = dataframe["Feature"].astype(str).str.strip()
    dataframe["Feature_Display"] = dataframe["Feature"].str.replace(
        "_", " ", regex=False
    )

    numeric_columns = [
        "Label",
        "Real_Mean",
        "Synthetic_Mean",
        "Real_SD",
        "Synthetic_SD",
        "Real_Median",
        "Synthetic_Median",
        "Real_IQR",
        "Synthetic_IQR",
        "Real_N",
        "Synthetic_N",
    ]
    for column in numeric_columns:
        dataframe[column] = pd.to_numeric(dataframe[column], errors="coerce")
    if dataframe[numeric_columns].isna().any().any():
        raise ValueError(
            "The synthetic-quality CSV files contain missing or non-numeric "
            "values in required summary columns."
        )

    expected_labels = dataframe["Condition"].map({"BCF": 0, "ACF": 1})
    if expected_labels.isna().any() or not (
        dataframe["Label"] == expected_labels
    ).all():
        raise ValueError(
            "Condition and Label are inconsistent. Expected BCF = 0 and "
            "ACF = 1 in every synthetic-quality row."
        )

    for metric_name, metric_config in BCF_ACF_SYNTHETIC_METRICS.items():
        difference_column = metric_config["difference"]
        absolute_column = metric_config["absolute"]
        dataframe[difference_column] = (
            dataframe[metric_config["synthetic"]]
            - dataframe[metric_config["real"]]
        )
        dataframe[absolute_column] = dataframe[difference_column].abs()

    absolute_columns = [
        metric_config["absolute"]
        for metric_config in BCF_ACF_SYNTHETIC_METRICS.values()
    ]
    dataframe["Average_Absolute_Summary_Gap"] = dataframe[
        absolute_columns
    ].mean(axis=1)

    duplicate_rows = dataframe.duplicated(
        ["Band", "Condition", "Channel", "Feature"]
    )
    if duplicate_rows.any():
        raise ValueError(
            "Duplicate Band-Condition-Channel-Feature rows were found in the "
            "BCF vs ACF synthetic-quality data."
        )

    available_bands = set(dataframe["Band"].unique())
    missing_bands = [
        band for band in BCF_ACF_BAND_ORDER if band not in available_bands
    ]
    if missing_bands:
        raise ValueError(
            "Synthetic-quality data are incomplete. Missing bands: "
            + ", ".join(missing_bands)
        )

    if set(dataframe["Condition"].unique()) != {"BCF", "ACF"}:
        raise ValueError(
            "Synthetic-quality data must contain both BCF and ACF conditions."
        )

    return dataframe


def get_bcf_acf_synthetic_feature_order(dataframe, band):
    """Return a stable display order for the selected band's six features."""
    preferred_features = [
        f"{band}_BP",
        f"{band}_RP",
        "Entropy",
        "Hjorth_Activity",
        "Hjorth_Mobility",
        "Hjorth_Complexity",
    ]
    available_features = set(dataframe["Feature"].dropna().unique())
    ordered = [
        feature for feature in preferred_features if feature in available_features
    ]
    ordered.extend(sorted(available_features.difference(ordered)))
    return ordered


def get_bcf_acf_synthetic_quality_key_finding(dataframe):
    """Create a global descriptive finding from all five quality tables."""
    metric_averages = {
        metric_name: dataframe[metric_config["absolute"]].mean()
        for metric_name, metric_config in BCF_ACF_SYNTHETIC_METRICS.items()
    }
    largest_metric = max(metric_averages, key=metric_averages.get)
    band_gaps = dataframe.groupby("Band", observed=True)[
        "Average_Absolute_Summary_Gap"
    ].mean()
    condition_gaps = dataframe.groupby("Condition", observed=True)[
        "Average_Absolute_Summary_Gap"
    ].mean()
    review_row = dataframe.loc[
        dataframe["Average_Absolute_Summary_Gap"].idxmax()
    ]

    return (
        f"Across {len(dataframe)} band-condition-channel-feature summaries, "
        f"the mean absolute gaps were {metric_averages['Mean']:.3f} for the "
        f"mean, {metric_averages['Standard deviation']:.3f} for SD, "
        f"{metric_averages['Median']:.3f} for the median, and "
        f"{metric_averages['IQR']:.3f} for IQR. {largest_metric} showed the "
        f"largest average discrepancy. {band_gaps.idxmax()} had the largest "
        f"average summary gap ({band_gaps.max():.3f}), while "
        f"{band_gaps.idxmin()} had the smallest ({band_gaps.min():.3f}). "
        f"Overall gaps were similar for BCF ({condition_gaps['BCF']:.3f}) "
        f"and ACF ({condition_gaps['ACF']:.3f}). The largest combined gap "
        f"was {review_row['Feature_Display']} at {review_row['Channel']} "
        f"under {review_row['Condition']} in {review_row['Band']} "
        f"({review_row['Average_Absolute_Summary_Gap']:.3f})."
    )


def get_bcf_acf_synthetic_quality_interpretation(
    selected_data,
    selected_band,
    selected_condition,
    selected_metric,
):
    """Explain the currently selected synthetic-quality view."""
    metric_config = BCF_ACF_SYNTHETIC_METRICS[selected_metric]
    difference_column = metric_config["difference"]
    absolute_column = metric_config["absolute"]
    average_gap = selected_data[absolute_column].mean()
    median_gap = selected_data[absolute_column].median()
    review_row = selected_data.loc[selected_data[absolute_column].idxmax()]
    synthetic_higher = int((selected_data[difference_column] > 0).sum())
    synthetic_lower = int((selected_data[difference_column] < 0).sum())
    condition_text = (
        "BCF and ACF"
        if selected_condition == "All Conditions"
        else selected_condition
    )

    return (
        f"For {selected_band} across {condition_text}, the average absolute "
        f"{selected_metric.lower()} gap was {average_gap:.3f}, with a median "
        f"of {median_gap:.3f}. The largest gap occurred for "
        f"{review_row['Feature_Display']} at {review_row['Channel']} under "
        f"{review_row['Condition']} ({review_row[absolute_column]:.3f}). "
        f"Synthetic values were higher than real values in {synthetic_higher} "
        f"of {len(selected_data)} summaries and lower in {synthetic_lower}. "
        "Smaller gaps indicate closer descriptive agreement; they do not by "
        "themselves establish distributional equivalence."
    )


def build_bcf_acf_synthetic_parity_figure(
    selected_data,
    selected_band,
    selected_condition,
    selected_metric,
):
    """Build a Real-versus-Synthetic parity plot for one summary statistic."""
    metric_config = BCF_ACF_SYNTHETIC_METRICS[selected_metric]
    real_column = metric_config["real"]
    synthetic_column = metric_config["synthetic"]
    figure = go.Figure()
    conditions = [
        condition
        for condition in [
            "BCF",
            "ACF",
            "BF",
            "AF",
            "BCM",
            "ACM",
            "BM",
            "AM",
        ]
        if condition in set(selected_data["Condition"])
    ]
    symbols = {
        "BCF": "circle",
        "ACF": "diamond",
        "BF": "circle",
        "AF": "diamond",
        "BCM": "circle",
        "ACM": "diamond",
        "BM": "circle",
        "AM": "diamond",
    }

    for channel in BCF_ACF_CHANNEL_ORDER:
        for condition in conditions:
            trace_data = selected_data[
                (selected_data["Channel"] == channel)
                & (selected_data["Condition"] == condition)
            ]
            if trace_data.empty:
                continue
            trace_name = (
                f"{channel} · {condition}"
                if selected_condition == "All Conditions"
                else channel
            )
            figure.add_trace(
                go.Scatter(
                    x=trace_data[real_column],
                    y=trace_data[synthetic_column],
                    mode="markers",
                    name=trace_name,
                    marker={
                        "size": 11,
                        "symbol": symbols[condition],
                        "color": BCF_ACF_PREPOST_CHANNEL_COLORS[channel],
                        "opacity": 0.82,
                        "line": {"color": "#F7FAF9", "width": 1.2},
                    },
                    customdata=trace_data[
                        ["Feature_Display", "Condition", "Channel"]
                    ].values,
                    hovertemplate=(
                        "Feature: %{customdata[0]}<br>"
                        "Condition: %{customdata[1]}<br>"
                        "Channel: %{customdata[2]}<br>"
                        "Real: %{x:.4f}<br>Synthetic: %{y:.4f}"
                        "<extra></extra>"
                    ),
                )
            )

    combined_values = pd.concat(
        [selected_data[real_column], selected_data[synthetic_column]],
        ignore_index=True,
    )
    value_min = combined_values.min()
    value_max = combined_values.max()
    value_range = value_max - value_min
    padding = value_range * 0.08 if value_range else 0.1
    axis_min = value_min - padding
    axis_max = value_max + padding
    figure.add_trace(
        go.Scatter(
            x=[axis_min, axis_max],
            y=[axis_min, axis_max],
            mode="lines",
            line={"color": "#607D72", "width": 1.5, "dash": "dash"},
            name="Perfect agreement",
            hoverinfo="skip",
        )
    )
    figure.update_layout(
        title=(
            f"Real vs Synthetic {selected_metric}<br>"
            f"<sup>{selected_band} · {selected_condition}</sup>"
        ),
        xaxis_title=f"Real {selected_metric}",
        yaxis_title=f"Synthetic {selected_metric}",
        legend={
            "orientation": "h",
            "yanchor": "bottom",
            "y": 1.02,
            "xanchor": "right",
            "x": 1,
        },
    )
    figure.update_xaxes(range=[axis_min, axis_max])
    figure.update_yaxes(
        range=[axis_min, axis_max],
        scaleanchor="x",
        scaleratio=1,
    )
    return style_bcf_acf_pre_post_figure(figure, 540)


def build_bcf_acf_synthetic_gap_heatmap(
    selected_data,
    selected_band,
    selected_condition,
    selected_metric,
):
    """Build a channel-by-feature heatmap of absolute summary gaps."""
    metric_config = BCF_ACF_SYNTHETIC_METRICS[selected_metric]
    absolute_column = metric_config["absolute"]
    heatmap_data = (
        selected_data.groupby(
            ["Channel", "Feature", "Feature_Display"], observed=True
        )[absolute_column]
        .mean()
        .reset_index()
    )
    feature_order = get_bcf_acf_synthetic_feature_order(
        selected_data, selected_band
    )
    display_lookup = (
        heatmap_data.drop_duplicates("Feature")
        .set_index("Feature")["Feature_Display"]
        .to_dict()
    )
    pivot = heatmap_data.pivot(
        index="Channel", columns="Feature", values=absolute_column
    ).reindex(index=BCF_ACF_CHANNEL_ORDER, columns=feature_order)
    feature_labels = [display_lookup.get(feature, feature) for feature in feature_order]

    figure = go.Figure(
        data=go.Heatmap(
            z=pivot.values,
            x=feature_labels,
            y=pivot.index,
            colorscale=[
                [0.0, "#F2F8F4"],
                [0.35, "#B8DFC8"],
                [0.7, "#66B091"],
                [1.0, "#2E6D55"],
            ],
            text=pivot.round(3).astype(str).values,
            texttemplate="%{text}",
            colorbar={"title": "Absolute<br>gap"},
            hovertemplate=(
                "Channel: %{y}<br>Feature: %{x}<br>"
                "Absolute gap: %{z:.4f}<extra></extra>"
            ),
        )
    )
    figure.update_layout(
        title=(
            f"Absolute {selected_metric} Gap by Channel and Feature<br>"
            f"<sup>{selected_band} · {selected_condition}</sup>"
        ),
        xaxis_title="Feature",
        yaxis_title="EEG Channel",
    )
    figure.update_xaxes(tickangle=-18)
    return style_bcf_acf_pre_post_figure(figure, 430)


def build_bcf_acf_synthetic_band_overview(
    dataframe,
    selected_condition,
):
    """Compare average absolute summary gaps across frequency bands."""
    overview_data = dataframe.copy()
    if selected_condition != "All Conditions":
        overview_data = overview_data[
            overview_data["Condition"] == selected_condition
        ]
    metric_colors = {
        "Mean": "#6C3FD1",
        "Standard deviation": "#FF7A00",
        "Median": "#18B7A0",
        "IQR": "#2F80ED",
    }
    figure = go.Figure()
    for metric_name, metric_config in BCF_ACF_SYNTHETIC_METRICS.items():
        summary = (
            overview_data.groupby("Band", observed=True)[
                metric_config["absolute"]
            ]
            .mean()
            .reindex(BCF_ACF_BAND_ORDER)
        )
        figure.add_trace(
            go.Bar(
                x=summary.index,
                y=summary.values,
                name=metric_name,
                marker_color=metric_colors[metric_name],
                hovertemplate=(
                    "Band: %{x}<br>Average absolute gap: %{y:.4f}"
                    "<extra>%{fullData.name}</extra>"
                ),
            )
        )
    figure.update_layout(
        title=(
            "Average Absolute Summary Gap by Frequency Band<br>"
            f"<sup>{selected_condition}</sup>"
        ),
        barmode="group",
        xaxis_title="Frequency band",
        yaxis_title="Average absolute gap",
        legend={
            "orientation": "h",
            "yanchor": "bottom",
            "y": 1.02,
            "xanchor": "right",
            "x": 1,
        },
    )
    return style_bcf_acf_pre_post_figure(figure, 460)


def render_bcf_acf_synthetic_feature_quality():
    """Render BCF-ACF descriptive Real-versus-Synthetic quality analysis."""
    st.subheader("Synthetic feature quality")
    st.caption(
        "Compare Real and ACGAN-generated feature summaries across frequency "
        "bands, conditions, EEG channels, and feature types."
    )

    try:
        dataframe = load_bcf_acf_synthetic_quality()
    except (FileNotFoundError, ValueError, pd.errors.ParserError) as error:
        st.error(str(error))
        st.info(
            "Keep 'synthetic_quality_master BCF ACF.zip' beside app.py, or "
            "extract its five CSV files into synthetic_quality_master/, "
            "data/, or assets/data/, then redeploy the application."
        )
        return

    st.success(
        "**Key finding.** "
        + get_bcf_acf_synthetic_quality_key_finding(dataframe)
    )

    filter_1, filter_2, filter_3 = st.columns(3)
    with filter_1:
        selected_band = st.selectbox(
            "Frequency band",
            BCF_ACF_BAND_ORDER,
            index=0,
            key="bcf_acf_synthetic_quality_band",
        )
    with filter_2:
        selected_condition = st.selectbox(
            "Condition",
            ["All Conditions", "BCF", "ACF"],
            index=0,
            key="bcf_acf_synthetic_quality_condition",
        )
    with filter_3:
        selected_metric = st.selectbox(
            "Summary statistic",
            list(BCF_ACF_SYNTHETIC_METRICS),
            index=0,
            key="bcf_acf_synthetic_quality_metric",
        )

    selected_data = dataframe[dataframe["Band"] == selected_band].copy()
    if selected_condition != "All Conditions":
        selected_data = selected_data[
            selected_data["Condition"] == selected_condition
        ].copy()
    if selected_data.empty:
        st.warning("No synthetic-quality rows match the selected filters.")
        return

    metric_columns = {
        "Mean": "Abs_Mean_Difference",
        "SD": "Abs_SD_Difference",
        "Median": "Abs_Median_Difference",
        "IQR": "Abs_IQR_Difference",
    }
    cards = st.columns(5)
    cards[0].metric("Summary Rows", len(selected_data))
    for card, (label, column) in zip(cards[1:], metric_columns.items()):
        card.metric(f"Avg |{label} Gap|", f"{selected_data[column].mean():.3f}")

    st.info(
        "**Selected-view interpretation.** "
        + get_bcf_acf_synthetic_quality_interpretation(
            selected_data,
            selected_band,
            selected_condition,
            selected_metric,
        )
    )

    parity_figure = build_bcf_acf_synthetic_parity_figure(
        selected_data,
        selected_band,
        selected_condition,
        selected_metric,
    )
    st.plotly_chart(
        parity_figure,
        use_container_width=True,
        key="bcf_acf_synthetic_quality_parity",
    )
    st.caption(
        "The dashed diagonal represents exact agreement. Points closer to the "
        "line have more similar Real and Synthetic summary values."
    )

    heatmap_figure = build_bcf_acf_synthetic_gap_heatmap(
        selected_data,
        selected_band,
        selected_condition,
        selected_metric,
    )
    st.plotly_chart(
        heatmap_figure,
        use_container_width=True,
        key="bcf_acf_synthetic_quality_heatmap",
    )
    st.caption(
        "Darker cells indicate larger absolute Real-versus-Synthetic gaps. "
        "When both conditions are selected, each cell is their average."
    )

    band_figure = build_bcf_acf_synthetic_band_overview(
        dataframe,
        selected_condition,
    )
    st.plotly_chart(
        band_figure,
        use_container_width=True,
        key="bcf_acf_synthetic_quality_band_overview",
    )
    st.caption(
        "Band-level bars average the absolute gaps across both conditions, "
        "all four channels, and all six features unless one condition is "
        "selected."
    )

    st.markdown("#### Feature combinations requiring closer review")
    review_table = selected_data.nlargest(
        10, "Average_Absolute_Summary_Gap"
    )[
        [
            "Condition",
            "Channel",
            "Feature_Display",
            "Abs_Mean_Difference",
            "Abs_SD_Difference",
            "Abs_Median_Difference",
            "Abs_IQR_Difference",
            "Average_Absolute_Summary_Gap",
        ]
    ].copy()
    review_table = review_table.rename(
        columns={
            "Feature_Display": "Feature",
            "Abs_Mean_Difference": "|Mean Gap|",
            "Abs_SD_Difference": "|SD Gap|",
            "Abs_Median_Difference": "|Median Gap|",
            "Abs_IQR_Difference": "|IQR Gap|",
            "Average_Absolute_Summary_Gap": "Average Absolute Gap",
        }
    )
    numeric_review_columns = [
        "|Mean Gap|",
        "|SD Gap|",
        "|Median Gap|",
        "|IQR Gap|",
        "Average Absolute Gap",
    ]
    review_table[numeric_review_columns] = review_table[
        numeric_review_columns
    ].round(4)
    st.dataframe(review_table, use_container_width=True, hide_index=True)

    real_counts = sorted(dataframe["Real_N"].astype(int).unique())
    synthetic_counts = sorted(dataframe["Synthetic_N"].astype(int).unique())
    sample_note = (
        f"Each summary row uses {real_counts[0]:,} Real and "
        f"{synthetic_counts[0]:,} Synthetic observations. "
        if len(real_counts) == 1 and len(synthetic_counts) == 1
        else "Sample counts vary across summary rows. "
    )
    st.warning(
        "**Methodological note.** "
        + sample_note
        + "Differences are recalculated as Synthetic minus Real; the table "
        "ranks rows by the average absolute gap across mean, SD, median, and "
        "IQR. The source files do not include a predefined feature-quality "
        "score, so no arbitrary score is introduced here. This descriptive "
        "summary does not test statistical significance or full distributional "
        "equivalence. Use the Quantitative Similarity tab for configured "
        "distance or distribution metrics."
    )


def get_bf_af_synthetic_quality_band_from_name(file_name):
    """Extract the frequency band from a BF-AF quality filename."""
    normalized_name = Path(file_name).stem.lower()
    for band in BF_AF_BAND_ORDER:
        if band.lower() in normalized_name:
            return band
    return None


def find_bf_af_synthetic_quality_source():
    """Find the BF-AF synthetic-quality ZIP or extracted CSV files."""
    for zip_path in BF_AF_SYNTHETIC_QUALITY_ZIPS:
        if zip_path.exists():
            return "zip", zip_path

    csv_files = []
    for directory in BF_AF_SYNTHETIC_QUALITY_DIRECTORIES:
        if not directory.exists():
            continue
        csv_files.extend(
            directory.rglob(
                "SyntheticQuality_*_FeatureComparison_BF_vs_AF.csv"
            )
        )

    unique_files = sorted({path.resolve() for path in csv_files})
    if unique_files:
        return "csv", unique_files
    return None, None


@st.cache_data
def load_bf_af_synthetic_quality():
    """Load and validate the five BF-AF synthetic-quality tables."""
    source_type, source = find_bf_af_synthetic_quality_source()
    if source is None:
        raise FileNotFoundError(
            "BF vs AF synthetic-quality data were not found. Keep "
            "'synthetic_quality_master BF AF.zip' beside app.py, or "
            "extract its five SyntheticQuality CSV files into "
            "synthetic_quality_master/, data/, or assets/data/."
        )

    frames = []
    if source_type == "zip":
        with ZipFile(source) as archive:
            csv_sources = [
                name
                for name in archive.namelist()
                if name.lower().endswith(".csv")
                and "syntheticquality" in name.lower()
                and "featurecomparison" in name.lower()
                and "bf" in name.lower()
                and "af" in name.lower()
            ]
            for csv_name in csv_sources:
                band = get_bf_af_synthetic_quality_band_from_name(csv_name)
                if band is None:
                    continue
                with archive.open(csv_name) as csv_file:
                    dataframe = pd.read_csv(csv_file)
                dataframe["Band"] = band
                dataframe["Source_File"] = Path(csv_name).name
                frames.append(dataframe)
    else:
        for csv_path in source:
            band = get_bf_af_synthetic_quality_band_from_name(csv_path.name)
            if band is None:
                continue
            dataframe = pd.read_csv(csv_path)
            dataframe["Band"] = band
            dataframe["Source_File"] = csv_path.name
            frames.append(dataframe)

    if not frames:
        raise FileNotFoundError(
            "No BF vs AF SyntheticQuality FeatureComparison CSV files were "
            "found in the configured source."
        )

    dataframe = pd.concat(frames, ignore_index=True, sort=False)
    missing_columns = BF_AF_SYNTHETIC_REQUIRED_COLUMNS.difference(
        dataframe.columns
    )
    if missing_columns:
        raise ValueError(
            "The BF vs AF synthetic-quality data are missing required "
            "columns: " + ", ".join(sorted(missing_columns))
        )

    dataframe = dataframe.copy()
    dataframe["Band"] = dataframe["Band"].astype(str).str.strip().str.title()
    dataframe["Condition"] = (
        dataframe["Condition"].astype(str).str.strip().str.upper()
    )
    dataframe["Channel"] = (
        dataframe["Channel"].astype(str).str.strip().str.upper()
    )
    dataframe["Feature"] = dataframe["Feature"].astype(str).str.strip()
    dataframe["Feature_Display"] = dataframe["Feature"].str.replace(
        "_", " ", regex=False
    )

    numeric_columns = [
        "Label",
        "Real_Mean",
        "Synthetic_Mean",
        "Real_SD",
        "Synthetic_SD",
        "Real_Median",
        "Synthetic_Median",
        "Real_IQR",
        "Synthetic_IQR",
        "Real_N",
        "Synthetic_N",
    ]
    for column in numeric_columns:
        dataframe[column] = pd.to_numeric(dataframe[column], errors="coerce")
    if dataframe[numeric_columns].isna().any().any():
        raise ValueError(
            "The BF vs AF synthetic-quality CSV files contain missing or "
            "non-numeric values in required summary columns."
        )

    expected_labels = dataframe["Condition"].map({"BF": 0, "AF": 1})
    if expected_labels.isna().any() or not (
        dataframe["Label"] == expected_labels
    ).all():
        raise ValueError(
            "Condition and Label are inconsistent. Expected BF = 0 and "
            "AF = 1 in every synthetic-quality row."
        )

    for metric_config in BF_AF_SYNTHETIC_METRICS.values():
        difference_column = metric_config["difference"]
        absolute_column = metric_config["absolute"]
        dataframe[difference_column] = (
            dataframe[metric_config["synthetic"]]
            - dataframe[metric_config["real"]]
        )
        dataframe[absolute_column] = dataframe[difference_column].abs()

    absolute_columns = [
        metric_config["absolute"]
        for metric_config in BF_AF_SYNTHETIC_METRICS.values()
    ]
    dataframe["Average_Absolute_Summary_Gap"] = dataframe[
        absolute_columns
    ].mean(axis=1)

    duplicate_rows = dataframe.duplicated(
        ["Band", "Condition", "Channel", "Feature"]
    )
    if duplicate_rows.any():
        raise ValueError(
            "Duplicate Band-Condition-Channel-Feature rows were found in the "
            "BF vs AF synthetic-quality data."
        )

    available_bands = set(dataframe["Band"].unique())
    missing_bands = [
        band for band in BF_AF_BAND_ORDER if band not in available_bands
    ]
    if missing_bands:
        raise ValueError(
            "BF vs AF synthetic-quality data are incomplete. Missing bands: "
            + ", ".join(missing_bands)
        )

    if set(dataframe["Condition"].unique()) != {"BF", "AF"}:
        raise ValueError(
            "Synthetic-quality data must contain both BF and AF conditions."
        )

    return dataframe


def get_bf_af_synthetic_quality_key_finding(dataframe):
    """Create the global descriptive BF-AF synthetic-quality finding."""
    metric_averages = {
        metric_name: dataframe[metric_config["absolute"]].mean()
        for metric_name, metric_config in BF_AF_SYNTHETIC_METRICS.items()
    }
    largest_metric = max(metric_averages, key=metric_averages.get)
    band_gaps = dataframe.groupby("Band", observed=True)[
        "Average_Absolute_Summary_Gap"
    ].mean()
    condition_gaps = dataframe.groupby("Condition", observed=True)[
        "Average_Absolute_Summary_Gap"
    ].mean()
    review_row = dataframe.loc[
        dataframe["Average_Absolute_Summary_Gap"].idxmax()
    ]
    lower_condition = condition_gaps.idxmin()
    higher_condition = condition_gaps.idxmax()

    return (
        f"Across {len(dataframe)} band-condition-channel-feature summaries, "
        f"the mean absolute gaps were {metric_averages['Mean']:.3f} for the "
        f"mean, {metric_averages['Standard deviation']:.3f} for SD, "
        f"{metric_averages['Median']:.3f} for the median, and "
        f"{metric_averages['IQR']:.3f} for IQR. {largest_metric} showed the "
        f"largest average discrepancy. {band_gaps.idxmax()} had the largest "
        f"average summary gap ({band_gaps.max():.3f}), while "
        f"{band_gaps.idxmin()} had the smallest ({band_gaps.min():.3f}). "
        f"The combined gap was lower for {lower_condition} "
        f"({condition_gaps[lower_condition]:.3f}) than for "
        f"{higher_condition} ({condition_gaps[higher_condition]:.3f}). "
        f"The largest combined gap was {review_row['Feature_Display']} at "
        f"{review_row['Channel']} under {review_row['Condition']} in "
        f"{review_row['Band']} "
        f"({review_row['Average_Absolute_Summary_Gap']:.3f})."
    )


def get_bf_af_synthetic_quality_interpretation(
    selected_data,
    selected_band,
    selected_condition,
    selected_metric,
):
    """Explain the currently selected BF-AF quality view."""
    metric_config = BF_AF_SYNTHETIC_METRICS[selected_metric]
    difference_column = metric_config["difference"]
    absolute_column = metric_config["absolute"]
    average_gap = selected_data[absolute_column].mean()
    median_gap = selected_data[absolute_column].median()
    review_row = selected_data.loc[selected_data[absolute_column].idxmax()]
    synthetic_higher = int((selected_data[difference_column] > 0).sum())
    synthetic_lower = int((selected_data[difference_column] < 0).sum())
    condition_text = (
        "BF and AF"
        if selected_condition == "All Conditions"
        else selected_condition
    )

    return (
        f"For {selected_band} across {condition_text}, the average absolute "
        f"{selected_metric.lower()} gap was {average_gap:.3f}, with a median "
        f"of {median_gap:.3f}. The largest gap occurred for "
        f"{review_row['Feature_Display']} at {review_row['Channel']} under "
        f"{review_row['Condition']} ({review_row[absolute_column]:.3f}). "
        f"Synthetic values were higher than real values in "
        f"{synthetic_higher} of {len(selected_data)} summaries and lower in "
        f"{synthetic_lower}. Smaller gaps indicate closer descriptive "
        "agreement; they do not by themselves establish distributional "
        "equivalence."
    )


def render_bf_af_synthetic_feature_quality():
    """Render BF-AF descriptive Real-versus-Synthetic quality analysis."""
    st.subheader("Synthetic feature quality")
    st.caption(
        "Compare Real and ACGAN-generated feature summaries across frequency "
        "bands, BF/AF conditions, EEG channels, and feature types."
    )

    try:
        dataframe = load_bf_af_synthetic_quality()
    except (FileNotFoundError, ValueError, pd.errors.ParserError) as error:
        st.error(str(error))
        st.info(
            "Keep 'synthetic_quality_master BF AF.zip' beside app.py, or "
            "extract its five CSV files into synthetic_quality_master/, "
            "data/, or assets/data/, then redeploy the application."
        )
        return

    st.success(
        "**Key finding.** "
        + get_bf_af_synthetic_quality_key_finding(dataframe)
    )

    filter_1, filter_2, filter_3 = st.columns(3)
    with filter_1:
        selected_band = st.selectbox(
            "Frequency band",
            BF_AF_BAND_ORDER,
            index=0,
            key="bf_af_synthetic_quality_band",
        )
    with filter_2:
        selected_condition = st.selectbox(
            "Condition",
            ["All Conditions", "BF", "AF"],
            index=0,
            key="bf_af_synthetic_quality_condition",
        )
    with filter_3:
        selected_metric = st.selectbox(
            "Summary statistic",
            list(BF_AF_SYNTHETIC_METRICS),
            index=0,
            key="bf_af_synthetic_quality_metric",
        )

    selected_data = dataframe[dataframe["Band"] == selected_band].copy()
    if selected_condition != "All Conditions":
        selected_data = selected_data[
            selected_data["Condition"] == selected_condition
        ].copy()
    if selected_data.empty:
        st.warning("No synthetic-quality rows match the selected filters.")
        return

    metric_columns = {
        "Mean": "Abs_Mean_Difference",
        "SD": "Abs_SD_Difference",
        "Median": "Abs_Median_Difference",
        "IQR": "Abs_IQR_Difference",
    }
    cards = st.columns(5)
    cards[0].metric("Summary Rows", len(selected_data))
    for card, (label, column) in zip(cards[1:], metric_columns.items()):
        card.metric(f"Avg |{label} Gap|", f"{selected_data[column].mean():.3f}")

    st.info(
        "**Selected-view interpretation.** "
        + get_bf_af_synthetic_quality_interpretation(
            selected_data,
            selected_band,
            selected_condition,
            selected_metric,
        )
    )

    parity_figure = build_bcf_acf_synthetic_parity_figure(
        selected_data,
        selected_band,
        selected_condition,
        selected_metric,
    )
    st.plotly_chart(
        parity_figure,
        use_container_width=True,
        key="bf_af_synthetic_quality_parity",
    )
    st.caption(
        "The dashed diagonal represents exact agreement. Points closer to the "
        "line have more similar Real and Synthetic summary values."
    )

    heatmap_figure = build_bcf_acf_synthetic_gap_heatmap(
        selected_data,
        selected_band,
        selected_condition,
        selected_metric,
    )
    st.plotly_chart(
        heatmap_figure,
        use_container_width=True,
        key="bf_af_synthetic_quality_heatmap",
    )
    st.caption(
        "Darker cells indicate larger absolute Real-versus-Synthetic gaps. "
        "When both conditions are selected, each cell is their average."
    )

    band_figure = build_bcf_acf_synthetic_band_overview(
        dataframe,
        selected_condition,
    )
    st.plotly_chart(
        band_figure,
        use_container_width=True,
        key="bf_af_synthetic_quality_band_overview",
    )
    st.caption(
        "Band-level bars average the absolute gaps across both conditions, "
        "all four channels, and all six features unless one condition is "
        "selected."
    )

    st.markdown("#### Feature combinations requiring closer review")
    review_table = selected_data.nlargest(
        10, "Average_Absolute_Summary_Gap"
    )[
        [
            "Condition",
            "Channel",
            "Feature_Display",
            "Abs_Mean_Difference",
            "Abs_SD_Difference",
            "Abs_Median_Difference",
            "Abs_IQR_Difference",
            "Average_Absolute_Summary_Gap",
        ]
    ].copy()
    review_table = review_table.rename(
        columns={
            "Feature_Display": "Feature",
            "Abs_Mean_Difference": "|Mean Gap|",
            "Abs_SD_Difference": "|SD Gap|",
            "Abs_Median_Difference": "|Median Gap|",
            "Abs_IQR_Difference": "|IQR Gap|",
            "Average_Absolute_Summary_Gap": "Average Absolute Gap",
        }
    )
    numeric_review_columns = [
        "|Mean Gap|",
        "|SD Gap|",
        "|Median Gap|",
        "|IQR Gap|",
        "Average Absolute Gap",
    ]
    review_table[numeric_review_columns] = review_table[
        numeric_review_columns
    ].round(4)
    st.dataframe(review_table, use_container_width=True, hide_index=True)

    real_counts = sorted(dataframe["Real_N"].astype(int).unique())
    synthetic_counts = sorted(dataframe["Synthetic_N"].astype(int).unique())
    sample_note = (
        f"Each summary row uses {real_counts[0]:,} Real and "
        f"{synthetic_counts[0]:,} Synthetic observations. "
        if len(real_counts) == 1 and len(synthetic_counts) == 1
        else "Sample counts vary across summary rows. "
    )
    st.warning(
        "**Methodological note.** "
        + sample_note
        + "Differences are recalculated as Synthetic minus Real; the table "
        "ranks rows by the average absolute gap across mean, SD, median, and "
        "IQR. The source files do not include a predefined feature-quality "
        "score, so no arbitrary score is introduced here. This descriptive "
        "summary does not test statistical significance or full distributional "
        "equivalence. Use the Quantitative Similarity tab for configured "
        "distance or distribution metrics."
    )


def get_bcm_acm_synthetic_quality_band_from_name(file_name):
    """Extract the frequency band from a BCM-ACM quality filename."""
    normalized_name = Path(file_name).stem.lower()
    for band in BCM_ACM_BAND_ORDER:
        if band.lower() in normalized_name:
            return band
    return None


def find_bcm_acm_synthetic_quality_source():
    """Find the BCM-ACM synthetic-quality ZIP or extracted CSV files."""
    for zip_path in BCM_ACM_SYNTHETIC_QUALITY_ZIPS:
        if zip_path.exists():
            return "zip", zip_path

    csv_files = []
    for directory in BCM_ACM_SYNTHETIC_QUALITY_DIRECTORIES:
        if not directory.exists():
            continue
        csv_files.extend(
            directory.rglob(
                "SyntheticQuality_*_FeatureComparison_BCM_vs_ACM.csv"
            )
        )

    unique_files = sorted({path.resolve() for path in csv_files})
    if unique_files:
        return "csv", unique_files
    return None, None


@st.cache_data
def load_bcm_acm_synthetic_quality():
    """Load and validate the five BCM-ACM synthetic-quality tables."""
    source_type, source = find_bcm_acm_synthetic_quality_source()
    if source is None:
        raise FileNotFoundError(
            "BCM vs ACM synthetic-quality data were not found. Keep "
            "'synthetic_quality_master BCM ACM.zip' beside app.py, or "
            "extract its five SyntheticQuality CSV files into "
            "synthetic_quality_master/, data/, or assets/data/."
        )

    frames = []
    if source_type == "zip":
        with ZipFile(source) as archive:
            csv_sources = [
                name
                for name in archive.namelist()
                if name.lower().endswith(".csv")
                and "syntheticquality" in name.lower()
                and "featurecomparison" in name.lower()
                and "bcm" in name.lower()
                and "acm" in name.lower()
            ]
            for csv_name in csv_sources:
                band = get_bcm_acm_synthetic_quality_band_from_name(csv_name)
                if band is None:
                    continue
                with archive.open(csv_name) as csv_file:
                    dataframe = pd.read_csv(csv_file)
                dataframe["Band"] = band
                dataframe["Source_File"] = Path(csv_name).name
                frames.append(dataframe)
    else:
        for csv_path in source:
            band = get_bcm_acm_synthetic_quality_band_from_name(csv_path.name)
            if band is None:
                continue
            dataframe = pd.read_csv(csv_path)
            dataframe["Band"] = band
            dataframe["Source_File"] = csv_path.name
            frames.append(dataframe)

    if not frames:
        raise FileNotFoundError(
            "No BCM vs ACM SyntheticQuality FeatureComparison CSV files "
            "were found in the configured source."
        )

    dataframe = pd.concat(frames, ignore_index=True, sort=False)
    missing_columns = BCM_ACM_SYNTHETIC_REQUIRED_COLUMNS.difference(
        dataframe.columns
    )
    if missing_columns:
        raise ValueError(
            "The BCM vs ACM synthetic-quality data are missing required "
            "columns: " + ", ".join(sorted(missing_columns))
        )

    dataframe = dataframe.copy()
    dataframe["Band"] = dataframe["Band"].astype(str).str.strip().str.title()
    dataframe["Condition"] = (
        dataframe["Condition"].astype(str).str.strip().str.upper()
    )
    dataframe["Channel"] = (
        dataframe["Channel"].astype(str).str.strip().str.upper()
    )
    dataframe["Feature"] = dataframe["Feature"].astype(str).str.strip()

    # The supplied Delta CSV labels its two band-specific fields as Alpha_BP
    # and Alpha_RP. Preserve the original label and correct only the dashboard
    # display key according to the frequency band encoded in the source file.
    dataframe["Source_Feature"] = dataframe["Feature"]
    delta_label_mask = (
        (dataframe["Band"] == "Delta")
        & dataframe["Feature"].isin(["Alpha_BP", "Alpha_RP"])
    )
    dataframe["Feature_Label_Corrected"] = delta_label_mask
    dataframe.loc[delta_label_mask, "Feature"] = dataframe.loc[
        delta_label_mask, "Feature"
    ].replace({"Alpha_BP": "Delta_BP", "Alpha_RP": "Delta_RP"})
    dataframe["Feature_Display"] = dataframe["Feature"].str.replace(
        "_", " ", regex=False
    )

    numeric_columns = [
        "Label",
        "Real_Mean",
        "Synthetic_Mean",
        "Real_SD",
        "Synthetic_SD",
        "Real_Median",
        "Synthetic_Median",
        "Real_IQR",
        "Synthetic_IQR",
        "Real_N",
        "Synthetic_N",
    ]
    for column in numeric_columns:
        dataframe[column] = pd.to_numeric(dataframe[column], errors="coerce")
    if dataframe[numeric_columns].isna().any().any():
        raise ValueError(
            "The BCM vs ACM synthetic-quality CSV files contain missing or "
            "non-numeric values in required summary columns."
        )

    expected_labels = dataframe["Condition"].map({"BCM": 0, "ACM": 1})
    if expected_labels.isna().any() or not (
        dataframe["Label"] == expected_labels
    ).all():
        raise ValueError(
            "Condition and Label are inconsistent. Expected BCM = 0 and "
            "ACM = 1 in every synthetic-quality row."
        )

    for metric_config in BCM_ACM_SYNTHETIC_METRICS.values():
        difference_column = metric_config["difference"]
        absolute_column = metric_config["absolute"]
        dataframe[difference_column] = (
            dataframe[metric_config["synthetic"]]
            - dataframe[metric_config["real"]]
        )
        dataframe[absolute_column] = dataframe[difference_column].abs()

    absolute_columns = [
        metric_config["absolute"]
        for metric_config in BCM_ACM_SYNTHETIC_METRICS.values()
    ]
    dataframe["Average_Absolute_Summary_Gap"] = dataframe[
        absolute_columns
    ].mean(axis=1)

    duplicate_rows = dataframe.duplicated(
        ["Band", "Condition", "Channel", "Feature"]
    )
    if duplicate_rows.any():
        raise ValueError(
            "Duplicate Band-Condition-Channel-Feature rows were found in the "
            "BCM vs ACM synthetic-quality data."
        )

    available_bands = set(dataframe["Band"].unique())
    missing_bands = [
        band for band in BCM_ACM_BAND_ORDER if band not in available_bands
    ]
    if missing_bands:
        raise ValueError(
            "BCM vs ACM synthetic-quality data are incomplete. Missing "
            "bands: " + ", ".join(missing_bands)
        )

    if set(dataframe["Condition"].unique()) != {"BCM", "ACM"}:
        raise ValueError(
            "Synthetic-quality data must contain both BCM and ACM conditions."
        )

    expected_band_features = {
        band: {f"{band}_BP", f"{band}_RP"}
        for band in BCM_ACM_BAND_ORDER
    }
    incomplete_feature_bands = [
        band
        for band, expected_features in expected_band_features.items()
        if not expected_features.issubset(
            set(dataframe.loc[dataframe["Band"] == band, "Feature"])
        )
    ]
    if incomplete_feature_bands:
        raise ValueError(
            "Band-specific BP/RP labels are incomplete for: "
            + ", ".join(incomplete_feature_bands)
        )

    return dataframe


def get_bcm_acm_synthetic_quality_key_finding(dataframe):
    """Create the global descriptive BCM-ACM synthetic-quality finding."""
    metric_averages = {
        metric_name: dataframe[metric_config["absolute"]].mean()
        for metric_name, metric_config in BCM_ACM_SYNTHETIC_METRICS.items()
    }
    largest_metric = max(metric_averages, key=metric_averages.get)
    band_gaps = dataframe.groupby("Band", observed=True)[
        "Average_Absolute_Summary_Gap"
    ].mean()
    condition_gaps = dataframe.groupby("Condition", observed=True)[
        "Average_Absolute_Summary_Gap"
    ].mean()
    review_row = dataframe.loc[
        dataframe["Average_Absolute_Summary_Gap"].idxmax()
    ]
    lower_condition = condition_gaps.idxmin()
    higher_condition = condition_gaps.idxmax()

    return (
        f"Across {len(dataframe)} band-condition-channel-feature summaries, "
        f"the mean absolute gaps were {metric_averages['Mean']:.3f} for the "
        f"mean, {metric_averages['Standard deviation']:.3f} for SD, "
        f"{metric_averages['Median']:.3f} for the median, and "
        f"{metric_averages['IQR']:.3f} for IQR. {largest_metric} showed the "
        f"largest average discrepancy. {band_gaps.idxmax()} had the largest "
        f"average summary gap ({band_gaps.max():.3f}), while "
        f"{band_gaps.idxmin()} had the smallest ({band_gaps.min():.3f}). "
        f"The combined gap was lower for {lower_condition} "
        f"({condition_gaps[lower_condition]:.3f}) than for "
        f"{higher_condition} ({condition_gaps[higher_condition]:.3f}). "
        f"The largest combined gap was {review_row['Feature_Display']} at "
        f"{review_row['Channel']} under {review_row['Condition']} in "
        f"{review_row['Band']} "
        f"({review_row['Average_Absolute_Summary_Gap']:.3f})."
    )


def get_bcm_acm_synthetic_quality_interpretation(
    selected_data,
    selected_band,
    selected_condition,
    selected_metric,
):
    """Explain the currently selected BCM-ACM quality view."""
    metric_config = BCM_ACM_SYNTHETIC_METRICS[selected_metric]
    difference_column = metric_config["difference"]
    absolute_column = metric_config["absolute"]
    average_gap = selected_data[absolute_column].mean()
    median_gap = selected_data[absolute_column].median()
    review_row = selected_data.loc[selected_data[absolute_column].idxmax()]
    synthetic_higher = int((selected_data[difference_column] > 0).sum())
    synthetic_lower = int((selected_data[difference_column] < 0).sum())
    condition_text = (
        "BCM and ACM"
        if selected_condition == "All Conditions"
        else selected_condition
    )

    return (
        f"For {selected_band} across {condition_text}, the average absolute "
        f"{selected_metric.lower()} gap was {average_gap:.3f}, with a median "
        f"of {median_gap:.3f}. The largest gap occurred for "
        f"{review_row['Feature_Display']} at {review_row['Channel']} under "
        f"{review_row['Condition']} ({review_row[absolute_column]:.3f}). "
        f"Synthetic values were higher than real values in "
        f"{synthetic_higher} of {len(selected_data)} summaries and lower in "
        f"{synthetic_lower}. Smaller gaps indicate closer descriptive "
        "agreement; they do not by themselves establish distributional "
        "equivalence."
    )


def render_bcm_acm_synthetic_feature_quality():
    """Render BCM-ACM descriptive Real-versus-Synthetic quality analysis."""
    st.subheader("Synthetic feature quality")
    st.caption(
        "Compare Real and ACGAN-generated feature summaries across frequency "
        "bands, BCM/ACM conditions, EEG channels, and feature types."
    )

    try:
        dataframe = load_bcm_acm_synthetic_quality()
    except (FileNotFoundError, ValueError, pd.errors.ParserError) as error:
        st.error(str(error))
        st.info(
            "Keep 'synthetic_quality_master BCM ACM.zip' beside app.py, or "
            "extract its five CSV files into synthetic_quality_master/, "
            "data/, or assets/data/, then redeploy the application."
        )
        return

    corrected_labels = int(dataframe["Feature_Label_Corrected"].sum())
    if corrected_labels:
        st.warning(
            "**Source-label note.** The Delta CSV labels its band-specific "
            f"features as Alpha_BP and Alpha_RP in {corrected_labels} rows. "
            "The dashboard displays them as Delta_BP and Delta_RP according "
            "to the source filename; all numeric values remain unchanged."
        )

    st.success(
        "**Key finding.** "
        + get_bcm_acm_synthetic_quality_key_finding(dataframe)
    )

    filter_1, filter_2, filter_3 = st.columns(3)
    with filter_1:
        selected_band = st.selectbox(
            "Frequency band",
            BCM_ACM_BAND_ORDER,
            index=0,
            key="bcm_acm_synthetic_quality_band",
        )
    with filter_2:
        selected_condition = st.selectbox(
            "Condition",
            ["All Conditions", "BCM", "ACM"],
            index=0,
            key="bcm_acm_synthetic_quality_condition",
        )
    with filter_3:
        selected_metric = st.selectbox(
            "Summary statistic",
            list(BCM_ACM_SYNTHETIC_METRICS),
            index=0,
            key="bcm_acm_synthetic_quality_metric",
        )

    selected_data = dataframe[dataframe["Band"] == selected_band].copy()
    if selected_condition != "All Conditions":
        selected_data = selected_data[
            selected_data["Condition"] == selected_condition
        ].copy()
    if selected_data.empty:
        st.warning("No synthetic-quality rows match the selected filters.")
        return

    metric_columns = {
        "Mean": "Abs_Mean_Difference",
        "SD": "Abs_SD_Difference",
        "Median": "Abs_Median_Difference",
        "IQR": "Abs_IQR_Difference",
    }
    cards = st.columns(5)
    cards[0].metric("Summary Rows", len(selected_data))
    for card, (label, column) in zip(cards[1:], metric_columns.items()):
        card.metric(f"Avg |{label} Gap|", f"{selected_data[column].mean():.3f}")

    st.info(
        "**Selected-view interpretation.** "
        + get_bcm_acm_synthetic_quality_interpretation(
            selected_data,
            selected_band,
            selected_condition,
            selected_metric,
        )
    )

    parity_figure = build_bcf_acf_synthetic_parity_figure(
        selected_data,
        selected_band,
        selected_condition,
        selected_metric,
    )
    st.plotly_chart(
        parity_figure,
        use_container_width=True,
        key="bcm_acm_synthetic_quality_parity",
    )
    st.caption(
        "The dashed diagonal represents exact agreement. Points closer to the "
        "line have more similar Real and Synthetic summary values."
    )

    heatmap_figure = build_bcf_acf_synthetic_gap_heatmap(
        selected_data,
        selected_band,
        selected_condition,
        selected_metric,
    )
    st.plotly_chart(
        heatmap_figure,
        use_container_width=True,
        key="bcm_acm_synthetic_quality_heatmap",
    )
    st.caption(
        "Darker cells indicate larger absolute Real-versus-Synthetic gaps. "
        "When both conditions are selected, each cell is their average."
    )

    band_figure = build_bcf_acf_synthetic_band_overview(
        dataframe,
        selected_condition,
    )
    st.plotly_chart(
        band_figure,
        use_container_width=True,
        key="bcm_acm_synthetic_quality_band_overview",
    )
    st.caption(
        "Band-level bars average the absolute gaps across both conditions, "
        "all four channels, and all six features unless one condition is "
        "selected."
    )

    st.markdown("#### Feature combinations requiring closer review")
    review_table = selected_data.nlargest(
        10, "Average_Absolute_Summary_Gap"
    )[
        [
            "Condition",
            "Channel",
            "Feature_Display",
            "Abs_Mean_Difference",
            "Abs_SD_Difference",
            "Abs_Median_Difference",
            "Abs_IQR_Difference",
            "Average_Absolute_Summary_Gap",
        ]
    ].copy()
    review_table = review_table.rename(
        columns={
            "Feature_Display": "Feature",
            "Abs_Mean_Difference": "|Mean Gap|",
            "Abs_SD_Difference": "|SD Gap|",
            "Abs_Median_Difference": "|Median Gap|",
            "Abs_IQR_Difference": "|IQR Gap|",
            "Average_Absolute_Summary_Gap": "Average Absolute Gap",
        }
    )
    numeric_review_columns = [
        "|Mean Gap|",
        "|SD Gap|",
        "|Median Gap|",
        "|IQR Gap|",
        "Average Absolute Gap",
    ]
    review_table[numeric_review_columns] = review_table[
        numeric_review_columns
    ].round(4)
    st.dataframe(review_table, use_container_width=True, hide_index=True)

    real_counts = sorted(dataframe["Real_N"].astype(int).unique())
    synthetic_counts = sorted(dataframe["Synthetic_N"].astype(int).unique())
    sample_note = (
        f"Each summary row uses {real_counts[0]:,} Real and "
        f"{synthetic_counts[0]:,} Synthetic observations. "
        if len(real_counts) == 1 and len(synthetic_counts) == 1
        else "Sample counts vary across summary rows. "
    )
    st.warning(
        "**Methodological note.** "
        + sample_note
        + "Differences are recalculated as Synthetic minus Real; the table "
        "ranks rows by the average absolute gap across mean, SD, median, and "
        "IQR. The source files do not include a predefined feature-quality "
        "score, so no arbitrary score is introduced here. This descriptive "
        "summary does not test statistical significance or full distributional "
        "equivalence. Use the Quantitative Similarity tab for configured "
        "distance or distribution metrics."
    )


def get_bm_am_synthetic_quality_band_from_name(file_name):
    """Extract the frequency band from a BM-AM quality filename."""
    normalized_name = Path(file_name).stem.lower()
    for band in BM_AM_BAND_ORDER:
        if band.lower() in normalized_name:
            return band
    return None


def find_bm_am_synthetic_quality_source():
    """Find the BM-AM synthetic-quality ZIP or extracted CSV files."""
    for zip_path in BM_AM_SYNTHETIC_QUALITY_ZIPS:
        if zip_path.exists():
            return "zip", zip_path

    csv_files = []
    for directory in BM_AM_SYNTHETIC_QUALITY_DIRECTORIES:
        if not directory.exists():
            continue
        csv_files.extend(
            directory.rglob(
                "SyntheticQuality_*_FeatureComparison_BM_vs_AM.csv"
            )
        )

    unique_files = sorted({path.resolve() for path in csv_files})
    if unique_files:
        return "csv", unique_files
    return None, None


@st.cache_data
def load_bm_am_synthetic_quality():
    """Load and validate the five BM-AM synthetic-quality tables."""
    source_type, source = find_bm_am_synthetic_quality_source()
    if source is None:
        raise FileNotFoundError(
            "BM vs AM synthetic-quality data were not found. Keep "
            "'synthetic_quality_master BM AM.zip' beside app.py, or "
            "extract its five SyntheticQuality CSV files into "
            "synthetic_quality_master/, data/, or assets/data/."
        )

    frames = []
    if source_type == "zip":
        with ZipFile(source) as archive:
            csv_sources = [
                name
                for name in archive.namelist()
                if name.lower().endswith(".csv")
                and "syntheticquality" in name.lower()
                and "featurecomparison" in name.lower()
                and "bm" in name.lower()
                and "am" in name.lower()
            ]
            for csv_name in csv_sources:
                band = get_bm_am_synthetic_quality_band_from_name(csv_name)
                if band is None:
                    continue
                with archive.open(csv_name) as csv_file:
                    dataframe = pd.read_csv(csv_file)
                dataframe["Band"] = band
                dataframe["Source_File"] = Path(csv_name).name
                frames.append(dataframe)
    else:
        for csv_path in source:
            band = get_bm_am_synthetic_quality_band_from_name(csv_path.name)
            if band is None:
                continue
            dataframe = pd.read_csv(csv_path)
            dataframe["Band"] = band
            dataframe["Source_File"] = csv_path.name
            frames.append(dataframe)

    if not frames:
        raise FileNotFoundError(
            "No BM vs AM SyntheticQuality FeatureComparison CSV files were "
            "found in the configured source."
        )

    dataframe = pd.concat(frames, ignore_index=True, sort=False)
    missing_columns = BM_AM_SYNTHETIC_REQUIRED_COLUMNS.difference(
        dataframe.columns
    )
    if missing_columns:
        raise ValueError(
            "The BM vs AM synthetic-quality data are missing required "
            "columns: " + ", ".join(sorted(missing_columns))
        )

    dataframe = dataframe.copy()
    dataframe["Band"] = dataframe["Band"].astype(str).str.strip().str.title()
    dataframe["Condition"] = (
        dataframe["Condition"].astype(str).str.strip().str.upper()
    )
    dataframe["Channel"] = (
        dataframe["Channel"].astype(str).str.strip().str.upper()
    )
    dataframe["Feature"] = dataframe["Feature"].astype(str).str.strip()
    dataframe["Feature_Display"] = dataframe["Feature"].str.replace(
        "_", " ", regex=False
    )

    numeric_columns = [
        "Label",
        "Real_Mean",
        "Synthetic_Mean",
        "Real_SD",
        "Synthetic_SD",
        "Real_Median",
        "Synthetic_Median",
        "Real_IQR",
        "Synthetic_IQR",
        "Real_N",
        "Synthetic_N",
    ]
    for column in numeric_columns:
        dataframe[column] = pd.to_numeric(dataframe[column], errors="coerce")
    if dataframe[numeric_columns].isna().any().any():
        raise ValueError(
            "The BM vs AM synthetic-quality CSV files contain missing or "
            "non-numeric values in required summary columns."
        )

    expected_labels = dataframe["Condition"].map({"BM": 0, "AM": 1})
    if expected_labels.isna().any() or not (
        dataframe["Label"] == expected_labels
    ).all():
        raise ValueError(
            "Condition and Label are inconsistent. Expected BM = 0 and "
            "AM = 1 in every synthetic-quality row."
        )

    for metric_config in BM_AM_SYNTHETIC_METRICS.values():
        difference_column = metric_config["difference"]
        absolute_column = metric_config["absolute"]
        dataframe[difference_column] = (
            dataframe[metric_config["synthetic"]]
            - dataframe[metric_config["real"]]
        )
        dataframe[absolute_column] = dataframe[difference_column].abs()

    absolute_columns = [
        metric_config["absolute"]
        for metric_config in BM_AM_SYNTHETIC_METRICS.values()
    ]
    dataframe["Average_Absolute_Summary_Gap"] = dataframe[
        absolute_columns
    ].mean(axis=1)

    duplicate_rows = dataframe.duplicated(
        ["Band", "Condition", "Channel", "Feature"]
    )
    if duplicate_rows.any():
        raise ValueError(
            "Duplicate Band-Condition-Channel-Feature rows were found in the "
            "BM vs AM synthetic-quality data."
        )

    available_bands = set(dataframe["Band"].unique())
    missing_bands = [
        band for band in BM_AM_BAND_ORDER if band not in available_bands
    ]
    if missing_bands:
        raise ValueError(
            "BM vs AM synthetic-quality data are incomplete. Missing bands: "
            + ", ".join(missing_bands)
        )

    if set(dataframe["Condition"].unique()) != {"BM", "AM"}:
        raise ValueError(
            "Synthetic-quality data must contain both BM and AM conditions."
        )

    expected_band_features = {
        band: {f"{band}_BP", f"{band}_RP"}
        for band in BM_AM_BAND_ORDER
    }
    incomplete_feature_bands = [
        band
        for band, expected_features in expected_band_features.items()
        if not expected_features.issubset(
            set(dataframe.loc[dataframe["Band"] == band, "Feature"])
        )
    ]
    if incomplete_feature_bands:
        raise ValueError(
            "Band-specific BP/RP labels are incomplete for: "
            + ", ".join(incomplete_feature_bands)
        )

    return dataframe


def get_bm_am_synthetic_quality_key_finding(dataframe):
    """Create the global descriptive BM-AM synthetic-quality finding."""
    metric_averages = {
        metric_name: dataframe[metric_config["absolute"]].mean()
        for metric_name, metric_config in BM_AM_SYNTHETIC_METRICS.items()
    }
    largest_metric = max(metric_averages, key=metric_averages.get)
    band_gaps = dataframe.groupby("Band", observed=True)[
        "Average_Absolute_Summary_Gap"
    ].mean()
    condition_gaps = dataframe.groupby("Condition", observed=True)[
        "Average_Absolute_Summary_Gap"
    ].mean()
    review_row = dataframe.loc[
        dataframe["Average_Absolute_Summary_Gap"].idxmax()
    ]
    lower_condition = condition_gaps.idxmin()
    higher_condition = condition_gaps.idxmax()

    return (
        f"Across {len(dataframe)} band-condition-channel-feature summaries, "
        f"the mean absolute gaps were {metric_averages['Mean']:.3f} for the "
        f"mean, {metric_averages['Standard deviation']:.3f} for SD, "
        f"{metric_averages['Median']:.3f} for the median, and "
        f"{metric_averages['IQR']:.3f} for IQR. {largest_metric} showed the "
        f"largest average discrepancy. {band_gaps.idxmax()} had the largest "
        f"average summary gap ({band_gaps.max():.3f}), while "
        f"{band_gaps.idxmin()} had the smallest ({band_gaps.min():.3f}). "
        f"The combined gap was lower for {lower_condition} "
        f"({condition_gaps[lower_condition]:.3f}) than for "
        f"{higher_condition} ({condition_gaps[higher_condition]:.3f}). "
        f"The largest combined gap was {review_row['Feature_Display']} at "
        f"{review_row['Channel']} under {review_row['Condition']} in "
        f"{review_row['Band']} "
        f"({review_row['Average_Absolute_Summary_Gap']:.3f})."
    )


def get_bm_am_synthetic_quality_interpretation(
    selected_data,
    selected_band,
    selected_condition,
    selected_metric,
):
    """Explain the currently selected BM-AM quality view."""
    metric_config = BM_AM_SYNTHETIC_METRICS[selected_metric]
    difference_column = metric_config["difference"]
    absolute_column = metric_config["absolute"]
    average_gap = selected_data[absolute_column].mean()
    median_gap = selected_data[absolute_column].median()
    review_row = selected_data.loc[selected_data[absolute_column].idxmax()]
    synthetic_higher = int((selected_data[difference_column] > 0).sum())
    synthetic_lower = int((selected_data[difference_column] < 0).sum())
    condition_text = (
        "BM and AM"
        if selected_condition == "All Conditions"
        else selected_condition
    )

    return (
        f"For {selected_band} across {condition_text}, the average absolute "
        f"{selected_metric.lower()} gap was {average_gap:.3f}, with a median "
        f"of {median_gap:.3f}. The largest gap occurred for "
        f"{review_row['Feature_Display']} at {review_row['Channel']} under "
        f"{review_row['Condition']} ({review_row[absolute_column]:.3f}). "
        f"Synthetic values were higher than real values in "
        f"{synthetic_higher} of {len(selected_data)} summaries and lower in "
        f"{synthetic_lower}. Smaller gaps indicate closer descriptive "
        "agreement; they do not by themselves establish distributional "
        "equivalence."
    )


def render_bm_am_synthetic_feature_quality():
    """Render BM-AM descriptive Real-versus-Synthetic quality analysis."""
    st.subheader("Synthetic feature quality")
    st.caption(
        "Compare Real and ACGAN-generated feature summaries across frequency "
        "bands, BM/AM conditions, EEG channels, and feature types."
    )

    try:
        dataframe = load_bm_am_synthetic_quality()
    except (FileNotFoundError, ValueError, pd.errors.ParserError) as error:
        st.error(str(error))
        st.info(
            "Keep 'synthetic_quality_master BM AM.zip' beside app.py, or "
            "extract its five CSV files into synthetic_quality_master/, "
            "data/, or assets/data/, then redeploy the application."
        )
        return

    st.success(
        "**Key finding.** "
        + get_bm_am_synthetic_quality_key_finding(dataframe)
    )

    filter_1, filter_2, filter_3 = st.columns(3)
    with filter_1:
        selected_band = st.selectbox(
            "Frequency band",
            BM_AM_BAND_ORDER,
            index=0,
            key="bm_am_synthetic_quality_band",
        )
    with filter_2:
        selected_condition = st.selectbox(
            "Condition",
            ["All Conditions", "BM", "AM"],
            index=0,
            key="bm_am_synthetic_quality_condition",
        )
    with filter_3:
        selected_metric = st.selectbox(
            "Summary statistic",
            list(BM_AM_SYNTHETIC_METRICS),
            index=0,
            key="bm_am_synthetic_quality_metric",
        )

    selected_data = dataframe[dataframe["Band"] == selected_band].copy()
    if selected_condition != "All Conditions":
        selected_data = selected_data[
            selected_data["Condition"] == selected_condition
        ].copy()
    if selected_data.empty:
        st.warning("No synthetic-quality rows match the selected filters.")
        return

    metric_columns = {
        "Mean": "Abs_Mean_Difference",
        "SD": "Abs_SD_Difference",
        "Median": "Abs_Median_Difference",
        "IQR": "Abs_IQR_Difference",
    }
    cards = st.columns(5)
    cards[0].metric("Summary Rows", len(selected_data))
    for card, (label, column) in zip(cards[1:], metric_columns.items()):
        card.metric(f"Avg |{label} Gap|", f"{selected_data[column].mean():.3f}")

    st.info(
        "**Selected-view interpretation.** "
        + get_bm_am_synthetic_quality_interpretation(
            selected_data,
            selected_band,
            selected_condition,
            selected_metric,
        )
    )

    parity_figure = build_bcf_acf_synthetic_parity_figure(
        selected_data,
        selected_band,
        selected_condition,
        selected_metric,
    )
    st.plotly_chart(
        parity_figure,
        use_container_width=True,
        key="bm_am_synthetic_quality_parity",
    )
    st.caption(
        "The dashed diagonal represents exact agreement. Points closer to the "
        "line have more similar Real and Synthetic summary values."
    )

    heatmap_figure = build_bcf_acf_synthetic_gap_heatmap(
        selected_data,
        selected_band,
        selected_condition,
        selected_metric,
    )
    st.plotly_chart(
        heatmap_figure,
        use_container_width=True,
        key="bm_am_synthetic_quality_heatmap",
    )
    st.caption(
        "Darker cells indicate larger absolute Real-versus-Synthetic gaps. "
        "When both conditions are selected, each cell is their average."
    )

    band_figure = build_bcf_acf_synthetic_band_overview(
        dataframe,
        selected_condition,
    )
    st.plotly_chart(
        band_figure,
        use_container_width=True,
        key="bm_am_synthetic_quality_band_overview",
    )
    st.caption(
        "Band-level bars average the absolute gaps across both conditions, "
        "all four channels, and all six features unless one condition is "
        "selected."
    )

    st.markdown("#### Feature combinations requiring closer review")
    review_table = selected_data.nlargest(
        10, "Average_Absolute_Summary_Gap"
    )[
        [
            "Condition",
            "Channel",
            "Feature_Display",
            "Abs_Mean_Difference",
            "Abs_SD_Difference",
            "Abs_Median_Difference",
            "Abs_IQR_Difference",
            "Average_Absolute_Summary_Gap",
        ]
    ].copy()
    review_table = review_table.rename(
        columns={
            "Feature_Display": "Feature",
            "Abs_Mean_Difference": "|Mean Gap|",
            "Abs_SD_Difference": "|SD Gap|",
            "Abs_Median_Difference": "|Median Gap|",
            "Abs_IQR_Difference": "|IQR Gap|",
            "Average_Absolute_Summary_Gap": "Average Absolute Gap",
        }
    )
    numeric_review_columns = [
        "|Mean Gap|",
        "|SD Gap|",
        "|Median Gap|",
        "|IQR Gap|",
        "Average Absolute Gap",
    ]
    review_table[numeric_review_columns] = review_table[
        numeric_review_columns
    ].round(4)
    st.dataframe(review_table, use_container_width=True, hide_index=True)

    real_counts = sorted(dataframe["Real_N"].astype(int).unique())
    synthetic_counts = sorted(dataframe["Synthetic_N"].astype(int).unique())
    sample_note = (
        f"Each summary row uses {real_counts[0]:,} Real and "
        f"{synthetic_counts[0]:,} Synthetic observations. "
        if len(real_counts) == 1 and len(synthetic_counts) == 1
        else "Sample counts vary across summary rows. "
    )
    st.warning(
        "**Methodological note.** "
        + sample_note
        + "Differences are recalculated as Synthetic minus Real; the table "
        "ranks rows by the average absolute gap across mean, SD, median, and "
        "IQR. The source files do not include a predefined feature-quality "
        "score, so no arbitrary score is introduced here. This descriptive "
        "summary does not test statistical significance or full distributional "
        "equivalence. Use the Quantitative Similarity tab for configured "
        "distance or distribution metrics."
    )


def get_bcf_acf_paired_band_from_name(file_name):
    """Extract the analysis band from a BCF vs ACF statistics filename."""
    normalized_name = Path(file_name).stem.lower()
    for band in BCF_ACF_BAND_ORDER:
        if band.lower() in normalized_name:
            return band
    return None


def find_bcf_acf_paired_statistics_source():
    """Find either the source ZIP or the five extracted statistics CSV files."""
    for zip_path in BCF_ACF_PAIRED_STATISTICS_ZIPS:
        if zip_path.exists():
            return "zip", zip_path

    csv_files = []
    for directory in BCF_ACF_PAIRED_STATISTICS_DIRECTORIES:
        if not directory.exists():
            continue
        csv_files.extend(
            directory.rglob(
                "PairedStatistics_EffectSize_FDR_*_BCF_vs_ACF.csv"
            )
        )

    unique_files = sorted({path.resolve() for path in csv_files})
    if unique_files:
        return "csv", unique_files
    return None, None


@st.cache_data
def load_bcf_acf_paired_statistics():
    """Load and validate the five BCF vs ACF paired-statistics tables."""
    source_type, source = find_bcf_acf_paired_statistics_source()
    if source is None:
        raise FileNotFoundError(
            "BCF vs ACF paired-statistics data were not found. Keep "
            "'paired_statistics_master BCF ACF.zip' beside app.py, or extract "
            "the five PairedStatistics_EffectSize_FDR CSV files into "
            "paired_statistics_master/, data/, or assets/data/."
        )

    frames = []

    if source_type == "zip":
        with ZipFile(source) as archive:
            csv_names = [
                name
                for name in archive.namelist()
                if name.lower().endswith(".csv")
                and "pairedstatistics_effectsize_fdr" in name.lower()
                and "bcf" in name.lower()
                and "acf" in name.lower()
            ]

            for csv_name in csv_names:
                band = get_bcf_acf_paired_band_from_name(csv_name)
                if band is None:
                    continue
                with archive.open(csv_name) as csv_file:
                    dataframe = pd.read_csv(csv_file)
                dataframe.insert(0, "Analysis_Band", band)
                dataframe["Source_File"] = Path(csv_name).name
                frames.append(dataframe)
    else:
        for csv_path in source:
            band = get_bcf_acf_paired_band_from_name(csv_path.name)
            if band is None:
                continue
            dataframe = pd.read_csv(csv_path)
            dataframe.insert(0, "Analysis_Band", band)
            dataframe["Source_File"] = csv_path.name
            frames.append(dataframe)

    if not frames:
        raise FileNotFoundError(
            "No BCF vs ACF PairedStatistics_EffectSize_FDR CSV files were "
            "found in the configured source."
        )

    missing_bands = [
        band
        for band in BCF_ACF_BAND_ORDER
        if band not in {frame["Analysis_Band"].iloc[0] for frame in frames}
    ]
    if missing_bands:
        raise ValueError(
            "The paired-statistics source is incomplete. Missing bands: "
            + ", ".join(missing_bands)
        )

    validated_frames = []
    numeric_columns = [
        "n_subjects",
        "mean_change",
        "ci95_lower",
        "ci95_upper",
        "cohens_dz",
        "t_statistic",
        "p_ttest",
        "wilcoxon_statistic",
        "p_wilcoxon",
        "p_fdr_ttest",
        "p_fdr_wilcoxon",
    ]

    for dataframe in frames:
        missing_columns = BCF_ACF_PAIRED_REQUIRED_COLUMNS.difference(
            dataframe.columns
        )
        if missing_columns:
            raise ValueError(
                f"{dataframe['Source_File'].iloc[0]} is missing required "
                "columns: " + ", ".join(sorted(missing_columns))
            )

        dataframe = dataframe.copy()
        dataframe["Analysis_Band"] = (
            dataframe["Analysis_Band"].astype(str).str.strip().str.title()
        )
        dataframe["channel"] = (
            dataframe["channel"].astype(str).str.strip().str.upper()
        )
        dataframe["feature"] = dataframe["feature"].astype(str).str.strip()
        dataframe["feature_type"] = (
            dataframe["feature_type"].astype(str).str.strip().str.upper()
        )
        dataframe["effect_size_interpretation"] = (
            dataframe["effect_size_interpretation"]
            .astype(str)
            .str.strip()
            .str.title()
        )

        for column in numeric_columns:
            dataframe[column] = pd.to_numeric(
                dataframe[column], errors="coerce"
            )

        required_numeric = [
            "n_subjects",
            "mean_change",
            "cohens_dz",
            "p_ttest",
            "p_wilcoxon",
            "p_fdr_ttest",
            "p_fdr_wilcoxon",
        ]
        if dataframe[required_numeric].isna().any().any():
            raise ValueError(
                f"{dataframe['Source_File'].iloc[0]} contains missing or "
                "non-numeric values in required statistical columns."
            )

        validated_frames.append(dataframe)

    master = pd.concat(validated_frames, ignore_index=True)
    duplicate_rows = master.duplicated(
        ["Analysis_Band", "channel", "feature"], keep=False
    )
    if duplicate_rows.any():
        raise ValueError(
            "Duplicate band-channel-feature rows were found in the BCF vs ACF "
            "paired-statistics source."
        )

    master["Analysis_Band"] = pd.Categorical(
        master["Analysis_Band"],
        categories=BCF_ACF_BAND_ORDER,
        ordered=True,
    )
    master = master.sort_values(
        ["Analysis_Band", "channel", "feature"]
    ).reset_index(drop=True)
    return master


def format_bcf_acf_p_value(value):
    """Format p-values and FDR-adjusted p-values for dashboard text."""
    if pd.isna(value):
        return "N/A"
    if value < 0.0001:
        return f"{value:.2e}"
    return f"{value:.4f}"


def get_bcf_acf_paired_band_statistics(dataframe, band, test_label):
    """Return the principal paired-statistics metrics for one band and test."""
    test_config = BCF_ACF_TEST_OPTIONS[test_label]
    p_column = test_config["p_column"]
    q_column = test_config["q_column"]
    band_data = dataframe[
        dataframe["Analysis_Band"].astype(str) == band
    ].copy()

    total = len(band_data)
    nominal_significant = int((band_data[p_column] < 0.05).sum())
    fdr_significant = int((band_data[q_column] < 0.05).sum())

    strongest = band_data.loc[band_data["cohens_dz"].abs().idxmax()]
    band_specific = band_data[
        band_data["feature_type"].isin(["BP", "RP"])
    ]
    strongest_band_specific = band_specific.loc[
        band_specific["cohens_dz"].abs().idxmax()
    ]
    smallest_q = band_data.loc[band_data[q_column].idxmin()]

    return {
        "data": band_data,
        "p_column": p_column,
        "q_column": q_column,
        "statistic_column": test_config["statistic_column"],
        "total": total,
        "paired_subjects": int(band_data["n_subjects"].max()),
        "nominal_significant": nominal_significant,
        "fdr_significant": fdr_significant,
        "strongest": strongest,
        "strongest_band_specific": strongest_band_specific,
        "smallest_q": smallest_q,
    }


def get_bcf_acf_paired_band_summary(dataframe, band, test_label):
    """Create a concise English interpretation for one frequency band."""
    summary = get_bcf_acf_paired_band_statistics(dataframe, band, test_label)
    strongest = summary["strongest"]
    strongest_band = summary["strongest_band_specific"]
    smallest_q = summary["smallest_q"]

    if summary["fdr_significant"] == 0:
        significance_text = (
            f"{summary['nominal_significant']} of {summary['total']} comparisons "
            "had an unadjusted p-value below 0.05, but none remained "
            "significant after FDR correction."
        )
    else:
        significance_text = (
            f"{summary['nominal_significant']} of {summary['total']} comparisons "
            "had an unadjusted p-value below 0.05, and "
            f"{summary['fdr_significant']} remained significant after FDR "
            "correction."
        )

    effect_text = (
        f"The largest absolute effect was {strongest['feature']} at "
        f"{strongest['channel']} (Cohen's dz = {strongest['cohens_dz']:+.3f}, "
        f"{strongest['effect_size_interpretation'].lower()})."
    )
    if (
        strongest["feature"] != strongest_band["feature"]
        or strongest["channel"] != strongest_band["channel"]
    ):
        effect_text += (
            f" The strongest band-specific power effect was "
            f"{strongest_band['feature']} at {strongest_band['channel']} "
            f"(dz = {strongest_band['cohens_dz']:+.3f})."
        )

    return (
        f"Using the {test_label}, {significance_text} {effect_text} The "
        f"smallest FDR-adjusted p-value was "
        f"{format_bcf_acf_p_value(smallest_q[summary['q_column']])}."
    )


def get_bcf_acf_paired_key_finding(dataframe):
    """Create the cross-band key finding without combining or averaging p-values."""
    t_nominal_counts = []
    w_nominal_counts = []
    t_fdr_count = 0
    w_fdr_count = 0

    for band in BCF_ACF_BAND_ORDER:
        band_data = dataframe[
            dataframe["Analysis_Band"].astype(str) == band
        ]
        t_nominal_counts.append(int((band_data["p_ttest"] < 0.05).sum()))
        w_nominal_counts.append(int((band_data["p_wilcoxon"] < 0.05).sum()))
        t_fdr_count += int((band_data["p_fdr_ttest"] < 0.05).sum())
        w_fdr_count += int((band_data["p_fdr_wilcoxon"] < 0.05).sum())

    strongest = dataframe.loc[dataframe["cohens_dz"].abs().idxmax()]
    t_range = (
        str(t_nominal_counts[0])
        if len(set(t_nominal_counts)) == 1
        else f"{min(t_nominal_counts)}-{max(t_nominal_counts)}"
    )
    w_range = (
        str(w_nominal_counts[0])
        if len(set(w_nominal_counts)) == 1
        else f"{min(w_nominal_counts)}-{max(w_nominal_counts)}"
    )
    t_result_word = "result" if t_range == "1" else "results"
    w_result_word = "result" if w_range == "1" else "results"

    return (
        "Each frequency-band file contains 24 channel-feature comparisons. "
        f"The paired t-test identified {t_range} nominal {t_result_word} with "
        f"p < 0.05 per band, and the Wilcoxon test identified {w_range} "
        f"nominal {w_result_word}. "
        f"After FDR correction, {t_fdr_count} t-test results and "
        f"{w_fdr_count} Wilcoxon results remained significant across the five "
        "band-specific correction families. The largest absolute effect was "
        f"{strongest['feature']} at {strongest['channel']} in the "
        f"{strongest['Analysis_Band']} file (Cohen's dz = "
        f"{strongest['cohens_dz']:+.3f})."
    )


def build_bcf_acf_effect_size_figure(band_data, band):
    """Build a horizontal Cohen's dz point plot for the selected band."""
    plot_data = band_data.copy()
    plot_data["Comparison"] = (
        plot_data["channel"] + " | " + plot_data["feature"]
    )
    plot_data = plot_data.sort_values("cohens_dz")
    comparison_order = plot_data["Comparison"].tolist()

    color_map = {
        "Negligible": "#9CA3AF",
        "Small": "#60A5FA",
        "Medium": "#F59E0B",
        "Large": "#B91C1C",
    }
    figure = px.scatter(
        plot_data,
        x="cohens_dz",
        y="Comparison",
        color="effect_size_interpretation",
        color_discrete_map=color_map,
        category_orders={"Comparison": comparison_order},
        hover_data={
            "mean_change": ":.4g",
            "p_ttest": ":.4f",
            "p_wilcoxon": ":.4f",
            "p_fdr_ttest": ":.4f",
            "p_fdr_wilcoxon": ":.4f",
            "effect_size_interpretation": False,
        },
        labels={
            "cohens_dz": "Cohen's dz",
            "effect_size_interpretation": "Effect size",
        },
        title=f"Cohen's dz by Channel and Feature<br><sup>{band}</sup>",
    )
    maximum_effect = max(1.0, float(plot_data["cohens_dz"].abs().max()) * 1.15)
    figure.add_vline(x=0, line_color="#374151", line_width=1)
    figure.update_traces(marker={"size": 11, "line": {"width": 0.5}})
    figure.update_layout(
        height=720,
        margin=dict(l=20, r=20, t=75, b=20),
        xaxis=dict(range=[-maximum_effect, maximum_effect], zeroline=False),
        yaxis_title="",
        legend_title_text="Effect magnitude",
    )
    return figure


def build_bcf_acf_fdr_heatmap(band_data, band, test_label, q_column):
    """Build the channel-by-feature FDR heatmap from the selected CSV values."""
    preferred_features = [
        f"{band} Band Power",
        f"{band} Relative Power",
        "Entropy",
        "Hjorth Activity",
        "Hjorth Mobility",
        "Hjorth Complexity",
    ]
    available_features = set(band_data["feature"].unique())
    feature_order = [
        feature for feature in preferred_features if feature in available_features
    ]
    available_channels = set(band_data["channel"].unique())
    channel_order = [
        channel for channel in BCF_ACF_CHANNEL_ORDER if channel in available_channels
    ]

    matrix = band_data.pivot(
        index="channel", columns="feature", values=q_column
    ).reindex(index=channel_order, columns=feature_order)

    figure = go.Figure(
        data=go.Heatmap(
            z=matrix.values,
            x=matrix.columns.tolist(),
            y=matrix.index.tolist(),
            zmin=0,
            zmax=1,
            colorscale=[
                [0.0, "#B91C1C"],
                [0.049, "#FCA5A5"],
                [0.05, "#FEF3C7"],
                [1.0, "#DCFCE7"],
            ],
            colorbar={"title": "FDR q"},
            hovertemplate=(
                "Channel: %{y}<br>Feature: %{x}<br>FDR q: %{z:.4f}"
                "<extra></extra>"
            ),
        )
    )

    for row_index, channel in enumerate(matrix.index):
        for column_index, feature in enumerate(matrix.columns):
            value = matrix.iloc[row_index, column_index]
            if pd.isna(value):
                label = "N/A"
                font_color = "#111827"
            else:
                label = f"{value:.3f}" + ("*" if value < 0.05 else "")
                font_color = "white" if value < 0.05 else "#111827"
            figure.add_annotation(
                x=feature,
                y=channel,
                text=label,
                showarrow=False,
                font={"size": 12, "color": font_color},
            )

    figure.update_layout(
        title=(
            "FDR-Adjusted P-Value Heatmap<br>"
            f"<sup>{band} | {test_label}</sup>"
        ),
        height=480,
        margin=dict(l=20, r=20, t=80, b=95),
        xaxis_title="Feature",
        yaxis_title="EEG Channel",
        xaxis={"tickangle": -25},
    )
    return figure


def prepare_bcf_acf_paired_display_table(band_data, q_column, p_column):
    """Prepare a readable results table while retaining the source values."""
    table = band_data[
        [
            "channel",
            "feature",
            "mean_change",
            "ci95_lower",
            "ci95_upper",
            "cohens_dz",
            "effect_size_interpretation",
            p_column,
            q_column,
        ]
    ].copy()
    table["95% CI for Mean Change"] = table.apply(
        lambda row: (
            f"[{row['ci95_lower']:.4g}, {row['ci95_upper']:.4g}]"
            if pd.notna(row["ci95_lower"]) and pd.notna(row["ci95_upper"])
            else "N/A"
        ),
        axis=1,
    )
    table["Significant After FDR"] = table[q_column] < 0.05
    table = table.drop(columns=["ci95_lower", "ci95_upper"])
    table = table.rename(
        columns={
            "channel": "Channel",
            "feature": "Feature",
            "mean_change": "Mean Change",
            "cohens_dz": "Cohen's dz",
            "effect_size_interpretation": "Effect",
            p_column: "Raw p",
            q_column: "FDR q",
        }
    )
    column_order = [
        "Channel",
        "Feature",
        "Mean Change",
        "95% CI for Mean Change",
        "Cohen's dz",
        "Effect",
        "Raw p",
        "FDR q",
        "Significant After FDR",
    ]
    return table[column_order].sort_values(["FDR q", "Raw p"])


def render_bcf_acf_paired_statistics():
    """Render the completed BCF vs ACF paired-statistics dashboard."""
    st.subheader("Paired statistics, effect size, and FDR")
    st.caption(
        "This section evaluates within-subject BCF-to-ACF changes using paired "
        "tests, Cohen's dz, confidence intervals for mean change, and "
        "FDR-adjusted p-values."
    )

    try:
        dataframe = load_bcf_acf_paired_statistics()
    except (
        FileNotFoundError,
        ValueError,
        KeyError,
        pd.errors.ParserError,
    ) as error:
        st.error(str(error))
        st.info(
            "Keep 'paired_statistics_master BCF ACF.zip' beside app.py. The "
            "dashboard can also read the five extracted CSV files from "
            "paired_statistics_master/, data/, or assets/data/."
        )
        return

    st.success(
        f"**Key finding.** {get_bcf_acf_paired_key_finding(dataframe)} "
        "Nominal p-values should not be described as confirmed findings because "
        "none of the results survived multiplicity correction."
    )

    filter_1, filter_2 = st.columns(2)
    with filter_1:
        selected_band = st.selectbox(
            "Frequency band",
            BCF_ACF_BAND_ORDER,
            index=0,
            key="bcf_acf_paired_band",
        )
    with filter_2:
        selected_test = st.selectbox(
            "Statistical test for p-value and FDR display",
            list(BCF_ACF_TEST_OPTIONS),
            index=0,
            key="bcf_acf_paired_test",
        )

    summary = get_bcf_acf_paired_band_statistics(
        dataframe, selected_band, selected_test
    )
    band_data = summary["data"]

    metric_1, metric_2, metric_3, metric_4, metric_5 = st.columns(5)
    metric_1.metric("Comparisons Tested", summary["total"])
    metric_2.metric(
        "Nominal p < 0.05",
        f"{summary['nominal_significant']} / {summary['total']}",
    )
    metric_3.metric(
        "Significant After FDR",
        f"{summary['fdr_significant']} / {summary['total']}",
    )
    metric_4.metric(
        "Largest |Cohen's dz|",
        f"{abs(summary['strongest']['cohens_dz']):.3f}",
    )
    metric_5.metric(
        "Smallest FDR q",
        format_bcf_acf_p_value(
            summary["smallest_q"][summary["q_column"]]
        ),
    )

    st.info(
        f"**{selected_band} interpretation.** "
        f"{get_bcf_acf_paired_band_summary(dataframe, selected_band, selected_test)}"
    )

    effect_figure = build_bcf_acf_effect_size_figure(
        band_data, selected_band
    )
    st.plotly_chart(
        effect_figure,
        use_container_width=True,
        key="bcf_acf_cohens_dz_plot",
    )
    st.caption(
        "Positive Cohen's dz values indicate higher measurements under ACF; "
        "negative values indicate lower measurements under ACF. The source CSV "
        "does not contain confidence intervals for Cohen's dz, so the plot shows "
        "effect-size point estimates only."
    )

    heatmap_figure = build_bcf_acf_fdr_heatmap(
        band_data,
        selected_band,
        selected_test,
        summary["q_column"],
    )
    st.plotly_chart(
        heatmap_figure,
        use_container_width=True,
        key="bcf_acf_fdr_heatmap",
    )
    st.caption(
        "Lower FDR q-values indicate stronger multiplicity-adjusted evidence. "
        "An asterisk marks q < 0.05; no cells meet that threshold in the current "
        "BCF vs ACF files."
    )

    st.markdown("#### Results with the smallest FDR-adjusted p-values")
    display_table = prepare_bcf_acf_paired_display_table(
        band_data,
        summary["q_column"],
        summary["p_column"],
    )
    st.dataframe(
        display_table.head(8),
        use_container_width=True,
        hide_index=True,
    )

    with st.expander("View summaries for all frequency bands", expanded=False):
        for band in BCF_ACF_BAND_ORDER:
            st.markdown(
                f"**{band}**  \n"
                f"{get_bcf_acf_paired_band_summary(dataframe, band, selected_test)}"
            )

    with st.expander("View complete paired-statistics table", expanded=False):
        st.dataframe(
            display_table,
            use_container_width=True,
            hide_index=True,
        )
        download_columns = [
            "Analysis_Band",
            "channel",
            "feature_band",
            "feature_type",
            "feature",
            "n_subjects",
            "mean_change",
            "median_change",
            "ci95_lower",
            "ci95_upper",
            "direction",
            "cohens_dz",
            "effect_size_interpretation",
            "t_statistic",
            "p_ttest",
            "wilcoxon_statistic",
            "p_wilcoxon",
            "p_fdr_ttest",
            "p_fdr_wilcoxon",
        ]
        st.download_button(
            "Download selected band statistics (CSV)",
            data=band_data[download_columns].to_csv(index=False).encode("utf-8"),
            file_name=f"BCF_ACF_Paired_Statistics_{selected_band}.csv",
            mime="text/csv",
            key="bcf_acf_paired_download",
        )

    with st.expander("Statistical and data notes", expanded=False):
        st.markdown(
            """
- Each band file contains 24 comparisons: four EEG channels multiplied by six features.
- FDR correction is interpreted within each band file. P-values and FDR-adjusted p-values are not averaged across bands.
- Entropy and the three Hjorth features are broadband measurements repeated in each band file. Select one band at a time to avoid treating these repetitions as independent tests.
- Cohen's dz reports paired effect magnitude. Its sign follows ACF minus BCF.
- The 95% confidence intervals in the table apply to the mean change, not to Cohen's dz.
- A nominal p-value below 0.05 is not considered an FDR-corrected significant result when its q-value is 0.05 or greater.
            """
        )


def find_bf_af_paired_statistics_source():
    """Find either the BF vs AF source ZIP or its five extracted CSV files."""
    for zip_path in BF_AF_PAIRED_STATISTICS_ZIPS:
        if zip_path.exists():
            return "zip", zip_path

    csv_files = []
    for directory in BF_AF_PAIRED_STATISTICS_DIRECTORIES:
        if not directory.exists():
            continue
        csv_files.extend(
            directory.rglob("PairedStatistics_EffectSize_FDR_*_BF_vs_AF.csv")
        )

    unique_files = sorted({path.resolve() for path in csv_files})
    if unique_files:
        return "csv", unique_files
    return None, None


@st.cache_data
def load_bf_af_paired_statistics():
    """Load and validate the five BF vs AF paired-statistics tables."""
    source_type, source = find_bf_af_paired_statistics_source()
    if source is None:
        raise FileNotFoundError(
            "BF vs AF paired-statistics data were not found. Keep "
            "'paired_statistics_master BF AF.zip' beside app.py, or extract "
            "the five PairedStatistics_EffectSize_FDR CSV files into "
            "paired_statistics_master/, data/, or assets/data/."
        )

    frames = []

    if source_type == "zip":
        with ZipFile(source) as archive:
            csv_names = [
                name
                for name in archive.namelist()
                if name.lower().endswith(".csv")
                and "pairedstatistics_effectsize_fdr" in name.lower()
                and "_bf_vs_af" in Path(name).name.lower()
            ]

            for csv_name in csv_names:
                band = get_bcf_acf_paired_band_from_name(csv_name)
                if band is None:
                    continue
                with archive.open(csv_name) as csv_file:
                    dataframe = pd.read_csv(csv_file)
                dataframe.insert(0, "Analysis_Band", band)
                dataframe["Source_File"] = Path(csv_name).name
                frames.append(dataframe)
    else:
        for csv_path in source:
            band = get_bcf_acf_paired_band_from_name(csv_path.name)
            if band is None:
                continue
            dataframe = pd.read_csv(csv_path)
            dataframe.insert(0, "Analysis_Band", band)
            dataframe["Source_File"] = csv_path.name
            frames.append(dataframe)

    if not frames:
        raise FileNotFoundError(
            "No BF vs AF PairedStatistics_EffectSize_FDR CSV files were found "
            "in the configured source."
        )

    available_bands = {
        frame["Analysis_Band"].iloc[0] for frame in frames
    }
    missing_bands = [
        band for band in BF_AF_BAND_ORDER if band not in available_bands
    ]
    if missing_bands:
        raise ValueError(
            "The BF vs AF paired-statistics source is incomplete. Missing "
            "bands: " + ", ".join(missing_bands)
        )

    validated_frames = []
    numeric_columns = [
        "n_subjects",
        "mean_change",
        "ci95_lower",
        "ci95_upper",
        "cohens_dz",
        "t_statistic",
        "p_ttest",
        "wilcoxon_statistic",
        "p_wilcoxon",
        "p_fdr_ttest",
        "p_fdr_wilcoxon",
    ]

    for dataframe in frames:
        missing_columns = BCF_ACF_PAIRED_REQUIRED_COLUMNS.difference(
            dataframe.columns
        )
        if missing_columns:
            raise ValueError(
                f"{dataframe['Source_File'].iloc[0]} is missing required "
                "columns: " + ", ".join(sorted(missing_columns))
            )

        dataframe = dataframe.copy()
        dataframe["Analysis_Band"] = (
            dataframe["Analysis_Band"].astype(str).str.strip().str.title()
        )
        dataframe["channel"] = (
            dataframe["channel"].astype(str).str.strip().str.upper()
        )
        dataframe["feature"] = dataframe["feature"].astype(str).str.strip()
        dataframe["feature_type"] = (
            dataframe["feature_type"].astype(str).str.strip().str.upper()
        )
        dataframe["effect_size_interpretation"] = (
            dataframe["effect_size_interpretation"]
            .astype(str)
            .str.strip()
            .str.title()
        )

        for column in numeric_columns:
            dataframe[column] = pd.to_numeric(
                dataframe[column], errors="coerce"
            )

        required_numeric = [
            "n_subjects",
            "mean_change",
            "cohens_dz",
            "p_ttest",
            "p_wilcoxon",
            "p_fdr_ttest",
            "p_fdr_wilcoxon",
        ]
        if dataframe[required_numeric].isna().any().any():
            raise ValueError(
                f"{dataframe['Source_File'].iloc[0]} contains missing or "
                "non-numeric values in required statistical columns."
            )

        validated_frames.append(dataframe)

    master = pd.concat(validated_frames, ignore_index=True)
    duplicate_rows = master.duplicated(
        ["Analysis_Band", "channel", "feature"], keep=False
    )
    if duplicate_rows.any():
        raise ValueError(
            "Duplicate band-channel-feature rows were found in the BF vs AF "
            "paired-statistics source."
        )

    master["Analysis_Band"] = pd.Categorical(
        master["Analysis_Band"],
        categories=BF_AF_BAND_ORDER,
        ordered=True,
    )
    return master.sort_values(
        ["Analysis_Band", "channel", "feature"]
    ).reset_index(drop=True)


def get_bf_af_paired_key_finding(dataframe):
    """Create the BF vs AF cross-band key finding from the source CSV values."""
    t_nominal_by_band = {}
    w_nominal_by_band = {}
    t_fdr_total = 0
    w_fdr_total = 0

    for band in BF_AF_BAND_ORDER:
        band_data = dataframe[
            dataframe["Analysis_Band"].astype(str) == band
        ]
        t_nominal_by_band[band] = int((band_data["p_ttest"] < 0.05).sum())
        w_nominal_by_band[band] = int((band_data["p_wilcoxon"] < 0.05).sum())
        t_fdr_total += int((band_data["p_fdr_ttest"] < 0.05).sum())
        w_fdr_total += int((band_data["p_fdr_wilcoxon"] < 0.05).sum())

    strongest = dataframe.loc[dataframe["cohens_dz"].abs().idxmax()]
    gamma = dataframe[
        dataframe["Analysis_Band"].astype(str) == "Gamma"
    ]
    gamma_nominal = gamma.loc[gamma["p_wilcoxon"].idxmin()]

    return (
        "Each frequency-band file contains 24 channel-feature comparisons. "
        "The paired t-test identified no unadjusted p-values below 0.05. "
        f"The Wilcoxon test identified {sum(w_nominal_by_band.values())} "
        "nominal result below 0.05: "
        f"{gamma_nominal['feature']} at {gamma_nominal['channel']} in Gamma "
        f"(p = {gamma_nominal['p_wilcoxon']:.6f}, "
        f"FDR q = {gamma_nominal['p_fdr_wilcoxon']:.6f}). "
        f"After FDR correction, {t_fdr_total} t-test results and "
        f"{w_fdr_total} Wilcoxon results remained significant. The largest "
        f"absolute effect was {strongest['feature']} at "
        f"{strongest['channel']} in {strongest['Analysis_Band']} "
        f"(Cohen's dz = {strongest['cohens_dz']:+.3f})."
    )


def render_bf_af_paired_statistics():
    """Render the completed BF vs AF paired-statistics dashboard."""
    st.subheader("Paired statistics, effect size, and FDR")
    st.caption(
        "This section evaluates within-subject BF-to-AF changes using paired "
        "tests, Cohen's dz, confidence intervals for mean change, and "
        "FDR-adjusted p-values."
    )

    try:
        dataframe = load_bf_af_paired_statistics()
    except (
        FileNotFoundError,
        ValueError,
        KeyError,
        pd.errors.ParserError,
    ) as error:
        st.error(str(error))
        st.info(
            "Keep 'paired_statistics_master BF AF.zip' beside app.py. The "
            "dashboard can also read the five extracted CSV files from "
            "paired_statistics_master/, data/, or assets/data/."
        )
        return

    st.success(
        f"**Key finding.** {get_bf_af_paired_key_finding(dataframe)} "
        "The Gamma Wilcoxon result is nominal only and should not be described "
        "as significant after correction."
    )

    filter_1, filter_2 = st.columns(2)
    with filter_1:
        selected_band = st.selectbox(
            "Frequency band",
            BF_AF_BAND_ORDER,
            index=0,
            key="bf_af_paired_band",
        )
    with filter_2:
        selected_test = st.selectbox(
            "Statistical test for p-value and FDR display",
            list(BCF_ACF_TEST_OPTIONS),
            index=0,
            key="bf_af_paired_test",
        )

    summary = get_bcf_acf_paired_band_statistics(
        dataframe, selected_band, selected_test
    )
    band_data = summary["data"]

    metric_1, metric_2, metric_3, metric_4, metric_5 = st.columns(5)
    metric_1.metric("Comparisons Tested", summary["total"])
    metric_2.metric(
        "Nominal p < 0.05",
        f"{summary['nominal_significant']} / {summary['total']}",
    )
    metric_3.metric(
        "Significant After FDR",
        f"{summary['fdr_significant']} / {summary['total']}",
    )
    metric_4.metric(
        "Largest |Cohen's dz|",
        f"{abs(summary['strongest']['cohens_dz']):.3f}",
    )
    metric_5.metric(
        "Smallest FDR q",
        format_bcf_acf_p_value(
            summary["smallest_q"][summary["q_column"]]
        ),
    )

    st.info(
        f"**{selected_band} interpretation.** "
        f"{get_bcf_acf_paired_band_summary(dataframe, selected_band, selected_test)}"
    )

    effect_figure = build_bcf_acf_effect_size_figure(
        band_data, selected_band
    )
    st.plotly_chart(
        effect_figure,
        use_container_width=True,
        key="bf_af_cohens_dz_plot",
    )
    st.caption(
        "Positive Cohen's dz values indicate higher measurements under AF; "
        "negative values indicate lower measurements under AF. The source CSV "
        "does not contain confidence intervals for Cohen's dz, so the plot "
        "shows effect-size point estimates only."
    )

    heatmap_figure = build_bcf_acf_fdr_heatmap(
        band_data,
        selected_band,
        selected_test,
        summary["q_column"],
    )
    st.plotly_chart(
        heatmap_figure,
        use_container_width=True,
        key="bf_af_fdr_heatmap",
    )
    st.caption(
        "Lower FDR q-values indicate stronger multiplicity-adjusted evidence. "
        "An asterisk marks q < 0.05; no cells meet that threshold in the "
        "current BF vs AF files."
    )

    st.markdown("#### Results with the smallest FDR-adjusted p-values")
    display_table = prepare_bcf_acf_paired_display_table(
        band_data,
        summary["q_column"],
        summary["p_column"],
    )
    st.dataframe(
        display_table.head(8),
        use_container_width=True,
        hide_index=True,
    )

    with st.expander("View summaries for all frequency bands", expanded=False):
        for band in BF_AF_BAND_ORDER:
            st.markdown(
                f"**{band}**  \n"
                f"{get_bcf_acf_paired_band_summary(dataframe, band, selected_test)}"
            )

    with st.expander("View complete paired-statistics table", expanded=False):
        st.dataframe(
            display_table,
            use_container_width=True,
            hide_index=True,
        )
        download_columns = [
            "Analysis_Band",
            "channel",
            "feature_band",
            "feature_type",
            "feature",
            "n_subjects",
            "mean_change",
            "median_change",
            "ci95_lower",
            "ci95_upper",
            "direction",
            "cohens_dz",
            "effect_size_interpretation",
            "t_statistic",
            "p_ttest",
            "wilcoxon_statistic",
            "p_wilcoxon",
            "p_fdr_ttest",
            "p_fdr_wilcoxon",
        ]
        st.download_button(
            "Download selected band statistics (CSV)",
            data=band_data[download_columns].to_csv(index=False).encode("utf-8"),
            file_name=f"BF_AF_Paired_Statistics_{selected_band}.csv",
            mime="text/csv",
            key="bf_af_paired_download",
        )

    with st.expander("Statistical and data notes", expanded=False):
        st.markdown(
            """
- Each band file contains 24 comparisons: four EEG channels multiplied by six features.
- FDR correction is interpreted within each band file. P-values and FDR-adjusted p-values are not averaged across bands.
- Entropy and the three Hjorth features are broadband measurements repeated in each band file. Select one band at a time to avoid treating these repetitions as independent tests.
- Cohen's dz reports paired effect magnitude. Its sign follows AF minus BF.
- The 95% confidence intervals in the table apply to the mean change, not to Cohen's dz.
- Gamma Band Power at AF7 has a nominal Wilcoxon p-value of 0.027344, but its FDR-adjusted q-value is 0.656250.
- A nominal p-value below 0.05 is not considered an FDR-corrected significant result when its q-value is 0.05 or greater.
            """
        )


def find_bcm_acm_paired_statistics_source():
    """Find either the BCM vs ACM source ZIP or its five extracted CSV files."""
    for zip_path in BCM_ACM_PAIRED_STATISTICS_ZIPS:
        if zip_path.exists():
            return "zip", zip_path

    csv_files = []
    for directory in BCM_ACM_PAIRED_STATISTICS_DIRECTORIES:
        if not directory.exists():
            continue
        csv_files.extend(
            directory.rglob(
                "PairedStatistics_EffectSize_FDR_*_BCM_vs_ACM.csv"
            )
        )

    unique_files = sorted({path.resolve() for path in csv_files})
    if unique_files:
        return "csv", unique_files
    return None, None


@st.cache_data
def load_bcm_acm_paired_statistics():
    """Load and validate the five BCM vs ACM paired-statistics tables."""
    source_type, source = find_bcm_acm_paired_statistics_source()
    if source is None:
        raise FileNotFoundError(
            "BCM vs ACM paired-statistics data were not found. Keep "
            "'paired_statistics_master BCM ACM.zip' beside app.py, or extract "
            "the five PairedStatistics_EffectSize_FDR CSV files into "
            "paired_statistics_master/, data/, or assets/data/."
        )

    frames = []

    if source_type == "zip":
        with ZipFile(source) as archive:
            csv_names = [
                name
                for name in archive.namelist()
                if name.lower().endswith(".csv")
                and "pairedstatistics_effectsize_fdr" in name.lower()
                and "_bcm_vs_acm" in Path(name).name.lower()
            ]

            for csv_name in csv_names:
                band = get_bcf_acf_paired_band_from_name(csv_name)
                if band is None:
                    continue
                with archive.open(csv_name) as csv_file:
                    dataframe = pd.read_csv(csv_file)
                dataframe.insert(0, "Analysis_Band", band)
                dataframe["Source_File"] = Path(csv_name).name
                frames.append(dataframe)
    else:
        for csv_path in source:
            band = get_bcf_acf_paired_band_from_name(csv_path.name)
            if band is None:
                continue
            dataframe = pd.read_csv(csv_path)
            dataframe.insert(0, "Analysis_Band", band)
            dataframe["Source_File"] = csv_path.name
            frames.append(dataframe)

    if not frames:
        raise FileNotFoundError(
            "No BCM vs ACM PairedStatistics_EffectSize_FDR CSV files were "
            "found in the configured source."
        )

    available_bands = {
        frame["Analysis_Band"].iloc[0] for frame in frames
    }
    missing_bands = [
        band for band in BCM_ACM_BAND_ORDER if band not in available_bands
    ]
    if missing_bands:
        raise ValueError(
            "The BCM vs ACM paired-statistics source is incomplete. Missing "
            "bands: " + ", ".join(missing_bands)
        )

    validated_frames = []
    numeric_columns = [
        "n_subjects",
        "mean_change",
        "ci95_lower",
        "ci95_upper",
        "cohens_dz",
        "t_statistic",
        "p_ttest",
        "wilcoxon_statistic",
        "p_wilcoxon",
        "p_fdr_ttest",
        "p_fdr_wilcoxon",
    ]

    for dataframe in frames:
        missing_columns = BCF_ACF_PAIRED_REQUIRED_COLUMNS.difference(
            dataframe.columns
        )
        if missing_columns:
            raise ValueError(
                f"{dataframe['Source_File'].iloc[0]} is missing required "
                "columns: " + ", ".join(sorted(missing_columns))
            )

        dataframe = dataframe.copy()
        dataframe["Analysis_Band"] = (
            dataframe["Analysis_Band"].astype(str).str.strip().str.title()
        )
        dataframe["channel"] = (
            dataframe["channel"].astype(str).str.strip().str.upper()
        )
        dataframe["feature"] = dataframe["feature"].astype(str).str.strip()
        dataframe["feature_type"] = (
            dataframe["feature_type"].astype(str).str.strip().str.upper()
        )
        dataframe["effect_size_interpretation"] = (
            dataframe["effect_size_interpretation"]
            .astype(str)
            .str.strip()
            .str.title()
        )

        for column in numeric_columns:
            dataframe[column] = pd.to_numeric(
                dataframe[column], errors="coerce"
            )

        required_numeric = [
            "n_subjects",
            "mean_change",
            "cohens_dz",
            "p_ttest",
            "p_wilcoxon",
            "p_fdr_ttest",
            "p_fdr_wilcoxon",
        ]
        if dataframe[required_numeric].isna().any().any():
            raise ValueError(
                f"{dataframe['Source_File'].iloc[0]} contains missing or "
                "non-numeric values in required statistical columns."
            )

        validated_frames.append(dataframe)

    master = pd.concat(validated_frames, ignore_index=True)
    duplicate_rows = master.duplicated(
        ["Analysis_Band", "channel", "feature"], keep=False
    )
    if duplicate_rows.any():
        raise ValueError(
            "Duplicate band-channel-feature rows were found in the BCM vs ACM "
            "paired-statistics source."
        )

    rows_per_band = master.groupby("Analysis_Band").size()
    incomplete_bands = rows_per_band[rows_per_band != 24]
    if not incomplete_bands.empty:
        details = ", ".join(
            f"{band}: {count}" for band, count in incomplete_bands.items()
        )
        raise ValueError(
            "Each BCM vs ACM band must contain 24 channel-feature "
            f"comparisons. Found {details}."
        )

    master["Analysis_Band"] = pd.Categorical(
        master["Analysis_Band"],
        categories=BCM_ACM_BAND_ORDER,
        ordered=True,
    )
    return master.sort_values(
        ["Analysis_Band", "channel", "feature"]
    ).reset_index(drop=True)


def get_bcm_acm_paired_key_finding(dataframe):
    """Create the BCM vs ACM cross-band key finding from source values."""
    t_nominal_counts = []
    w_nominal_counts = []
    t_fdr_count = 0
    w_fdr_count = 0

    for band in BCM_ACM_BAND_ORDER:
        band_data = dataframe[
            dataframe["Analysis_Band"].astype(str) == band
        ]
        t_nominal_counts.append(int((band_data["p_ttest"] < 0.05).sum()))
        w_nominal_counts.append(int((band_data["p_wilcoxon"] < 0.05).sum()))
        t_fdr_count += int((band_data["p_fdr_ttest"] < 0.05).sum())
        w_fdr_count += int((band_data["p_fdr_wilcoxon"] < 0.05).sum())

    strongest = dataframe.loc[dataframe["cohens_dz"].abs().idxmax()]
    t_range = (
        str(t_nominal_counts[0])
        if len(set(t_nominal_counts)) == 1
        else f"{min(t_nominal_counts)}-{max(t_nominal_counts)}"
    )
    w_range = (
        str(w_nominal_counts[0])
        if len(set(w_nominal_counts)) == 1
        else f"{min(w_nominal_counts)}-{max(w_nominal_counts)}"
    )
    t_result_word = "result" if t_range == "1" else "results"
    w_result_word = "result" if w_range == "1" else "results"

    return (
        "Each frequency-band file contains 24 channel-feature comparisons. "
        f"The paired t-test identified {t_range} nominal {t_result_word} with "
        f"p < 0.05 per band, and the Wilcoxon test identified {w_range} "
        f"nominal {w_result_word} per band. "
        f"After FDR correction, {t_fdr_count} t-test results and "
        f"{w_fdr_count} Wilcoxon results remained significant across the five "
        "band-specific correction families. The largest absolute effect was "
        f"{strongest['feature']} at {strongest['channel']} "
        f"(Cohen's dz = {strongest['cohens_dz']:+.3f}). Because this is a "
        "broadband Hjorth feature repeated in every band file, it represents "
        "one shared comparison rather than five independent findings."
    )


def render_bcm_acm_paired_statistics():
    """Render the completed BCM vs ACM paired-statistics dashboard."""
    st.subheader("Paired statistics, effect size, and FDR")
    st.caption(
        "This section evaluates within-subject BCM-to-ACM changes using paired "
        "tests, Cohen's dz, confidence intervals for mean change, and "
        "FDR-adjusted p-values."
    )

    try:
        dataframe = load_bcm_acm_paired_statistics()
    except (
        FileNotFoundError,
        ValueError,
        KeyError,
        pd.errors.ParserError,
    ) as error:
        st.error(str(error))
        st.info(
            "Keep 'paired_statistics_master BCM ACM.zip' beside app.py. The "
            "dashboard can also read the five extracted CSV files from "
            "paired_statistics_master/, data/, or assets/data/."
        )
        return

    st.success(
        f"**Key finding.** {get_bcm_acm_paired_key_finding(dataframe)} "
        "The nominal TP9 Hjorth Complexity result did not survive FDR "
        "correction and must not be described as FDR-significant."
    )

    filter_1, filter_2 = st.columns(2)
    with filter_1:
        selected_band = st.selectbox(
            "Frequency band",
            BCM_ACM_BAND_ORDER,
            index=0,
            key="bcm_acm_paired_band",
        )
    with filter_2:
        selected_test = st.selectbox(
            "Statistical test for p-value and FDR display",
            list(BCF_ACF_TEST_OPTIONS),
            index=0,
            key="bcm_acm_paired_test",
        )

    summary = get_bcf_acf_paired_band_statistics(
        dataframe, selected_band, selected_test
    )
    band_data = summary["data"]

    metric_1, metric_2, metric_3, metric_4, metric_5 = st.columns(5)
    metric_1.metric("Comparisons Tested", summary["total"])
    metric_2.metric(
        "Nominal p < 0.05",
        f"{summary['nominal_significant']} / {summary['total']}",
    )
    metric_3.metric(
        "Significant After FDR",
        f"{summary['fdr_significant']} / {summary['total']}",
    )
    metric_4.metric(
        "Largest |Cohen's dz|",
        f"{abs(summary['strongest']['cohens_dz']):.3f}",
    )
    metric_5.metric(
        "Smallest FDR q",
        format_bcf_acf_p_value(
            summary["smallest_q"][summary["q_column"]]
        ),
    )

    st.info(
        f"**{selected_band} interpretation.** "
        f"{get_bcf_acf_paired_band_summary(dataframe, selected_band, selected_test)}"
    )

    effect_figure = build_bcf_acf_effect_size_figure(
        band_data, selected_band
    )
    st.plotly_chart(
        effect_figure,
        use_container_width=True,
        key="bcm_acm_cohens_dz_plot",
    )
    st.caption(
        "Positive Cohen's dz values indicate higher measurements under ACM; "
        "negative values indicate lower measurements under ACM. The source CSV "
        "does not contain confidence intervals for Cohen's dz, so the plot "
        "shows effect-size point estimates only."
    )

    heatmap_figure = build_bcf_acf_fdr_heatmap(
        band_data,
        selected_band,
        selected_test,
        summary["q_column"],
    )
    st.plotly_chart(
        heatmap_figure,
        use_container_width=True,
        key="bcm_acm_fdr_heatmap",
    )
    st.caption(
        "Lower FDR q-values indicate stronger multiplicity-adjusted evidence. "
        "An asterisk marks q < 0.05; no cells meet that threshold in the "
        "current BCM vs ACM files."
    )

    st.markdown("#### Results with the smallest FDR-adjusted p-values")
    display_table = prepare_bcf_acf_paired_display_table(
        band_data,
        summary["q_column"],
        summary["p_column"],
    )
    st.dataframe(
        display_table.head(8),
        use_container_width=True,
        hide_index=True,
    )

    with st.expander("View summaries for all frequency bands", expanded=False):
        for band in BCM_ACM_BAND_ORDER:
            st.markdown(
                f"**{band}**  \n"
                f"{get_bcf_acf_paired_band_summary(dataframe, band, selected_test)}"
            )

    with st.expander("View complete paired-statistics table", expanded=False):
        st.dataframe(
            display_table,
            use_container_width=True,
            hide_index=True,
        )
        download_columns = [
            "Analysis_Band",
            "channel",
            "feature_band",
            "feature_type",
            "feature",
            "n_subjects",
            "mean_change",
            "median_change",
            "ci95_lower",
            "ci95_upper",
            "direction",
            "cohens_dz",
            "effect_size_interpretation",
            "t_statistic",
            "p_ttest",
            "wilcoxon_statistic",
            "p_wilcoxon",
            "p_fdr_ttest",
            "p_fdr_wilcoxon",
        ]
        st.download_button(
            "Download selected band statistics (CSV)",
            data=band_data[download_columns].to_csv(index=False).encode("utf-8"),
            file_name=f"BCM_ACM_Paired_Statistics_{selected_band}.csv",
            mime="text/csv",
            key="bcm_acm_paired_download",
        )

    with st.expander("Statistical and data notes", expanded=False):
        st.markdown(
            """
- Each band file contains 24 comparisons: four EEG channels multiplied by six features.
- FDR correction is interpreted within each band file. P-values and FDR-adjusted p-values are not averaged across bands.
- Entropy and the three Hjorth features are broadband measurements repeated in each band file. Select one band at a time to avoid treating these repetitions as independent tests.
- Cohen's dz reports paired effect magnitude. Its sign follows ACM minus BCM.
- The 95% confidence intervals in the table apply to the mean change, not to Cohen's dz.
- Hjorth Complexity at TP9 has paired t-test p = 0.008642 and FDR q = 0.207402; its Wilcoxon p = 0.013672 and FDR q = 0.328125.
- A nominal p-value below 0.05 is not considered an FDR-corrected significant result when its q-value is 0.05 or greater.
            """
        )


def find_bm_am_paired_statistics_source():
    """Find either the BM vs AM source ZIP or its five extracted CSV files."""
    for zip_path in BM_AM_PAIRED_STATISTICS_ZIPS:
        if zip_path.exists():
            return "zip", zip_path

    csv_files = []
    for directory in BM_AM_PAIRED_STATISTICS_DIRECTORIES:
        if not directory.exists():
            continue
        csv_files.extend(
            directory.rglob("PairedStatistics_EffectSize_FDR_*_BM_vs_AM.csv")
        )

    unique_files = sorted({path.resolve() for path in csv_files})
    if unique_files:
        return "csv", unique_files
    return None, None


@st.cache_data
def load_bm_am_paired_statistics():
    """Load and validate the five BM vs AM paired-statistics tables."""
    source_type, source = find_bm_am_paired_statistics_source()
    if source is None:
        raise FileNotFoundError(
            "BM vs AM paired-statistics data were not found. Keep "
            "'paired_statistics_master BM AM.zip' beside app.py, or extract "
            "the five PairedStatistics_EffectSize_FDR CSV files into "
            "paired_statistics_master/, data/, or assets/data/."
        )

    frames = []

    if source_type == "zip":
        with ZipFile(source) as archive:
            csv_names = [
                name
                for name in archive.namelist()
                if name.lower().endswith(".csv")
                and "pairedstatistics_effectsize_fdr" in name.lower()
                and "_bm_vs_am" in Path(name).name.lower()
            ]

            for csv_name in csv_names:
                band = get_bcf_acf_paired_band_from_name(csv_name)
                if band is None:
                    continue
                with archive.open(csv_name) as csv_file:
                    dataframe = pd.read_csv(csv_file)
                dataframe.insert(0, "Analysis_Band", band)
                dataframe["Source_File"] = Path(csv_name).name
                frames.append(dataframe)
    else:
        for csv_path in source:
            band = get_bcf_acf_paired_band_from_name(csv_path.name)
            if band is None:
                continue
            dataframe = pd.read_csv(csv_path)
            dataframe.insert(0, "Analysis_Band", band)
            dataframe["Source_File"] = csv_path.name
            frames.append(dataframe)

    if not frames:
        raise FileNotFoundError(
            "No BM vs AM PairedStatistics_EffectSize_FDR CSV files were found "
            "in the configured source."
        )

    available_bands = {
        frame["Analysis_Band"].iloc[0] for frame in frames
    }
    missing_bands = [
        band for band in BM_AM_BAND_ORDER if band not in available_bands
    ]
    if missing_bands:
        raise ValueError(
            "The BM vs AM paired-statistics source is incomplete. Missing "
            "bands: " + ", ".join(missing_bands)
        )

    validated_frames = []
    numeric_columns = [
        "n_subjects",
        "mean_change",
        "ci95_lower",
        "ci95_upper",
        "cohens_dz",
        "t_statistic",
        "p_ttest",
        "wilcoxon_statistic",
        "p_wilcoxon",
        "p_fdr_ttest",
        "p_fdr_wilcoxon",
    ]

    for dataframe in frames:
        # The supplied Beta table omits the two test-statistic columns while
        # retaining its raw p-values, FDR q-values, confidence intervals, and
        # effect sizes. Preserve that source limitation explicitly as N/A.
        for optional_column in ["t_statistic", "wilcoxon_statistic"]:
            if optional_column not in dataframe.columns:
                dataframe[optional_column] = pd.NA

        missing_columns = BCF_ACF_PAIRED_REQUIRED_COLUMNS.difference(
            dataframe.columns
        )
        if missing_columns:
            raise ValueError(
                f"{dataframe['Source_File'].iloc[0]} is missing required "
                "columns: " + ", ".join(sorted(missing_columns))
            )

        dataframe = dataframe.copy()
        dataframe["Analysis_Band"] = (
            dataframe["Analysis_Band"].astype(str).str.strip().str.title()
        )
        dataframe["channel"] = (
            dataframe["channel"].astype(str).str.strip().str.upper()
        )
        dataframe["feature"] = dataframe["feature"].astype(str).str.strip()
        dataframe["feature_type"] = (
            dataframe["feature_type"].astype(str).str.strip().str.upper()
        )
        dataframe["effect_size_interpretation"] = (
            dataframe["effect_size_interpretation"]
            .astype(str)
            .str.strip()
            .str.title()
        )

        for column in numeric_columns:
            dataframe[column] = pd.to_numeric(
                dataframe[column], errors="coerce"
            )

        required_numeric = [
            "n_subjects",
            "mean_change",
            "cohens_dz",
            "p_ttest",
            "p_wilcoxon",
            "p_fdr_ttest",
            "p_fdr_wilcoxon",
        ]
        if dataframe[required_numeric].isna().any().any():
            raise ValueError(
                f"{dataframe['Source_File'].iloc[0]} contains missing or "
                "non-numeric values in required statistical columns."
            )

        validated_frames.append(dataframe)

    master = pd.concat(validated_frames, ignore_index=True)
    duplicate_rows = master.duplicated(
        ["Analysis_Band", "channel", "feature"], keep=False
    )
    if duplicate_rows.any():
        raise ValueError(
            "Duplicate band-channel-feature rows were found in the BM vs AM "
            "paired-statistics source."
        )

    rows_per_band = master.groupby("Analysis_Band").size()
    incomplete_bands = rows_per_band[rows_per_band != 24]
    if not incomplete_bands.empty:
        details = ", ".join(
            f"{band}: {count}" for band, count in incomplete_bands.items()
        )
        raise ValueError(
            "Each BM vs AM band must contain 24 channel-feature comparisons. "
            f"Found {details}."
        )

    master["Analysis_Band"] = pd.Categorical(
        master["Analysis_Band"],
        categories=BM_AM_BAND_ORDER,
        ordered=True,
    )
    return master.sort_values(
        ["Analysis_Band", "channel", "feature"]
    ).reset_index(drop=True)


def get_bm_am_paired_key_finding(dataframe):
    """Create the BM vs AM cross-band key finding from source values."""
    t_nominal_counts = []
    w_nominal_counts = []
    t_fdr_count = 0
    w_fdr_count = 0

    for band in BM_AM_BAND_ORDER:
        band_data = dataframe[
            dataframe["Analysis_Band"].astype(str) == band
        ]
        t_nominal_counts.append(int((band_data["p_ttest"] < 0.05).sum()))
        w_nominal_counts.append(int((band_data["p_wilcoxon"] < 0.05).sum()))
        t_fdr_count += int((band_data["p_fdr_ttest"] < 0.05).sum())
        w_fdr_count += int((band_data["p_fdr_wilcoxon"] < 0.05).sum())

    strongest = dataframe.loc[dataframe["cohens_dz"].abs().idxmax()]
    t_range = (
        str(t_nominal_counts[0])
        if len(set(t_nominal_counts)) == 1
        else f"{min(t_nominal_counts)}-{max(t_nominal_counts)}"
    )
    w_range = (
        str(w_nominal_counts[0])
        if len(set(w_nominal_counts)) == 1
        else f"{min(w_nominal_counts)}-{max(w_nominal_counts)}"
    )
    t_result_word = "result" if t_range == "1" else "results"
    w_result_word = "result" if w_range == "1" else "results"
    smallest_w_q = float(dataframe["p_fdr_wilcoxon"].min())

    return (
        "Each frequency-band file contains 24 channel-feature comparisons. "
        f"The paired t-test identified {t_range} nominal {t_result_word} with "
        f"p < 0.05 per band, while the Wilcoxon test identified {w_range} "
        f"nominal {w_result_word} per band. After FDR correction, "
        f"{t_fdr_count} t-test results and {w_fdr_count} Wilcoxon results "
        "remained significant across the five band-specific correction "
        "families. The largest absolute effect was "
        f"{strongest['feature']} at {strongest['channel']} in "
        f"{strongest['Analysis_Band']} (Cohen's dz = "
        f"{strongest['cohens_dz']:+.3f}). The smallest Wilcoxon FDR q-value "
        f"was {smallest_w_q:.4f}."
    )


def render_bm_am_paired_statistics():
    """Render the completed BM vs AM paired-statistics dashboard."""
    st.subheader("Paired statistics, effect size, and FDR")
    st.caption(
        "This section evaluates within-subject BM-to-AM changes using paired "
        "tests, Cohen's dz, confidence intervals for mean change, and "
        "FDR-adjusted p-values."
    )

    try:
        dataframe = load_bm_am_paired_statistics()
    except (
        FileNotFoundError,
        ValueError,
        KeyError,
        pd.errors.ParserError,
    ) as error:
        st.error(str(error))
        st.info(
            "Keep 'paired_statistics_master BM AM.zip' beside app.py. The "
            "dashboard can also read the five extracted CSV files from "
            "paired_statistics_master/, data/, or assets/data/."
        )
        return

    st.success(
        f"**Key finding.** {get_bm_am_paired_key_finding(dataframe)} "
        "The nominal Wilcoxon results did not survive FDR correction and "
        "must not be described as FDR-significant."
    )

    filter_1, filter_2 = st.columns(2)
    with filter_1:
        selected_band = st.selectbox(
            "Frequency band",
            BM_AM_BAND_ORDER,
            index=0,
            key="bm_am_paired_band",
        )
    with filter_2:
        selected_test = st.selectbox(
            "Statistical test for p-value and FDR display",
            list(BCF_ACF_TEST_OPTIONS),
            index=0,
            key="bm_am_paired_test",
        )

    summary = get_bcf_acf_paired_band_statistics(
        dataframe, selected_band, selected_test
    )
    band_data = summary["data"]

    metric_1, metric_2, metric_3, metric_4, metric_5 = st.columns(5)
    metric_1.metric("Comparisons Tested", summary["total"])
    metric_2.metric(
        "Nominal p < 0.05",
        f"{summary['nominal_significant']} / {summary['total']}",
    )
    metric_3.metric(
        "Significant After FDR",
        f"{summary['fdr_significant']} / {summary['total']}",
    )
    metric_4.metric(
        "Largest |Cohen's dz|",
        f"{abs(summary['strongest']['cohens_dz']):.3f}",
    )
    metric_5.metric(
        "Smallest FDR q",
        format_bcf_acf_p_value(
            summary["smallest_q"][summary["q_column"]]
        ),
    )

    st.info(
        f"**{selected_band} interpretation.** "
        f"{get_bcf_acf_paired_band_summary(dataframe, selected_band, selected_test)}"
    )

    effect_figure = build_bcf_acf_effect_size_figure(
        band_data, selected_band
    )
    st.plotly_chart(
        effect_figure,
        use_container_width=True,
        key="bm_am_cohens_dz_plot",
    )
    st.caption(
        "Positive Cohen's dz values indicate higher measurements under AM; "
        "negative values indicate lower measurements under AM. The source CSV "
        "does not contain confidence intervals for Cohen's dz, so the plot "
        "shows effect-size point estimates only."
    )

    heatmap_figure = build_bcf_acf_fdr_heatmap(
        band_data,
        selected_band,
        selected_test,
        summary["q_column"],
    )
    st.plotly_chart(
        heatmap_figure,
        use_container_width=True,
        key="bm_am_fdr_heatmap",
    )
    st.caption(
        "Lower FDR q-values indicate stronger multiplicity-adjusted evidence. "
        "An asterisk marks q < 0.05; no cells meet that threshold in the "
        "current BM vs AM files."
    )

    st.markdown("#### Results with the smallest FDR-adjusted p-values")
    display_table = prepare_bcf_acf_paired_display_table(
        band_data,
        summary["q_column"],
        summary["p_column"],
    )
    st.dataframe(
        display_table.head(8),
        use_container_width=True,
        hide_index=True,
    )

    with st.expander("View summaries for all frequency bands", expanded=False):
        for band in BM_AM_BAND_ORDER:
            st.markdown(
                f"**{band}**  \n"
                f"{get_bcf_acf_paired_band_summary(dataframe, band, selected_test)}"
            )

    with st.expander("View complete paired-statistics table", expanded=False):
        st.dataframe(
            display_table,
            use_container_width=True,
            hide_index=True,
        )
        download_columns = [
            "Analysis_Band",
            "channel",
            "feature_band",
            "feature_type",
            "feature",
            "n_subjects",
            "mean_change",
            "median_change",
            "ci95_lower",
            "ci95_upper",
            "direction",
            "cohens_dz",
            "effect_size_interpretation",
            "t_statistic",
            "p_ttest",
            "wilcoxon_statistic",
            "p_wilcoxon",
            "p_fdr_ttest",
            "p_fdr_wilcoxon",
        ]
        st.download_button(
            "Download selected band statistics (CSV)",
            data=band_data[download_columns].to_csv(index=False).encode("utf-8"),
            file_name=f"BM_AM_Paired_Statistics_{selected_band}.csv",
            mime="text/csv",
            key="bm_am_paired_download",
        )

    with st.expander("Statistical and data notes", expanded=False):
        st.markdown(
            """
- Each band file contains 24 comparisons: four EEG channels multiplied by six features.
- FDR correction is interpreted within each band file. P-values and FDR-adjusted p-values are not averaged across bands.
- Entropy and the three Hjorth features are broadband measurements repeated in each band file. Select one band at a time to avoid treating these repetitions as independent tests.
- Cohen's dz reports paired effect magnitude. Its sign follows AM minus BM.
- The 95% confidence intervals in the table apply to the mean change, not to Cohen's dz.
- The paired t-test has no nominal p-values below 0.05 in any band. Wilcoxon has 2-4 nominal results per band, but none remains significant after FDR correction.
- In Delta, Hjorth Activity at TP10 and Delta Band Power at AF8 share the smallest Wilcoxon FDR q-value (q = 0.117188).
- A nominal p-value below 0.05 is not considered an FDR-corrected significant result when its q-value is 0.05 or greater.
            """
        )


def render_analysis_placeholder(title, scope, description, planned_outputs):
    """Render a consistent insertion point for analysis results not yet linked to the app."""
    st.subheader(title)
    with st.container(border=True):
        st.info(f"The {scope} analysis output has not been connected to this dashboard yet.")
        st.write(description)

    with st.expander("Planned outputs", expanded=False):
        for output in planned_outputs:
            st.markdown(f"- {output}")


def render_subject_10_analysis(comparison_name, test_results=None, train_results=None):
    """Render the six-part statistical and synthetic analysis workspace."""
    st.subheader(f"Analysis: {comparison_name}")
    st.caption(
        "Classification accuracy remains in Results. This workspace is reserved for "
        "pre-post statistics and real-versus-synthetic validation."
    )

    (
        subject_level_tab,
        paired_statistics_tab,
        pre_post_visuals_tab,
        synthetic_quality_tab,
        similarity_tab,
        synthetic_visuals_tab,
    ) = st.tabs(
        [
            "Subject-Level Analysis",
            "Paired Statistics",
            "Pre-Post Visualizations",
            "Synthetic Feature Quality",
            "Quantitative Similarity",
            "Synthetic Visual Comparison",
        ]
    )

    with subject_level_tab:
        if comparison_name == "BCF vs ACF":
            render_bcf_acf_subject_level()
        elif comparison_name == "BF vs AF":
            render_bf_af_subject_level()
        elif comparison_name == "BCM vs ACM":
            render_bcm_acm_subject_level()
        elif comparison_name == "BM vs AM":
            render_bm_am_subject_level()
        else:
            render_analysis_placeholder(
                "Pre-post subject-level analysis",
                comparison_name,
                "This section will show the paired change for every subject while preserving "
                "the identity of each pre-post observation.",
                [
                    "Per-subject pre and post values",
                    "Absolute and percentage change (delta)",
                    "Direction of change for each subject",
                    "Responder and non-responder summary, when defined",
                ],
            )

    with paired_statistics_tab:
        if comparison_name == "BCF vs ACF":
            render_bcf_acf_paired_statistics()
        elif comparison_name == "BF vs AF":
            render_bf_af_paired_statistics()
        elif comparison_name == "BCM vs ACM":
            render_bcm_acm_paired_statistics()
        elif comparison_name == "BM vs AM":
            render_bm_am_paired_statistics()
        else:
            render_analysis_placeholder(
                "Paired statistics, effect size, and FDR",
                comparison_name,
                "This section will contain pairing-aware hypothesis tests and corrected "
                "significance results for the analysed EEG features.",
                [
                    "Paired statistical test and test statistic",
                    "Raw p-value and FDR-adjusted p-value",
                    "Effect size and confidence interval",
                    "Significant-feature summary",
                ],
            )

    with pre_post_visuals_tab:
        if comparison_name == "BCF vs ACF":
            render_bcf_acf_pre_post_visualizations()
        elif comparison_name == "BF vs AF":
            render_bf_af_pre_post_visualizations()
        elif comparison_name == "BCM vs ACM":
            render_bcm_acm_pre_post_visualizations()
        elif comparison_name == "BM vs AM":
            render_bm_am_pre_post_visualizations()
        else:
            render_analysis_placeholder(
                "Pre-post visualizations",
                comparison_name,
                "This section will visualize the direction, magnitude, and distribution of "
                "paired feature changes.",
                [
                    "Paired line or slope plots",
                    "Box plots or violin plots",
                    "Distribution of pre-post change",
                    "Band-level or feature-level comparison",
                ],
            )

    with synthetic_quality_tab:
        if comparison_name == "BCF vs ACF":
            render_bcf_acf_synthetic_feature_quality()
        elif comparison_name == "BF vs AF":
            render_bf_af_synthetic_feature_quality()
        elif comparison_name == "BCM vs ACM":
            render_bcm_acm_synthetic_feature_quality()
        elif comparison_name == "BM vs AM":
            render_bm_am_synthetic_feature_quality()
        else:
            render_analysis_placeholder(
                "Synthetic feature quality",
                comparison_name,
                "This section will compare descriptive feature properties between real and "
                "ACGAN-generated samples.",
                [
                    "Real-versus-synthetic mean and standard deviation",
                    "Feature-distribution agreement",
                    "Feature quality score, when available",
                    "Features requiring additional review",
                ],
            )

    with similarity_tab:
        render_analysis_placeholder(
            "Quantitative similarity analysis",
            comparison_name,
            "This section will report numerical similarity and distance measurements between "
            "the real and synthetic feature distributions.",
            [
                "Similarity score and correlation",
                "Wasserstein distance",
                "Kolmogorov-Smirnov statistic",
                "MMD or other configured distance metrics",
            ],
        )

    with synthetic_visuals_tab:
        render_analysis_placeholder(
            "Synthetic data visual comparison",
            comparison_name,
            "This section will visually inspect overlap, separation, and coverage between "
            "real and synthetic observations.",
            [
                "Real-versus-synthetic histogram or KDE",
                "PCA, UMAP, or t-SNE projection",
                "Scatter plot and distribution comparison",
                "Class-conditional visual comparison",
            ],
        )


def render_subject_10_pending_analysis(comparison_name):
    """Render the complete analysis workspace even when classification output is pending."""
    render_subject_10_analysis(comparison_name)


def render_subject_10_all_conditions():
    """Render a combined, read-only summary across all four comparison conditions."""
    summary_data = pd.DataFrame(
        [
            {
                "Comparison": "BCF vs ACF",
                "Status": "Completed",
                "EEG Segments": 8540,
                "Training": int(SUBJECT_10_SPLIT.loc[0, "Samples"]),
                "Validation": int(SUBJECT_10_SPLIT.loc[1, "Samples"]),
                "Test": int(SUBJECT_10_SPLIT.loc[2, "Samples"]),
                "Best Band": SUBJECT_10_TEST_RESULTS.loc[
                    SUBJECT_10_TEST_RESULTS["Accuracy"].idxmax(), "Band"
                ],
                "Best Model": SUBJECT_10_TEST_RESULTS.loc[
                    SUBJECT_10_TEST_RESULTS["Accuracy"].idxmax(), "Model"
                ],
                "Best Test Accuracy": SUBJECT_10_TEST_RESULTS["Accuracy"].max(),
            },
            {
                "Comparison": "BF vs AF",
                "Status": "Completed",
                "EEG Segments": 3600,
                "Training": int(SUBJECT_10_BF_AF_SPLIT.loc[0, "Samples"]),
                "Validation": int(SUBJECT_10_BF_AF_SPLIT.loc[1, "Samples"]),
                "Test": int(SUBJECT_10_BF_AF_SPLIT.loc[2, "Samples"]),
                "Best Band": SUBJECT_10_BF_AF_TEST_RESULTS.loc[
                    SUBJECT_10_BF_AF_TEST_RESULTS["Accuracy"].idxmax(), "Band"
                ],
                "Best Model": SUBJECT_10_BF_AF_TEST_RESULTS.loc[
                    SUBJECT_10_BF_AF_TEST_RESULTS["Accuracy"].idxmax(), "Model"
                ],
                "Best Test Accuracy": SUBJECT_10_BF_AF_TEST_RESULTS["Accuracy"].max(),
            },
            {
                "Comparison": "BCM vs ACM",
                "Status": "Completed",
                "EEG Segments": 8220,
                "Training": int(SUBJECT_10_BCM_ACM_SPLIT.loc[0, "Samples"]),
                "Validation": int(SUBJECT_10_BCM_ACM_SPLIT.loc[1, "Samples"]),
                "Test": int(SUBJECT_10_BCM_ACM_SPLIT.loc[2, "Samples"]),
                "Best Band": SUBJECT_10_BCM_ACM_TEST_RESULTS.loc[
                    SUBJECT_10_BCM_ACM_TEST_RESULTS["Accuracy"].idxmax(), "Band"
                ],
                "Best Model": SUBJECT_10_BCM_ACM_TEST_RESULTS.loc[
                    SUBJECT_10_BCM_ACM_TEST_RESULTS["Accuracy"].idxmax(), "Model"
                ],
                "Best Test Accuracy": SUBJECT_10_BCM_ACM_TEST_RESULTS["Accuracy"].max(),
            },
            {
                "Comparison": "BM vs AM",
                "Status": "Completed" if SUBJECT_10_BM_AM_READY else "Pending",
                "EEG Segments": SUBJECT_10_BM_AM_TOTAL_EPOCHS if SUBJECT_10_BM_AM_READY else pd.NA,
                "Training": (
                    int(SUBJECT_10_BM_AM_SPLIT.loc[0, "Samples"])
                    if SUBJECT_10_BM_AM_READY
                    else pd.NA
                ),
                "Validation": (
                    int(SUBJECT_10_BM_AM_SPLIT.loc[1, "Samples"])
                    if SUBJECT_10_BM_AM_READY
                    else pd.NA
                ),
                "Test": (
                    int(SUBJECT_10_BM_AM_SPLIT.loc[2, "Samples"])
                    if SUBJECT_10_BM_AM_READY
                    else pd.NA
                ),
                "Best Band": (
                    SUBJECT_10_BM_AM_TEST_RESULTS.loc[
                        SUBJECT_10_BM_AM_TEST_RESULTS["Accuracy"].idxmax(), "Band"
                    ]
                    if SUBJECT_10_BM_AM_READY and not SUBJECT_10_BM_AM_TEST_RESULTS.empty
                    else "-"
                ),
                "Best Model": (
                    SUBJECT_10_BM_AM_TEST_RESULTS.loc[
                        SUBJECT_10_BM_AM_TEST_RESULTS["Accuracy"].idxmax(), "Model"
                    ]
                    if SUBJECT_10_BM_AM_READY and not SUBJECT_10_BM_AM_TEST_RESULTS.empty
                    else "-"
                ),
                "Best Test Accuracy": (
                    SUBJECT_10_BM_AM_TEST_RESULTS["Accuracy"].max()
                    if SUBJECT_10_BM_AM_READY and not SUBJECT_10_BM_AM_TEST_RESULTS.empty
                    else pd.NA
                ),
            },
        ]
    )
    completed_data = summary_data[summary_data["Status"] == "Completed"].copy()
    for numeric_column in [
        "EEG Segments",
        "Training",
        "Validation",
        "Test",
        "Best Test Accuracy",
    ]:
        completed_data[numeric_column] = pd.to_numeric(
            completed_data[numeric_column], errors="coerce"
        )

    metric_1, metric_2, metric_3, metric_4 = st.columns(4)
    metric_1.metric("Comparisons", "4")
    metric_2.metric("Completed", f"{len(completed_data)} / 4")
    metric_3.metric("EEG Channels", "4")
    metric_4.metric("Total Features", "56")

    (
        overview_tab,
        cross_condition_tab,
        synthetic_validation_tab,
        classification_tab,
        conclusion_tab,
    ) = st.tabs(
        [
            "Overview",
            "Cross-Condition Analysis",
            "Synthetic Data Validation",
            "Classification Summary",
            "Conclusion",
        ]
    )

    with overview_tab:
        st.subheader("All-condition overview")
        with st.container(border=True):
            st.write(
                "This panel combines BCF vs ACF, BF vs AF, BCM vs ACM, and BM vs AM in one "
                "summary. Select an individual comparison above to inspect its complete "
                "preprocessing, feature extraction, ACGAN, results, and analysis panels."
            )
        overview_display = summary_data[
            ["Comparison", "Status", "EEG Segments", "Best Band", "Best Model", "Best Test Accuracy"]
        ].copy()
        overview_display["Best Test Accuracy"] = overview_display["Best Test Accuracy"].map(
            lambda value: "-" if pd.isna(value) else f"{value:.2%}"
        )
        st.dataframe(overview_display, use_container_width=True, hide_index=True)

        with st.expander("Dataset split coverage", expanded=False):
            statistics_display = summary_data[
                ["Comparison", "Status", "EEG Segments", "Training", "Validation", "Test"]
            ].copy()
            st.dataframe(statistics_display, use_container_width=True, hide_index=True)

    with cross_condition_tab:
        st.subheader("Cross-condition analysis")
        st.caption(
            "This section compares the four condition pairs without treating All Conditions "
            "as a fifth classification label."
        )
        (
            subject_summary_tab,
            paired_fdr_tab,
            combined_pre_post_tab,
        ) = st.tabs(
            [
                "Subject-Level Summary",
                "Paired Statistics & FDR",
                "Pre-Post Visualizations",
            ]
        )

        with subject_summary_tab:
            render_analysis_placeholder(
                "Subject-level summary across conditions",
                "all-condition",
                "This section will compare the magnitude and direction of paired changes "
                "across BCF vs ACF, BF vs AF, BCM vs ACM, and BM vs AM.",
                [
                    "Per-condition subject response summary",
                    "Responder and non-responder comparison",
                    "Shared and condition-specific change patterns",
                    "Subject-level consistency across comparisons",
                ],
            )

        with paired_fdr_tab:
            render_analysis_placeholder(
                "Paired statistics and FDR across conditions",
                "all-condition",
                "This section will compare effect size, confidence intervals, raw p-values, "
                "and FDR-adjusted results without averaging p-values.",
                [
                    "Forest plot of effect sizes and confidence intervals",
                    "FDR-adjusted significance heatmap",
                    "Significant-feature count by comparison",
                    "Shared significant features across conditions",
                ],
            )

        with combined_pre_post_tab:
            render_analysis_placeholder(
                "Combined pre-post visualizations",
                "all-condition",
                "This section will place the pre-post patterns from all four comparisons on "
                "consistent axes for visual comparison.",
                [
                    "Condition-level paired change plots",
                    "Effect-size comparison by feature or band",
                    "Distribution of change across comparisons",
                    "Cross-condition trend visualization",
                ],
            )

    with synthetic_validation_tab:
        st.subheader("Synthetic data validation")
        st.caption(
            "Sample counts describe augmentation coverage. Feature quality, quantitative "
            "similarity, and visual agreement are reported separately below."
        )
        quality_rows = [
            {
                "Comparison": "BCF vs ACF",
                "Real Samples": int(SUBJECT_10_ACGAN["Real Samples"].sum()),
                "Synthetic Samples": int(SUBJECT_10_ACGAN["Synthetic Samples"].sum()),
                "Augmented Samples": int(SUBJECT_10_ACGAN["Augmented Samples"].sum()),
                "Status": "Completed",
            },
            {
                "Comparison": "BF vs AF",
                "Real Samples": int(SUBJECT_10_BF_AF_ACGAN["Real Samples"].sum()),
                "Synthetic Samples": int(SUBJECT_10_BF_AF_ACGAN["Synthetic Samples"].sum()),
                "Augmented Samples": int(SUBJECT_10_BF_AF_ACGAN["Augmented Samples"].sum()),
                "Status": "Completed",
            },
            {
                "Comparison": "BCM vs ACM",
                "Real Samples": int(SUBJECT_10_BCM_ACM_ACGAN["Real Samples"].sum()),
                "Synthetic Samples": int(SUBJECT_10_BCM_ACM_ACGAN["Synthetic Samples"].sum()),
                "Augmented Samples": int(SUBJECT_10_BCM_ACM_ACGAN["Augmented Samples"].sum()),
                "Status": "Completed",
            },
        ]
        if SUBJECT_10_BM_AM_READY:
            quality_rows.append(
                {
                    "Comparison": "BM vs AM",
                    "Real Samples": int(SUBJECT_10_BM_AM_ACGAN["Real Samples"].sum()),
                    "Synthetic Samples": int(
                        SUBJECT_10_BM_AM_ACGAN["Synthetic Samples"].sum()
                    ),
                    "Augmented Samples": int(
                        SUBJECT_10_BM_AM_ACGAN["Augmented Samples"].sum()
                    ),
                    "Status": "Completed",
                }
            )
        else:
            quality_rows.append(
                {
                    "Comparison": "BM vs AM",
                    "Real Samples": pd.NA,
                    "Synthetic Samples": pd.NA,
                    "Augmented Samples": pd.NA,
                    "Status": "Pending",
                }
            )
        quality_data = pd.DataFrame(quality_rows)
        with st.expander("Synthetic sample coverage", expanded=False):
            st.dataframe(quality_data, use_container_width=True, hide_index=True)

        feature_quality_tab, quantitative_similarity_tab, visual_comparison_tab = st.tabs(
            ["Feature Quality", "Quantitative Similarity", "Visual Comparison"]
        )

        with feature_quality_tab:
            render_analysis_placeholder(
                "Synthetic feature quality across conditions",
                "all-condition",
                "This section will compare real-versus-synthetic descriptive statistics and "
                "feature quality scores for all four condition pairs.",
                [
                    "Mean and standard-deviation agreement",
                    "Feature quality score by condition",
                    "Number of well-matched features",
                    "Features requiring additional validation",
                ],
            )

        with quantitative_similarity_tab:
            render_analysis_placeholder(
                "Quantitative similarity across conditions",
                "all-condition",
                "This section will compare the configured distribution-similarity metrics "
                "using the same scale across conditions.",
                [
                    "Real-synthetic similarity score by condition",
                    "Correlation and distance metrics",
                    "Wasserstein, KS, and MMD comparison",
                    "Similarity ranking with interpretation limits",
                ],
            )

        with visual_comparison_tab:
            render_analysis_placeholder(
                "Synthetic visual comparison across conditions",
                "all-condition",
                "This section will compare real-versus-synthetic distribution overlap and "
                "latent-space coverage for every condition pair.",
                [
                    "Comparable histogram or KDE panels",
                    "PCA, UMAP, or t-SNE panels",
                    "Condition-level overlap and separation",
                    "Class-conditional visual comparison",
                ],
            )

    with classification_tab:
        st.subheader("Classification summary across conditions")
        classification_sources = [
            (
                "BCF vs ACF",
                SUBJECT_10_TEST_RESULTS,
                SUBJECT_10_TRAIN_RESULTS,
                True,
            ),
            (
                "BF vs AF",
                SUBJECT_10_BF_AF_TEST_RESULTS,
                SUBJECT_10_BF_AF_TRAIN_RESULTS,
                True,
            ),
            (
                "BCM vs ACM",
                SUBJECT_10_BCM_ACM_TEST_RESULTS,
                SUBJECT_10_BCM_ACM_TRAIN_RESULTS,
                True,
            ),
            (
                "BM vs AM",
                SUBJECT_10_BM_AM_TEST_RESULTS,
                SUBJECT_10_BM_AM_TRAIN_RESULTS,
                SUBJECT_10_BM_AM_READY
                and not SUBJECT_10_BM_AM_TEST_RESULTS.empty
                and not SUBJECT_10_BM_AM_TRAIN_RESULTS.empty,
            ),
        ]
        classification_rows = []
        listed_results = []
        for comparison, test_results, train_results, is_ready in classification_sources:
            if is_ready:
                best_test = test_results.loc[test_results["Accuracy"].idxmax()]
                best_train = train_results.loc[train_results["Accuracy"].idxmax()]
                classification_rows.append(
                    {
                        "Comparison": comparison,
                        "Status": "Completed",
                        "Best Test Band": best_test["Band"],
                        "Best Test Model": best_test["Model"],
                        "Best Test Accuracy": best_test["Accuracy"],
                        "Best Training Band": best_train["Band"],
                        "Best Training Model": best_train["Model"],
                        "Best Training Accuracy": best_train["Accuracy"],
                    }
                )
                for evaluation_set, results in [
                    ("Test", test_results),
                    ("Training", train_results),
                ]:
                    listed = results.copy()
                    listed["Comparison"] = comparison
                    listed["Evaluation Set"] = evaluation_set
                    listed_results.append(listed)
            else:
                classification_rows.append(
                    {
                        "Comparison": comparison,
                        "Status": "Pending",
                        "Best Test Band": "-",
                        "Best Test Model": "-",
                        "Best Test Accuracy": pd.NA,
                        "Best Training Band": "-",
                        "Best Training Model": "-",
                        "Best Training Accuracy": pd.NA,
                    }
                )

        classification_data = pd.DataFrame(classification_rows)
        classification_display = classification_data.copy()
        for accuracy_column in ["Best Test Accuracy", "Best Training Accuracy"]:
            classification_display[accuracy_column] = classification_display[accuracy_column].map(
                lambda value: "-" if pd.isna(value) else f"{value:.2%}"
            )
        st.dataframe(classification_display, use_container_width=True, hide_index=True)

        chart_data = classification_data[classification_data["Status"] == "Completed"].copy()
        chart_data["Best Test Accuracy"] = pd.to_numeric(
            chart_data["Best Test Accuracy"], errors="coerce"
        )
        chart_data["Best Training Accuracy"] = pd.to_numeric(
            chart_data["Best Training Accuracy"], errors="coerce"
        )
        chart_data = chart_data.melt(
            id_vars="Comparison",
            value_vars=["Best Training Accuracy", "Best Test Accuracy"],
            var_name="Evaluation",
            value_name="Accuracy",
        )
        chart_data["Evaluation"] = chart_data["Evaluation"].replace(
            {
                "Best Training Accuracy": "Training",
                "Best Test Accuracy": "Test",
            }
        )
        figure = px.bar(
            chart_data,
            x="Comparison",
            y="Accuracy",
            color="Evaluation",
            barmode="group",
            text="Accuracy",
            color_discrete_map={"Training": "#1F6B35", "Test": "#8FCF9C"},
        )
        figure.update_traces(texttemplate="%{text:.2%}", textposition="outside")
        figure.update_layout(
            height=420,
            margin=dict(l=10, r=10, t=30, b=10),
            plot_bgcolor="#FFFFFF",
            paper_bgcolor="#FFFFFF",
            legend_title_text="",
            xaxis_title="",
            yaxis_title="Best Accuracy",
            yaxis=dict(range=[0, 1], tickformat=".0%"),
        )
        st.plotly_chart(figure, use_container_width=True)

        if listed_results:
            listed_data = pd.concat(listed_results, ignore_index=True)
            model_summary = (
                listed_data.groupby(["Comparison", "Evaluation Set", "Model"], as_index=False)
                .agg(
                    **{
                        "Mean Listed Accuracy": ("Accuracy", "mean"),
                        "Listed Configurations": ("Accuracy", "size"),
                    }
                )
            )
            model_summary_display = model_summary.copy()
            model_summary_display["Mean Listed Accuracy"] = model_summary_display[
                "Mean Listed Accuracy"
            ].map(lambda value: f"{value:.2%}")
            st.subheader("SVM vs 1D CNN within the available Top-5 lists")
            st.dataframe(model_summary_display, use_container_width=True, hide_index=True)
            st.caption(
                "This table summarizes only the configurations included in each existing "
                "Top-5 table; it is not a replacement for a full model-to-model evaluation."
            )

    with conclusion_tab:
        best_overall = completed_data.loc[completed_data["Best Test Accuracy"].idxmax()]
        st.subheader("Cross-condition conclusion")
        with st.container(border=True):
            st.subheader("Current highest result")
            st.write(
                f"{best_overall['Comparison']} currently has the highest listed test result: "
                f"{best_overall['Best Band']} band with {best_overall['Best Model']} at "
                f"{best_overall['Best Test Accuracy']:.2%}."
            )
        with st.container(border=True):
            st.subheader("Interpretation")
            st.write(
                "The completed comparisons show relatively close best-result accuracies. "
                "Because their dataset sizes and condition definitions differ, this summary "
                "should be treated as a descriptive comparison rather than proof that one "
                "condition is intrinsically easier to classify."
            )
            if not SUBJECT_10_BM_AM_READY:
                st.info(
                    "BM vs AM is still pending and is excluded from the current accuracy ranking."
                )


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
    overview_title="About",
    objective_text=None,
    workflow_text=None,
    channel_names=None,
    include_random_forest=False,
    model_section_title="Classification models",
    acgan_metric_values=None,
    augmentation_details=None,
    dataset_count_column="Data Distribution",
):
    """Render a completed 10-subject comparison using a shared dashboard layout."""
    metric_1, metric_2, metric_3, metric_4 = st.columns(4)
    metric_1.metric("EEG Segment", f"{total_epochs:,}")
    metric_2.metric("EEG Channels", "4")
    metric_3.metric("Feature Methods", "4")
    metric_4.metric("Total Features", "56")

    (
        overview_tab,
        dataset_tab,
        preprocessing_tab,
        feature_tab,
        models_tab,
        acgan_tab,
        results_tab,
        analysis_tab,
        conclusion_tab,
    ) = st.tabs(
        [
            "Overview",
            "Dataset",
            "Preprocessing",
            "Feature Extraction",
            "Baseline Models",
            "ACGAN",
            "Results",
            "Analysis",
            "Conclusion",
        ]
    )

    with overview_tab:
        left_column, right_column = st.columns(2)
        with left_column:
            with st.container(border=True):
                st.subheader(overview_title)
                st.write(
                    objective_text
                    or (
                        f"Compare the {comparison_name} multi-subject cannabis EEG conditions "
                        "using machine-learning and deep-learning models."
                    )
                )
        with right_column:
            with st.container(border=True):
                st.subheader("Classification labels")
                st.write(f"Label 0: {condition_0}, Before.")
                st.write(f"Label 1: {condition_1}, After.")
        with st.container(border=True):
            st.subheader("Research workflow")
            st.write(
                workflow_text
                or (
                    "Raw EEG data → preprocessing → feature extraction → baseline modelling → "
                    "ACGAN augmentation → final evaluation."
                )
            )

    with dataset_tab:
        st.subheader("Dataset summary")
        dataset_1, dataset_2, dataset_3 = st.columns(3)
        dataset_1.metric("Before Condition", f"{condition_epochs:,}")
        dataset_2.metric("After Condition", f"{condition_epochs:,}")
        dataset_3.metric("Epoch Shape", "(512, 4)")
        conditions = pd.DataFrame(
            {
                "Condition": [condition_0, condition_1],
                "Label": [0, 1],
                dataset_count_column: [condition_epochs, condition_epochs],
                "State": ["Before", "After"],
            }
        )
        st.dataframe(conditions, use_container_width=True, hide_index=True)
        st.subheader("EEG channels")
        if channel_names:
            channel_columns = st.columns(len(channel_names))
            for column, channel_name in zip(channel_columns, channel_names):
                column.metric("Channel", channel_name)
        else:
            st.caption(
                "The study uses 4 EEG channels. Add the channel names here once they are finalised."
            )

    with preprocessing_tab:
        render_preprocessing_tab()
    with feature_tab:
        render_feature_tab()

    with models_tab:
        st.subheader(model_section_title)
        model_columns = st.columns(3 if include_random_forest else 2)
        model_1 = model_columns[0]
        with model_1:
            with st.container(border=True):
                st.subheader("SVM")
                st.write(
                    "Support Vector Machine for supervised classification between Label 0 and Label 1."
                )
        if include_random_forest:
            with model_columns[1]:
                with st.container(border=True):
                    st.subheader("Random Forest")
                    st.write(
                        "Ensemble tree classifier for identifying nonlinear relationships in EEG features."
                    )
            cnn_column = model_columns[2]
        else:
            cnn_column = model_columns[1]
        with cnn_column:
            with st.container(border=True):
                st.subheader("1D CNN")
                st.write(
                    "Deep-learning classifier using one-dimensional convolution over feature sequences."
                )
        st.write("")
        st.subheader("Dataset split")
        st.dataframe(split_data, use_container_width=True, hide_index=True)

    with acgan_tab:
        st.subheader("ACGAN-based data augmentation")
        if acgan_metric_values is None:
            acgan_metric_values = (total_epochs, total_epochs, total_epochs * 2)
        real_metric, synthetic_metric, mixed_metric = acgan_metric_values
        acgan_1, acgan_2, acgan_3 = st.columns(3)
        acgan_1.metric("Real Training Data", f"{real_metric:,}")
        acgan_2.metric("Synthetic Training Data", f"{synthetic_metric:,}")
        acgan_3.metric("Mixed Training Data", f"{mixed_metric:,}")
        with st.container(border=True):
            st.subheader("Augmentation strategy")
            details = augmentation_details or [
                "ACGAN generates a synthetic counterpart for each real sample. The real and "
                "synthetic samples are then combined for the classification experiment."
            ]
            for detail in details:
                st.write(detail)
        st.dataframe(acgan_data, use_container_width=True, hide_index=True)

    with results_tab:
        render_accuracy_chart(test_results, "Top 5 Accuracy on the Test Dataset")
        test_display = test_results.copy()
        test_display["Accuracy"] = test_display["Accuracy"].map(lambda value: f"{value:.2%}")
        st.dataframe(test_display, use_container_width=True, hide_index=True)
        best_result = test_results.loc[test_results["Accuracy"].idxmax()]
        st.success(
            f"Best test result: {best_result['Band']} band, {best_result['Model']}, "
            f"{best_result['Data']}, {best_result['Accuracy']:.2%} accuracy."
        )

        st.write("")
        render_accuracy_chart(train_results, "Top 5 Accuracy on the Training Dataset")
        train_display = train_results.copy()
        train_display["Accuracy"] = train_display["Accuracy"].map(lambda value: f"{value:.2%}")
        st.dataframe(train_display, use_container_width=True, hide_index=True)

    with analysis_tab:
        render_subject_10_analysis(comparison_name, test_results, train_results)

    with conclusion_tab:
        render_subject_10_conclusion(comparison_name)

def render_subject_10_pending_comparison(comparison_name, condition_0, condition_1):
    """Render a 10-subject comparison whose experimental output is not available yet.

    The layout matches the completed comparisons so the page stays visually
    consistent, but no dataset or accuracy figures are shown until the real
    values have been entered.
    """
    metric_1, metric_2, metric_3, metric_4 = st.columns(4)
    metric_1.metric("EEG Segment", f"{SUBJECT_10_BM_AM_TOTAL_EPOCHS:,}")
    metric_2.metric("EEG Channels", "4")
    metric_3.metric("Feature Methods", "4")
    metric_4.metric("Total Features", "56")

    (
        overview_tab,
        dataset_tab,
        preprocessing_tab,
        feature_tab,
        models_tab,
        acgan_tab,
        results_tab,
        analysis_tab,
        conclusion_tab,
    ) = st.tabs(
        [
            "Overview",
            "Dataset",
            "Preprocessing",
            "Feature Extraction",
            "Baseline Models",
            "ACGAN",
            "Results",
            "Analysis",
            "Conclusion",
        ]
    )

    with overview_tab:
        left_column, right_column = st.columns(2)
        with left_column:
            with st.container(border=True):
                st.subheader("About")
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
                "Raw EEG data → preprocessing → feature extraction → baseline modelling → "
                "ACGAN augmentation → final evaluation."
            )

    with dataset_tab:
        with st.container(border=True):
            st.subheader("Dataset status")
            st.write(
                f"Epoch counts for the {condition_0} and {condition_1} conditions have not "
                "been entered yet."
            )

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
        with st.container(border=True):
            st.subheader("Dataset split")
            st.write("The training, validation, and test split will appear here.")

    with acgan_tab:
        with st.container(border=True):
            st.subheader("ACGAN-based data augmentation")
            st.write(
                "Real, synthetic, and mixed sample counts will appear here once the "
                "augmentation run has been completed."
            )

    with results_tab:
        with st.container(border=True):
            st.subheader("Results status")
            st.write(
                "Top 5 accuracy on the training and test datasets will appear here once "
                "the experiment has been evaluated."
            )

    with analysis_tab:
        render_subject_10_pending_analysis(comparison_name)

    with conclusion_tab:
        with st.container(border=True):
            st.subheader(f"Conclusion: {comparison_name}")
            st.write("The conclusion will be written after the results have been evaluated.")


def render_subject_10_bcf_acf():
    """Render the completed BCF vs ACF dashboard for the 10-subject study."""
    metric_1, metric_2, metric_3, metric_4 = st.columns(4)
    metric_1.metric("EEG Segment", "8,540")
    metric_2.metric("EEG Channels", "4")
    metric_3.metric("Feature Methods", "4")
    metric_4.metric("Total Features", "56")

    (
        overview_tab,
        dataset_tab,
        preprocessing_tab,
        feature_tab,
        models_tab,
        acgan_tab,
        results_tab,
        analysis_tab,
        conclusion_tab,
    ) = st.tabs(
        [
            "Overview",
            "Dataset",
            "Preprocessing",
            "Feature Extraction",
            "Baseline Models",
            "ACGAN",
            "Results",
            "Analysis",
            "Conclusion",
        ]
    )

    with overview_tab:
        left_column, right_column = st.columns(2)
        with left_column:
            with st.container(border=True):
                st.subheader("About")
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
                "Raw EEG data → preprocessing → feature extraction → baseline modelling → "
                "ACGAN augmentation → final evaluation."
            )

    with dataset_tab:
        st.subheader("Dataset summary")
        dataset_1, dataset_2, dataset_3 = st.columns(3)
        dataset_1.metric("Before Condition", "4,270")
        dataset_2.metric("After Condition", "4,270")
        dataset_3.metric("Epoch Shape", "(512, 4)")
        conditions = pd.DataFrame(
            {
                "Condition": ["BCF", "ACF"],
                "Label": [0, 1],
                "Data Distribution": [4270, 4270],
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
        render_accuracy_chart(SUBJECT_10_TEST_RESULTS, "Top 5 Accuracy on the Test Dataset")
        test_display = SUBJECT_10_TEST_RESULTS.copy()
        test_display["Accuracy"] = test_display["Accuracy"].map(lambda value: f"{value:.2%}")
        st.dataframe(test_display, use_container_width=True, hide_index=True)
        st.success("Best test result: Beta band, SVM, Real + Synthetic, 84.70% accuracy.")

        st.write("")
        render_accuracy_chart(SUBJECT_10_TRAIN_RESULTS, "Top 5 Accuracy on the Training Dataset")
        train_display = SUBJECT_10_TRAIN_RESULTS.copy()
        train_display["Accuracy"] = train_display["Accuracy"].map(lambda value: f"{value:.2%}")
        st.dataframe(train_display, use_container_width=True, hide_index=True)

    with analysis_tab:
        render_subject_10_analysis(
            "BCF vs ACF",
            SUBJECT_10_TEST_RESULTS,
            SUBJECT_10_TRAIN_RESULTS,
        )

    with conclusion_tab:
        render_subject_10_conclusion("BCF vs ACF")

def render_subject_10():
    st.caption("EXPERIMENTAL REPORT 02")
    st.title("EEG Data Analysis of 10 Cannabis Subjects")
    st.write(
        "Multi-subject cannabis EEG analysis across 10 users, including comparative "
        "classification of BCF vs ACF, BF vs AF, BCM vs ACM, and BM vs AM conditions."
    )
    if st.button("Back to all reports", key="back_subject_10"):
        return_to_home()

    st.write("")
    comparison_name = st.radio(
        "Select comparison",
        options=["BCF vs ACF", "BF vs AF", "BCM vs ACM", "BM vs AM", "All Conditions"],
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
    elif comparison_name == "BCM vs ACM":
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
    elif comparison_name == "All Conditions":
        render_subject_10_all_conditions()
    elif SUBJECT_10_BM_AM_READY:
        render_subject_10_completed_comparison(
            comparison_name="BM vs AM",
            condition_0="BM",
            condition_1="AM",
            total_epochs=SUBJECT_10_BM_AM_TOTAL_EPOCHS,
            condition_epochs=SUBJECT_10_BM_AM_CONDITION_EPOCHS,
            split_data=SUBJECT_10_BM_AM_SPLIT,
            acgan_data=SUBJECT_10_BM_AM_ACGAN,
            test_results=SUBJECT_10_BM_AM_TEST_RESULTS,
            train_results=SUBJECT_10_BM_AM_TRAIN_RESULTS,
            overview_title="About",
            objective_text=(
                "Compare BM vs AM multi-subject cannabis EEG conditions using "
                "machine-learning and deep-learning models."
            ),
            workflow_text=(
                "Raw EEG data → preprocessing → feature extraction → "
                "baseline modelling → ACGAN augmentation → final evaluation."
            ),
            channel_names=["RAW_TP9", "RAW_AF7", "RAW_AF8", "RAW_TP10"],
            include_random_forest=True,
            model_section_title="Baseline classifiers",
            acgan_metric_values=(7440, 7440, 10416),
            augmentation_details=[
                "ACGAN generates synthetic data for each feature set. Real and synthetic "
                "samples are combined for model training and evaluation.",
                "Frequency-band feature sets contain 24 features, while the All Bands "
                "feature set contains 56 features.",
            ],
            dataset_count_column="Epochs",
        )
    else:
        render_subject_10_pending_comparison(
            comparison_name="BM vs AM",
            condition_0="BM",
            condition_1="AM",
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

    overview_tab, dataset_tab, models_tab, results_tab = st.tabs(["Overview", "Dataset", "Baseline Models", "Results"])
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
