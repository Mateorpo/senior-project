# Real Estate Price Prediction Model
This senior capstone project aims to build models that predict house prices, and determine what input variables are the most important in this prediction. The model will be implemented in the back end of a web-based platform that helps give users an idea of how much a house would cost based on their preferences.

# Dataset
- [House Prices - Advanced Regression Techniques](https://www.kaggle.com/c/house-prices-advanced-regression-techniques)
- A large dataset based in Ames City, Iowa, containing housing data from 2006 - 2009
- train.csv and test.csv files in the repository
- data_description.txt explains what each variable in the dataset is

# Libraries Used
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Calendar
- Sklearn.preprocessing
- TensorFlow
- Pickle
- XGBoost

# Models Implemented
- Linear Regression
- SVR
- SGDRegressor
- KNeighbors Regressor
- Gaussian Process Regressor
- Decision Tree
- Random Forest
- Gradient Boosting Regressor
- XGB Regressor
- MLP Regressor
- Deep Neural Networks

# Best Model: Gradient Boosting Regressor
- Score of 86%
- Most important features: Condition 1, Exterior1st, LotConfig, LotFrontage, Alley, Utilities, MasVnrType, YearRemodAdd, RoofStyle, and LandSlope
- Basing our application off of this model

# How to Run the Model: Google Collab
1. Download the train.csv, test.csv, and real_estate_price_prediction_model.ipynb to your Google Drive
2. Create a folder in Google Drive called "project" and place the files in there
3. Open file in Google Collab
4. Press "Runtime" at the top and select "Run all"

# How to run React  
1. Create folder house_prediction
2. Create folders backend and frontend
3. In backend paste files (app.py; and folders model(scaler.pkl; house_price_model.pkl) venv(libraries requiered)
4. In frontend paste files (index.html, package.json, vit.config.js; create folder src(App.css; App.jsx; index.css; main.jsx subfolder components(PredictionForm.css; PredicitonForm.jsx; PredictionResults.css; PredictionResults.jsx)
