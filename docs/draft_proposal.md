# Capstone Project Data Science 606 
##### Proposal By : Sushanthik Reddy Poreddy
### Heart Disease Prediction Using Machine Learning

#### Issue of interest
In the present world we do see people of different ages keep on running behind the money and they neglect their health. But the past few years had meade the people to think of their health rather than the money. During the COVID period we had seen many people loosing their life due to lack of proper immunity. In olden days only certain age of people above 60's used to have heart diseases but now the situation has completely changed. Their are many cases where the people between age group 25-30 had lost their life due to heart diseases. The reason that made me to choose this project is it is very important to identify the chance of such heart diseases and take appropriate precautions. 
 
#### Issue importance
Heart is the major part of the body that helps the human body to pump the blood and also for the functionality of the human body. It's working is very important and the halt in it's functionaliy means nothing but the physical exsistence of the human body came to an end. In most of the cases the person doesn't even know that he/she have certain heart disease and the lack of identification risks their life. It is very important to identify such case and handle them accordingly. It is not like only certain age of people will have such heart diseases and the younger generation is out risk. The food that we take and the change in the life style was the main reason for having very less immunity and that also increases the risk of having heart diseases. 

#### What questions do you have in mind and would like to answer?
- What is the impact of the heart rate on heart diseases?
- Based on the dataset available, I will try to figure out which gender and which age group are more prone to heart diseases?
- How accurate the Machine Learning models are being able to predict the chance of having heart diseases on the basis of variables that I considered?

#### Data source 
The dataset for this project was taken for IEEE site which stands for "Institute of Electrical and Electronics Engineers". This dataset is a combination of 5 different datasets namely Cleveland, Hungarian, Switzerland, Long Beach VA, and Statlog (Heart) Data Sets. This datase was submitted by "Manu Siddhartha" to IEEE and the formate of this dataset is CSV.

It is an opensource data and it can be accessed though this link : [Dataset](https://ieee-dataport.org/open-access/heart-disease-dataset-comprehensive)

This dataset was lastly update on November 6th, 2020.

The dataset that I considered has 13 different columns with the number of observations 1190. 
Below are the list of columns that I have in my dataset with the type of the data:

<img width="500" height="350" alt="image" src="https://github.com/SushanthikPoreddy/sushanthik_data606/blob/1b929b87ea6f1e0c785a1a60b0261218ae96d433/images/List%20of%20Columns.JPG">

The dataset that I considered has three different types of data namely 
- Continuous Data: This is the data that can be measured.
For example, their are certain columns in the dataset like **"cholesterol"** which can be measured and recorded.
- Ordinal Data: This is the categorical data that has a specific order and that may be from 0,1,2, and so on.
For example, the column named **"chest pain type"** is the ordinal type because interms of chest pain type, their are 4 different types and each type has a specific categorical value assigned. Instead of having each chest pain type, this Ordinal data helps us to represent that specific chest pain type.
- Binary Data: This is the data that holds the value of True or False. 
For example, we do have a specific condition, if that condition is passed then the binary value of that row will be 1 else it will be 0.
 **Note:** This dataset doesn't have any geographical or time frame related data.

#### Unit of analysis

#### What variables/measures do you plan to use in your analysis (variables should be tied to the questions in #3)?
My variables would be heart rate, gender, age and target which helps me to develop the model that has the ability to predict the outcome whether the person is affected with heart diseases or not. I do have a column named "target" in my dataset 

#### What kinds of techniques/models do you plan to use (for example, clustering, NLP, ARIMA, etc.)?

#### How do you plan to develop/apply ML and how you evaluate/compare the performance of the models?
#### What outcomes do you intend to achieve (better understanding of problems, tools to help solve problems, predictive analytics with practicle applications, etc)?
