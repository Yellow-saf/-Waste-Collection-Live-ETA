# 🚛 Waste Collection Live ETA System

## 📌 Project Overview

The **Waste Collection Live ETA System** is designed to provide more reliable Estimated Time of Arrival (ETA) for waste collection services.

In a traditional system, a fixed or planned ETA may become inaccurate because of changing operational conditions such as:

- 🚦 Traffic conditions
- 🗑️ Collection/dwell time
- 🛣️ Route changes or blockages
- 🚛 Vehicle workload
- 📍 Operational conditions

This project combines a **Rule-Based Dynamic ETA** approach with **Machine Learning** to improve ETA accuracy.

---

## 🎯 Problem Statement

Waste collection vehicles may not reach customers at the planned time because real-world operational conditions change during collection.

A fixed ETA does not sufficiently consider these changes, which can lead to:

- Incorrect arrival-time information
- Customer waiting
- Increased status enquiries
- Poor service visibility
- Operational uncertainty

### Proposed Solution

The system continuously considers operational factors and calculates a more realistic ETA.

The project follows a hybrid approach:

**Planned ETA → Dynamic ETA → ML Correction → Hybrid ETA**

---

## 💡 Key Features

### 1. Baseline ETA

The initial planned ETA is calculated using the expected travel and collection time.

### 2. Dynamic ETA

The system adjusts the planned ETA using:

- Traffic delay
- Collection/dwell-time delay
- Route delay

### 3. Hybrid Machine Learning ETA

A **Gradient Boosting Regressor** is used to learn the remaining ETA error and provide an ML-based correction to the Dynamic ETA.

The final approach is:

```text
Hybrid ML ETA
      =
Dynamic ETA + ML Error Correction
