# 📊 Interactive Distribution Explorer

A simple Streamlit web application designed to interactively demonstrate the characteristics of the Normal and Skew-Normal distributions. Users can adjust parameters like mean (location), standard deviation (scale), and skewness to see their immediate effect on the distribution's shape, histogram, and key statistics.

This app is a great educational tool for understanding how these fundamental parameters influence probability distributions.

---

## ✨ Features

*   Visualize **Normal** (when skewness α=0) and **Skew-Normal** distributions.
*   **Interactive sliders** for adjusting:
    *   Location Parameter (ξ) - Related to the mean.
    *   Scale Parameter (ω) - Related to the standard deviation.
    *   Skewness Parameter (α) - Controls the asymmetry.
    *   Number of Samples (N) - For the generated data histogram.
*   **Real-time updates:** The plot and calculated statistics instantly reflect parameter changes.
*   Displays both:
    *   A **histogram** of randomly generated sample data based on the parameters.
    *   The **theoretical Probability Density Function (PDF)** curve.
*   Overlays vertical lines indicating the calculated **Sample Mean** and **Sample Median** on the plot.
*   Shows key **Sample Statistics** calculated from the generated data (Mean, Median, Standard Deviation, Skewness).
*   Built with **Streamlit** for a clean and user-friendly web interface.
*   Uses **Plotly** for interactive and informative charts.

---

## 🛠️ Technology Stack

*   Python 3.x
*   Streamlit
*   NumPy
*   SciPy (for statistical functions like `skewnorm`)
*   Plotly (for creating interactive plots)

---

## 🚀 Getting Started

### Prerequisites

*   Python 3.7 or higher installed.
*   `pip` (Python package installer).

### Installation

1.  **Clone the repository (or download the script):**
    ```bash
    git clone https://github.com/manyan-chan/distribution-explorer.git
    cd distribution-explorer
    ```

2.  **Install the required Python libraries:**
    ```bash
    pip install streamlit numpy scipy plotly
    ```

### Running the App

1.  Navigate to the directory containing the `distribution_explorer.py` script (or whatever you named it).
2.  Run the following command in your terminal:
    ```bash
    streamlit run distribution_explorer.py
    ```
3.  Streamlit will automatically open the application in your default web browser.

---

## 🕹️ How to Use

1.  Once the app is running, you'll see the distribution plot and statistics.
2.  Use the sliders in the **left sidebar** (⚙️ Distribution Parameters) to modify the distribution's characteristics:
    *   **Number of Samples (N):** Adjust the size of the random sample generated for the histogram. Larger values generally make the histogram conform better to the theoretical PDF.
    *   **Skewness Parameter (α):**
        *   Set to `0` for a symmetric Normal distribution.
        *   Positive values (`> 0`) create a right (positive) skew.
        *   Negative values (`< 0`) create a left (negative) skew.
    *   **Location Parameter (ξ):** Shifts the distribution along the x-axis. Roughly corresponds to the mean when skewness is zero.
    *   **Scale Parameter (ω):** Controls the spread or width of the distribution. Roughly corresponds to the standard deviation when skewness is zero. Must be positive.
3.  Observe how the **plot** (histogram shape, PDF curve, mean/median lines) and the calculated **Sample Statistics** update dynamically as you move the sliders.
4.  Hover over the plot elements (bars, lines) for potential tooltips and interactive features provided by Plotly.
5.  Read the **Parameter Explanations** section within the app for more detailed descriptions of `ξ`, `ω`, and `α`.

---

## 🎓 Concepts Demonstrated

This application helps visualize and understand:

*   The characteristics of the **Normal Distribution**.
*   The concept of **Skewness** and how it affects symmetry.
*   The impact of **Mean (Location)** and **Standard Deviation (Scale)** on a distribution's position and spread.
*   The relationship between the **Mean** and **Median** in symmetric vs. skewed distributions.
*   The difference between a **theoretical probability distribution (PDF)** and a **histogram generated from a finite sample**.
