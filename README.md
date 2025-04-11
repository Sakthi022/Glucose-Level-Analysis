
# Glucose Level Analysis using Acetone Sensor

This project focuses on analysing and predicting blood glucose levels based on the output values from the MQ-138 Acetone Sensor using breath analysis.

## Project Flow

1. Acetone Sensor Data (MQ-138) Collected
2. AI Model (Linear Regression) for Glucose Estimation
3. R-Squared Testing for Model Accuracy

## Sample Dataset (Observation Based)

| Sensor Reading | Approx Glucose (mg/dL) |
|----------------|------------------------|
| 350 - 390      | 70 - 90                |
| 390 - 430      | 90 - 110               |
| 430 - 470      | 110 - 140              |
| 470 - 520+     | 140+                   |

## Python Libraries Used
- numpy
- matplotlib
- sklearn

## How To Run

```
python glucose_analysis.py
```

## Output
- AI Predicted Glucose Graph
- R-Squared Accuracy Score

## Note
This is an experimental model for research purposes. Accuracy may vary based on real-time sensor data and environmental conditions.

## Credits
Developed by Sakthi  
Biomedical Engineering | NexGenbme  
Final Year Project - Non-Invasive Glucose Monitoring using Breath Analysis
