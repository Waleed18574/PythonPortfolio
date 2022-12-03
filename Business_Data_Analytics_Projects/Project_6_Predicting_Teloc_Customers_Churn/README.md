
# Predicting Telco Customers Churn
![](https://insidetelecom.com/wp-content/uploads/2020/11/Telecom-operators-and-reducing-customer-churn.jpg)

By [ Waleed on LinkedIn](https://www.linkedin.com/in/waleedabdulla/)


A major issue facing the telecommunications (Telco) sector is customer attrition. It is described as the loss of clients who switch Telco providers. Telco operators can employ business marketing practices to such turnover clients to retain and grow the customer base if customer churn can be forecast in advance, such as "is this customer going to leave us within the next X months?" Particularly, considering the millions of Telco customers, even a 1% decrease in churn will result in a huge rise in earnings.

### Problem Statement

The objective of this project is to predict customers that are about to churn in order to catch them with a discount or attractive offers. It is desirable to develop a machine learning model that can predict customers who will leave the company. You are expected to perform the necessary data analysis and feature engineering steps before developing the model.


***telecom_customer_churn_joined.csv*** data includes information about a fictitious telecom company that provided home phone and Internet services to 7,043 California customers with 37 variables in the third quarter. Each row represents a customer, each variable contains the customer's attributes. It shows which clients have canceled their service shows, stayed, or joined up.


The following table shows the  the 37 variables with their meaning.


| Variable         | Meaning |
| ---------------- | ----------------------------------------------- |
|CustomerID|ID that identifies each customer
|Gender|The customer’s gender: Male, Female
|Age|The customer’s current age, in years, at the time the fiscal quarter ended (Q2 2022)
|Married|Indicates if the customer is married: Yes, No
|Number of Dependents|Indicates the number of dependents that live with the customer (dependents could be children, parents, grandparents, etc.)
|City|The city of the customer’s primary residence in California
|PostalCode| The PostalCode of the customer’s primary residenc
|Latitude| The latitude of the customer’s primary residence
|Longitude| The longitude of the customer’s primary residence
|Number of Referrals| Indicates the number of times the customer has referred a friend or family member to this company to date
|Tenure in Months|Indicates the total amount of months that the customer has been with the company by the end of the quarter specified above
|Offer|Identifies the last marketing offer that the customer accepted: None, Offer A, Offer B, Offer C, Offer D, Offer E
|Phone Service|Indicates if the customer subscribes to home phone service with the company: Yes, No
|Avg Monthly Long Distance Charges|Indicates the customer’s average long distance charges, calculated to the end of the quarter specified above (if the customer is not subscribed to home phone service, this will be 0)
|Multiple Lines|Indicates if the customer subscribes to multiple telephone lines with the company: Yes, No (if the customer is not subscribed to home phone service, this will be No)
|Internet Service|Indicates if the customer subscribes to Internet service with the company: Yes, No
|Internet Type|Indicates the customer's type of internet connection: DSL, Fiber Optic, Cable (if the customer is not subscribed to internet service, this will be None)
|Avg Monthly GB Download|Indicates the customer’s average download volume in gigabytes, calculated to the end of the quarter specified above (if the customer is not subscribed to internet service, this will be 0)
|Online Security|Indicates if the customer subscribes to an additional online security service provided by the company: Yes, No (if the customer is not subscribed to internet service, this will be No)
|Online Backup|Indicates if the customer subscribes to an additional online backup service provided by the company: Yes, No (if the customer is not subscribed to internet service, this will be No)
|Device Protection Plan|Indicates if the customer subscribes to an additional device protection plan for their Internet equipment provided by the company: Yes, No (if the customer is not subscribed to internet service, this will be No)
|Premium Tech Support|Indicates if the customer subscribes to an additional technical support plan from the company with reduced wait times: Yes, No (if the customer is not subscribed to internet service, this will be No)
|Streaming TV|Indicates if the customer uses their Internet service to stream television programing from a third party provider at no additional fee: Yes, No (if the customer is not subscribed to internet service, this will be No)
|Streaming Movies|Indicates if the customer uses their Internet service to stream movies from a third party provider at no additional fee: Yes, No (if the customer is not subscribed to internet service, this will be No)
|Streaming Music|Indicates if the customer uses their Internet service to stream music from a third party provider at no additional fee: Yes, No (if the customer is not subscribed to internet service, this will be No)
|Unlimited Data|Indicates if the customer has paid an additional monthly fee to have unlimited data downloads/uploads: Yes, No (if the customer is not subscribed to internet service, this will be No)
|Contract|Indicates the customer’s current contract type: Month-to-Month, One Year, Two Year
|Paperless Billing|Indicates if the customer has chosen paperless billing: Yes, No
|Payment Method|Indicates how the customer pays their bill: Bank Withdrawal, Credit Card, Mailed Check
|Monthly Charge|Indicates the customer’s current total monthly charge for all their services from the company
|Total Charges|Indicates the customer’s total charges, calculated to the end of the quarter specified above
|Total Refunds|Indicates the customer’s total refunds, calculated to the end of the quarter specified above
|Total Extra Data Charges|Indicates the customer’s total charges for extra data downloads above those specified in their plan, by the end of the quarter specified above
|Total Long Distance Charges|Indicates the customer’s total charges for long distance above those specified in their plan, by the end of the quarter specified above
|Total Revenue|Indicates the company's total revenue from this customer, calculated to the end of the quarter specified above (Total Charges - Total Refurnds + Total Extra Data Charges + Total Lond Distance Charges)
|Customer Status|Indicates the status of the customer at the end of the quarter: Churned, Stayed, or Joined
|Churn Category|A high-level category for the customer’s reason for churning, which is asked when they leave the company: Attitude, Competitor, Dissatisfaction, Other, Price (directly related to Churn Reason)
|Churn Reason|A customer’s specific reason for leaving the company, which is asked when they leave the company (directly related to Churn Category)
|Population|A current population estimate for the entire PostalCode area
