
# Predicting Telco Customers Churn
![](https://insidetelecom.com/wp-content/uploads/2020/11/Telecom-operators-and-reducing-customer-churn.jpg)

By [ Waleed on LinkedIn](https://www.linkedin.com/in/waleedabdulla/)


A major issue facing the telecommunications (Telco) sector is customer attrition. It is described as the loss of clients who switch Telco providers. Telco operators can employ business marketing practices to such turnover clients to retain and grow the customer base if customer churn can be forecast in advance, such as "is this customer going to leave us within the next X months?" Particularly, considering the millions of Telco customers, even a 1% decrease in churn will result in a huge rise in earnings.

### Problem Statement

The objective of this project is to predict customers that are about to churn in order to catch them with a discount or attractive offers. It is desirable to develop a machine learning model that can predict customers who will leave the company. You are expected to perform the necessary data analysis and feature engineering steps before developing the model.


***WA_Fn-UseC_-Telco-Customer-Churn*** data includes information about a fictitious telecom company that provided home phone and Internet services to 7,043 California customers in the third quarter. contains details about a hypothetical telecom provider that served 7,043 clients in California in the third quarter with residential phone and Internet services. It shows which clients have canceled their service shows, stayed, or joined up? You can find the dataset [here](https://www.kaggle.com/datasets/blastchar/telco-customer-churn). I have droped the "CustomerID" variable in this dataset since it is irrelevant to the objective of the project. Each row represents a customer, each column contains the customer's attributes. This dataset contains 20 variables (I removed the CustomerID since it is irrelevant) and 7043 rows (customers) with information such as  gender, Phone Service, and Internet Service ...etc. 

The following table shows the data types of the variables with 17 categorical and 3 numerical data type.


| Variable         | Meaning |
| ---------------- | ----------------------------------------------- |
| gender           | whether the customer is a male or a female|
| SeniorCitizen    | whether the customer is a senior citizen or not (1, 0)|
| Partner          | whether the customer has a partner or not (Yes, No)|
| Dependents       | whether the customer has dependents or not (Yes, No). A dependent is a person who relies on another as a primary source of income|
| tenure           | number of months the customer has stayed with the company|
| PhoneService     | whether the customer has a phone service or not (Yes, No)|
| MultipleLines    | whether the customer has multiple lines or not (Yes, No, No phone service)|
| InternetService  | customer’s internet service provider (DSL, Fiber optic, No)|
| OnlineSecurity   | whether the customer has online security or not (Yes, No, No internet service)|
| OnlineBackup     | whether the customer has online backup or not (Yes, No, No internet service)|
| DeviceProtection | whether the customer has device protection or not (Yes, No, No internet service)|
| TechSupport      | whether the customer has tech support or not (Yes, No, No internet service)|
| StreamingTV      | whether the customer has tech support or not (Yes, No, No internet service)|
| StreamingMovies  | whether the customer has streaming movies or not (Yes, No, No internet service)|
| Contract         | type of contract according to duration (Month-to-month, One year, Two year)|
| PaperlessBilling | bills issued in paperless form (Yes, No)|
| PaymentMethod    | ayment method used by customer (Electronic check, Mailed check, Credit card (automatic), Bank transfer (automatic))|
| MonthlyCharges   | amount of charge for service on monthly bases|
| TotalCharges     | cumulative charges for service during subscription (tenure) period|
| Churn            | output value, predict variable (Yes, No)|