import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
import joblib

# Load the dataset
data = pd.read_csv('heart_disease_uci.csv')

# Data Preprocessing
# Drop unnecessary columns
data = data.drop(['id', 'dataset'], axis=1)

# Handle missing values
num_cols = ['age', 'trestbps', 'chol', 'thalch', 'oldpeak', 'ca']
for col in num_cols:
    data[col] = data[col].replace(0, np.nan)  # Treat 0 as missing
    data[col] = data[col].fillna(data[col].median())

cat_cols = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'thal']
for col in cat_cols:
    data[col] = data[col].fillna(data[col].mode()[0])

# Convert target to binary
data['num'] = data['num'].apply(lambda x: 1 if x > 0 else 0)

# Split into features and target
X = data.drop('num', axis=1)
y = data['num']

# Define preprocessing
numeric_features = ['age', 'trestbps', 'chol', 'thalch', 'oldpeak', 'ca']
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())])

categorical_features = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'thal']
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)])

# Create and train model
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(random_state=42))])

model.fit(X, y)

# Save the model
joblib.dump(model, 'heart_disease_model.pkl')

print("Model trained and saved successfully!")