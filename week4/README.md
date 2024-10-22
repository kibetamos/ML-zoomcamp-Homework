# Bank Marketing Prediction

## Overview
This project analyzes a bank marketing dataset to predict if a client will subscribe to a term deposit using logistic regression.

## Steps

1. **Import Libraries**: Loaded necessary libraries for data analysis and model training.
   
2. **Load Data**: Imported the dataset from a CSV file.

3. **Data Preprocessing**: Selected relevant columns and encoded the target variable.

4. **Train-Validation-Test Split**: Split the dataset into training (60%), validation (20%), and test (20%) sets.

5. **Feature Importance**: Calculated AUC scores for numerical features to determine their importance.

6. **Model Training**: Trained a logistic regression model and evaluated its performance using AUC.

7. **Precision and Recall**: Analyzed precision and recall at different thresholds and plotted the results.

8. **Intersection of Precision and Recall**: Found the threshold where precision and recall intersect.

9. **F1 Score**: Computed F1 scores for various thresholds to find the optimal threshold.

10. **Hyperparameter Tuning**: Tuned the model's hyperparameters (C values) using cross-validation to improve performance.

## Conclusion
The project demonstrates the process of building a predictive model using a real-world dataset, focusing on evaluation metrics to optimize performance.
