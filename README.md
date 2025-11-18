🚗 Auto MPG Prediction using XGBoost & Streamlit
App link - https://auto-mpg-prediction-using-xgboost-hszdrpodz7hknynyy9c9xm.streamlit.app/

This project predicts Miles Per Gallon (MPG) for cars using important features such as horsepower, cylinders, displacement, weight, and more.
It uses:

XGBoost Regressor

Outlier removal (IQR method)

Feature engineering

Pickle file for model saving

Streamlit Web App for making predictions interactively

📌 Features

✔ Cleaned the dataset using IQR
✔ Removed outliers from horsepower & acceleration
✔ Trained an XGBoost model
✔ Saved trained model as .pkl
✔ Built a Streamlit app for user predictions
✔ User can input specifications such as:

Cylinders

Displacement

Horsepower

Weight

Acceleration

Model Year

Origin

And get predicted MPG instantly.

📂 Project Structure
├── app.py
├── xgboost_model.pkl
├── requirements.txt
├── README.md
└── dataset.csv

▶️ How to Run the Project
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Run Streamlit App
streamlit run app.py

3️⃣ Open in Browser

Your app will open automatically at:

http://localhost:8501/

🛠 technologies Used
Tool	Purpose
Python	Data processing & ML
Pandas, NumPy	Data cleaning
Matplotlib & Seaborn	Visualization
Scikit-learn	Splitting, evaluation
XGBoost	Prediction model
Streamlit	Web interface
Pickle	Model saving/loading
🧠 Model Training Summary

Removed outliers using IQR

Used top features based on correlation & feature importance

Trained XGBoostRegressor

Saved final model as xgboost_model.pkl

Achieved good accuracy with low MAE / RMSE

🌐 Live Demo (optional)

If you deploy on Streamlit Cloud, add your link here.

🎯 Example Prediction Input
{
    'cylinders': 8,
    'displacement': 350,
    'horsepower': 165,
    'weight': 3693,
    'acceleration': 11.5,
    'model year': 70,
    'origin': 1
}


🙌 Author

Om Laxman Khairnar
BCA Student | Data Science & ML Learner
