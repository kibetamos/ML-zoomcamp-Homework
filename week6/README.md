# Decision Trees and Ensemble Learning

This project aims to analyze the "Students Performance in 2024 JAMB" dataset and build predictive models using decision trees and ensemble learning techniques. The primary goal is to predict students' performance on a standardized test based on various features.

## Table of Contents

- [Dataset](#dataset)
- [Installation](#installation)
- [Data Preparation](#data-preparation)
- [Model Training](#model-training)
  - [Decision Tree](#decision-tree)
  - [Random Forest](#random-forest)
  - [XGBoost](#xgboost)
- [Results](#results)
- [Questions and Answers](#questions-and-answers)
- [License](#license)

## Dataset

The dataset used in this project is the "Students Performance in 2024 JAMB" dataset, which can be downloaded using the following command:

```bash
wget https://github.com/alexeygrigorev/datasets/raw/refs/heads/master/jamb_exam_results.csv


Installation

To set up the environment, you need to have Python installed. This project uses the following libraries:

    pandas
    numpy
    scikit-learn
    xgboost

You can install the required libraries using pip:
## Data Preparation

1. Load the dataset and convert column names to lowercase and replace spaces with underscores.
2. Remove the `student_id` column.
3. Fill missing values with zeros.
4. Split the dataset into training, validation, and test sets (60%/20%/20%).
5. Use `DictVectorizer` to convert the DataFrames into matrices for model training.

## Model Training

### Decision Tree

A decision tree regressor was trained with a maximum depth of 1. The most important feature used for splitting the data was identified as **study_hours_per_week**.

### Random Forest

A random forest model was trained with the following parameters:

- `n_estimators=10`
- `random_state=1`
- `n_jobs=-1` (optional)

The Root Mean Squared Error (RMSE) calculated on the validation set was **42.13**.

### XGBoost

XGBoost was used to further enhance model performance. The `eta` parameter was tuned to evaluate its effect on RMSE. The following parameters were set for training:

```python
xgb_params = {
    'eta': 0.3, 
    'max_depth': 6,
    'min_child_weight': 1,
    'objective': 'reg:squarederror',
    'nthread': 8,
    'seed': 1,
    'verbosity': 1,
}
