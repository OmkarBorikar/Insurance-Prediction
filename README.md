# Insurance Predictor

* **Overview of project**

This web app is the simplified prototype of application that can be used in Insurance provider company to predict the medical cost they might nead to bear 
given the customers details like Age, Sex, is he/she smoker or not, number of childrens they have etc.

* **Libraries and Tools Used**

Pandas - for data manipulation and reading files.

Seaborn and Matplotlib - For data visualization

Scikit-learn - for data preprocessing and model building

Catboost,XGBoost and LightGBM - For Model building.

* **About Dataset Used**

Dataset used for this project can be found here - [Medical Cost Personal Details](https://www.kaggle.com/mirichoi0218/insurance)
The dataset contains records of 1338 patients and their respective medical charges. Alongwith medical charges folowing features are given in this dataset 
for each observation -

    age: age of primary beneficiary.

    sex: insurance contractor gender (female, male)

    bmi: Body mass index, providing an understanding of body, weights that are relatively high or low relative to height,objective index of body weight 
         (kg / m ^ 2) using the ratio of height to weight, ideally 18.5 to 24.9

    children: Number of children covered by health insurance / Number of dependents

    smoker: Smoking (Yes/No)

    region: the beneficiary's residential area in the US, northeast, southeast, southwest, northwest.

    charges: Individual medical costs billed by health insurance (in USD)
    
    
* **Features of web app**

This app is deployed on streamlit share and can be run from here - [Insurance Predictor](https://share.streamlit.io/omkarborikar/insurance-prediction/main/app.py)

After clicking on above link below page will open -

![image](https://user-images.githubusercontent.com/82905366/143280580-cd9b74e9-3999-49bf-944c-8021e5af61c4.png)

Following are the constraints on input data - 

    Age can be selected from 18 - 70

    Number of childrens can be entered from 0 - 5

    BMI can be entered between 14.00 - 55.00

After clicking on 'Predict Insurance cost' button output can be seen as follows -

![image](https://user-images.githubusercontent.com/82905366/143280870-b9a26053-5266-4389-8b30-190e4f9f275e.png)

* **Approach** 

The Notebook contains detailed Analysis of each feature and its correlation with the target feature and other features, glimpse of which can be seen below -

![image](https://user-images.githubusercontent.com/82905366/143281512-cb09202b-7ff5-4858-85c8-a8f274f27115.png)


I have tried carious Machine Learning models for this regression problem, such as LinearRegression, RandomForest, XGBoost, CatbBoost, LightGBM and Decision Tree.

Catbbost, XGBoost and RandomForest were predicting with high accuracy, so i have tuned their hyperparameter using OPTUNA and blended 3 of them using Weighted 
average sum. I have got o.90% accuracy (R2_Score) with this approach. In future i am planning to add visyalization dashboard to this project and to acheive better
accuracy also.

