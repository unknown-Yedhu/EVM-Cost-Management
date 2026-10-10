# EVM Cost Management & AI-Based Anomaly Detection System

## 1. Project Overview

The **EVM Cost Management & AI-Based Anomaly Detection System** is a Python-based project developed to analyze software project cost performance, schedule performance, and potential risks using Earned Value Management (EVM) techniques and machine learning.

The system processes project data across eight sprints and calculates key performance indicators, including Cost Variance (CV), Schedule Variance (SV), Cost Performance Index (CPI), and Schedule Performance Index (SPI).

It also forecasts the expected project completion cost using Estimate at Completion (EAC) and Estimate to Complete (ETC). Additionally, the system uses the **Isolation Forest algorithm** to identify unusual cost and schedule performance patterns that may indicate project risks.

This project demonstrates how traditional project management techniques can be combined with machine learning to support project monitoring and risk identification.

## 2. Student Information

- **Student Name:** Yedhu Krishnan TA
- **Student ID:** CU23BCA0068A
- **Course:** Bachelor of Computer Applications (BCA)
- **Subject:** Software Project Management
- **Assignment:** EVM in Cost Management
- **Project Type:** Python-Based EVM Analysis and AI Anomaly Detection

## 3. Objectives

The main objectives of this project are:

- Calculate cost and schedule variances using EVM formulas.
- Evaluate project cost efficiency using CPI.
- Analyze schedule performance using SPI.
- Compare performance across multiple project sprints.
- Forecast the expected total project cost.
- Calculate Estimate at Completion (EAC) and Estimate to Complete (ETC).
- Apply machine learning to detect unusual project performance.
- Identify potential cost overruns and schedule delays.
- Generate a structured report of analysis results.

## 4. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Dataset processing and numerical calculations |
| Scikit-learn | Machine learning and anomaly detection |
| Isolation Forest | Identifying unusual EVM performance patterns |
| CSV | Storing input data and analysis results |
| Visual Studio Code | Development environment |
| Git and GitHub | Version control and project hosting |

## 5. Project Structure

```text
EVM-Cost-Management/
│
├── dataset.csv
│   └── Input dataset containing EVM data for eight sprints
│
├── evm_analysis.py
│   └── Main program for EVM calculations,
│       cost forecasting, and anomaly detection
│
├── evm_analysis_results.csv
│   └── Generated analysis results
│
├── requirements.txt
│   └── Required Python packages
│
├── README.md
│   └── Project documentation
│
├── .gitignore
│   └── Files and folders excluded from Git
│
└── .venv/
    └── Local Python virtual environment (not uploaded)
```

## 6. Earned Value Management (EVM) Metrics

The system calculates the following metrics from the project dataset.

### 6.1 Cost Variance (CV)

Cost Variance measures the difference between the value of work completed and the actual cost incurred.

**Formula:**

```text
CV = EV - AC
```

- Positive CV: Under budget.
- Negative CV: Over budget.
- Zero CV: On budget.

### 6.2 Schedule Variance (SV)

Schedule Variance measures the difference between earned value and planned value.

**Formula:**

```text
SV = EV - PV
```

- Positive SV: Ahead of schedule in earned-value terms.
- Negative SV: Behind schedule.
- Zero SV: On schedule.

### 6.3 Cost Performance Index (CPI)

CPI measures how efficiently the project uses its budget.

**Formula:**

```text
CPI = EV / AC
```

- CPI greater than 1: Favorable cost efficiency.
- CPI less than 1: Unfavorable cost efficiency.
- CPI equal to 1: Cost efficiency is on target.

### 6.4 Schedule Performance Index (SPI)

SPI measures progress relative to the planned work.

**Formula:**

```text
SPI = EV / PV
```

- SPI greater than 1: Ahead of schedule.
- SPI less than 1: Behind schedule.
- SPI equal to 1: On schedule.

**Abbreviations:**

- **PV:** Planned Value
- **EV:** Earned Value
- **AC:** Actual Cost

## 7. EVM Cost Forecasting

The system uses EVM forecasting formulas to estimate the expected project cost.

### 7.1 Budget at Completion (BAC)

BAC represents the total planned budget for the project. In this implementation, it is calculated as the sum of the planned values across the dataset.

### 7.2 Estimate at Completion (EAC)

EAC estimates the total project cost at completion, assuming the current cost performance continues.

**Formula used:**

```text
EAC = BAC / CPI
```

Where the overall CPI is calculated using total earned value divided by total actual cost.

### 7.3 Estimate to Complete (ETC)

ETC estimates the additional cost required to complete the remaining work.

**Formula used:**

```text
ETC = EAC - AC
```

These forecasts help project managers understand whether the project is likely to exceed its planned budget.

## 8. AI-Based Anomaly Detection

The project implements **Isolation Forest**, an unsupervised machine learning algorithm available in Scikit-learn.

The algorithm analyzes EVM performance indicators to identify observations that differ significantly from the other sprint records.

### Features used

- Cost Variance (CV)
- Schedule Variance (SV)
- Cost Performance Index (CPI)
- Schedule Performance Index (SPI)

### Working process

1. Load the sprint dataset.
2. Calculate the EVM metrics.
3. Prepare the performance indicators for analysis.
4. Apply the Isolation Forest algorithm.
5. Identify observations classified as anomalies.
6. Display the flagged sprints and their performance values.
7. Save the analysis results to a CSV file.

The algorithm identifies unusual patterns; it does not automatically prove that a sprint contains an actual project failure. Flagged sprints should be investigated by the project manager.

## 9. Implementation Workflow

```text
Start
  |
  v
Load EVM Dataset
  |
  v
Calculate CV and SV
  |
  v
Calculate CPI and SPI
  |
  v
Analyze Cost and Schedule Status
  |
  v
Calculate EAC and ETC
  |
  v
Apply Isolation Forest
  |
  v
Identify Unusual Sprint Performance
  |
  v
Display Results
  |
  v
Export Results to CSV
  |
  v
End
```

## 10. Installation and Execution

### Prerequisites

- Python 3.13 or a compatible Python version
- Visual Studio Code
- Required Python packages
- Git (optional, for version control)

### Step 1: Clone the Repository

```bash
git clone https://github.com/unknown-Yedhu/EVM-Cost-Management.git
```

### Step 2: Open the Project Folder

```bash
cd EVM-Cost-Management
```

### Step 3: Create a Virtual Environment

```bash
python -m venv .venv
```

### Step 4: Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Step 5: Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 6: Run the Program

```bash
python evm_analysis.py
```

After execution, the program displays the EVM analysis, cost forecast, project health summary, and AI anomaly detection results in the terminal.

The generated results are saved to `evm_analysis_results.csv`.

## 11. Results and Findings

The program was executed successfully using the eight-sprint dataset.

### EVM analysis findings

- Some sprints show favorable cost performance, while others show cost overruns.
- The schedule variance is negative across all eight sprints.
- Sprint 8 has particularly poor cost and schedule performance.
- The overall CPI is approximately **0.921**, indicating unfavorable cost efficiency.
- The estimated completion cost is approximately **$1,477,049.18**.
- The estimated additional cost to complete is approximately **$152,049.18**.

### AI anomaly detection findings

The current execution flagged the following sprints:

| Sprint | Cost Variance (CV) | Schedule Variance (SV) | CPI | SPI |
|---|---:|---:|---:|---:|
| Sprint 4 | -20,000 | -25,000 | 0.871 | 0.844 |
| Sprint 8 | -70,000 | -60,000 | 0.720 | 0.750 |

These sprints show unusual performance patterns in the current dataset and should be investigated for possible cost and schedule risks.

The anomaly results depend on the dataset and the Isolation Forest configuration.

## 12. Conclusion

The EVM Cost Management & AI-Based Anomaly Detection System demonstrates the use of traditional Earned Value Management techniques and machine learning in software project monitoring.

The system calculates cost and schedule variances, evaluates performance indexes, forecasts project completion costs, and identifies unusual sprint performance using Isolation Forest.

The results show how EVM metrics can help assess project health, while anomaly detection can highlight areas that require further investigation.

This project provides practical experience in Python programming, cost management, project performance analysis, forecasting, and machine learning.

## 13. Future Enhancements

Possible future improvements include:

- Develop an interactive dashboard for EVM metrics.
- Add charts showing CPI and SPI trends across sprints.
- Allow users to upload their own project datasets.
- Compare multiple forecasting methods.
- Tune and evaluate anomaly detection models using labeled or additional historical data.
- Generate downloadable PDF reports.
- Add recommendations to help project managers investigate flagged risks.

## 14. Repository

**GitHub Repository:**  
https://github.com/unknown-Yedhu/EVM-Cost-Management

---

*Developed by Yedhu Krishnan TA as part of the Software Project Management assignment on Earned Value Management in Cost Management.*
