import streamlit as st
import pandas as pd
import numpy as np

# Configure Streamlit page settings
st.set_page_config(
    page_title="LQ-ERGCN Fraud Detection Metrics",
    page_icon="🛡️",
    layout="wide", # Use full width of the browser
    initial_sidebar_state="collapsed" # Hide the sidebar by default
)

# Custom CSS for dark mode and layout
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

/* Apply dark background and light text globally */
.stApp {
    background-color: #0e1117 !important;
    color: #fafafa !important;
}

/* Center and set max width for the main content area */
.main .block-container {
    background-color: #0e1117 !important;
    color: #fafafa !important;
    max-width: 1000px !important; /* Fixed width for content */
    margin: 0 auto !important; /* Centers the content block */
}

/* Global font family */
.main {
    font-family: 'Inter', sans-serif;
    padding: 1rem;
}

/* Dashboard title styling */
.main-title {
    font-size: 2.2rem; /* Keep original size, or adjust */
    font-weight: 700;
    color: #fafafa;
    text-align: center;
    margin-bottom: 2rem;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    background-clip: text;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.4); /* Subtle shadow */
}

/* Styling for main containers like upload, filter, and about sections */
.upload-container, .filter-container, .about-container {
    max-width: 600px; /* Limit width of these sections */
    margin: 2rem auto; /* Center them horizontally with vertical spacing */
    background: #262730; /* Darker background for sections */
    border: 1px solid #404040; /* Subtle border */
    border-radius: 12px; /* Rounded corners */
    padding: 1.5rem;
    text-align: center;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3); /* Soft shadow */
}

/* Adjust filter container specific max-width */
.filter-container {
    max-width: 500px;
}

/* Section headers within containers */
.section-header {
    font-size: 1.1rem;
    font-weight: 600;
    color: #fafafa;
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
}

/* Statistics section styling */
.stats-section {
    max-width: 800px;
    margin: 2rem auto;
    padding: 2rem;
    background: #262730;
    border-radius: 16px;
    border: 1px solid #404040;
    text-align: center;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
}

.stats-title {
    font-size: 1.3rem;
    font-weight: 600;
    color: #fafafa;
    margin-bottom: 1.5rem;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.stats-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr); /* 4 columns for stats */
    gap: 2rem;
    max-width: 600px; /* Limit width of the stat grid */
    margin: 0 auto;
}

.stat-item {
    text-align: center;
}

.stat-number {
    font-size: 2.5rem;
    font-weight: 700;
    color: #667eea; /* Primary accent color for numbers */
    margin-bottom: 0.5rem;
    display: block;
}

.stat-number.fraud {
    color: #ef4444; /* Red for fraud numbers */
}

.stat-number.safe {
    color: #22c55e; /* Green for legitimate numbers */
}

.stat-label {
    font-size: 0.9rem;
    color: #d1d5db; /* Lighter gray for labels */
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

/* Table header styling */
.table-header {
    font-size: 1.3rem;
    font-weight: 600;
    color: #fafafa;
    margin: 2rem 0 1rem 0;
    text-align: center;
    text-transform: uppercase;
    letter-spacing: 1px;
}

/* About section specific styling */
.about-title {
    font-size: 1.1rem;
    font-weight: 600;
    color: #fafafa;
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.about-text {
    color: #d1d5db; /* Light gray for body text */
    font-size: 0.9rem;
    line-height: 1.6;
}

.about-text strong {
    color: #fafafa; /* White for strong text */
}

/* Dark theme for Streamlit dataframes */
.stDataFrame {
    background-color: #262730 !important;
}

/* Styling for Streamlit alert boxes */
.stAlert {
    max-width: 800px !important;
    width: fit-content !important;
    margin-left: auto !important;
    margin-right: auto !important;
}

/* Center text inside all alert boxes */
.stAlert > div > div {
    text-align: center;
}

/* Specific styling for each alert type */
.stInfo {
    background-color: #0e1117 !important; /* Matches main web background */
    color: #bfdbfe !important; /* Light blue for info text */
    border: 1px solid #404040 !important; /* Subtle border */
}

.stSuccess {
    background-color: #166534 !important; /* Green for success */
    color: #bbf7d0 !important;
}

.stWarning {
    background-color: #92400e !important; /* Orange for warning */
    color: #fde68a !important;
}

.stError {
    background-color: #991b1b !important; /* Red for error */
    color: #fecaca !important;
}

/* Responsive adjustments for smaller screens */
@media (max-width: 768px) {
    .main {
        padding: 0.5rem;
    }

    .main-title {
        font-size: 1.8rem;
    }

    .upload-container,
    .filter-container,
    .about-container,
    .stats-section {
        max-width: 90%;
        margin: 1rem auto;
        padding: 1rem;
    }

    .stats-grid {
        grid-template-columns: repeat(2, 1fr); /* 2 columns on smaller screens */
        gap: 1rem;
    }

    .stat-number {
        font-size: 2rem;
    }
}

@media (max-width: 480px) {
    .stats-grid {
        grid-template-columns: repeat(2, 1fr);
        gap: 0.5rem;
    }

    .stat-number {
        font-size: 1.8rem;
    }

    .upload-container,
    .filter-container,
    .stats-section,
    .about-container {
        max-width: 95%;
        margin: 1rem auto;
    }
}
</style>
""", unsafe_allow_html=True)

# Function to generate sample data for demonstration
def generate_sample_data(num_rows=150):
    np.random.seed(42) # Ensures consistent sample data every time

    data = {
        'IdentityID': [f"ID-{np.random.randint(1000, 9999)}" for _ in range(num_rows)], # Only IdentityID
        'Precision': np.round(np.random.uniform(0.75, 0.98, num_rows), 4),
        'Recall': np.round(np.random.uniform(0.70, 0.95, num_rows), 4),
        'F1_Score': np.round(np.random.uniform(0.72, 0.96, num_rows), 4),
        'AUC': np.round(np.random.uniform(0.80, 0.99, num_rows), 4),
        'isFraud': np.random.choice([0, 1], size=num_rows, p=[0.7, 0.3]) # 0: Not Fraud, 1: Fraud
    }
    return pd.DataFrame(data)

# Dashboard Title
st.markdown('<h1 class="main-title">🛡️ LQ-ERGCN Fraud Detection Dashboard</h1>', unsafe_allow_html=True)

# File uploader section for CSV files
uploaded_file = st.file_uploader(
    "", # No visible label
    type="csv",
    label_visibility="collapsed", # Hide default label
    help="Upload your CSV file containing fraud detection metrics"
)

# Columns for centering informative messages
col1_info, col2_info, col3_info = st.columns([1, 2, 1])

# Logic to handle file upload or use sample data
if uploaded_file is not None:
    try:
        with col2_info:
            df = pd.read_csv(uploaded_file)
            st.success(f"✅ File uploaded successfully - {len(df)} rows loaded")
            data_to_display = df
    except Exception as e:
        with col2_info:
            st.error(f"❌ Error loading file: {str(e)}")
            data_to_display = generate_sample_data() # Fallback to sample data on error
            st.warning("📋 Using sample data instead due to file error.")
else:
    with col2_info:
        data_to_display = generate_sample_data() # Default to sample data if no file uploaded
        st.info("📋 No file uploaded - displaying sample data.")


st.markdown('<h2 class="table-header">Results</h2>', unsafe_allow_html=True)

# Filter options for the displayed results table
fraud_filter = st.pills(
    "", # No visible label for pills
    options=["Show All", "Fraud Only", "Not Fraud Only"],
    default="Show All",
    label_visibility="collapsed"
)

# Apply filters to create a DataFrame for table display
filtered_df = data_to_display.copy()
if fraud_filter == "Fraud Only":
    if 'isFraud' in filtered_df.columns:
        filtered_df = filtered_df[filtered_df['isFraud'] == 1]
    else:
        st.warning("⚠️ 'isFraud' column not found for filtering.")
elif fraud_filter == "Not Fraud Only":
    if 'isFraud' in filtered_df.columns:
        filtered_df = filtered_df[filtered_df['isFraud'] == 0]
    else:
        st.warning("⚠️ 'isFraud' column not found for filtering.")

# Reset index for clean table display
filtered_df = filtered_df.reset_index(drop=True)

# Display the filtered data in an interactive Streamlit DataFrame
st.dataframe(
    filtered_df,
    use_container_width=True, # Makes the table expand to fit its container
    height=400,
    column_config={
        "IdentityID": st.column_config.TextColumn("Identity ID", width="medium"),     # Only IdentityID is here now
        "Precision": st.column_config.NumberColumn("Precision", format="%.4f", help="Model precision score"),
        "Recall": st.column_config.NumberColumn("Recall", format="%.4f", help="Model recall score"),
        "F1_Score": st.column_config.NumberColumn("F1 Score", format="%.4f", help="Harmonic mean of precision and recall"),
        "AUC": st.column_config.NumberColumn("AUC", format="%.4f", help="Area Under the ROC Curve"),
        "isFraud": st.column_config.NumberColumn("isFraud", help="0 = Legitimate, 1 = Fraud")
    }
)

# Statistics Overview section (always based on the complete dataset)
if len(data_to_display) > 0:
    total_records = len(data_to_display)
    # Safely get fraud/legitimate counts if 'isFraud' column exists
    if 'isFraud' in data_to_display.columns:
        fraud_count = len(data_to_display[data_to_display['isFraud'] == 1])
        not_fraud_count = len(data_to_display[data_to_display['isFraud'] == 0])
    else:
        fraud_count = 0
        not_fraud_count = 0
        st.warning("⚠️ 'isFraud' column not found in overall data for statistics calculation.")

    fraud_rate = (fraud_count / total_records) * 100 if total_records > 0 else 0

    st.markdown(f"""
    <div class="stats-section">
        <div class="stats-title">📊 Statistics Overview (Overall Data)</div>
        <div class="stats-grid">
            <div class="stat-item">
                <span class="stat-number">{total_records}</span>
                <div class="stat-label">Total Records</div>
            </div>
            <div class="stat-item">
                <span class="stat-number fraud">{fraud_count}</span>
                <div class="stat-label">Fraud Cases</div>
            </div>
            <div class="stat-item">
                <span class="stat-number safe">{not_fraud_count}</span>
                <div class="stat-label">Legitimate Cases</div>
            </div>
            <div class="stat-item">
                <span class="stat-number">{fraud_rate:.1f}%</span>
                <div class="stat-label">Fraud Rate</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
else:
    st.warning("Cannot display overall statistics as no data is loaded.")


# About section with integrated project credits
st.markdown("""
<div class="about-container">
    <div class="about-title">ℹ️ About This Dashboard</div>
    <div class="about-text">
        This dashboard analyzes the performance metrics of the <strong>LQ-ERGCN fraud detection model</strong>.
        Upload your CSV file to analyze real data or explore the sample dataset provided.
        <br><br>
        <strong>Metrics Explained:</strong><br>
        • <strong>Precision:</strong> Accuracy of fraud predictions (TP / (TP + FP))<br>
        • <strong>Recall:</strong> Coverage of actual fraud cases (TP / (TP + FN))<br>
        • <strong>F1 Score:  </strong> Harmonic mean of precision and recall<br>
        • <strong>AUC:</strong> Area Under the ROC Curve (model discrimination ability)<br>
        • <strong>isFraud:</strong> Binary indicator (0 = Legitimate, 1 = Fraudulent)
        <br><br>
        <small>This dashboard was developed by <strong>students</strong> from <strong>Polytechnic University of The Philippines</strong> as a requirement for their <strong>Software Engineering 1</strong> course.</small>
    </div>
</div>
""", unsafe_allow_html=True)

# Message displayed if no data matches the current table filter
if len(filtered_df) == 0:
    st.warning("📭 No data matches the current filter criteria for table display.")

# Final confirmation log for developers
print("LQ-ERGCN Fraud Detection Dashboard is running!")