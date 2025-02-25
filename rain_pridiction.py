import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Here loaded the dataset or you can use the dataset from the link
# url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%203/data/weatherAUS.csv"
# df = pd.read_csv(url)

# Load the dataset
df = pd.read_csv('weatherAUS.csv')

# Now we will convert the feature 'RainTomorrow' to binary (1 for 'Yes', 0 for 'No')
df['RainTomorrow'] = df['RainTomorrow'].map({'Yes': 1, 'No': 0})

# Dropped the rows where RainTomorrow is None or Null
df = df.dropna(subset=['RainTomorrow'])

# Select the features (X) and the target variable (y)
X = df[['Temp9am', 'Temp3pm', 'Humidity9am', 'Humidity3pm', 'WindSpeed9am', 'WindSpeed3pm']]
y = df['RainTomorrow']

# Handle missing values by filling with the median
X = X.fillna(X.median())

# Split into  the training and the testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest Classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Here make predictions
y_pred = clf.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
