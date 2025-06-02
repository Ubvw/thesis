import streamlit as st
import pandas as pd
import numpy as np

# Configure Streamlit page settings
st.set_page_config(
    page_title="ERGCN Fraud Detection Metrics",
    page_icon="🛡️",
    layout="wide", # Use full width of the browser
    initial_sidebar_state="collapsed" # Hide the sidebar by default
)

# Load external CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Function to generate sample data for demonstration
def generate_sample_data(num_rows=1000): # Generates 1000 rows
    np.random.seed(42) # Ensures consistent sample data every time

    data = {
        'TransactionID': [str(np.random.randint(1000000, 9999999)) for _ in range(num_rows)], # Generates 7-digit numbers
        'isFraud': np.random.choice([0, 1], size=num_rows, p=[0.7, 0.3]) # 0: Not Fraud, 1: Fraud
    }
    return pd.DataFrame(data)

# Dashboard Title
st.markdown('<h1 class="main-title">ERGCN Fraud Detection Dashboard</h1>', unsafe_allow_html=True)

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
            # Rename 'is_Fraud' to 'isFraud' if present in the uploaded file
            if 'is_Fraud' in df.columns:
                df.rename(columns={'is_Fraud': 'isFraud'}, inplace=True)
            # Ensure only TransactionID and isFraud are kept if other columns are in uploaded file
            # This is a critical step for uploaded files to match the desired table structure
            if 'TransactionID' in df.columns and 'isFraud' in df.columns:
                df = df[['TransactionID', 'isFraud']]
            else:
                st.warning("⚠️ Uploaded file missing 'TransactionID' or 'isFraud' columns. Using sample data.")
                df = generate_sample_data() # Fallback if essential columns are missing
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

# Reset index for clean table display (important after filtering if index isn't hidden)
filtered_df = filtered_df.reset_index(drop=True)

# Calculate total pages based on selected rows per page
rows_per_page_options = [10, 25, 50, 100]
rows_per_page = st.session_state.get("rows_per_page", 25)

# Calculate total pages
total_rows = len(filtered_df)
total_pages = max((total_rows - 1) // rows_per_page + 1, 1)

# Get current page from session state (or default to 1)
current_page = st.session_state.get("current_page", 1)

# Clamp current page to valid range
current_page = max(1, min(current_page, total_pages))

# Slice the dataframe
start_idx = (current_page - 1) * rows_per_page
end_idx = start_idx + rows_per_page
paginated_df = filtered_df.iloc[start_idx:end_idx]

# Show the paginated table
st.dataframe(paginated_df, use_container_width=True)

# --- Compact controls stacked below table ---
with st.container():
    col1, _ = st.columns([1, 3])
    with col1:
        st.number_input(
            "Page",
            min_value=1,
            max_value=total_pages,
            value=current_page,
            step=1,
            key="current_page",
            label_visibility="collapsed",
        )

    with col1:
        st.selectbox(
            "Rows per page",
            options=rows_per_page_options,
            index=rows_per_page_options.index(rows_per_page),
            key="rows_per_page",
            label_visibility="collapsed",
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
        This dashboard analyzes the performance metrics of the <strong>ERGCN fraud detection model</strong>.
        Upload your CSV file to analyze real data or explore the sample dataset provided.
        <br><br>
        <strong>Metrics Explained:</strong><br>
        • <strong>isFraud:</strong> Binary indicator (0 = Legitimate, 1 = Fraudulent)<br>
        <br>
        <small>This dashboard was developed by <strong>students</strong> from Polytechnic University of the Philippines as a requirement for their <strong>Software Engineering 1</strong> course.</small>
    </div>
</div>
""", unsafe_allow_html=True)

# Message displayed if no data matches the current table filter
if len(filtered_df) == 0:
    st.warning("📭 No data matches the current filter criteria for table display.")

# Final confirmation log for developers
print("ERGCN Fraud Detection Dashboard is running!")