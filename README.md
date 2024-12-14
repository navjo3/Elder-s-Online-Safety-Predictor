# **Interactive Machine Learning Dashboard for Enhancing Online Safety Among Elderly Users**

## **Project Summary**
With the increasing prevalence of online scams, particularly targeting elderly individuals, this project aimed to develop a robust machine learning solution to predict the likelihood of an elderly person being safe online. The solution culminates in an **interactive dashboard** that allows users to input personal behavioral and demographic details to receive tailored safety predictions. The project involved comprehensive data generation, preprocessing, feature engineering, model development, and deployment, with a focus on user-friendly visualization and interactivity.

### **Problem**
Elderly individuals often fall victim to online scams due to a lack of awareness, technological savviness, and other demographic or behavioral factors. Existing tools provide limited predictive analysis to identify those at higher risk.

### **Approach**
We developed a **machine learning model** to predict the safety of elderly users online. The predictions and visualizations are presented through a **Streamlit dashboard** that provides:
- Real-time predictions for user inputs.
- Insights and visualizations from the raw and processed datasets.
- Easy toggling between datasets for deeper analysis.

---

## **Data Generation and Overview**
To simulate the online safety behaviors of elderly individuals, a synthetic dataset was generated using Python libraries like **NumPy** and **Pandas**. The dataset was designed to include realistic values and ranges for each feature. Specifically:
- Random distributions (Gaussian and Uniform) were used for numerical features like `Tech Savviness` and `Hours Spent Online Daily`.
- Probabilistic distributions were applied for categorical variables like `Primary Device Used` and `Scam History`.
- Logical relationships were embedded to introduce realistic correlations between features.

The dataset comprises key features capturing the behavioral, demographic, and awareness-related traits of elderly users. The features were split into input variables (predictors) and the target variable (Online Safety Status).

### **Features Used**
| **Feature**                       | **Description**                                               | **Type**     | **Range / Categories**          |
|----------------------------------|---------------------------------------------------------------|-------------|--------------------------------|
| Age                              | Age of the individual in years                                | Numerical   | 60 - 100                       |
| Gender                           | Gender of the individual                                      | Categorical | Male, Female                   |
| Education Level                  | Highest level of education attained                           | Categorical | High School, College, Graduate |
| Tech Savviness                   | User's perceived technological proficiency                    | Numerical   | 1 - 10                         |
| Hours Spent Online Daily         | Average time spent online per day                             | Numerical   | 0.5 - 24.0                     |
| Primary Device Used              | Device primarily used to access the internet                  | Categorical | Smartphone, Laptop, Tablet     |
| Social Media Usage               | Whether the individual uses social media                     | Categorical | Yes, No                        |
| Email Awareness                  | Awareness of phishing/scam emails                             | Numerical   | 1 - 10                         |
| Password Practices               | Strength and frequency of password practices                  | Numerical   | 1 - 10                         |
| Two-Factor Authentication (2FA)  | Whether 2FA is enabled                                        | Categorical | Yes, No                        |
| Scam History                     | Whether the individual has been scammed before                | Categorical | Yes, No                        |
| Scam Type Encountered            | Type of scam encountered                                      | Categorical | Phishing, None                 |
| Awareness Programs Attended      | Whether the individual attended awareness programs            | Categorical | Yes, No                        |
| Confidence in Identifying Scams  | Confidence in identifying potential scams                     | Numerical   | 1 - 10                         |
| Recent Scam Attempts             | Number of recent scam attempts targeting the user             | Numerical   | 0 - 50                         |
| Online Safety Status (Target)    | Predicted safety level of the individual                      | Categorical | Safe, Moderately Safe, Not Safe|

---

## **Data Science Techniques Used**

### **1. Data Preprocessing**
- **Handling Missing Values**: Missing categorical values were imputed using the most frequent value, while numerical columns were filled using mean/median values.
- **Outlier Detection and Treatment**: Outliers in numerical columns (e.g., `Hours Spent Online Daily`, `Recent Scam Attempts`) were detected using the Interquartile Range (IQR) method and replaced with mean values.
- **Encoding Categorical Variables**:
    - Gender, Education Level, and Device Used were encoded using **one-hot encoding**.
    - Binary variables such as 2FA and Social Media Usage were label-encoded (Yes=1, No=0).
- **Feature Scaling**: Min-Max scaling was applied to normalize features like `Hours Spent Online Daily`, `Tech Savviness`, and `Confidence in Identifying Scams`.

### **2. Data Inconsistencies**
Several inconsistencies were identified and addressed:
- **Missing Values**: Missing entries in `Scam Type Encountered` and `Confidence in Identifying Scams`.
- **Outliers**: Extreme values for `Hours Spent Online Daily` and `Recent Scam Attempts` were detected and adjusted.
- **Categorical Mismatch**: Some incorrectly labeled entries for `Primary Device Used` were corrected.

### **3. Feature Engineering**
- **New Feature Creation**:
   - A composite `Awareness Score` combining `Email Awareness` and `Awareness Programs Attended`.
- **Feature Selection**:
   - Recursive Feature Elimination (RFE) and correlation matrix analysis were used to identify the most influential features.

### **4. Model Development**
We experimented with multiple classification algorithms, including:
- **Decision Tree Classifier** (final model)
- Random Forest Classifier
- Logistic Regression
- Support Vector Machine (SVM)

The **Decision Tree Classifier** was selected as the final model based on its performance metrics (accuracy, precision, recall, F1-score) and interpretability.

- **Evaluation Metrics**:
   - Confusion Matrix
   - Precision, Recall, F1-Score
   - Accuracy

---

## **Interactive Dashboard**
The dashboard was developed using **Streamlit** to present the predictions and visualizations interactively.

### **Key Features of the Dashboard**
1. **User Input Form**: Users can enter their details such as age, hours spent online, education level, and awareness scores to get a prediction on their online safety status.
2. **Dynamic Toggle**: Allows users to toggle between the **raw dataset** and the **processed dataset**.
3. **Multiple Visualizations**:
   - **Boxplot**: Distribution of `Recent Scam Attempts`.
   - **Bar Plot**: Comparison of Online Safety Status across `Education Levels`.
   - **Histogram**: Distribution of `Hours Spent Online Daily`.
   - **Heatmap**: Correlation between numerical features.
   - **Pie Chart**: Proportion of `Social Media Usage` and `2FA Adoption`.
   - **Scatter Plot**: Relationship between `Tech Savviness` and `Confidence in Identifying Scams`.
4. **Model Prediction Display**: Shows predicted safety status (Safe, Moderately Safe, Not Safe) and the model's confidence score.

---

## **Results and Insights**
- **Model Accuracy**: The Decision Tree achieved an accuracy of **91%**.
- **Feature Importance**: Key features influencing predictions include:
   - `Recent Scam Attempts`
   - `Tech Savviness`
   - `Password Practices`
   - `Education Level`

### **Insights from Data Comparison**
- **Raw Data**: The raw dataset contained inconsistencies such as missing values and outliers, which could skew predictions.
- **Processed Data**: Preprocessing improved data quality, leading to better accuracy and model robustness.
- **Findings**:
   - Elderly individuals with low awareness scores and no 2FA are at a higher risk.
   - Users spending excessive time online tend to have higher recent scam attempts.
   - Social media users exhibit mixed levels of safety based on their awareness levels.

---

## **Technologies Used**
- **Programming Languages**: Python
- **Libraries**: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, Streamlit
- **Model Deployment**: Streamlit (web application framework)
- **Data Storage**: CSV files for raw and processed datasets

---

## **Project Guidelines Met**
The project successfully met the following objectives:
- **Dataset Creation**: Generated a synthetic dataset that aligns with real-world scenarios.
- **Data Science Techniques**: Applied comprehensive preprocessing, feature engineering, and model selection techniques.
- **Interactivity**: Developed a Streamlit dashboard to visualize insights and provide real-time predictions.
- **Comparative Analysis**: Provided insights from both raw and processed data, emphasizing the importance of clean data for robust predictions.
- **User-Centric**: Designed features to enhance usability and interpretability for non-technical users.

---

## **Conclusion**
This project successfully integrates **data science** techniques to address a pressing

