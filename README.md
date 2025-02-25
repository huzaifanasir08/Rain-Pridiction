# 🌧 Rain Prediction Model
This project uses a Random Forest Classifier to predict whether it will rain tomorrow based on historical weather data. The model is trained on the Australian weather dataset and considers key weather features like temperature, humidity, and wind speed.
# 🚀 Getting Started
Follow these steps to set up and run the project:
 ## 1️⃣ Clone the Repository
 ```python
git clone https://github.com/huzaifanasir08/Rain-Pridiction.git
cd Rain-Pridiction/RainPridiction
```
 ## 2️⃣ Create a Virtual Environment
  ```python
python -m venv venv
```
## 3️⃣ Activate the Virtual Environment
  * #### Windows (CMD/PowerShell):
 ```python
venv\Scripts\activate
```
* #### macOS/Linux:
 ```python
source venv/bin/activate
```
## 4️⃣ Install Dependencies
 ```python
pip install -r req.txt
```
## 5️⃣ Download the Dataset
Make sure you have the dataset weatherAUS.csv in the same directory as RainPridiction.py.
Alternatively, uncomment the provided dataset URL in RainPridiction.py to load it directly from the web.

## 6️⃣ Run the Model
 ```python
python RainPridiction.py
```
## 7️⃣ Expected Output
The script will train the model and print an accuracy score indicating the performance of the classifier.

# 📌 Features
*  Uses Random Forest Classifier for prediction.
*  Handles missing values by filling them with the median.
*  Selects key weather features like temperature, humidity, and wind speed.
*  Splits data into training (80%) and testing (20%).
*  Outputs model accuracy.
