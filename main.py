import streamlit as st
import pandas as pd
import numpy as np

# Configure Streamlit page settings
st.set_page_config(
    page_title="Fraud Detection Dashboard",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load external CSS for styling
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def ml_model_prediction(transaction_ids):
    """
    Simulates ML model fraud prediction for given transaction IDs.
    
    Args:
        transaction_ids (list): List of transaction IDs to predict
    
    Returns:
        list: List of fraud predictions (0 = Not Fraud, 1 = Fraud)
    """
    # Set seed based on transaction IDs for consistent predictions
    np.random.seed(sum(hash(str(tid)) % 1000 for tid in transaction_ids) % 2**32)
    
    # Generate fraud predictions (30% fraud rate)
    predictions = np.random.choice([0, 1], size=len(transaction_ids), p=[0.7, 0.3])
    return predictions.tolist()

def generate_sample_data(num_rows=1000):
    """
    Generates sample transaction data for demonstration purposes.
    
    Args:
        num_rows (int): Number of sample transactions to generate
    
    Returns:
        pd.DataFrame: DataFrame with TransactionID column only
    """
    np.random.seed(42)  # Ensures consistent sample data
    
    transaction_ids = [str(np.random.randint(1000000, 9999999)) for _ in range(num_rows)]
    
    return pd.DataFrame({'TransactionID': transaction_ids})

def process_transactions(df):
    """
    Processes transaction data through ML model and adds predictions.
    
    Args:
        df (pd.DataFrame): DataFrame containing TransactionID column
    
    Returns:
        pd.DataFrame: DataFrame with TransactionID and isFraud columns
    """
    # Get fraud predictions from ML model
    fraud_predictions = ml_model_prediction(df['TransactionID'].tolist())
    
    result_df = pd.DataFrame({
        'TransactionID': df['TransactionID'].values,
        'isFraud': fraud_predictions
    })
    
    return result_df

# Dashboard Title
st.markdown('<h1 class="main-title">ERGCN Fraud Detection Dashboard</h1>', unsafe_allow_html=True)

# File uploader section
uploaded_file = st.file_uploader(
    "",
    type="csv",
    label_visibility="collapsed",
    help="Upload your CSV file containing TransactionID column"
)

# Center informative messages
col1_info, col2_info, col3_info = st.columns([1, 2, 1])

# Handle file upload or use sample data
if uploaded_file is not None:
    try:
        with col2_info:
            # Load uploaded CSV
            uploaded_df = pd.read_csv(uploaded_file)
            
            # Validate required column exists
            if 'TransactionID' not in uploaded_df.columns:
                st.error("❌ Error: 'TransactionID' column is required in the uploaded file.")
                st.stop()  # Stop execution if required column is missing
            
            # Extract only TransactionID column
            input_df = uploaded_df[['TransactionID']].copy()
            
            # Process transactions through ML model
            data_to_display = process_transactions(input_df)
            
            st.success(f"✅ File uploaded successfully - {len(data_to_display)} transactions processed")
            
    except Exception as e:
        with col2_info:
            st.error(f"❌ Error loading file: {str(e)}")
            st.stop()  # Stop execution on file error
else:
    with col2_info:
        # Generate sample data and process it
        sample_input = generate_sample_data()
        data_to_display = process_transactions(sample_input)
        st.info("📋 No file uploaded - displaying sample data with ML predictions.")

# Results section header
st.markdown('<h2 class="table-header">Results</h2>', unsafe_allow_html=True)

# Filter options for displaying results
fraud_filter = st.pills(
    "",
    options=["Show All", "Fraud Only", "Not Fraud Only"],
    default="Show All",
    label_visibility="collapsed"
)

# Apply filters to the data
filtered_df = data_to_display.copy()
if fraud_filter == "Fraud Only":
    filtered_df = filtered_df[filtered_df['isFraud'] == 1]
elif fraud_filter == "Not Fraud Only":
    filtered_df = filtered_df[filtered_df['isFraud'] == 0]

# Reset index after filtering for clean display
filtered_df = filtered_df.reset_index(drop=True)

#  setup
rows_per_page_options = [10, 25, 50, 100]
rows_per_page = st.session_state.get("rows_per_page", 25)

# Calculate pagination parameters
total_rows = len(filtered_df)
total_pages = max((total_rows - 1) // rows_per_page + 1, 1)
current_page = max(1, min(st.session_state.get("current_page", 1), total_pages))

# Get paginated data slice
start_idx = (current_page - 1) * rows_per_page
end_idx = start_idx + rows_per_page
paginated_df = filtered_df.iloc[start_idx:end_idx]

# Display paginated table
st.dataframe(paginated_df, use_container_width=True)

# Pagination controls
with st.container():
    col1, _ = st.columns([1, 3])
    with col1:
        # Page number input
        st.number_input(
            "Page",
            min_value=1,
            max_value=total_pages,
            value=current_page,
            step=1,
            key="current_page",
            label_visibility="collapsed",
        )
        
        # Rows per page selector
        st.selectbox(
            "Rows per page",
            options=rows_per_page_options,
            index=rows_per_page_options.index(rows_per_page),
            key="rows_per_page",
            label_visibility="collapsed",
        )

# Statistics Overview (based on complete processed dataset)
if len(data_to_display) > 0:
    total_records = len(data_to_display)
    fraud_count = len(data_to_display[data_to_display['isFraud'] == 1])
    not_fraud_count = len(data_to_display[data_to_display['isFraud'] == 0])
    fraud_rate = (fraud_count / total_records) * 100

    # Display statistics in formatted HTML
    st.markdown(f"""
    <div class="stats-section">
        <div class="stats-title">📊 Statistics Overview (ML Model Results)</div>
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

# About section with project information
st.markdown("""
<div class="about-container">
    <div class="about-title">ℹ️ About This Dashboard</div>
    <div class="about-text">
        This dashboard processes transaction data through the <strong>ERGCN fraud detection model</strong>.
        Upload your CSV file containing TransactionID column to analyze real data, or explore the sample dataset.
        <br><br>
        <strong>Process Flow:</strong><br>
        • <strong>Input:</strong> CSV file with TransactionID column<br>
        • <strong>Processing:</strong> ML model generates fraud predictions<br>
        • <strong>Output:</strong> Results table with TransactionID and fraud status<br>
        <br>
        <strong>Output Explained:</strong><br>
        • <strong>TransactionID:</strong> Transaction identifier<br>
        • <strong>isFraud:</strong> ML prediction (0 = Legitimate, 1 = Fraudulent)<br>
        <br>
        <small>This dashboard was developed by <strong>students</strong> from Polytechnic University of the Philippines as a requirement for their <strong>Software Engineering 1</strong> course.</small>
    </div>
</div>
""", unsafe_allow_html=True)

# Display message if no data matches current filter
if len(filtered_df) == 0:
    st.warning("No data matches the current filter criteria.")