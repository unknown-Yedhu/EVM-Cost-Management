import pandas as pd
from sklearn.ensemble import IsolationForest


# =========================================================
# AI-BASED EVM COST MANAGEMENT & ANOMALY DETECTION SYSTEM
# =========================================================

print("\n" + "=" * 65)
print("        EVM COST MANAGEMENT & ANOMALY DETECTION SYSTEM")
print("=" * 65)
print("Student: Yedhu Krishnan TA")


# =========================================================
# 1. LOAD DATASET
# =========================================================

data = pd.read_csv("dataset.csv")


# =========================================================
# 2. EVM VARIANCE CALCULATION
# =========================================================

data["CV"] = data["EV"] - data["AC"]
data["SV"] = data["EV"] - data["PV"]


# =========================================================
# 3. PERFORMANCE INDEX CALCULATION
# =========================================================

data["CPI"] = data["EV"] / data["AC"]
data["SPI"] = data["EV"] / data["PV"]


# =========================================================
# 4. BUDGET STATUS
# =========================================================

def budget_status(cv):
    if cv > 0:
        return "Under Budget"
    elif cv < 0:
        return "Over Budget"
    else:
        return "On Budget"


# =========================================================
# 5. SCHEDULE STATUS
# =========================================================

def schedule_status(sv):
    if sv > 0:
        return "Ahead of Schedule"
    elif sv < 0:
        return "Behind Schedule"
    else:
        return "On Schedule"


data["Budget Status"] = data["CV"].apply(budget_status)
data["Schedule Status"] = data["SV"].apply(schedule_status)


# =========================================================
# 6. DISPLAY EVM ANALYSIS
# =========================================================

print("\n")
print("=" * 65)
print("                    EVM ANALYSIS")
print("=" * 65)

display_columns = [
    "Sprint",
    "PV",
    "EV",
    "AC",
    "CV",
    "SV",
    "CPI",
    "SPI",
    "Budget Status",
    "Schedule Status"
]

print(data[display_columns].to_string(index=False))


# =========================================================
# 7. EVM FORECASTING
# =========================================================

print("\n")
print("=" * 65)
print("                  EVM FORECASTING")
print("=" * 65)

# Budget at Completion
BAC = data["PV"].sum()

# Total project values
total_EV = data["EV"].sum()
total_AC = data["AC"].sum()

# Overall CPI
overall_CPI = total_EV / total_AC

# Estimate at Completion
EAC = BAC / overall_CPI

# Estimate to Complete
ETC = EAC - total_AC


print(f"\nBudget at Completion (BAC): ${BAC:,.2f}")
print(f"Total Earned Value (EV):    ${total_EV:,.2f}")
print(f"Total Actual Cost (AC):     ${total_AC:,.2f}")
print(f"Overall CPI:                {overall_CPI:.3f}")
print(f"Estimate at Completion:     ${EAC:,.2f}")
print(f"Estimate to Complete:       ${ETC:,.2f}")


# =========================================================
# 8. PROJECT HEALTH SUMMARY
# =========================================================

print("\n")
print("=" * 65)
print("                 PROJECT HEALTH SUMMARY")
print("=" * 65)

if overall_CPI < 1:
    print("Cost Performance: OVER BUDGET / COST INEFFICIENCY")
elif overall_CPI > 1:
    print("Cost Performance: UNDER BUDGET / COST EFFICIENT")
else:
    print("Cost Performance: ON BUDGET")

overall_SPI = total_EV / data["PV"].sum()

if overall_SPI < 1:
    print("Schedule Performance: BEHIND SCHEDULE")
elif overall_SPI > 1:
    print("Schedule Performance: AHEAD OF SCHEDULE")
else:
    print("Schedule Performance: ON SCHEDULE")


# =========================================================
# 9. AI ANOMALY DETECTION
# =========================================================

print("\n")
print("=" * 65)
print("               AI ANOMALY DETECTION")
print("=" * 65)

# Features used by the AI model
features = data[["CV", "SV", "CPI", "SPI"]]

# Create Isolation Forest model
model = IsolationForest(
    contamination=0.25,
    random_state=42
)

# Train the model
data["Anomaly"] = model.fit_predict(features)

# Convert model output into readable labels
data["Anomaly Status"] = data["Anomaly"].apply(
    lambda x: "Anomaly" if x == -1 else "Normal"
)


# Display anomaly results
anomaly_columns = [
    "Sprint",
    "CV",
    "SV",
    "CPI",
    "SPI",
    "Anomaly Status"
]

print(data[anomaly_columns].to_string(index=False))


# =========================================================
# 10. DISPLAY FLAGGED RISKS
# =========================================================

print("\n")
print("=" * 65)
print("                    FLAGGED RISKS")
print("=" * 65)

anomalies = data[data["Anomaly"] == -1]

if len(anomalies) > 0:
    print("\nPotentially unusual project performance detected:\n")

    for _, row in anomalies.iterrows():
        print(
            f"{row['Sprint']}: "
            f"CV={row['CV']:.0f}, "
            f"SV={row['SV']:.0f}, "
            f"CPI={row['CPI']:.3f}, "
            f"SPI={row['SPI']:.3f}"
        )
else:
    print("\nNo significant anomalies detected.")


# =========================================================
# 11. SAVE COMPLETE RESULTS
# =========================================================

data.to_csv("evm_analysis_results.csv", index=False)

print("\n")
print("=" * 65)
print("Analysis results saved to: evm_analysis_results.csv")
print("=" * 65)

print("\nEVM analysis and anomaly detection completed successfully.")