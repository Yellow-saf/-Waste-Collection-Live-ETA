# Waste Collection Live ETA System

## Project Overview

The Waste Collection Live ETA System is designed to provide more reliable Estimated Time of Arrival (ETA) for waste collection services.

A fixed ETA can become inaccurate due to changing traffic, collection time, route conditions, and operational workload. This project addresses this problem by dynamically updating ETA based on operational conditions.

## Problem Statement

Waste collection services may face delays because of:

- Heavy traffic
- Longer collection/dwell time
- Route changes or blockage
- High operational workload

These factors can make the planned ETA inaccurate and may cause customer waiting and status enquiries.

## Proposed Solution

The system calculates a dynamic ETA by considering:

- Traffic delay
- Collection/dwell time
- Route conditions
- Operational conditions

A Streamlit dashboard is used to display the project results and operational information.

## Current Progress – Review 1 (~35%)

The current milestone focuses on the core functionality of the project.

### Completed

- Problem identification and project planning
- Synthetic dataset generation
- Data preprocessing and validation
- Baseline ETA calculation
- Dynamic ETA calculation
- Traffic condition handling
- Collection/dwell-time handling
- Route-condition handling
- Workload monitoring
- ETA error analysis
- MAE and RMSE evaluation
- Basic failure-case analysis
- Customer notification simulation
- Working Streamlit prototype

## Evaluation Results

The system was evaluated using a 1,000-record experimental dataset.

| Metric | Baseline ETA | Dynamic ETA |
|---|---:|---:|
| MAE | 15.96 min | 3.35 min |
| RMSE | 18.18 min | 4.08 min |
| Accuracy within 5 min | 7.30% | 76.30% |
| Accuracy within 10 min | 29.30% | 100.00% |

The dynamic ETA approach achieved approximately 79% improvement in ETA error compared with the baseline on the experimental dataset.

## Technology Stack

- Python
- Pandas
- NumPy
- Streamlit
- Plotly
- Jupyter Notebook
- VS Code
- GitHub

## Project Structure

```text
Waste-Collection-Live-ETA/
│
├── Waste_Collection_Review1_35Percent.ipynb
└── README.md
