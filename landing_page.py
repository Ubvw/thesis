import streamlit as st

st.set_page_config(layout="wide")

# Remove Streamlit's default padding and enhance button styling
st.markdown(
    """
    <style>
    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        padding-left: 0rem !important;
        padding-right: 0rem !important;
    }
    .hero-content, .cta-section, .hero-title, .hero-subtitle {
        text-align: center !important;
        margin-left: auto;
        margin-right: auto;
    }
    .stButton > button {
        display: block;
        margin: 2rem auto 0 auto;
        font-size: 1.4rem !important;
        padding: 1rem 3rem !important;
        border-radius: 12px !important;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: #fff !important;
        border: none !important;
        font-weight: 700 !important;
        box-shadow: 0 4px 20px rgba(102,126,234,0.3) !important;
        transition: all 0.3s ease !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        min-width: 280px;
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%) !important;
        color: #fff !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 25px rgba(102,126,234,0.4) !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

with st.container():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: 'Inter', sans-serif;
            background-color: #0e1117;
            color: #fafafa;
            line-height: 1.6;
            overflow-x: hidden;
        }
        .container {
            width: 100%;
            margin: 0;
            padding: 0 2rem;
        }
        /* Enhanced Hero Section */
        .hero {
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            background: linear-gradient(135deg, #0e1117 0%, #1a1d29 100%);
            position: relative;
            overflow: hidden;
            padding: 4rem 0;
        }
        .hero::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: radial-gradient(circle at 50% 50%, rgba(102, 126, 234, 0.15) 0%, transparent 60%);
            pointer-events: none;
        }
        .hero-content {
            position: relative;
            z-index: 2;
            width: 100%;
            max-width: 900px;
            margin: 0 auto;
            text-align: center;
        }
        .hero-title {
            font-size: 10rem !important;
            font-weight: 900;
            margin-bottom: 2rem;
            background: linear-gradient(135deg, #ffffff 0%, #667eea 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            line-height: 0.9;
            text-shadow: 0 0 50px rgba(240, 216, 180, 0.5);
            letter-spacing: -3px;
            text-align: center !important;
            text-transform: uppercase;
            font-family: 'Inter', sans-serif;
        }
        .hero-subtitle {
            font-size: 1.5rem;
            color: #d1d5db;
            margin-bottom: 4rem;
            font-weight: 400;
            max-width: 700px;
            margin-left: auto !important;
            margin-right: auto !important;
            line-height: 1.7;
            text-align: center !important;
        }
        .cta-text {
            font-size: 1.3rem;
            color: #fafafa;
            margin-bottom: 2rem;
            font-weight: 600;
            text-align: center !important;
        }
        /* Enhanced Features Section */
        .features {
            padding: 8rem 0;
            background: #0e1117;
        }
        .section-header {
            text-align: center;
            margin-bottom: 5rem;
        }
        .section-title {
            font-size: 4rem !important;
            font-weight: 800;
            color: #ffffff;
            margin-bottom: 1.5rem;
            letter-spacing: -1px;
        }
        .section-description {
            font-size: 1.3rem;
            color: #d1d5db;
            max-width: 700px;
            margin: 0 auto !important;
            line-height: 1.6;
            font-weight: 400;
            text-align: center !important;
        }
        .features-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 2.5rem;
            margin-top: 4rem;
        }
        .feature-card {
            background: #262730;
            border: 1px solid #404040;
            border-radius: 20px;
            padding: 3rem 2.5rem;
            text-align: center;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }
        .feature-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: linear-gradient(90deg, #667eea, #764ba2);
        }
        .feature-card:hover {
            transform: translateY(-8px);
            border-color: #667eea;
            box-shadow: 0 10px 40px rgba(102, 126, 234, 0.2);
        }
        .feature-icon {
            font-size: 4rem;
            margin-bottom: 2rem;
            display: block;
        }
        .feature-title {
            font-size: 1.6rem;
            font-weight: 700;
            color: #ffffff;
            margin-bottom: 1.5rem;
            letter-spacing: -0.5px;
        }
        .feature-description {
            color: #d1d5db;
            font-size: 1.1rem;
            line-height: 1.7;
            font-weight: 400;
            text-align: center !important;
        }
        /* Enhanced How It Works Section */
        .how-it-works {
            padding: 8rem 0;
            background: linear-gradient(135deg, #1a1d29 0%, #0e1117 100%);
        }
        .process-steps {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 4rem;
            margin-top: 5rem;
        }
        .process-step {
            text-align: center;
            position: relative;
        }
        .step-number {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 80px;
            height: 80px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            border-radius: 50%;
            font-size: 2rem;
            font-weight: 800;
            margin-bottom: 2rem;
            box-shadow: 0 4px 20px rgba(102, 126, 234, 0.3);
        }
        .step-title {
            font-size: 1.5rem;
            font-weight: 700;
            color: #ffffff;
            margin-bottom: 1.5rem;
            letter-spacing: -0.5px;
        }
        .step-description {
            color: #d1d5db;
            font-size: 1.1rem;
            line-height: 1.7;
            font-weight: 400;
            text-align: center !important;
        }
        /* Enhanced Technology Section */
        .technology {
            padding: 8rem 0;
            background: #0e1117;
        }
        .tech-content {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 5rem;
            align-items: center;
        }
        .tech-info {
            background: #262730;
            border: 1px solid #404040;
            border-radius: 20px;
            padding: 4rem;
        }
        .tech-title {
            font-size: 2.5rem;
            font-weight: 800;
            color: #ffffff;
            margin-bottom: 2rem;
            letter-spacing: -1px;
        }
        .tech-description {
            color: #d1d5db;
            font-size: 1.2rem;
            line-height: 1.8;
            margin-bottom: 2.5rem;
            font-weight: 400;
            text-align: left !important;
        }
        .tech-features {
            list-style: none;
        }
        .tech-features li {
            color: #d1d5db;
            margin-bottom: 1rem;
            padding-left: 2rem;
            position: relative;
            font-size: 1.1rem;
            font-weight: 500;
        }
        .tech-features li::before {
            content: '✓';
            position: absolute;
            left: 0;
            color: #22c55e;
            font-weight: bold;
            font-size: 1.2rem;
        }
        .stats-preview {
            background: #262730;
            border: 1px solid #404040;
            border-radius: 20px;
            padding: 3rem;
        }
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 2.5rem;
        }
        .stat-item {
            text-align: center;
        }
        .stat-number {
            font-size: 3rem;
            font-weight: 800;
            color: #667eea;
            display: block;
            margin-bottom: 0.75rem;
        }
        .stat-number.fraud {
            color: #ef4444;
        }
        .stat-number.safe {
            color: #22c55e;
        }
        .stat-label {
            font-size: 1rem;
            color: #d1d5db;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        /* Enhanced About Section */
        .about {
            padding: 8rem 0;
            background: linear-gradient(135deg, #1a1d29 0%, #0e1117 100%);
        }
        .about-content {
            max-width: 900px;
            margin: 0 auto;
            text-align: center;
        }
        .about-text {
            font-size: 1.3rem;
            color: #d1d5db;
            line-height: 1.8;
            margin-bottom: 2.5rem;
            font-weight: 400;
            text-align: center !important;
        }
        .about-text strong {
            color: #ffffff;
            font-weight: 700;
        }
        .university-badge {
            display: inline-block;
            background: rgba(102, 126, 234, 0.15);
            border: 1px solid rgba(102, 126, 234, 0.4);
            color: #667eea;
            padding: 1.5rem 3rem;
            border-radius: 16px;
            font-weight: 700;
            margin-top: 3rem;
            font-size: 1.1rem;
            backdrop-filter: blur(10px);
        }
        /* Enhanced Responsive Design */
        @media (max-width: 768px) {
            .container {
                padding: 0 1rem;
            }
            .hero-title {
                font-size: 4.5rem;
                letter-spacing: -2px;
            }
            .hero-subtitle {
                font-size: 1.3rem;
            }
            .section-title {
                font-size: 2.5rem;
            }
            .tech-content {
                grid-template-columns: 1fr;
                gap: 3rem;
            }
            .features-grid {
                grid-template-columns: 1fr;
            }
            .process-steps {
                grid-template-columns: 1fr;
                gap: 3rem;
            }
            .stats-grid {
                grid-template-columns: 1fr;
                gap: 2rem;
            }
            .feature-description, .step-description, .tech-description, .about-text {
                font-size: 1rem;
            }
        }
        @media (max-width: 480px) {
            .hero-title {
                font-size: 3.5rem;
                letter-spacing: -1px;
            }
            .hero-subtitle {
                font-size: 1.1rem;
            }
            .feature-card,
            .tech-info,
            .stats-preview {
                padding: 2rem;
            }
            .section-title {
                font-size: 2rem;
            }
        }
        </style>
        <section class="hero">
            <div class="container">
                <div class="hero-content">
                    <h1 class="hero-title">CredSight</h1>
                    <p class="hero-subtitle">
                        Powered by ERGCN machine learning model to analyze transaction data and detect fraudulent activities
                    </p>
                </div>
            </div>
        </section>
        """,
        unsafe_allow_html=True
    )

    # Render the rest of the enhanced HTML
    st.markdown(
        """
        <section class="features">
            <div class="container">
                <div class="section-header">
                    <h2 class="section-title">Key Features</h2>
                    <p class="section-description">
                        Comprehensive fraud detection capabilities designed for accuracy and ease of use
                    </p>
                </div>
                <div class="features-grid">
                    <div class="feature-card">
                        <span class="feature-icon">⚙️</span>
                        <h3 class="feature-title">CSV Data Processing</h3>
                        <p class="feature-description">
                            Upload your transaction data in CSV format with TransactionID column for instant analysis and fraud detection.
                        </p>
                    </div>
                    <div class="feature-card">
                        <span class="feature-icon">🤖</span>
                        <h3 class="feature-title">ERGCN ML Model</h3>
                        <p class="feature-description">
                            Advanced machine learning model specifically trained for fraud detection with high accuracy and low false positive rates.
                        </p>
                    </div>
                    <div class="feature-card">
                        <span class="feature-icon">⚡</span>
                        <h3 class="feature-title">Real-time Analysis</h3>
                        <p class="feature-description">
                            Get instant fraud predictions and comprehensive statistics overview with filtering options for detailed analysis.
                        </p>
                    </div>
                    <div class="feature-card">
                        <span class="feature-icon">📈</span>
                        <h3 class="feature-title">Statistical Insights</h3>
                        <p class="feature-description">
                            Detailed statistics including fraud rates, case counts, and comprehensive data visualization for informed decisions.
                        </p>
                    </div>
                </div>
            </div>
        </section>
        """,
        unsafe_allow_html=True
    )

    # --- CTA and Go to Dashboard Button (centered, prominent) ---
    cta_col = st.columns([1,2,1])[1]
    with cta_col:
        st.markdown('<p class="cta-text" style="margin-top: 0.5rem; margin-bottom: 0.5rem; font-size:1.4rem; font-weight:700; text-align:center;">Ready to analyze your transaction data?</p>', unsafe_allow_html=True)
        go_dashboard = st.button("Go to Dashboard", key="hero_dashboard_btn")
        st.markdown("<div style='height:2.5rem;'></div>", unsafe_allow_html=True)
    if go_dashboard:
        st.switch_page("dashboard.py")

    # Enhanced button styling (make it more prominent and properly centered)
    st.markdown(
        """
        <style>
        div[data-testid="column"] .stButton > button#hero_dashboard_btn,
        .stButton > button#hero_dashboard_btn {
            display: block !important;
            margin: 0 auto !important;
            font-size: 1.6rem !important;
            padding: 1.2rem 3.5rem !important;
            border-radius: 16px !important;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
            color: #fff !important;
            border: none !important;
            font-weight: 800 !important;
            box-shadow: 0 6px 28px rgba(102,126,234,0.35) !important;
            transition: all 0.3s ease !important;
            text-transform: uppercase !important;
            letter-spacing: 1.5px !important;
            min-width: 320px !important;
            width: auto !important;
            text-align: center !important;
        }
        div[data-testid="column"] .stButton > button#hero_dashboard_btn:hover,
        .stButton > button#hero_dashboard_btn:hover {
            background: linear-gradient(135deg, #764ba2 0%, #667eea 100%) !important;
            color: #fff !important;
            transform: translateY(-3px) scale(1.04) !important;
            box-shadow: 0 10px 36px rgba(102,126,234,0.45) !important;
        }
        div[data-testid="column"] .stButton,
        .stButton {
            display: flex !important;
            justify-content: center !important;
            align-items: center !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Render the rest of the enhanced HTML
    st.markdown(
        """
        <section class="how-it-works">
            <div class="container">
                <div class="section-header">
                    <h2 class="section-title">How It Works</h2>
                    <p class="section-description">
                        Simple three-step process to analyze your transaction data for fraud detection
                    </p>
                </div>
                <div class="process-steps">
                    <div class="process-step">
                        <div class="step-number">1</div>
                        <h3 class="step-title">Upload Data</h3>
                        <p class="step-description">
                            Upload your CSV file containing transaction data with TransactionID column
                        </p>
                    </div>
                    <div class="process-step">
                        <div class="step-number">2</div>
                        <h3 class="step-title">ML Analysis</h3>
                        <p class="step-description">
                            ERGCN model processes each transaction and generates fraud probability scores
                        </p>
                    </div>
                    <div class="process-step">
                        <div class="step-number">3</div>
                        <h3 class="step-title">View Results</h3>
                        <p class="step-description">
                            Get detailed results with filtering options and comprehensive statistics overview
                        </p>
                    </div>
                </div>
            </div>
        </section>
        <section class="technology">
            <div class="container">
                <div class="tech-content">
                    <div class="tech-info">
                        <h2 class="tech-title">ERGCN Technology</h2>
                        <p class="tech-description">
                            Our fraud detection system utilizes the Enhanced Relational Graph Convolutional Network (ERGCN) model, 
                            specifically designed for financial fraud detection with superior performance in identifying complex fraud patterns.
                        </p>
                        <ul class="tech-features">
                            <li>Advanced graph neural network architecture</li>
                            <li>High accuracy fraud detection</li>
                            <li>Low false positive rates</li>
                            <li>Real-time processing capabilities</li>
                            <li>Scalable for large datasets</li>
                        </ul>
                    </div>
                    <div class="stats-preview">
                        <h3 class="section-title" style="font-size: 1.8rem; margin-bottom: 2rem; text-align: center;">Sample Results</h3>
                        <div class="stats-grid">
                            <div class="stat-item">
                                <span class="stat-number">1,000</span>
                                <div class="stat-label">Total Records</div>
                            </div>
                            <div class="stat-item">
                                <span class="stat-number fraud">284</span>
                                <div class="stat-label">Fraud Cases</div>
                            </div>
                            <div class="stat-item">
                                <span class="stat-number safe">716</span>
                                <div class="stat-label">Legitimate</div>
                            </div>
                            <div class="stat-item">
                                <span class="stat-number">28.4%</span>
                                <div class="stat-label">Fraud Rate</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <section class="about">
            <div class="container">
                <div class="about-content">
                    <h2 class="section-title">About This Project</h2>
                    <p class="about-text">
                        This fraud detection dashboard was developed as part of the <strong>Software Engineering 1</strong> course 
                        at <strong>Polytechnic University of the Philippines</strong>. The project demonstrates the practical 
                        application of machine learning in financial technology, combining advanced algorithms with user-friendly 
                        interface design.
                    </p>
                </div>
            </div>
        </section>
        """,
        unsafe_allow_html=True
    )

# <div class="university-badge">
#     🎓 Polytechnic University of the Philippines<br>
#     Software Engineering 1 Project
# </div>