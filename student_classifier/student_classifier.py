import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Create synthetic dataset
np.random.seed(42)
n_students = 500

data = {
    'MST_Score': np.random.normal(70, 15, n_students),  # Mid-Semester Test scores
    'Quiz_Score': np.random.normal(75, 10, n_students), 
    'Attendance': np.random.normal(85, 12, n_students),  # Percentage
    'Assignment_Score': np.random.normal(80, 10, n_students)
}

df = pd.DataFrame(data)

# Introduce some missing values
for col in df.columns:
    df.loc[df.sample(frac=0.1).index, col] = np.nan

# Step 2: Define target based on overall performance
# Calculate average score
df['Average_Score'] = df.mean(axis=1)

def classify_performance(score):
    if score >= 80:
        return 'High Performer'
    elif score >= 60:
        return 'Average Performer'
    else:
        return 'Needs Improvement'

df['Performance'] = df['Average_Score'].apply(classify_performance)

# Drop Average_Score after creating target
df.drop(columns=['Average_Score'], inplace=True)

# Step 3: Preprocessing
# Separate features and target
X = df.drop('Performance', axis=1)
y = df['Performance']

# Handle missing values using mean imputation
imputer = SimpleImputer(strategy='mean')
X_imputed = imputer.fit_transform(X)

# Normalize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_imputed)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42, stratify=y)

# Step 4: Train classification models
models = {
    'Logistic Regression': LogisticRegression(max_iter=1000, random_state=42),
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
    'SVM': SVC(kernel='rbf', probability=True, random_state=42)
}

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    print(f"--- {name} ---")
    print(classification_report(y_test, y_pred))
    
    cm = confusion_matrix(y_test, y_pred, labels=['High Performer', 'Average Performer', 'Needs Improvement'])
    plt.figure(figsize=(6,4))
    sns.heatmap(cm, annot=True, fmt='d', xticklabels=['High Performer', 'Average Performer', 'Needs Improvement'],
                yticklabels=['High Performer', 'Average Performer', 'Needs Improvement'])
    plt.title(f'{name} Confusion Matrix')
    plt.ylabel('Actual')
    plt.xlabel('Predicted')
    plt.show()
