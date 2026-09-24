# EVM Cost Management & AI-Based Anomaly Detection

## Project Overview

This project implements Earned Value Management (EVM) techniques for monitoring software project cost and schedule performance.

The system calculates traditional EVM metrics such as Cost Variance (CV), Schedule Variance (SV), Cost Performance Index (CPI), and Schedule Performance Index (SPI).

It also performs EVM-based forecasting using Estimate at Completion (EAC) and Estimate to Complete (ETC).

Since the student's ID ends with an even number, the project additionally implements an AI-based anomaly detection system using the Isolation Forest algorithm to identify unusual cost and schedule performance.

---

## Student Information

**Student Name:** Yedhu Krishnan TA  
**Student ID:** [Add Student ID]  
**Course:** Software Project Management  
**Assignment:** EVM in Cost Management  

---

## Objectives

The main objectives of this project are:

- Calculate EVM cost and schedule variances.
- Analyze project performance using CPI and SPI.
- Forecast the expected project completion cost.
- Calculate Estimate at Completion (EAC).
- Calculate Estimate to Complete (ETC).
- Detect unusual project performance using AI.
- Identify potential cost and schedule risks.

---

## EVM Metrics

### Cost Variance

CV measures the difference between Earned Value and Actual Cost.

```text
CV = EV - AC