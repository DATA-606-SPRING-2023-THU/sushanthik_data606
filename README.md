<img width="950" height="370" alt="image" src="https://github.com/SushanthikPoreddy/sushanthik_data606/blob/main/images/heart-disease-image.png">

# **Heart Disease Predection Using Machine Learning**
### Data 606 Capstone project
###### Sushanthik Reddy Poreddy

[Project link Youtube](https://youtu.be/vc3as84qhiM)

[Presentation link](https://github.com/SushanthikPoreddy/sushanthik_data606/blob/main/docs/Heart%20Disease%20Prediction.pptx)

#### **Contents**
* [Introduction & Overview](#introduction--overview)
* [Dataset Overview](#dataset-overview)
* [Data Cleaning & preparation](#data-cleaning--preparation)
* [EDA](#eda)
* [Data Processing & Encoding](#data-processing--encoding)
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

After the data cleaning process I have started doing EDA on all the available features of the dataset and pulled out the graphs for the columns. I have carried out the EDA process on the dataset. This EDA process was carried in [Google colab notebook](https://github.com/HariChandana1116/harichandana_data606/blob/main/EDA%20and%20Machine%20Learning/EDA%20%26%20ML.ipynb) and they can be seen in the repository.

<img width="809" alt="image" src="https://user-images.githubusercontent.com/77841272/185717343-1e652df9-3586-4ff9-9662-f05c20da3409.png">
<img width="813" alt="image" src="https://user-images.githubusercontent.com/77841272/185717398-ab84f425-dc69-4ddb-a3dd-d9bc6ba18d02.png">
Then after correlation matrix shows all the posible pairs of values correlated in the table and below is the visualization of it.
<img width="507" alt="image" src="https://user-images.githubusercontent.com/77841272/185717839-150ca134-f9d5-434f-8979-29443e9aeff8.png">
we have also plotted scatter plot for the relationship between obesity and high blood pressure.
<img width="323" alt="image" src="https://user-images.githubusercontent.com/77841272/185717688-6b630665-5be1-42d3-a587-6154ef83f083.png">

### **Data Processing & Encoding**

After EDA, the we had to further process our dataset in order to make it ready for our machine learning analysis. We have found a significant imbalance in our dataset. So we have performed resampling to balace our data as using imbalance data for machine learning analysis can produce biased results. Below is the image that shows the data before and after resampling.
<img width="571" alt="image" src="https://user-images.githubusercontent.com/77841272/185727245-6756ded7-260c-499e-a45f-254160f4737e.png">

After resampling we have started encoding all the categorical values using OneHotEncoder. As part of encoding we have encoded the Target variable values as the following
* Health Outcomes = 1
* Unhealthy Behavior =2
* Prevention = 3
The below is the final dataset that we have used for machine learning models.
<img width="542" alt="image" src="https://user-images.githubusercontent.com/77841272/185726822-6efac626-c9ee-49c5-b782-89ba3a60aec9.png">
We have split this final dataset into training and test dataset with 70% of the data in training and the remaininng 30% for testing.


### **Machine Learning Models**

We have decided to perform three regression models and two classifier models on our data.
1. Linear Regression
2. Ridge Regression
3. Lasso Regression
4. Decision Tree Classifier
5. Random Forest CLassifier

The three linear regression models Linear, Lasso and Ridge can be found in the [Regression](https://github.com/HariChandana1116/harichandana_data606/blob/main/EDA%20and%20Machine%20Learning/Regression_models.ipynb) notebook. Ridge and Lasso regression models fall into the same family of Linear regression model. But the difference is the model is penalized for its choice of the weights. In Lasso regression the absolute values of weight will be reduced, and many will tend to be zeros. Therefore it will avoid overfitting which generally happen in linear regression model. Similar to Lasso in Ridge regression the model is penalized for the sum of squared value of the weights.

Decision tree is a supervised machine learning algorithm that can be used for both classification and regression. And as the name suggests Random Forest is a tree-based machine learning algorithm that uses the power of multiple decision trees for making decisions.


### **Conclusion**
The analysis has given a good picture regarding the measures that are leading to various health outcomes along with various measures people are taking for preventing certain health outcomes. We have occured to the following conclusion that there are less number of people who are into prevention measures. Also there are more people who are depending on medications.
From our machine learning models performance scores, we have found out that the classification models i.e. Decision Tree classifier and Random Forest classifier are better suitable for our dataset than the three regression models. 

<img width="457" alt="image" src="https://user-images.githubusercontent.com/77841272/185714625-0319845d-e80a-46bd-a388-994df6a25729.png">

This analysis has further scope where each measure can be analysed seperately for specific geographic location. Such analysis will be useful for government agencies and digital health care application developers in designing new initiatives and business ventures in respect to each specific geographical location.

### **References**

[GitHub link](https://github.com/HariChandana1116/harichandana_data606)

[500 Cities- CDC](https://chronicdata.cdc.gov/500-Cities-Places/500-Cities-Local-Data-for-Better-Health-2018-relea/rja3-32tc)

[Regression models](https://towardsdatascience.com/whats-the-difference-between-linear-regression-lasso-ridge-and-elasticnet-8f997c60cf29)

[Classification models](https://www.analyticsvidhya.com/blog/2020/05/decision-tree-vs-random-forest-algorithm/)
