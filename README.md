🚛 Waste Collection Live ETA System

📌 Project Overview

The Waste Collection Live ETA System is designed to provide more reliable Estimated Time of Arrival (ETA) for waste collection services.

In a traditional system, a fixed or planned ETA may become inaccurate because of changing operational conditions such as:

* 🚦 Traffic conditions
* 🗑️ Collection/dwell time
* 🛣️ Route changes or blockages
* 🚛 Vehicle workload
* 📍 Operational conditions

This project combines a Rule-Based Dynamic ETA approach with Machine Learning to improve ETA accuracy.

⸻

🎯 Problem Statement

Waste collection vehicles may not reach customers at the planned time because real-world operational conditions change during collection.

A fixed ETA does not sufficiently consider these changes, which can lead to:

* Incorrect arrival-time information
* Customer waiting
* Increased status enquiries
* Poor service visibility
* Operational uncertainty

Proposed Solution

The system considers operational factors and calculates a more realistic ETA.

The project follows a hybrid approach:

Planned ETA → Dynamic ETA → ML Correction → Hybrid ETA

⸻

💡 Key Features

1. Baseline ETA

The initial planned ETA is calculated using the expected travel and collection time.

2. Dynamic ETA

The system adjusts the planned ETA using:

* Traffic delay
* Collection/dwell-time delay
* Route delay

3. Hybrid Machine Learning ETA

A Gradient Boosting Regressor is used to learn the remaining ETA error and provide an ML-based correction to the Dynamic ETA.

The final approach is:

Hybrid ML ETA
      =
Dynamic ETA + ML Error Correction

4. Live ETA Simulator

The Streamlit application allows users to simulate different operational conditions such as:

* Traffic level
* Route condition
* Vehicle workload
* Expected collection time
* Current collection time

The simulator provides an updated ETA and operational alert.

5. Operational Alerts

The prototype generates alerts based on estimated delay, such as:

* ETA Updated
* Delay Update
* Major Delay
* On Schedule

6. Performance Evaluation

The system evaluates ETA performance using:

* MAE (Mean Absolute Error)
* RMSE (Root Mean Squared Error)
* Accuracy within 5 minutes
* Accuracy within 10 minutes
* ETA error improvement

⸻

📊 Review 2 Results

The current prototype was evaluated on a synthetic dataset containing 1,000 records.

Metric	Baseline ETA	Dynamic ETA	Hybrid ML ETA
MAE	15.96 min	3.35 min	1.73 min
RMSE	18.18 min	4.08 min	Not reported
Accuracy within 10 min	29.30%	100%	Not reported

Key Improvements

* Dynamic ETA reduced ETA error by approximately 79% compared with the baseline.
* Hybrid ML ETA achieved an MAE of approximately 1.73 minutes on the experimental dataset.
* A Streamlit dashboard has been implemented.
* A Live ETA Simulator is available for testing different traffic, route, and workload conditions.

These results are based on synthetic experimental data and require validation with real-world operational data.

⸻

🚀 Review 2 Progress

Approximately 70% of the planned project scope has been completed.

Completed

* Baseline ETA calculation
* Dynamic ETA calculation
* Traffic condition handling
* Collection/dwell-time handling
* Route condition handling
* Workload analysis
* ETA error evaluation
* Hybrid ML ETA
* Gradient Boosting ML correction
* Streamlit dashboard
* Live ETA Simulator
* Operational alerts
* Performance comparison

Remaining Work

* Real-time GPS integration
* Live traffic API
* Real-world historical data
* Real-time route optimization
* Production database/backend
* SMS/push notification integration
* Cloud deployment
* Advanced testing and optimization

⸻

⚠️ Current Limitations

The current system is a working prototype.

* The dataset is currently synthetic.
* Real-time GPS is not yet integrated.
* Live traffic API is not yet integrated.
* Customer notifications are currently simulated.
* Production deployment is not yet completed.

The Live ETA Simulator is a simulation of live operational conditions, not a real GPS-based tracking system.
