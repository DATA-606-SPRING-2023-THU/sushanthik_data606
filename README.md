<img width="950" height="370" alt="image" src="https://github.com/SushanthikPoreddy/sushanthik_data606/blob/main/images/heart-disease-image.png">

# **Heart Disease Predection Using Machine Learning**
### Data 606 Capstone project
###### Sushanthik Reddy Poreddy

[Project link Youtube]()

[Presentation link](https://github.com/SushanthikPoreddy/sushanthik_data606/blob/main/docs/Heart%20Disease%20Prediction.pptx)

#### **Contents**
* [Introduction & Overview](#introduction--overview)
* [Dataset Overview](#dataset-overview)
* [Data Cleaning & preparation](#data-cleaning--preparation)
* [EDA](#eda)
* [Machine Learning Models](#machine-learning-models)
* [Conclusion](#conclusion)
* [References](#references)

#### **Introduction & Overview**
In the present world we do see people of different ages keep on running behind the money and they neglect their health. But the past few years had meade the people to think of their health rather than the money. During the COVID period we had seen many people loosing their life due to lack of proper immunity. In olden days only certain age of people above 60's used to have heart diseases but now the situation has completely changed. Their are many cases where the people between age group 25-30 had lost their life due to heart diseases. The reason that made me to choose this project is it is very important to identify the chance of such heart diseases and take appropriate precautions.

Heart is the major part of the body that helps the human body to pump the blood and also for the functionality of the human body. It's working is very important and the halt in it's functionaliy means nothing but the physical exsistence of the human body came to an end. In most of the cases the person doesn't even know that he/she have certain heart disease and the lack of identification risks their life. It is very important to identify such case and handle them accordingly. It is not like only certain age of people will have such heart diseases and the younger generation is out risk. The food that we take and the change in the life style was the main reason for having very less immunity and that also increases the risk of having heart diseases.

#### **Dataset Overview**
The dataset for this project was taken for IEEE site which stands for "Institute of Electrical and Electronics Engineers". This dataset is a combination of 5 different datasets namely Cleveland, Hungarian, Switzerland, Long Beach VA, and Statlog (Heart) Data Sets. This datase was submitted by "Manu Siddhartha" to IEEE and the formate of this dataset is CSV.

It is an opensource data and it can be accessed though this link : [Dataset](https://ieee-dataport.org/open-access/heart-disease-dataset-comprehensive)

This dataset was lastly update on November 6th, 2020.

Size of dataset is 38.76 KB.

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

### **Data Cleaning & preparation**

The first step in the project is data cleaning. There I checked for the null values and duplicate values in the columns of the dataset. There are no null values and the duplicate records in the dataset.

### **EDA**

After the data cleaning process I have started doing EDA on all the available features of the dataset and pulled out the graphs for the columns. I have carried out the EDA process on the dataset. This EDA process was carried in [Google colab notebook](https://github.com/SushanthikPoreddy/sushanthik_data606/blob/main/src/final_project_code_part1.ipynb) and they can be seen in the repository.

<img width="809" alt="image" src="https://github.com/SushanthikPoreddy/sushanthik_data606/blob/main/images/avg_heart_rate_healthy_unhealthy_heart.png">
<img width="809" alt="image" src="https://github.com/SushanthikPoreddy/sushanthik_data606/blob/main/images/avg_heart_rate_male_female.png">
<img width="809" height="300" alt="image" src="https://github.com/SushanthikPoreddy/sushanthik_data606/blob/main/images/bloodpressure_male_female.png">
<img width="809" height="300" alt="image" src="https://github.com/SushanthikPoreddy/sushanthik_data606/blob/main/images/chest_pain_types.png">
<img width="809" height="300" alt="image" src="https://github.com/SushanthikPoreddy/sushanthik_data606/blob/main/images/chol_male_female.png">
<img width="809" height="300" alt="image" src="https://github.com/SushanthikPoreddy/sushanthik_data606/blob/main/images/exercise_healthy_unhealthy.png">
<img width="809" height="300" alt="image" src="https://github.com/SushanthikPoreddy/sushanthik_data606/blob/main/images/healthy_unhealthy_heart.png">
<img width="809" height="300" alt="image" src="https://github.com/SushanthikPoreddy/sushanthik_data606/blob/main/images/heart_male_female.png">
<img width="809" height="300" alt="image" src="https://github.com/SushanthikPoreddy/sushanthik_data606/blob/main/images/restingecg_healthy_unhealthy.png">

Then after correlation matrix shows all the posible pairs of values correlated in the table and below is the visualization of it.
<img width="507" alt="image" src="https://github.com/SushanthikPoreddy/sushanthik_data606/blob/main/images/corelation.png">

### **Machine Learning Models**

I have decided to perform three classifier models on the data.
1. Naive Bayes Classifier
2. Decision Tree Classifier
3. Random Forest CLassifier

The three classification models Naive Bayes, Decision Tree and Random Forest can be found in the [Machine Learning Models](https://github.com/SushanthikPoreddy/sushanthik_data606/blob/main/src/final_project_code_part1.ipynb) notebook. 

Decision tree is a supervised machine learning algorithm. And as the name suggests Random Forest is a tree-based machine learning algorithm that uses the power of multiple decision trees for making decisions.

It is obeserved that different classifier models have different accuracy scores and the based on the best accuracy score I can choose the best model that helps me in predecting the chance of heart disease. 
The train f1 score for all the above mentioned classifier models is as follows:
<img width="507" alt="image" src="https://github.com/SushanthikPoreddy/sushanthik_data606/blob/main/images/train_accuracy.png">

Based on the above results the Random Forest Classifier has the highest accuracy score and it is used to run on the test data. The results of the test and train data are as follows:
<img width="507" alt="image" src="https://github.com/SushanthikPoreddy/sushanthik_data606/blob/main/images/train_test_accuracy.png">

### **Most Important Feature**
Once after find the best model, I had used that model to find the most important features that has the highest weightage in predecting the heart health status among the list of multiple features from my dataset. The results for the most important features is as follows:
<img width="507" alt="image" src="https://github.com/SushanthikPoreddy/sushanthik_data606/blob/main/images/most_important_feature.png">

### **Streamlit Results**
Find the best model helped me to predect the target variable and I had visualized the results with the help of the streamlit/ Streamlit is used to generate the user interface and this accepts all other feature values as the inputs and generates the target variable as the output. 
The screen for predecting heart disease looks like below:

<img width="507" alt="image" src="https://github.com/SushanthikPoreddy/sushanthik_data606/blob/main/images/Streamlit%20UI.JPG">

### **Conclusion**
Random Forest Classifier model best predicts the chance of heart diseases. It has the accuracy score of 0.90 on train data and 0.95 on test data. Which means this model predects 90% accurately in terms of heart disease when compared to the other machine learning classification models.

The slope of the peak exercise(ST_Slope) segment feature is figured as the most important feature in the dataset when compared to the other features of the dataset with the value of 0.175 and the feature fasting blood pressure is identified as the least important feature since it has the least important value.

### **References**

[GitHub link](https://github.com/SushanthikPoreddy/sushanthik_data606)

[Heart Disease Predection using Machine Learning](https://ieee-dataport.org/open-access/heart-disease-dataset-comprehensive)

[Classification models](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)

[Streamlit](https://streamlit.io/)

[Heart disease prediction using supervised machine learning algorithms: Performance analysis and comparison](https://pubmed.ncbi.nlm.nih.gov/34315030/)
