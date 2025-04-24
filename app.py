import streamlit as st
import numpy as np
import scipy.stats as stats
import plotly.graph_objects as go

# --- Page Configuration ---
st.set_page_config(
    page_title="Distribution Explorer",
    page_icon="📊",
    layout="wide"
)

# --- Title and Intro ---
st.title("📊 Interactive Distribution Explorer")
st.markdown("""
Explore the Normal and Skew-Normal distributions by adjusting their parameters.
See how changing the mean, standard deviation, and skewness affects the shape
and characteristics of the distribution.
""")

# --- Sidebar for Controls ---
st.sidebar.header("⚙️ Distribution Parameters")

# Sample Size
n_samples = st.sidebar.slider(
    "Number of Samples (N)",
    min_value=100,
    max_value=10000,
    value=2000,
    step=100,
    help="Number of random data points to generate for the histogram."
)

# Skewness Parameter (alpha) for Skew-Normal
# a=0 corresponds to a standard normal distribution
skew_param = st.sidebar.slider(
    "Skewness Parameter (α)",
    min_value=-10.0,
    max_value=10.0,
    value=0.0,  # Start with a normal distribution
    step=0.1,
    help="Controls the skewness. α=0 results in a Normal distribution. α>0 means right-skewed, α<0 means left-skewed."
)

# Location Parameter (Mean for Normal, related to mean for Skew-Normal)
loc_param = st.sidebar.slider(
    "Location Parameter (ξ)",
    min_value=-10.0,
    max_value=10.0,
    value=0.0,
    step=0.1,
    help="Represents the location (center) of the distribution. For α=0, this is the Mean (μ)."
)

# Scale Parameter (Standard Deviation for Normal, related for Skew-Normal)
scale_param = st.sidebar.slider(
    "Scale Parameter (ω)",
    min_value=0.1,
    max_value=10.0,
    value=1.0,
    step=0.1,
    help="Represents the spread of the distribution. For α=0, this is the Standard Deviation (σ)."
)

# --- Data Generation and Calculations ---

# Generate random samples from the skew-normal distribution
# Note: For skewnorm, 'loc' is the location parameter (xi) and 'scale' is the scale parameter (omega).
# The mean and std dev of the *resulting* skewed distribution are different from loc and scale when skew_param != 0.
generated_data = stats.skewnorm.rvs(a=skew_param, loc=loc_param, scale=scale_param, size=n_samples)

# Calculate actual statistics from the generated sample
sample_mean = np.mean(generated_data)
sample_std_dev = np.std(generated_data)
sample_skewness = stats.skew(generated_data)
sample_median = np.median(generated_data)

# --- Create the Plot ---
fig = go.Figure()

# 1. Histogram of generated data
fig.add_trace(go.Histogram(
    x=generated_data,
    name='Sample Data',
    histnorm='probability density', # Normalize histogram to compare with PDF
    marker_color='#1f77b4', # Blue color
    opacity=0.7
))

# 2. Theoretical Probability Density Function (PDF)
# Create a range of x values for plotting the PDF curve
x_min = min(generated_data.min(), loc_param - 4*scale_param) # Adjust range based on data and params
x_max = max(generated_data.max(), loc_param + 4*scale_param)
x_pdf = np.linspace(x_min, x_max, 500)
pdf_values = stats.skewnorm.pdf(x_pdf, a=skew_param, loc=loc_param, scale=scale_param)

fig.add_trace(go.Scatter(
    x=x_pdf,
    y=pdf_values,
    mode='lines',
    name='Theoretical PDF',
    line=dict(color='red', width=2)
))

# --- Add Mean/Median Lines ---
fig.add_vline(
    x=sample_mean, line_width=2, line_dash="dash", line_color="orange",
    annotation_text=f"Mean: {sample_mean:.2f}", annotation_position="top right"
)
fig.add_vline(
    x=sample_median, line_width=2, line_dash="dot", line_color="green",
    annotation_text=f"Median: {sample_median:.2f}", annotation_position="top left"
)


# Update layout for clarity
distribution_name = "Normal" if abs(skew_param) < 0.01 else "Skew-Normal"
fig.update_layout(
    title=f'{distribution_name} Distribution (α={skew_param:.1f}, ξ={loc_param:.1f}, ω={scale_param:.1f})',
    xaxis_title='Value',
    yaxis_title='Density',
    legend_title_text='Components',
    bargap=0.1, # Gap between bars in histogram
)

# --- Display Plot and Statistics ---
st.plotly_chart(fig, use_container_width=True)

st.subheader("📊 Sample Statistics (Calculated from Generated Data)")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Sample Mean", f"{sample_mean:.3f}")
col2.metric("Sample Median", f"{sample_median:.3f}")
col3.metric("Sample Std Dev", f"{sample_std_dev:.3f}")
col4.metric("Sample Skewness", f"{sample_skewness:.3f}")

# --- Explanations ---
st.markdown("---")
st.subheader("💡 Parameter Explanations")
st.markdown(f"""
*   **Location (ξ):** `{loc_param:.1f}` - Roughly determines the center of the distribution. For a perfect Normal distribution (α=0), this *is* the Mean (μ).
*   **Scale (ω):** `{scale_param:.1f}` - Controls the spread or width. For a perfect Normal distribution (α=0), this *is* the Standard Deviation (σ). Must be positive.
*   **Skewness (α):** `{skew_param:.1f}` - Controls the asymmetry.
    *   `α = 0`: Symmetric (Normal Distribution). Mean ≈ Median.
    *   `α > 0`: Positively skewed (Right Skew). Tail extends to the right. Mean > Median.
    *   `α < 0`: Negatively skewed (Left Skew). Tail extends to the left. Mean < Median.
*   **Number of Samples (N):** `{n_samples}` - The number of data points generated. Larger N generally makes the histogram closer to the theoretical PDF.

**Note:** For skewed distributions (α ≠ 0), the final *Sample Mean*, *Sample Std Dev*, and *Sample Skewness* calculated from the data will differ from the input `ξ`, `ω`, and `α` parameters due to the nature of the skew-normal transformation. The plot shows both the generated data (histogram) and the theoretical shape (red line).
""")

st.sidebar.markdown("---")
st.sidebar.info("Adjust the sliders to see how the distribution changes!")