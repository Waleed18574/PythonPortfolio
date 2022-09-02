# Parch & Posey Exploratory Data analysis

## Problem Statment
Parch and Posey is a comapny that sell 3 paper types (standard, gloss, poster). The company's data areaccumulated for the several years and stored in 4 csv files ; 
orders, accounts, sales_persons and regions. As a data analyst you are required to help the management to make informed decisions by analyzing the the data and 
generate business insights. The management wants to acquire general knowledge of the data, and get answers for specific questions from the departments of Sales & 
Marketing, HR and Finance.


## Dataset
The dataset of this project consists of 4 tables of orders, accounts, sales_representatives and regions. I extracted those tables from Parch
and Posey DB into csv files, then modified the orders tables by slightly decreasing its length. Even after this modification, there were more than 300,000 records left.
![](assets/0.png)

## Executive Summary
In the first part of this project, I used a combination of libraries including #pandas, #matplotlib, #seabron, #folium, #geocoder, #geopy and #plotly. The visuals plotted using folium 
and ploty are interactive. I divided this project into 2 stages. In the first stage, I defined the #problem_statement, collected, cleaned and organized data. Then, I performed a general EDA on 
the categorical and numeric columns to get to know the data. In the second stage, I answered specific hypothetical business questions from the departments of HR, 
Finance and Sales and Marketing. Here some of the visuals used in the first part of this project:
![](assets/1.PNG)
![](assets/2.PNG)
![](assets/3.PNG)
![](assets/4.PNG)
![](assets/5.PNG)

In the second part of this project, I:
- Connected python with local PostgreSQL database.

- Retireved 4 tables from database into 4 dataframes and merged them into 1 dataframe.

- Answered 15 business questions by using SQL code within Python.

- Answered the same questions using Pandas methods and functions.

- Compared between the 2 answers for every question.

I found that Pandas methods and functions are easier to write while querying the database using SQL code with the established connection is more efficient.

